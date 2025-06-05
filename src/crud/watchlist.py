from typing import List, Optional
from sqlalchemy.orm import Session
from src.models.watchlist import Watchlist, WatchStatus
from src.schemas.watchlist import WatchlistCreate, WatchlistUpdate

def get_watchlist_item(db: Session, user_id: int, movie_id: int) -> Optional[Watchlist]:
    return db.query(Watchlist).filter(
        Watchlist.user_id == user_id,
        Watchlist.movie_id == movie_id
    ).first()

def get_user_watchlist(
    db: Session, 
    user_id: int, 
    skip: int = 0, 
    limit: int = 100,
    status: Optional[WatchStatus] = None
) -> List[Watchlist]:
    query = db.query(Watchlist).filter(Watchlist.user_id == user_id)
    if status:
        query = query.filter(Watchlist.status == status)
    return query.offset(skip).limit(limit).all()

def add_to_watchlist(
    db: Session,
    user_id: int,
    watchlist_in: WatchlistCreate
) -> Watchlist:
    db_watchlist = Watchlist(
        user_id=user_id,
        movie_id=watchlist_in.movie_id,
        status=watchlist_in.status.value
    )
    db.add(db_watchlist)
    db.commit()
    db.refresh(db_watchlist)
    return db_watchlist

def update_watchlist_status(
    db: Session,
    user_id: int,
    movie_id: int,
    watchlist_in: WatchlistUpdate
) -> Optional[Watchlist]:
    db_watchlist = get_watchlist_item(db, user_id, movie_id)
    if not db_watchlist:
        return None
    
    db_watchlist.status = watchlist_in.status
    db.commit()
    db.refresh(db_watchlist)
    return db_watchlist

def remove_from_watchlist(
    db: Session,
    user_id: int,
    movie_id: int
) -> bool:
    db_watchlist = get_watchlist_item(db, user_id, movie_id)
    if not db_watchlist:
        return False
    
    db.delete(db_watchlist)
    db.commit()
    return True 