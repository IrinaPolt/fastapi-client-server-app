import httpx
from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/result/")
async def result(
    data: dict
):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://server:8001/", json=data)
        response_data = response.json()
    return response_data


@app.post("/query/")
async def query(
        number: str = Form(...),
        longitude: str = Form(...),
        latitude: str = Form(...)
):
    data = {"number": number, "longitude": longitude, "latitude": latitude}
    response = await result(data)
    return response


@app.get("/ping/")
async def ping():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://server:8001/")
        response_data = response.json()
    return response_data
