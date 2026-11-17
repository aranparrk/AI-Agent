from fastapi import FastAPI

app = FastAPI(title="Board RAG AI Service")

@app.get("/health")
async def health():
    return {"status": "OK"}
