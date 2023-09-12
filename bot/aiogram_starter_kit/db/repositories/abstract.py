from collections.abc import Sequence
from typing import Any, Generic, Optional, Type, TypeVar

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from aiogram_starter_kit.db.entities import BaseEntity


TEntity = TypeVar("TEntity", bound=BaseEntity)


class Repository(Generic[TEntity]):
    def __init__(self, session: AsyncSession, entity: Type[TEntity]) -> None:
        self.session = session
        self.entity = entity

    async def get_by_id(self, ident: int | str) -> Optional[TEntity]:
        return await self.session.get(entity=self.entity, ident=ident)

    async def get_one(self, whereclause: Any) -> Optional[TEntity]:
        statement = select(self.entity).where(whereclause)
        result = await self.session.execute(statement)

        return result.scalar_one_or_none()

    async def get_many(
        self,
        whereclause: Any,
        offset: int = 0,
        limit: int = 100,
        order_by: Any = None,
    ) -> Sequence[TEntity]:
        statement = select(self.entity).where(whereclause).offset(offset).limit(limit)

        if order_by:
            statement = statement.order_by(order_by)

        result = await self.session.execute(statement)

        return result.scalars().all()

    async def add(self, record: TEntity) -> TEntity:
        async with self.session.begin():
            self.session.add(record)
            await self.session.flush()

        return record

    async def update(self, record: TEntity) -> TEntity:
        async with self.session.begin():
            await self.session.merge(record)
            await self.session.flush()

        return record

    async def remove(self, whereclause: Any) -> None:
        statement = delete(self.entity).where(whereclause)
        await self.session.execute(statement)
