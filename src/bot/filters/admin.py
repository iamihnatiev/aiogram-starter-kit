from aiogram.filters import BaseFilter
from aiogram.types import Message

from src.bot.enums import Role
from src.db import Database


class AdminFilter(BaseFilter):
    async def __call__(self, message: Message, db: Database) -> bool:
        user_role = await db.user.get_role(user_id=message.from_user.id)

        return user_role == Role.ADMINISTRATOR
