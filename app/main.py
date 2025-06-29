from fastapi import FastAPI
from app.api.joke import router as joke_router

app = FastAPI(
    title="Meow Norris API",
    description="A Chuck Norris joke API turned Meow Norries",
    version="1.0.0"
)


@app.get("/")
async def home():
    """Welcome message for the API"""
    return {"message": "Are you ready to be entertained?"}


app.include_router(joke_router)