from pydantic import BaseModel, Field


class CreateSecret(BaseModel):
    secret: str
    code_phrase: str


class ReadSecret(BaseModel):
    code_phrase: str
