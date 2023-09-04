from sqlalchemy import BigInteger, Text, Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.bot.enums import Role, Gender
from .base import BaseEntity


class User(BaseEntity):
    __tablename__ = 'user_account'

    user_id: Mapped[int] = mapped_column(
        BigInteger, unique=True, nullable=False,
    )

    user_name: Mapped[str] = mapped_column(
        Text, unique=False, nullable=True,
    )

    first_name: Mapped[str] = mapped_column(
        Text, unique=False, nullable=True,
    )

    second_name: Mapped[str] = mapped_column(
        Text, unique=False, nullable=True,
    )

    role: Mapped[Role] = mapped_column(
        Enum(Role), default=Role.USER,
    )

    gender: Mapped[Gender] = mapped_column(
        Enum(Gender), default=Gender.UNKNOWN,
    )