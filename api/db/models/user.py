from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, Float, DateTime

from db import Base


class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    number = Column(String(18), unique=True, nullable=False)
    balance = Column(Float, default=0.0, nullable=False)
    orders_count = Column(Integer, default=0, nullable=False)
    positive_reviews = Column(Integer, default=0, nullable=False)
    negative_reviews = Column(Integer, default=0, nullable=False)
    created_at = Column(
        DateTime, 
        default=datetime.now(timezone.utc),
        nullable=False
    )