from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from app.cores.authentication import get_current_user
from app.db.database import get_users, get_db
from app.models.user import UserRegister, UserOutput, UserLogin
from app.services.user_managment import register_user, delete_user, login_user

"""HTTP API routes for user registration, login, listing, and deletion."""
router = APIRouter()

@router.get("/")
def welcome():
    """Simple health/welcome endpoint."""
    return {"message": "Welcome to the Webapp."}

@router.post("/register/")
def register(user: UserRegister, conn = Depends(get_db)):
    """Register a new user."""
    try:
        register_user(conn, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return UserOutput(username=user.username)

@router.post("/login/")
def login(user: UserLogin, conn = Depends(get_db)):
    """Authenticate a user."""
    try:
        login_user(conn, user)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    return {"Login succeded"}

@router.get("/users/")
def users(conn = Depends(get_db)) -> list:
    """Return all users (usernames)."""
    try:
        users_list = get_users(conn)
    except SystemError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return users_list

@router.delete("/user/")
def delete(user: UserLogin, conn = Depends(get_db)):
    """Delete a user after credential verification."""
    try:
        delete_user(conn, user)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    return {"deleted user: " : user.username}

@router.get("/protected/")
def protected(current_user: Annotated[str, Depends(get_current_user)]) -> str:
    """A protected endpoint that requires authentication."""
    return current_user