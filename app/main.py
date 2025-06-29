from fastapi import FastAPI
from app.api.joke import router as joke_router

app = FastAPI()
app.include_router(joke_router)