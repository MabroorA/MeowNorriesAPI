from fastapi import APIRouter

router = APIRouter()

async def fetch_joke():
    return "Meow Norris is unstoppable!"

@router.get("/joke")
async def get_joke():
    joke = fetch_joke()
    return {"joke": joke}
