from collections.abc import Awaitable, Callable
from typing import Any, Dict

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from sqlalchemy.ext.asyncio import AsyncSession

from aiogram_starter_kit.structures.dtos import DatabaseDTO
from db import Database


class DatabaseMiddleware(BaseMiddleware):
    """
    A custom middleware for handling database sessions.

    This middleware is responsible for managing the database session and providing it to handlers.
    It uses the 'DatabaseDTO' data transfer object to pass the database engine and session.

    Returns:
        Any: The result of calling the handler function.
    """

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: DatabaseDTO,
    ) -> Any:
        # Create a new database session within a context manager
        async with AsyncSession(bind=data["engine"]) as session:
            # Create a Database instance and attach it to the data dictionary
            data["db"] = Database(session=session)

            # Call the original handler function with the event and data
            return await handler(event, data)
