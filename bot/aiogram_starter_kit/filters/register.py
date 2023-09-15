from aiogram.filters import BaseFilter
from aiogram.types import Message

from aiogram_starter_kit.db import Database


class RegisterFilter(BaseFilter):
    """
    A custom filter for checking if a user is not registered.

    This filter is used to restrict access to certain commands or actions to unregistered users.

    Returns:
        bool: True if the user is not registered, False otherwise.
    """

    async def __call__(self, message: Message, db: Database) -> bool:
        return not await db.user.exist(user_id=message.from_user.id)
