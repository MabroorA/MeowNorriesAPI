from fastapi import FastAPI
from app.api.joke import router as joke_router

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Are you ready to be entertained?"}

app.include_router(joke_router)