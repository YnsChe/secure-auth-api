from pydantic import BaseModel, constr

class UserInput(BaseModel):
    username: constr(strip_whitespace=True, min_length=3, max_length=20)
    password: constr(min_length=8)

class UserOutput(BaseModel):
    username: str