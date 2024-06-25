import uuid
from datetime import datetime

from sqlalchemy import String, UUID
from sqlalchemy.orm import mapped_column, Mapped

from backend.src.db import Base
from backend.src.secrets.utils import get_expire_datetime


class Secret(Base):
    __tablename__ = 'secret'

    id: Mapped[UUID] = mapped_column(
        UUID, primary_key=True, default=uuid.uuid4
    )
    secret_key: Mapped[str] = mapped_column(
        String(length=200), nullable=False
    )
    message: Mapped[str] = mapped_column(
        String(length=2000), nullable=False
    )
    expire: Mapped[datetime] = mapped_column(
        nullable=False, default=get_expire_datetime
    )

