import httpx
import random
import time
from fastapi import FastAPI, Form
from pydantic import BaseModel, constr, StrictFloat

app = FastAPI()


class QueryModel(BaseModel):
    number: constr(min_length=5, max_length=20)
    longitude: StrictFloat
    latitude: StrictFloat


@app.post("/query/")
async def query(
        data: QueryModel
):
    response = await result(data.dict())
    return response


@app.post("/result/")
async def result(
    data: dict
):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://server:8000/", json=data)
        time.sleep(45)
        response_data = response.json()
    return response_data


@app.get("/ping/")
async def ping():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://server:8000/")
    if response.status_code == 200:
        return 'pong'
    else:
        return 'something went wrong'


@app.get("/")
async def ping():
    return 'pong'


@app.post("/")
async def check(data: dict):
    random.seed(15)
    response = random.choice([True, False])
    return response
