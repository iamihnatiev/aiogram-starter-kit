from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from .repositories import UserRepository


def get_engine(url: str | URL) -> AsyncEngine:
    return create_async_engine(url=url, echo=True, pool_pre_ping=True)


class Database:
    session: AsyncSession

    user: UserRepository

    def __init__(
        self,
        session: AsyncSession,
        user: UserRepository = None,
    ) -> None:
        self.session = session
        self.user = user or UserRepository(session=session)
