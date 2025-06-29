import httpx
import re
from typing import Dict, Any
from app.config import CHUCK_NORRIS_API_URL


class JokeServiceError(Exception):
    """Custom exception for joke service errors"""
    pass


async def fetch_chuck_norris_joke() -> Dict[str, Any]:
    """Fetch a joke from the Chuck Norris API"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(CHUCK_NORRIS_API_URL)
            response.raise_for_status()
            return response.json()
    except (httpx.RequestError, httpx.HTTPStatusError) as e:
        raise JokeServiceError(f"Failed to fetch joke from external API: {str(e)}")
    except KeyError:
        raise JokeServiceError("Invalid response format from external API")


def transform_joke_text(joke_text: str) -> str:
    """Transform Chuck Norris to Meow Norris in joke text"""
    return re.sub(r"Chuck Norris", "Meow Norris", joke_text, flags=re.IGNORECASE)


async def get_transformed_joke() -> str:
    """Get a joke and transform it to use Meow Norris"""
    joke_data = await fetch_chuck_norris_joke()
    
    if "value" not in joke_data:
        raise JokeServiceError("Missing 'value' field in API response")
    
    original_joke = joke_data["value"]
    return transform_joke_text(original_joke)