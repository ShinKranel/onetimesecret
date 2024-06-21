from fastapi import APIRouter

from backend.src.secrets.schemas import CreateSecret

router = APIRouter()


@router.post("/generate")
def generate_secret_key(new_secret: CreateSecret):
    return new_secret
