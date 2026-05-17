from fastapi import APIRouter
from app.db.database import get_users
from app.models.user import User
from app.services.user_managment import login_user, register_user, delete_user

router = APIRouter()

@router.get("/")
def welcome():
    return {"message": "Welcome to the Webapp."}

@router.post("/register/")
def register(user: User):
    register_user(user.username, user.password)
    return {"new user registred: ": user.username}

@router.post("/login/")
def login(user: User):
    login_user(user.username, user.password)
    return {"Login Succeeded."}

@router.get("/users/")
def users() -> list:
    print("message Welcome to the users page.")
    return get_users()

@router.delete("/user/")
def delete(user: User):
    delete_user(user.username, user.password)
    return {"deleted user: " : user.username}
