"""HTTP API routes for user registration, login, listing, and deletion."""
from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.cores.authentication import get_current_user
from app.cores.rate_limit import LOGIN_RATE_LIMIT
from app.db.database import get_db
from app.models.users import UserRegister, UserOutput, UserLogin, UserInDB
from app.services.user_service import register_user, delete_service, login_user, list_users_service, update_service

router = APIRouter()

@router.get("/")
def welcome():
    """Simple health/welcome endpoint."""
    return {"message": "Welcome to the Webapp."}


@router.post("/register/", response_model=UserOutput)
def register(user: UserRegister, conn=Depends(get_db)):
    """Register a new user."""
    try:
        register_user(conn, user)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    return UserOutput(username=user.username)


@router.post("/login/", dependencies=[Depends(LOGIN_RATE_LIMIT)])
def login(user: UserLogin, conn=Depends(get_db)):
    """login a user."""
    try:
        token = login_user(conn, user)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    return {"access_token": token, "token_type": "bearer"}


@router.post("/token", dependencies=[Depends(LOGIN_RATE_LIMIT)])
def oauth2_login(form_data: OAuth2PasswordRequestForm = Depends(), conn=Depends(get_db)):
    """Login using OAuth2 Form"""
    user = UserLogin(username=form_data.username, password=form_data.password)
    try:
        token = login_user(conn, user)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    return {"access_token": token, "token_type": "bearer"}


@router.get("/users/")
def list_users(current_user: Annotated[UserInDB, Depends(get_current_user)], conn=Depends(get_db)):
    """Return all users (usernames)."""
    try:
        return list_users_service(conn, current_user)
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))


@router.get("/user/me", response_model=UserOutput)
def read_users_me(current_user: Annotated[UserInDB, Depends(get_current_user)]):
    """Returns logged in user"""
    return UserOutput(username=current_user.username)


@router.delete("/user/{user_name}")
def delete_user(user_name: str, current_user: Annotated[UserInDB, Depends(get_current_user)], conn=Depends(get_db)):
    """Delete a user after credential verification."""
    try:
        delete_service(conn, current_user, user_name)
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    return {"deleted user: ": user_name}


@router.put("/user/{user_name}/{role}")
def update_user_role(user_name: str, role: str, current_user: Annotated[UserInDB, Depends(get_current_user)],
                     conn=Depends(get_db)):
    """Update an attribute of an existing user"""
    try:
        update_service(conn, current_user, user_name, role)
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    return "Role updated successfully"
