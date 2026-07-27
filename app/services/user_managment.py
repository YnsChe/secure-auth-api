from sqlite3 import Connection
from app.cores.hash import hash_password
from app.db.database import add_user_db,delete_user_db
from app.models.user import UserOutput, UserRegister, UserLogin
from app.services.auth_service import authenticate_user, login_jwt

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
    return login_jwt(userdb)


def delete_user(conn: Connection, user: UserLogin):
    """Delete a user after verifying their credentials."""
    authenticate_user(conn, user)
    delete_user_db(conn, user.username)