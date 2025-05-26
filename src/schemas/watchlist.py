from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from src.models.watchlist import WatchStatus

class WatchlistBase(BaseModel):
    movie_id: int
    status: WatchStatus = WatchStatus.PENDING

class WatchlistCreate(WatchlistBase):
    pass

class WatchlistUpdate(BaseModel):
    status: WatchStatus

class WatchlistInDBBase(WatchlistBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class Watchlist(WatchlistInDBBase):
    pass 