from typing import TypedDict


class UserCreateDTO(TypedDict):
    user_id: int

    username: str

    first_name: str

    last_name: str
