from aiogram.filters import BaseFilter
from aiogram.types import Message

from aiogram_starter_kit.structures.enums import Role
from db import Database


class AdminFilter(BaseFilter):
    """
    A custom filter for checking if a user has the 'Administrator' role.

    This filter is used to restrict access to certain commands or actions to users with the 'Administrator' role.

    Returns:
        bool: True if the user has the 'Administrator' role, False otherwise.
    """

    async def __call__(self, message: Message, db: Database) -> bool:
        user_role = await db.user.get_role(user_id=message.from_user.id)

        return user_role == Role.ADMINISTRATOR
