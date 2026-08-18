"""Business logic for user registration, login, and deletion."""
from sqlite3 import Connection

from app.cores.authentication import create_access_token
from app.cores.hashing import hash_password
from app.db.database import add_user_db, delete_user_db, get_role, list_users_db, update_user_db
from app.models.users import UserOutput, UserRegister, UserLogin, UserInDB
from app.services.auth_service import authenticate_user, issue_token


def register_user(conn: Connection, user: UserRegister) -> UserOutput:
    """Register a user and return a sanitized output model."""
    hashed_password = hash_password(user.password)
    add_user_db(conn, user.username, hashed_password)
    return UserOutput(username=user.username)


def login_user(conn: Connection, user: UserLogin):
    """Login User and return """
    user_db = authenticate_user(conn, user)
    return issue_token(user_db)


def delete_service(conn: Connection, user: UserInDB, user_name):
    """Delete a user, can only be done from admins."""
    if user.role != "admin":
        raise PermissionError("Only admins can delete users")
    delete_user_db(conn, user_name)



def list_users_service(conn: Connection, user: UserInDB):
    if get_role(conn, user.username) != "admin":
        raise PermissionError("Only admins can list users")
    try:
        return list_users_db(conn)
    except ValueError:
        raise ValueError("List cannot be displayed")


def update_service(conn: Connection, user: UserInDB, user_name: str, role: str):
    # authenticate_user(conn, user) got protected
    if get_role(conn, user.username) == "admin":
        try:
            update_user_db(conn, user_name, role)
        except ValueError:
            raise ValueError("User cannot be updated")
