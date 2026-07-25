from pydantic import BaseModel

"""
Pydantic models for tokens.
"""
ACCESS_TOKEN_EXPIRE_MINUTES = 5

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None