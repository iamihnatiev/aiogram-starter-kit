from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

from aiogram_starter_kit.configuration import conf

from .repositories import UserRepository


def get_engine(connection_url: str | URL) -> AsyncEngine:
    """
    Create and return an asynchronous SQLAlchemy engine.

    Args:
        connection_url (str | URL): The database connection URL.

    Returns:
        AsyncEngine: An asynchronous SQLAlchemy engine.
    """
    return create_async_engine(url=connection_url, echo=conf.debug, pool_pre_ping=True)


class Database:
    """
    Represents a database connection manager.

    Attributes:
        session (AsyncSession): The asynchronous SQLAlchemy session.
        user (UserRepository): The repository for user-related database operations.
    """

    session: AsyncSession

    user: UserRepository

    def __init__(
        self,
        session: AsyncSession,
        user: UserRepository = None,
    ) -> None:
        """
        Initialize the Database manager.
        """
        self.session = session
        self.user = user or UserRepository(session=session)
