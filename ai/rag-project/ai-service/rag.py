"""Train sparse TF-IDF weights and index dense and sparse embeddings in Qdrant."""
import hashlib
import json
import math
import os
import re
from collections import Counter
from contextlib import closing
from pathlib import Path
from threading import Lock

from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
from qdrant_client import QdrantClient, models

from collector import DATA, collect

load_dotenv(Path(__file__).with_name(".env"))
INDEX = DATA / "index.json"
CHUNKS = DATA / "processed" / "chunks.json"
TOP_K = 4


def openai_client():
    key = os.getenv("OPENAI_API_KEY", "").strip()
    return OpenAI(api_key=key, timeout=15, max_retries=0) if key else None


def terms(text):
    counts = Counter()
    for word in re.findall(r"[a-z0-9_]+|[가-힣]+", text.lower()):
        if word[0].isascii():
            counts[word] += 1
        else:
            counts.update(word[i:i + 2] for i in range(len(word) - 1))
    return counts


def fit(texts):
    frequencies = Counter()
    for text in texts:
        frequencies.update(terms(text).keys())
    return {term: (i, 1 + math.log((1 + len(texts)) / (1 + df)))
            for i, (term, df) in enumerate(sorted(frequencies.items()))}


def sparse(text, weights):
    counts = terms(text)
    pairs = sorted((idx, (1 + math.log(counts[term])) * idf)
                   for term in counts if term in weights for idx, idf in [weights[term]])
    # Keep unknown terms in the query norm to avoid over-scoring incidental matches.
    unknown = sum((2 * (1 + math.log(count))) ** 2 for term, count in counts.items() if term not in weights)
    norm = math.sqrt(sum(value ** 2 for _, value in pairs) + unknown)
    return models.SparseVector(indices=[idx for idx, _ in pairs],
                               values=[value / norm for _, value in pairs])


def dense(client, model, texts):
    response = client.embeddings.create(model=model, input=texts, dimensions=512)
    return [item.embedding for item in sorted(response.data, key=lambda item: item.index)]


def build_index():
    records = collect()
    source = CHUNKS.read_bytes()
    model = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
    client = openai_client()
    if not client:
        model = None
    fingerprint = hashlib.sha256(source + f"|v1|{model}".encode()).hexdigest()[:20]
    collection = f"dev_docs_{fingerprint}"
    texts = [f"{row['technology']} {row['title']} {row['heading']}\n{row['excerpt']}" for row in records]
    weights = fit(texts)
    with closing(QdrantClient(path=str(DATA / "qdrant"))) as db:
        if not db.collection_exists(collection) or db.count(collection, exact=True).count != len(records):
            if db.collection_exists(collection):
                db.delete_collection(collection)
            db.create_collection(
                collection,
                vectors_config={"dense": models.VectorParams(size=512, distance=models.Distance.COSINE)} if model else {},
                sparse_vectors_config={"sparse": models.SparseVectorParams()},
            )
            for start in range(0, len(records), 48):
                batch = texts[start:start + 48]
                vectors = dense(client, model, batch) if model else [None] * len(batch)
                points = []
                for offset, (text, vector) in enumerate(zip(batch, vectors, strict=True)):
                    row = start + offset
                    named = {"sparse": sparse(text, weights)}
                    if vector is not None:
                        named["dense"] = vector
                    points.append(models.PointStruct(id=row, vector=named, payload=records[row]))
                db.upsert(collection, points=points, wait=True)
        config = dict(collection=collection, embedding_model=model, weights=weights, chunks=len(records),
                      documents=len({row["document_id"] for row in records}))
        pending = INDEX.with_suffix(".tmp")
        pending.write_text(json.dumps(config, ensure_ascii=False), encoding="utf-8")
        pending.replace(INDEX)
    return config


class SearchIndex:
    def __init__(self):
        self.config = json.loads(INDEX.read_text(encoding="utf-8"))
        self.db = QdrantClient(path=str(DATA / "qdrant"))
        self.openai = openai_client()
        self.lock = Lock()

    def search(self, question, *, use_dense=True):
        model = self.config["embedding_model"]
        query = None
        if use_dense and model and self.openai:
            try:
                query = dense(self.openai, model, [question])[0]
            except OpenAIError:
                pass
        lexical = sparse(question, self.config["weights"])
        streams = []
        with self.lock:
            if query:
                streams.append(self.query(query, "dense", 0.30))
            if lexical.indices:
                streams.append(self.query(lexical, "sparse", 0.12))
        # Reciprocal rank fusion favors chunks returned by both retrieval methods.
        scores = Counter()
        points = {}
        for stream in streams:
            for rank, point in enumerate(stream, start=1):
                scores[point.id] += 1 / (10 + rank)
                points[point.id] = point
        selected = {}
        for point_id, score in scores.most_common():
            payload = points[point_id].payload
            doc_id = payload["document_id"]
            if doc_id not in selected:
                selected[doc_id] = {**payload, "score": round(score, 4), "number": len(selected) + 1}
            if len(selected) == TOP_K:
                break
        return list(selected.values())

    def query(self, query, using, minimum):
        return self.db.query_points(self.config["collection"], query=query, using=using,
                                    limit=12, score_threshold=minimum).points


if __name__ == "__main__":
    config = build_index()
    print(f"{config['documents']} documents, {config['chunks']} chunks, embedding={config['embedding_model']}")
