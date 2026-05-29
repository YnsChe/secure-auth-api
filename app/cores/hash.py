from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

def hash_password(password: str) -> str:
    return ph.hash(password)

def verify_password(hashed: str, password: str):
    try:
        return ph.verify(hashed, password)
    except VerifyMismatchError:
        return False

