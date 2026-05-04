from fastapi import FastAPI

from app.models import user
from app.models.user import User
from app.db.database import *

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to the Webapp."}

@app.post("/register/")
async def regitser(user: User):
    print("Welcome to the registration process.")
    add_user(user.username, user.password)
    return user
@app.post("/delete")
def delete(user: User):
    print("Wlcome to deleteing users")
    delete_user(user.username)
    return {"deleted user": user.username}

@app.post("/login")
def login(user: User):
    check_user(user.username, user.password)
    return {"Send your credentials as a RequestBody to login."}

@app.get("/users")
def get_users():
    return {"message": "Welcome to the users page."}