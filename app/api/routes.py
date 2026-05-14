from fastapi import APIRouter
from app.models.user import User
#from app.db.database import *
from app.services.user_managment import login_user, register_user

router = APIRouter()

@router.get("/")
def welcome():
    return {"message": "Welcome to the Webapp."}

@router.post("/register/")
def register(user: User):
    register_user(user.username, user.password)
    return {"new user registred: ": user.username}


@router.post("/delete/")
def delete(user: User):
    print("Welcome to deleteing users")
    #delete_user(user.username)
    return {"deleted user: ": user.username}


@router.post("/login/")
def login(user: User):
    login_user(user.username, user.password)
    return {"Login Succeeded."}


@router.get("/users/")
async def users():
    print("message Welcome to the users page.")
    #return get_users()
