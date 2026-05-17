from app.cores.hash import hash_password
from app.db.database import add_user_db, search_user, delete_user_db
from app.services.auth_service import check_password, check_username


def register_user(username, pwd):
    hs_pwd = hash_password(pwd)
    add_user_db(username, hs_pwd)
    return {"Registration complete DB"}

def get_user():
    #TODO: implement later to check if user valid and get its data
    pass

def login_user(username, pwd):
    user, stored_pwd = search_user(username)
    if not check_password(stored_pwd, pwd) or check_username(username) == False:
       raise ValueError("Username or password is incorrect.")
    print("Login Succeeded DB")
    return user

def delete_user(username, pwd):
    user, stored_pwd = search_user(username)
    if not check_password(stored_pwd, pwd):
        print("False password! try again")
    print("User deleted DB")
    delete_user_db(username)