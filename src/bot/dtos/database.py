from typing import TypedDict

from sqlalchemy.ext.asyncio import AsyncEngine

from src.db.database import Database


class DatabaseDTO(TypedDict):
    engine: AsyncEngine

    db: Database
