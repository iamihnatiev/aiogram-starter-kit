from collections.abc import Awaitable, Callable
from typing import Any, Dict

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from sqlalchemy.ext.asyncio import AsyncSession

from aiogram_starter_kit.db import Database
from aiogram_starter_kit.dtos import DatabaseDTO


class DatabaseMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: DatabaseDTO,
    ) -> Any:
        async with AsyncSession(bind=data["engine"]) as session:
            data["db"] = Database(session=session)

            return await handler(event, data)
