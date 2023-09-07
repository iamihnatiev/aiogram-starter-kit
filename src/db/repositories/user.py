from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.entities import User
from src.bot.enums import Role
from .abstract import Repository


class UserRepository(Repository[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session, entity=User)

    async def get_role(self, user_id: int) -> Role:
        return await self.session.scalar(
            select(User.role).where(User.user_id == user_id).limit(1)
        )
