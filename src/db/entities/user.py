from sqlalchemy import BigInteger, Enum, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.bot.enums import Gender, Role

from .base import BaseEntity


class User(BaseEntity):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(
        BigInteger, unique=True, nullable=False,
    )

    username: Mapped[str] = mapped_column(
        Text, unique=True, nullable=True,
    )

    phone_number: Mapped[str] = mapped_column(
        Text, unique=True, nullable=True,
    )

    first_name: Mapped[str] = mapped_column(
        Text, unique=False, nullable=True,
    )

    last_name: Mapped[str] = mapped_column(
        Text, unique=False, nullable=True,
    )

    middle_name: Mapped[str] = mapped_column(
        Text, unique=False, nullable=True,
    )

    role: Mapped[Role] = mapped_column(
        Enum(Role), default=Role.USER,
    )

    gender: Mapped[Gender] = mapped_column(
        Enum(Gender), default=Gender.UNKNOWN,
    )
