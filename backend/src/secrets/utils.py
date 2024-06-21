from backend.src.config import settings


def get_secret_link(secret_id):
    return f"{settings.SECRET_LINK_DEV}{secret_id}"
