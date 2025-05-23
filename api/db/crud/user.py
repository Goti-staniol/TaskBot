from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.utils.decorators import connection
from db.models import User


@connection()
async def create_user(
    session: AsyncSession, 
    user_id: int,
    number: str
) -> bool:
    user = User(user_id=user_id, number=number)
    session.add(user)
    return True


@connection(return_result=True)
async def get_user(
    session: AsyncSession, 
    user_id: Optional[int] = None, 
    number: Optional[str] = None
) -> Optional[User]:
    if user_id and number:
        raise ValueError('Use user_id or number, not together!')
    
    if user_id:
        stmt = select(User).filter_by(user_id=user_id)
    elif number:
        stmt = select(User).filter_by(number=number)
    
    result = await session.execute(stmt) # type: ignore
    return result.scalar_one_or_none()
    