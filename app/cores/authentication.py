""" Here JWT Creation and verification (Low level Authentication)"""
from datetime import timedelta, datetime, timezone
from http.client import HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import Depends,HTTPException, status
import jwt
from jwt import InvalidTokenError

from app.db.database import check_username, get_db
from app.models.tokens import TokenData

''' Building variables of the Token '''
# TODO: store the variable in a .env file
SECRET_KEY = "46b58bd07a60babe3292e8c5f8a9f7aee5b7a055413e15255f8226a97366f29e"
ALGORITHM = "HS256"


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], conn = Depends(get_db)):
    #TODO: Make a error library for all possible errors
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate Credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = check_username(conn, token_data.username)
    return user