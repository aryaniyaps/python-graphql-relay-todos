from sqlalchemy.ext.asyncio import async_sessionmaker

from app.database.engine import database_engine

async_session_factory = async_sessionmaker(
    bind=database_engine,
    expire_on_commit=False,
)
