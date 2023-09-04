from collections.abc import Callable, Awaitable
from typing import Any, Dict

from sqlalchemy.ext.asyncio import AsyncSession

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from src.db.database import Database
from src.bot.dtos import DatabaseDTO


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
