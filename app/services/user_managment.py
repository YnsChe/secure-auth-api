from sqlite3 import Connection

from app.cores.hash import hash_password, verify_password
from app.db.database import add_user_db, check_username, delete_user_db, get_stored_password
from app.models.user import UserOutput, UserRegister, UserLogin

def register_user(conn: Connection, user: UserRegister) -> UserOutput:
    hashed_password = hash_password(user.password)
    try:
        add_user_db(conn, user.username, hashed_password)
    except ValueError:
        raise ValueError("Error while registering")
    return UserOutput(username=user.username)

def login_user(conn: Connection, user: UserLogin) -> UserOutput:
    check_username(conn, user.username)
    stored_password = get_stored_password(conn, user.username)
    if not verify_password(stored_password, user.password):
        raise ValueError("Invalid credentials")
    return UserOutput(username=user.username)

def delete_user(conn: Connection, user: UserLogin):
    check_username(conn, user.username)
    stored_password = get_stored_password(conn, user.username)
    if not verify_password(stored_password, user.password):
        raise ValueError("Invalid credentials")
    delete_user_db(conn, user.username)