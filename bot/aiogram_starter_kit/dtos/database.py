from typing import TypedDict

from sqlalchemy.ext.asyncio import AsyncEngine

from aiogram_starter_kit.db import Database


class DatabaseDTO(TypedDict):
    engine: AsyncEngine

    db: Database
