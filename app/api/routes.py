from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from app.cores.authentication import get_current_user
from app.db.database import get_db
from app.models.users import UserRegister, UserOutput, UserLogin
from app.services.user_service import register_user, delete_service, login_user, list_users_service, update_service
from app.cores.rate_limit import LOGIN_RATE_LIMIT

"""HTTP API routes for user registration, login, listing, and deletion."""
router = APIRouter()


@router.get("/")
def welcome():
    """Simple health/welcome endpoint."""
    return {"message": "Welcome to the Webapp."}


@router.post("/register/")
def register(user: UserRegister, conn= Depends(get_db)):
    """Register a new user."""
    try:
        register_user(conn, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return UserOutput(username=user.username)


@router.post("/login/", dependencies= [Depends(LOGIN_RATE_LIMIT)])
def login(user: UserLogin, conn= Depends(get_db)):
    """Authenticate a user."""
    try:
        token = login_user(conn, user)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    return {"access_token": token, "token_type": "Bearer"}

# for now as a POST methode because GET with a body did not work and is not recomended.
# Later when the tokens will be stored in the front end, we ll use the GET Mehtod.
@router.post("/users/")
def list_users(user: UserLogin,conn= Depends(get_db)) -> list:
    """Return all users (usernames)."""
    try:
        return list_users_service(conn, user)
    except SystemError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/user/me")
def read_users_me(current_user: Annotated[UserLogin, Depends(get_current_user)]):
    """Returns logged in user"""
    return current_user

@router.delete("/user/{user_name}")
def delete_user(user_name: str, user: UserLogin, conn= Depends(get_db)):
    """Delete a user after credential verification."""
    try:
        delete_service(conn, user, user_name)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    return {"deleted user: ": user_name}

@router.put("/user/{user_name}/{role}")
def update_user_role(user_name: str, role, user: UserLogin, conn= Depends(get_db)):
    """Update an attribute of an existing user"""
    try:
        update_service(conn, user, user_name, role)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    return "Role updated successfully"

@router.get("/protected/")
def protected_endpoint(current_user: Annotated[str, Depends(get_current_user)]) -> str:
    """A protected endpoint that requires authentication."""
    return current_user