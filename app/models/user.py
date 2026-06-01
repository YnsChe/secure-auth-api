from pydantic import BaseModel, constr

"""
Pydantic models for user input/output.

Login and registration are separated so that we can:
- Enforce stricter password rules on registration,
- Avoid hinting password rules during login.
"""

class UserRegister(BaseModel):
    username: constr(strip_whitespace=True, min_length=3, max_length=20)
    password: constr(min_length=8)

class UserLogin(BaseModel):
    username: str
    password: str

class UserOutput(BaseModel):
    username: str