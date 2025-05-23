from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class BaseUser(BaseModel):
    user_id: int
    number: Optional[str] = None
    balance: Decimal
    orders_count: int
    positive_reviews: int
    negative_reviews: int
    created_at: datetime


class CreateUser(BaseModel):
    user_id: int
    number: str
    created_at: datetime
    

class GetUser(BaseUser):
    pass