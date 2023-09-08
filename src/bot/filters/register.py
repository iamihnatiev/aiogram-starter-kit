from aiogram.filters import BaseFilter
from aiogram.types import Message

from src.db import Database


class RegisterFilter(BaseFilter):
    async def __call__(self, message: Message, db: Database) -> bool:
        return not await db.user.exist(user_id=message.from_user.id)
