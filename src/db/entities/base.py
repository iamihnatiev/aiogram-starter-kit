from datetime import datetime

from sqlalchemy import DateTime, Integer, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseEntity(DeclarativeBase):
    __allow_unmapped__ = False

    id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now(),
    )
