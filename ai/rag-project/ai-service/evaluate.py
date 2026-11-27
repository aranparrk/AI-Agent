"""Measure document retrieval on questions excluded from the fitted corpus."""
import argparse
import json
from contextlib import closing
from pathlib import Path

from rag import SearchIndex, TOP_K

EVALUATION = Path(__file__).parent / "evaluation"


def evaluate(index, questions, use_dense):
    cases = []
    for question, expected in questions:
        hits = index.search(question, use_dense=use_dense)
        retrieved = [hit["document_id"] for hit in hits]
        rank = next((i for i, doc in enumerate(retrieved, 1) if doc in expected), None)
        cases.append(dict(question=question, expected=expected, retrieved=retrieved, rank=rank))
    answerable = [row for row in cases if row["expected"]]
    outside = [row for row in cases if not row["expected"]]
    return dict(
        top_k=TOP_K,
        retrieval="hybrid" if use_dense else "sparse",
        hit_rate=round(sum(row["rank"] is not None for row in answerable) / len(answerable), 4),
        mrr=round(sum(1 / row["rank"] for row in answerable if row["rank"]) / len(answerable), 4),
        out_of_scope_abstention=round(sum(not row["retrieved"] for row in outside) / len(outside), 4),
        cases=cases,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sparse", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    questions = json.loads((EVALUATION / "questions.json").read_text(encoding="utf-8"))
    index = SearchIndex()
    with closing(index.db):
        use_dense = not args.sparse and bool(index.config["embedding_model"] and index.openai)
        result = evaluate(index, questions, use_dense)
    print(json.dumps({key: value for key, value in result.items() if key != "cases"}, indent=2))
    if args.output:
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
