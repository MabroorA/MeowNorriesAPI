from fastapi import APIRouter
from app.config import CHUCK_NORRIS_API_URL

from app.services.joke_service import fetch_chuck_norris_joke

router = APIRouter()

@router.get("/joke")
async def get_joke():
    joke = await fetch_chuck_norris_joke()
    return {"joke": joke}