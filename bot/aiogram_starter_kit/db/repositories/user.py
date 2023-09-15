from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from aiogram_starter_kit.db.entities import User
from aiogram_starter_kit.enums import Gender, Role

from .abstract import Repository


class UserRepository(Repository[User]):
    def __init__(self, session: AsyncSession):
        """
        Initialize the UserRepository.

        Args:
            session (AsyncSession): An asynchronous SQLAlchemy session.

        Note: The `entity` argument is not specified here as it's automatically set to the `User` type.
        """
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
        """
        Create and add a new User entity to the database.
        """
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
        """
        Retrieve a User entity by its user ID.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Optional[User]: The retrieved User entity or None if not found.
        """
        statement = select(User).where(User.user_id == user_id)
        result = await self.session.execute(statement)

        return result.scalar_one_or_none()

    async def get_role(self, user_id: int) -> Role:
        """
        Retrieve the role of a user by their user ID.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Role: The user's role or Role.UNKNOWN if the user is not found.
        """
        user = await self.get_by_user_id(user_id)

        if not user:
            return Role.UNKNOWN

        return user.role

    async def exist(self, user_id: int) -> bool:
        """
        Check if a user with a given user ID exists in the database.

        Args:
            user_id (int): The ID of the user.

        Returns:
            bool: True if the user exists, False otherwise.
        """
        user = await self.get_by_user_id(user_id)

        return user is not None
