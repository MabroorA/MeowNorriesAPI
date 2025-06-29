import httpx
from app.config import CHUCK_NORRIS_API_URL

async def fetch_chuck_norris_joke():
    async with httpx.AsyncClient() as client:
        response = await client.get(CHUCK_NORRIS_API_URL)
        response.raise_for_status()
        joke = response.json()["value"]
        return joke.replace("Chuck Norris", "Meow Norris")