from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.game import Game
from app.schemas.game import GameCreate, GameUpdate


class CRUDGame(CRUDBase[Game, GameCreate, GameUpdate]):
    async def create_with_owner(
        self, db: AsyncSession, *, obj_in: GameCreate, owner_id: int
    ) -> Game:
        pass

game = CRUDGame(Game)
