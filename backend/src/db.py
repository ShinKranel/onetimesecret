from typing import AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from backend.src.config import settings

engine = create_engine(url=settings.DATABASE_URL, pool_size=10, max_overflow=20)
async_engine = create_async_engine(url=settings.DATABASE_URL_ASYNC, pool_size=10, max_overflow=20)


session_maker = sessionmaker(bind=engine)
async_session_maker = async_sessionmaker(bind=async_engine)


def get_session():
    with session_maker() as session:
        yield session


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


class Base(DeclarativeBase):
    pass
