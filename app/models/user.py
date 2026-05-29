from pydantic import BaseModel, constr

'''
Seperated login and register to avoid returning password 
constraints while trying to log in and give attacker hints
about password structure.
'''
class UserRegister(BaseModel):
    username: constr(strip_whitespace=True, min_length=3, max_length=20)
    password: constr(min_length=8)

class UserLogin(BaseModel):
    username: str
    password: str

# Output just for returning as repsonce
class UserOutput(BaseModel):
    username: str