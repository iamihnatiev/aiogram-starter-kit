from collections.abc import Awaitable, Callable
from typing import Any, Dict

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from sqlalchemy.ext.asyncio import AsyncSession

from src.bot.dtos import DatabaseDTO
from src.db.database import Database


class DatabaseMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: DatabaseDTO,
    ) -> Any:
        async with AsyncSession(bind=data['engine']) as session:
            data['db'] = Database(session=session)

            return await handler(event, data)
