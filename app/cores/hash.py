from argon2 import PasswordHasher

ph = PasswordHasher()

def hash_password(password: str) -> str:
    return ph.hash(password)

def verify_password(hashed: str, password: str):
    try:
        ph.verify(hashed, password)
    except TypeError:
        raise ValueError("Invalid Password")
    return ph.verify(hashed, password)
