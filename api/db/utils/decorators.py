from functools import wraps

from db import async_session
from utils.logger import api_logger


def connection(commit: bool = True, return_result: bool = False):
    def handler(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            async with async_session() as session:
                try:
                    result = await func(session, *args, **kwargs)
                    
                    if commit:
                        await session.commit()
                        
                    if return_result:
                        return result
                    
                except Exception as e:
                    api_logger.error(e)
                    await session.rollback()
                return None
        return wrapper
    return handler