from datetime import datetime
from typing import TypedDict

from src.bot.enums import Role, Gender


class UserDTO(TypedDict):
    id: int

    user_id: int

    phone_number: str

    username: str

    first_name: str

    last_name: str

    middle_name: str

    role: Role

    gender: Gender

    created_at: datetime

    updated_at: datetime
