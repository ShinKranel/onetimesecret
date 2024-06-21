import uuid

from sqlalchemy import Column, Integer, String, UUID
from sqlalchemy.orm import mapped_column, Mapped

from backend.src.db import Base


class Secret(Base):
    __tablename__ = 'secret'

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    secret_key: Mapped[str] = mapped_column(String(length=200), nullable=False)
    message: Mapped[str] = mapped_column(String(length=2000), nullable=False)

