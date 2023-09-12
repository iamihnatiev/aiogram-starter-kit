from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

from aiogram_starter_kit.configuration import conf

from .repositories import UserRepository


def get_engine(connection_url: str | URL) -> AsyncEngine:
    return create_async_engine(url=connection_url, echo=conf.debug, pool_pre_ping=True)


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
