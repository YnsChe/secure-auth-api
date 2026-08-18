""" High Level Authentication, like authenticate_user(); Login()... """
from datetime import timedelta
from app.cores.authentication import create_access_token
from app.cores.hashing import verify_password, DUMMY_HASH
from app.db.database import get_user_by_username, get_stored_password, get_role
from app.models.tokens import ACCESS_TOKEN_EXPIRE_MINUTES
from app.models.users import UserLogin, UserInDB


def authenticate_user(conn, user: UserLogin) -> UserInDB:
    """Validate user credentials and return a sanitized output model."""
    user_db = get_user_by_username(conn, user.username)
    if user_db is None:
        verify_password(DUMMY_HASH, user.password)
        raise ValueError("Invalid Credentials")
    if not verify_password(user_db.hashed_password, user.password):
        raise ValueError("Invalid Credentials")
    return user_db

def issue_token(user: UserInDB):
    """Sets expiration time for the token and returns an access token created for the given user  """
    access_token_expires = timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return access_token