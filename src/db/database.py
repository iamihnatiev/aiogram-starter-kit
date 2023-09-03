from sqlalchemy.ext.asyncio import AsyncSession

from .repositories import UserRepository


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
