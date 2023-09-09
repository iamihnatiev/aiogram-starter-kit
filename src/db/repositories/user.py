from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .abstract import Repository
from src.db.entities import User
from src.bot.enums import Role, Gender


class UserRepository(Repository[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session, entity=User)

    async def new(
        self,
        user_id: int,
        username: str | None = None,
        phone_number: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        middle_name: str | None = None,
        role: Role | None = Role.USER,
        gender: Gender | None = Gender.UNKNOWN,
    ) -> None:
        await self.add(
            User(
                user_id=user_id,
                username=username,
                phone_number=phone_number,
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                role=role,
                gender=gender,
            )
        )

    async def get_by_user_id(self, user_id: int) -> Optional[User]:
        statement = select(User).where(User.user_id == user_id)
        result = await self.session.execute(statement)

        return result.scalar_one_or_none()

    async def get_role(self, user_id: int) -> Role:
        user = await self.get_by_user_id(user_id)

        return user.role

    async def exist(self, user_id: int) -> bool:
        user = await self.get_by_user_id(user_id)

        return user is not None
