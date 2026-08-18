""" Here JWT Creation and verification forLow level Authentication"""
import os
from datetime import timedelta, datetime, timezone
from typing import Annotated

import jwt
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError

from app.db.database import get_user_by_username, get_db
from app.models.tokens import TokenData
from app.models.users import UserInDB

#Load variables for the JWT
load_dotenv("var.env")
key = os.getenv("JWT_KEY")
algorithm = os.getenv("JWT_ALG")

#Defining the Scheme tha we will be using ot authenticate
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """Create a signed JWT with an expiration time."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=5)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, key, algorithm=algorithm)
    return encoded_jwt


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], conn=Depends(get_db)) -> UserInDB:
    """Decode the JWT and return the corresponding authenticated user."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate Credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, key, algorithms=[algorithm])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user_by_username(conn, token_data.username)
    if user is None:
        raise credentials_exception
    return user
