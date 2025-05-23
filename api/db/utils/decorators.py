from functools import wraps

from db import async_session
from utils.logger import api_logger


def connection(autocommit: bool = True):
    def handler(func):
        @wraps(func)
        async def wrapper(*args):
            async with async_session() as session:
                try:
                    await func(session, *args)
                    if autocommit:
                        await session.commit()
                except Exception as e:
                    api_logger.error(e)
                    await session.rollback()
        return wrapper
    return handler