from app.cores.hash import hash_password, verify_password
from app.db.database import add_user, search_user, delete_user_db


def register_user(username, pwd):
    hs_pwd = hash_password(pwd)
    add_user(username, hs_pwd)
    return {"User registred successfully"}

def get_user(username, pwd):
    pass

def login_user(username, pwd):
    user, stored_pwd = search_user(username)
    vf_pwd = verify_password(stored_pwd, pwd)
    if vf_pwd:
       print("Correct password")
       return user
    else:
       print("False password! try again")
       return None

def delete_user(username):
    delete_user_db(username)
    pass