from typing import Optional
from dataclasses import dataclass

from src.db import Database
from src.bot.dtos.user import UserDTO


@dataclass
class UserService:
    db: Database

    async def get_user(self, user_id: int) -> Optional[UserDTO]:
        # TODO
        return await self.db.user.get(ident=user_id)
