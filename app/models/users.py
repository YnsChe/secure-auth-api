"""
Pydantic models for user input/output.

Login and registration are separated so that we can:
- Enforce stricter password rules on registration,
- Avoid hinting password rules during login.
- Added UserInDB for getting the hashed pwd directly for the DB.
"""
from typing import Annotated

from pydantic import BaseModel, StringConstraints


Username = Annotated[str, StringConstraints(strip_whitespace=True, min_length=3, max_length=20)]
Password = Annotated[str, StringConstraints(min_length=8)]


class UserRegister(BaseModel):
    username:  Username
    password: Password


class UserLogin(BaseModel):
    username: str
    password: str


class UserInDB(BaseModel):
    username: Username
    hashed_password: str
    role: str


class UserOutput(BaseModel):
    username: Username
