from fastapi import APIRouter, HTTPException, Depends
from app.db.database import get_users, get_db
from app.models.user import UserRegister, UserOutput, UserLogin
from app.services.user_managment import login_user, register_user, delete_user

router = APIRouter()

@router.get("/")
def welcome():
    return {"message": "Welcome to the Webapp."}

@router.post("/register/")
def register(user: UserRegister, conn = Depends(get_db)):
    try:
        register_user(conn, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return UserOutput(username=user.username)

@router.post("/login/")
def login(user: UserLogin, conn = Depends(get_db)):
    try:
        login_user(conn, user)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    return {"Login Succeeded."}

@router.get("/users/")
def users(conn = Depends(get_db)) -> list:
    try:
        users_list = get_users(conn)
    except SystemError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return users_list

@router.delete("/user/")
def delete(user: UserLogin, conn = Depends(get_db)):
    try:
        delete_user(conn, user)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    return {"deleted user: " : user.username}
