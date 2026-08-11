from operator import truediv
from sqlite3 import Connection
from app.cores.hashing import hash_password
from app.db.database import add_user_db, delete_user_db, get_role, list_users
from app.models.users import UserOutput, UserRegister, UserLogin, UserInDB
from app.services.auth_service import authenticate_user, issue_token

"""Business logic for user registration, login, and deletion."""

def register_user(conn: Connection, user: UserRegister) -> UserOutput:
    """Register a user and return a sanitized output model."""
    hashed_password = hash_password(user.password)
    try:
        add_user_db(conn, user.username, hashed_password)
    except ValueError:
        raise ValueError("Error while registering")
    return UserOutput(username=user.username)

def login_user(conn: Connection, user: UserLogin):
    userdb = authenticate_user(conn,user)
    return issue_token(userdb)

def delete_service(conn: Connection, user: UserLogin, user_name):
    """Delete a user after verifying their credentials."""
    authenticate_user(conn, user)
    if get_role(conn, user.username) == "admin":
        try:
            delete_user_db(conn, user_name)
        except ValueError:
            raise ValueError("Contact an Admin to delete the user")


def list_users_service(conn: Connection, user: UserLogin):
    authenticate_user(conn, user)
    if get_role(conn, user.username) == "admin":
        try:
            list_users(conn)
        except ValueError:
            raise ValueError("Contact an Admin to list all users")

"""def check_admin(user: UserInDB)-> bool:
    if user.role == "admin":
        return True
    return False"""