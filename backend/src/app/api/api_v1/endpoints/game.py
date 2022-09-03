from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.api import deps
router = APIRouter()

@router.get("/",)
async def get_games(
    db: AsyncSession = Depends(deps.get_db),
):
    return {"Hello": "World"}

