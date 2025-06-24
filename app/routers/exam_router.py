from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def run():
    return {"message": "exam is running"}