"""Collect pinned official Markdown and split its text by section."""
import json
import re
from pathlib import Path
from urllib.request import urlopen

DATA = Path(__file__).parent / "data"
REACT_REVISION = "e8701c4993b37d2f3cb478baae70667223e0afd5"
FASTAPI_REVISION = "05e6df7e906c3decba377c37548019973f40bf15"
SOURCES = [
    ("React", "reactjs/ko.react.dev", REACT_REVISION, f"src/content/{slug}.md",
     f"https://ko.react.dev/{slug}")
    for slug in ["reference/react/useState", "reference/react/useEffect", "reference/react/useRef",
                 "learn/thinking-in-react", "learn/sharing-state-between-components"]
] + [
    ("FastAPI", "fastapi/fastapi", FASTAPI_REVISION, f"docs/{language}/docs/tutorial/{slug}.md",
     f"https://fastapi.tiangolo.com/{'ko/' if language == 'ko' else ''}tutorial/{slug.removesuffix('/index')}/")
    for language, slug in [("ko", "path-params"), ("ko", "body"), ("ko", "dependencies/index"),
                           ("ko", "cors"), ("ko", "response-model")]
]

CODE_INCLUDE = re.compile(r"(?m)^\s*\{\*\s+\.\./\.\./(docs_src/[\w/.-]+\.py)[^\n]*?\*\}[ \t]*$")


def download(origin, local):
    if not local.exists():
        local.parent.mkdir(parents=True, exist_ok=True)
        with urlopen(origin, timeout=30) as response:
            content = response.read().decode("utf-8")
        local.write_text(content, encoding="utf-8")
    return local.read_text(encoding="utf-8")


def chunks(markdown, title):
    text = re.sub(r"\A---\n.*?\n---\s*", "", markdown, count=1, flags=re.S)
    text = re.sub(r"<!--.*?-->|\{\/\*.*?\*\/\}", "", text, flags=re.S)
    text = re.sub(r"(?m)^\s*</?[A-Z][\w.]*[^\n>]*>\s*$", "", text)
    text = re.sub(r"(?m)^\s*<img\b[^\n>]*>\s*$", "", text)
    text = re.sub(r"(?m)^\s*(?:\{!|\{\*).*?(?:!\}|\*\})\s*$", "", text)
    parts = re.split(r"(?m)^#{1,6}\s+(.+)$", text)
    for heading, body in zip([title, *parts[1::2]], parts[::2]):
        heading = re.sub(r"\s*\{\s*#.*?\}\s*$", "", heading).strip()
        body = body.strip()
        start = 0
        while start < len(body):
            end = min(start + 1100, len(body))
            if end < len(body):
                boundary = body.rfind("\n", start + 650, end)
                if boundary > start:
                    end = boundary
            excerpt = body[start:end].strip()
            if len(excerpt) >= 30:
                yield heading, excerpt
            if end == len(body):
                break
            start = end - 120


def collect():
    raw_dir = DATA / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for technology, repository, revision, path, url in SOURCES:
        origin = f"https://raw.githubusercontent.com/{repository}/{revision}/{path}"
        document_id = f"{technology.lower()}-{url.rstrip('/').rsplit('/', 1)[-1]}"
        local = raw_dir / repository / revision / path
        markdown = download(origin, local)
        if technology == "FastAPI":
            def expand(match):
                code_path = match[1]
                # Only follow Python snippets under the pinned repository's docs_src.
                if ".." in Path(code_path).parts:
                    return ""
                code_url = f"https://raw.githubusercontent.com/{repository}/{revision}/{code_path}"
                code = download(code_url, raw_dir / "snippets" / revision / code_path)
                return f"\n\n```python\n{code.rstrip()}\n```\n\n"

            markdown = CODE_INCLUDE.sub(expand, markdown)
        match = re.search(r"(?m)^(?:title:\s*|#\s+)(.+)$", markdown)
        title = match[1].strip("'\u0022 ") if match else document_id
        for heading, excerpt in chunks(markdown, title):
            records.append(dict(document_id=document_id, technology=technology, title=title,
                                heading=heading, excerpt=excerpt, url=url,
                                revision=revision, origin=origin))
    target = DATA / "processed" / "chunks.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    return records
