from pydantic import BaseModel, Field


class CreateSecret(BaseModel):
    message: str
    secret_key: str


class ReadSecret(BaseModel):
    code_phrase: str
