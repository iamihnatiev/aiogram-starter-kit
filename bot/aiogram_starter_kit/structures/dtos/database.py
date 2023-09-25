from typing import TypedDict

from sqlalchemy.ext.asyncio import AsyncEngine

from db import Database


class DatabaseDTO(TypedDict):
    engine: AsyncEngine

    db: Database
