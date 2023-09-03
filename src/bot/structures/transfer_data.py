from typing import TypedDict

from sqlalchemy.ext.asyncio import AsyncEngine

from src.db.database import Database


class TransferData(TypedDict):
    engine: AsyncEngine

    db: Database
