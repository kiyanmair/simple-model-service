import os

from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
from sentence_transformers import SentenceTransformer

app = FastAPI()

model_path = os.environ.get("MODEL_PATH")
model_seq_len = os.environ.get("MODEL_SEQ_LEN")

model = SentenceTransformer(model_path)
model.max_seq_length = int(model_seq_len)

class Request(BaseModel):
    text: str = Field(..., min_length=1)

    @field_validator("text")
    def check_non_whitespace(cls, value: str):
        if value.strip() == "":
            raise ValueError("value cannot be empty or contain only whitespaces")
        return value

@app.post("/embed")
async def embed(request: Request) -> list[float]:
    text = request.text
    embedding = model.encode(text, normalize_embeddings=True)
    return embedding.tolist()

@app.get("/healthcheck")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
