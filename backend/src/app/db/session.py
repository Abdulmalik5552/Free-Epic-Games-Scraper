from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, future=True)
SessionLocal = sessionmaker(
    bind=engine,
    class_= AsyncSession
)
