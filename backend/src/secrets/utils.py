from datetime import datetime, timedelta

from backend.src.config import settings


def get_secret_link(secret_id):
    return f"{settings.SECRET_LINK_DEV}{secret_id}"


def get_expire_datetime():
    create_datetime = datetime.now()
    expire_datetime = create_datetime + timedelta(days=7)
    return expire_datetime
