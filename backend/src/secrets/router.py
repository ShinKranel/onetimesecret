from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.db import get_async_session
from backend.src.secrets.models import Secret
from backend.src.secrets.schemas import CreateSecret, ReadSecret, CheckSecret
from backend.src.secrets.utils import get_secret_link

router = APIRouter()


@router.post("/secrets/{secret_id}", response_model=ReadSecret)
async def read_secret(
        secret_id: UUID4,
        check_secret: CheckSecret,
        session: AsyncSession = Depends(get_async_session)
):
    """
    READ the secret message, after which it will be deleted.
    """
    # read secret message
    secret = await session.get(Secret, secret_id)
    if not secret:
        raise HTTPException(status_code=404, detail="Secret not found")
    if secret.secret_key != check_secret.secret_key:
        raise HTTPException(status_code=400, detail="Wrong secret key")

    # delete after reading
    await session.delete(secret)
    await session.commit()

    return secret


@router.post("/generate")
async def create_secret(
        new_secret: CreateSecret,
        session: AsyncSession = Depends(get_async_session)
):
    """
    CREATE the secret message and return a secret link.
    """
    secret = Secret(**new_secret.model_dump())
    session.add(secret)
    await session.commit()
    await session.refresh(secret)
    return {"Link to secret": get_secret_link(secret.id)}


@router.delete("/secrets/{secret_id}/burn")
async def delete_secret(
        secret_id: UUID4,
        session: AsyncSession = Depends(get_async_session)
):
    """
        DELETE the secret message, before it is read.
    """
    secret = await session.get(Secret, secret_id)
    if not secret:
        raise HTTPException(status_code=404, detail="Secret not found")
    await session.delete(secret)
    await session.commit()
    return {"status": "Secret burn in flames"}
