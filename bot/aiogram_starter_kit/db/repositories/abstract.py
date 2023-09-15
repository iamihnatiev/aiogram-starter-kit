from collections.abc import Sequence
from typing import Any, Generic, Optional, Type, TypeVar

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from aiogram_starter_kit.db.entities import BaseEntity


TEntity = TypeVar("TEntity", bound=BaseEntity)


class Repository(Generic[TEntity]):
    def __init__(self, session: AsyncSession, entity: Type[TEntity]) -> None:
        """
        Initialize a repository for working with database entities.

        Args:
            session (AsyncSession): An asynchronous SQLAlchemy session.
            entity (Type[TEntity]): The type of entity this repository works with.
        """
        self.session = session
        self.entity = entity

    async def get_by_id(self, ident: int | str) -> Optional[TEntity]:
        """
        Retrieve an entity by its ID.

        Args:
            ident (int | str): The ID of the entity to retrieve.

        Returns:
            Optional[TEntity]: The retrieved entity or None if not found.
        """
        return await self.session.get(entity=self.entity, ident=ident)

    async def get_one(self, whereclause: Any) -> Optional[TEntity]:
        """
        Retrieve a single entity based on a custom WHERE clause.

        Args:
            whereclause (Any): The WHERE clause to filter the entity.

        Returns:
            Optional[TEntity]: The retrieved entity or None if not found.
        """
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
        """
        Retrieve multiple entities based on a custom WHERE clause with optional pagination and ordering.

        Args:
            whereclause (Any): The WHERE clause to filter the entities.
            offset (int): Offset for pagination (default is 0).
            limit (int): Maximum number of entities to retrieve (default is 100).
            order_by (Any): Optional sorting criteria.

        Returns:
            Sequence[TEntity]: A list of retrieved entities.
        """
        statement = select(self.entity).where(whereclause).offset(offset).limit(limit)

        if order_by:
            statement = statement.order_by(order_by)

        result = await self.session.execute(statement)

        return result.scalars().all()

    async def add(self, record: TEntity) -> TEntity:
        """
        Add a new entity to the database.

        Args:
            record (TEntity): The entity to add.

        Returns:
            TEntity: The added entity.
        """
        async with self.session.begin():
            self.session.add(record)
            await self.session.flush()

        return record

    async def update(self, record: TEntity) -> TEntity:
        """
        Update an existing entity in the database.

        Args:
            record (TEntity): The entity to update.

        Returns:
            TEntity: The updated entity.
        """
        async with self.session.begin():
            await self.session.merge(record)
            await self.session.flush()

        return record

    async def remove(self, whereclause: Any) -> None:
        """
        Remove entities from the database based on a custom WHERE clause.

        Args:
            whereclause (Any): The WHERE clause to filter the entities to be removed.
        """
        statement = delete(self.entity).where(whereclause)
        await self.session.execute(statement)
