from sqlalchemy.ext.asyncio import AsyncSession

from src.db.entities import User
from .abstract import Repository


class UserRepository(Repository[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session, entity=User)
