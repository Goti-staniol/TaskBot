from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker, 
    AsyncSession
)

from data.config import DB_URL


Base = declarative_base()
engine = create_async_engine(DB_URL, echo=False)
async_session = async_sessionmaker(
    engine, 
    class_=AsyncSession,
    expire_on_commit=False
)
