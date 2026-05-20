from pydantic import BaseModel

class UserInput(BaseModel):
    username: str
    password: str

class UserOutput(BaseModel):
    username: str