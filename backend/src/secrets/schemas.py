from pydantic import BaseModel, Field


class CreateSecret(BaseModel):
    message: str = Field(max_length=2000)
    secret_key: str = Field(max_length=255)


class ReadSecret(BaseModel):
    message: str


class CheckSecret(BaseModel):
    secret_key: str = Field(max_length=255)
