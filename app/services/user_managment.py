from app.cores.hash import hash_password, verify_password
from app.db.database import add_user_db, check_username, delete_user_db, get_stored_password
from app.models.user import UserOutput, UserInput

def register_user(conn, user: UserInput) -> UserOutput:
    hashed_password = hash_password(user.password)
    add_user_db(conn, user.username, hashed_password)
    return UserOutput(username=user.username)

def login_user(conn, user: UserInput) -> UserOutput:
    if not check_username(conn, user.username):
        raise ValueError("Username is incorrect.")
    stored_password = get_stored_password(conn, user.username)
    if not verify_password(stored_password, user.password) :
       raise ValueError("Incorrect password.")
    return UserOutput(username=user.username)

def delete_user(conn, user: UserInput):
    stored_pwd = get_stored_password(conn, user.username)
    if not verify_password(stored_pwd, user.password):
        raise ValueError("password is incorrect.")
    print("User deleted DB")
    delete_user_db(conn, user.username)