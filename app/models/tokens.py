"""Pydantic models for tokens."""
from pydantic import BaseModel

ACCESS_TOKEN_EXPIRE_MINUTES = 5

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None