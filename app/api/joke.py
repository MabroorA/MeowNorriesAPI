from fastapi import APIRouter, HTTPException
from app.config import CHUCK_NORRIS_API_URL

from app.services.joke_service import fetch_chuck_norris_joke

router = APIRouter()

@router.get("/joke")
async def get_joke():
    try:
        joke = await fetch_chuck_norris_joke()
    except Exception:
        raise HTTPException(status_code=503, detail="Failed to fetch joke from external service.")
    return {"joke": joke}