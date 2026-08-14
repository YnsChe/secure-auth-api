""" High Level Authentication, like authenticate_user(); Login()... """
from datetime import timedelta
from app.cores.authentication import create_access_token
from app.cores.hashing import verify_password, DUMMY_HASH
from app.db.database import check_username, get_stored_password, get_role
from app.models.tokens import ACCESS_TOKEN_EXPIRE_MINUTES
from app.models.users import UserLogin, UserInDB


def authenticate_user(conn, user: UserLogin) -> UserInDB:
    """Validate user credentials and return a sanitized output model."""
    if not check_username(conn, user.username):
        verify_password(DUMMY_HASH, user.password)
        raise ValueError("Invalid Credentials")
    stored_pwd = get_stored_password(conn, user.username)
    if not verify_password(stored_pwd, user.password):
        raise ValueError("Invalid Credentials")
    role_db = get_role(conn, user.username)
    return UserInDB(username=user.username, hashed_password=stored_pwd, role=role_db)

def issue_token(user: UserInDB):
    access_token_expires = timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return access_token