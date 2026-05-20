from fastapi import APIRouter, HTTPException, Depends
from app.db.database import get_users, get_db
from app.models.user import UserInput
from app.services.user_managment import login_user, register_user, delete_user

router = APIRouter()

@router.get("/")
def welcome():
    return {"message": "Welcome to the Webapp."}

@router.post("/register/")
def register(user: UserInput, conn = Depends(get_db)):
    try:
        UserInput.model_validate(user)
        register_user(conn, user.username, user.password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return UserInput(username=user.username, password=user.password)

@router.post("/login/")
def login(user: UserInput, conn = Depends(get_db)):
    login_user(conn, user.username, user.password)
    return {"Login Succeeded."}

@router.get("/users/")
def users(conn = Depends(get_db)) -> list:
    print("message Welcome to the users page.")
    return get_users(conn)

@router.delete("/user/")
def delete(user: UserInput, conn = Depends(get_db)):
    delete_user(conn, user.username, user.password)
    return {"deleted user: " : user.username}
