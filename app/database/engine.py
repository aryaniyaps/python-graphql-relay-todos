from sqlalchemy.ext.asyncio import (
    create_async_engine,
)

from app.config import settings

database_engine = create_async_engine(
    url=str(settings.database_url),
    echo=settings.debug,
    pool_size=settings.database_pool_size,
    pool_use_lifo=True,
    pool_pre_ping=True,
)
