import pytest
from alembic import config
from app.config import settings
from app.database.session import async_session_factory
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


@pytest.fixture(scope="session")
def database_url() -> str:
    return settings.database_url


@pytest.fixture(autouse=True)
def _break_sessionmaker() -> None:
    async_session_factory.configure(bind=None)


@pytest.fixture(scope="session", name="async_sessionmaker")
def async_sessionmaker_() -> async_sessionmaker[AsyncSession]:
    return async_session_factory


@pytest.fixture(scope="session")
def alembic_config() -> config.Config | None:
    return config.Config("alembic.ini")
