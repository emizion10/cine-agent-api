from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, CheckConstraint
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum
from src.db.base_class import Base

class WatchStatus(str, enum.Enum):
    PENDING = "pending"
    WATCHING = "watching"
    WATCHED = "watched"
    DROPPED = "dropped"

class Watchlist(Base):
    __tablename__ = "watchlist"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    movie_id = Column(Integer, nullable=False)  # TMDB movie ID
    status = Column(String(20), nullable=False, default=WatchStatus.PENDING.value)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationship with User model
    user = relationship("User", back_populates="watchlist")

    __table_args__ = (
        CheckConstraint(
            "status IN ('pending', 'watching', 'watched', 'dropped')",
            name="watchlist_status_check"
        ),
    ) 