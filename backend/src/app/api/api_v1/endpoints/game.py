from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import deps
from app.schemas.game import Game
from app import crud
router = APIRouter()

@router.get("/", response_model=list[Game])
async def get_games(
    db: AsyncSession = Depends(deps.get_db),
    page: int = 0,
    limit: int = 10,
):
    return await crud.game.get_multi(
        db=db,
        skip=page * limit,
        limit=limit,
    )

