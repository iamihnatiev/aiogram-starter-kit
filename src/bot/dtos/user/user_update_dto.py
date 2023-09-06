from typing import TypedDict


class UserUpdateDTO(TypedDict):
    phone_number: str

    username: str

    first_name: str

    last_name: str

    middle_name: str

