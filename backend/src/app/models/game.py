from sqlalchemy import Boolean, Column, Integer, String, DateTime

from app.db.base_class import Base

class Game(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    start_date = Column(DateTime, index=True)
    end_date = Column(DateTime, index=True)
    is_free_now = Column(Boolean(), default=False)
