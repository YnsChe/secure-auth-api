"""Business logic for user registration, login, and deletion."""
from sqlite3 import Connection

from app.cores.hashing import hash_password
from app.db.database import add_user_db, delete_user_db, list_users_db, update_user_db
from app.models.users import UserOutput, UserRegister, UserLogin, UserInDB
from app.services.auth_service import authenticate_user, issue_token


def register_user(conn: Connection, user: UserRegister) -> UserOutput:
    """Register a user and return a sanitized output model."""
    hashed_password = hash_password(user.password)
    add_user_db(conn, user.username, hashed_password)
    return UserOutput(username=user.username)


def login_user(conn: Connection, user: UserLogin):
    """Login User and return an access token"""
    user_db = authenticate_user(conn, user)
    return issue_token(user_db)


def delete_service(conn: Connection, user: UserInDB, user_name):
    """Delete a user if the requesting user is an admin."""
    if user.role != "admin":
        raise PermissionError("Only admins can delete users")
    delete_user_db(conn, user_name)



def list_users_service(conn: Connection, user: UserInDB):
    """Return all usernames if the requesting user is an admin."""
    if user.role != "admin":
        raise PermissionError("Only admins can list users")
    list_users_db(conn)


def update_service(conn: Connection, user: UserInDB, user_name: str, role: str):
    """Update a user's role if the requesting user is an admin."""
    if user.role != "admin":
        raise PermissionError("Only admins can update data")
    update_user_db(conn, user_name, role)
