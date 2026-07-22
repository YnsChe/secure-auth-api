from pydantic import BaseModel

"""
Pydantic models for tokens.
"""

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None