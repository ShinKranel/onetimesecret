from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.db import get_async_session
from backend.src.secrets.models import Secret
from backend.src.secrets.schemas import CreateSecret, ReadSecret

router = APIRouter()


@router.get("/secrets")
async def read_secrets(session: AsyncSession = Depends(get_async_session)):
    query = select(Secret)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/secrets/{secret_id}", response_model=ReadSecret)
async def read_secrets(
        secret_id: UUID4,
        session: AsyncSession = Depends(get_async_session)
):
    secret = await session.get(Secret, secret_id)
    if not secret:
        raise HTTPException(status_code=404, detail="Secret not found")
    return secret


@router.post("/generate")
async def create_secret(
        new_secret: CreateSecret,
        session: AsyncSession = Depends(get_async_session)
):
    stmt = insert(Secret).values(**new_secret.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"status": "ok"}
