""" Here JWT Creation and verification (Low level Authentication)"""

from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token():
    pass

def decode_token():
    pass