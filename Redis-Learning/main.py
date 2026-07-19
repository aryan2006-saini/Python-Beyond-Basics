from fastapi import FastAPI
from redis import Redis
import httpx
import json

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    app.state.redis = Redis(
        host="localhost",
        port=6379,
        decode_responses=True
    )
    app.state.http_client = httpx.AsyncClient()


@app.on_event("shutdown")
async def shutdown_event():
    app.state.redis.close()
    await app.state.http_client.aclose()


@app.get("/")
async def home():
    return {"message": "Welcome to FastAPI!"}


@app.get("/posts")
async def get_posts():
    value = app.state.redis.get("posts")

    if value is None:
        response = await app.state.http_client.get(
            "https://jsonplaceholder.typicode.com/posts"
        )
        response.raise_for_status()

        value = response.json()

        app.state.redis.set("posts", json.dumps(value))

        return value

    return json.loads(value)