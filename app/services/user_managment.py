from app.cores.hash import hash_password, verify_password
from app.db.database import add_user_db, search_user, delete_user_db, get_stored_pwd
from app.services.auth_service import check_password


def register_user(conn, username: str, password: str):
    hashed_password = hash_password(password)
    add_user_db(conn, username, hashed_password)


def get_user():
    #TODO: implement later to check if user valid and get its data
    pass

def login_user(conn, username, pwd):
    user = search_user(conn, username)
    stored_pwd = get_stored_pwd(conn, username)
    if not verify_password(stored_pwd, pwd) :
       raise ValueError("Username or password is incorrect.")
    print("Login Succeeded DB")
    return user

def delete_user(conn, username, pwd):
    stored_pwd = get_stored_pwd(conn, username)
    if not verify_password(stored_pwd, pwd):
def delete_user(conn, username: str, password: str):
        raise ValueError("password is incorrect.")
    print("User deleted DB")
    delete_user_db(conn, username)