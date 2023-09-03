from typing import TypeVar, Generic, Type, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models import BaseModel

TEntity = TypeVar('TEntity', bound=BaseModel)


class Repository(Generic[TEntity]):
    def __init__(self, session: AsyncSession, entity: Type[TEntity]) -> None:
        self.session = session
        self.entity = entity

    async def find(self, ident: int | str) -> Optional[TEntity]:
        return await self.session.get(entity=self.entity, ident=ident)
