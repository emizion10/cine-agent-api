from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.api import deps
from src.crud import watchlist as watchlist_crud
from src.models.user import User
from src.models.watchlist import WatchStatus
from src.schemas.watchlist import Watchlist, WatchlistCreate, WatchlistUpdate

router = APIRouter()

@router.get("/", response_model=List[Watchlist])
def get_watchlist(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
    skip: int = 0,
    limit: int = 100,
    status: Optional[WatchStatus] = None
):
    """
    Get user's watchlist with optional status filter.
    """
    return watchlist_crud.get_user_watchlist(
        db=db,
        user_id=current_user.id,
        skip=skip,
        limit=limit,
        status=status
    )

@router.post("/{movie_id}", response_model=Watchlist)
def add_to_watchlist(
    movie_id: int,
    watchlist_in: WatchlistCreate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user)
):
    """
    Add a movie to user's watchlist.
    """
    if movie_id != watchlist_in.movie_id:
        raise HTTPException(
            status_code=400,
            detail="Movie ID in path must match movie ID in request body"
        )
    
    existing_item = watchlist_crud.get_watchlist_item(db, current_user.id, movie_id)
    if existing_item:
        raise HTTPException(
            status_code=400,
            detail="Movie already in watchlist"
        )
    
    return watchlist_crud.add_to_watchlist(
        db=db,
        user_id=current_user.id,
        watchlist_in=watchlist_in
    )

@router.patch("/{movie_id}", response_model=Watchlist)
def update_watchlist_status(
    movie_id: int,
    watchlist_in: WatchlistUpdate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user)
):
    """
    Update the status of a movie in user's watchlist.
    """
    watchlist_item = watchlist_crud.update_watchlist_status(
        db=db,
        user_id=current_user.id,
        movie_id=movie_id,
        watchlist_in=watchlist_in
    )
    if not watchlist_item:
        raise HTTPException(
            status_code=404,
            detail="Movie not found in watchlist"
        )
    return watchlist_item

@router.delete("/{movie_id}")
def remove_from_watchlist(
    movie_id: int,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user)
):
    """
    Remove a movie from user's watchlist.
    """
    success = watchlist_crud.remove_from_watchlist(
        db=db,
        user_id=current_user.id,
        movie_id=movie_id
    )
    if not success:
        raise HTTPException(
            status_code=404,
            detail="Movie not found in watchlist"
        )
    return {"message": "Movie removed from watchlist"} 