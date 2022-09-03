from typing import AsyncGenerator

from app.db.session import SessionLocal


async def get_db() -> AsyncGenerator:
    try:
        db = SessionLocal()
        yield db
    finally:
        await db.close()
