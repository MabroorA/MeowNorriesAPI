from fastapi import APIRouter, HTTPException
from app.config import CHUCK_NORRIS_API_URL
from app.services.joke_service import fetch_chuck_norris_joke
import re

router = APIRouter()

@router.get("/joke")
async def get_joke():
    try:
        joke_data = await fetch_chuck_norris_joke()
        joke = joke_data["value"]
        modified_joke = re.sub(r"Chuck Norris", "Meow Norris", joke, flags=re.IGNORECASE)
        return {"joke": modified_joke}
    except Exception:
        raise HTTPException(status_code=503, detail="Failed to fetch joke from external API")
