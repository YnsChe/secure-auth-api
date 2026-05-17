from app.cores.hash import verify_password
from app.db.database import user_found


def check_password(stored_pwd, pwd):
    verified = verify_password(stored_pwd, pwd)
    return verified

def check_username (username) -> bool:
    if user_found(username):
        return True
    else:
        return False