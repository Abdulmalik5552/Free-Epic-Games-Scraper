from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from app.crud.base import CRUDBase
from app.models.game import Game
from app.schemas.game import GameCreate, GameUpdate


class CRUDGame(CRUDBase[Game, GameCreate, GameUpdate]):
    async def get_multi(
        self, 
        db: AsyncSession,
        *, 
        skip: int = 0, 
        limit: int = 100,
    ) -> list[Game]:
        """get all games ordered by thier start date ascending.

        Args:
            db (AsyncSession): _description_
            skip (int, optional): the number of skipped rows. Defaults to 0.
            limit (int, optional): limit the number of rows. Defaults to 100.
            is_free_now (bool, optional): filter result by is_free_now. Defaults to False.

        Returns:
            list[Game]: _description_
        """
        query = select(self.model)\
            .offset(skip)\
            .limit(limit)\
            .order_by(Game.start_date)
        result : Result = await db.execute(query)
        return result.scalars().all()


game = CRUDGame(Game)
