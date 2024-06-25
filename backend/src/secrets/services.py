from datetime import datetime

from sqlalchemy import delete
from backend.src.db import async_session_maker
from backend.src.secrets.models import Secret


async def delete_expires_secrets():
    async with async_session_maker() as session:
        secrets = delete(Secret).where(datetime.now() > Secret.expire)
        await session.execute(secrets)
        await session.commit()
