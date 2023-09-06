from collections.abc import Callable, Awaitable
from typing import Any, Dict

from sqlalchemy.ext.asyncio import AsyncSession

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from src.db.database import Database
from src.bot.dtos import DatabaseDTO, UserDTO


class RoleMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: DatabaseDTO | UserDTO,
    ) -> Any:
        db: Database = data['db']
        data['role'] = await db.user.get_role(user_id=event.from_user.id)

        return await handler(event, data)
