from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

"""Password hashing and verification using Argon2."""
# Instantiate the PasswordHasher
ph = PasswordHasher()

def hash_password(password: str) -> str:
    """Return an Argon2 hash for the given plaintext password."""
    return ph.hash(password)

def verify_password(hashed: str, password: str):
    """Verify a plaintext password against an Argon2 hash."""
    try:
        return ph.verify(hashed, password)
    except VerifyMismatchError:
        return False

