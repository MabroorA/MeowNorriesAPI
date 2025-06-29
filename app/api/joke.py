from fastapi import APIRouter, HTTPException
from app.services.joke_service import get_transformed_joke, JokeServiceError

router = APIRouter()


@router.get("/joke")
async def get_joke():
    """Get a transformed Chuck Norris joke"""
    try:
        joke = await get_transformed_joke()
        return {"joke": joke}
    except JokeServiceError:
        raise HTTPException(
            status_code=503, 
            detail="Failed to fetch joke from external API"
        )
