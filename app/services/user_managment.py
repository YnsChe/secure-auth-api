from app.cores.hash import hash_password, verify_password
from app.db.database import add_user_db, check_username, delete_user_db, get_stored_password
from app.models.user import UserOutput, UserInput

def register_user(conn, user: UserInput) -> UserOutput:
    hashed_password = hash_password(user.password)
    add_user_db(conn, user.username, hashed_password)
    return UserOutput(username=user.username)

def login_user(conn, user: UserInput) -> UserOutput:
    check_username(conn, user.username)
    stored_password = get_stored_password(conn, user.username)
    verify_password(stored_password, user.password)
    return UserOutput(username=user.username)

def delete_user(conn, user: UserInput):
    check_username(conn, user.username)
    stored_password = get_stored_password(conn, user.username)
    verify_password(stored_password, user.password)
    delete_user_db(conn, user.username)