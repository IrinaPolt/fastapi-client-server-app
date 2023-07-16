import random
from fastapi import FastAPI, Form
from pydantic import BaseModel, Field

app = FastAPI()


class FormData(BaseModel):
    number: str = Field(..., min_length=10, max_length=20)
    longitude: str = Field(..., min_legth=10, max_length=20)
    latitude: str = Field(..., min_legth=10, max_length=20)


@app.get("/")
async def ping():
    return 'pong'


@app.post("/")
async def query(data: dict):
    FormData.parse_obj(data)
    response = random.choice([True, False])
    return response
