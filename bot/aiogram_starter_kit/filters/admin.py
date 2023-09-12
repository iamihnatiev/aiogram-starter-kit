from aiogram.filters import BaseFilter
from aiogram.types import Message

from aiogram_starter_kit.db import Database
from aiogram_starter_kit.enums import Role


class AdminFilter(BaseFilter):
    async def __call__(self, message: Message, db: Database) -> bool:
        user_role = await db.user.get_role(user_id=message.from_user.id)

        return user_role == Role.ADMINISTRATOR
