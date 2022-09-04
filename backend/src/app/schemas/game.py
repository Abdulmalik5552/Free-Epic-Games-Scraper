from datetime import datetime
from pydantic import BaseModel, validator, Field
from datetime import datetime, timezone


class GameCreate(BaseModel):
    title: str
    start_date: datetime
    end_date: datetime
    is_free_now: bool = Field(default=False)
    # TODO: Add is_purchased, and URL to purchase.
    
    @validator('start_date')
    def start_date_zone(cls, v: datetime):
        if v.tzinfo is timezone.utc:
            return v.replace(tzinfo=timezone.utc).astimezone(tz=None).replace(tzinfo=None)
        return v

    @validator('end_date')
    def end_date_zone(cls, v: datetime):
        if v.tzinfo is timezone.utc:
            return v.replace(tzinfo=timezone.utc).astimezone(tz=None).replace(tzinfo=None)
        return v

    @validator('is_free_now', always=True,)
    def set_free_game_now(cls, v: bool, values):
        return values["start_date"] == values["end_date"]
    

class Game(GameCreate):
    id: int

    class Config:
        orm_mode = True

class GameUpdate(BaseModel):
    title: str | None
    start_date: datetime | None
    end_date: datetime | None
    is_free_now: bool | None
