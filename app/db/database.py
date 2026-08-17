import sqlite3
from pathlib import Path
from sqlite3 import Connection

from app.models.users import UserInDB

#Low-level database access for the `users` table (SQLite).
BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "users.db"

# parametrized queries
sql_create_users_table = """CREATE TABLE IF NOT EXISTS users
                (
                    id       INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    hashed_password TEXT NOT NULL,
                    role     TEXT NOT NULL
                )
             """
sql_insert_user = "INSERT INTO users (username, hashed_password, role) VALUES (?, ?, ?)"
sql_delete_user = "DELETE FROM users WHERE username=?"
sql_get_usernames = "SELECT username FROM users"
sql_update_user_role = "UPDATE users SET role = ? WHERE username = ?"
sql_get_user_by_username = "SELECT username, hashed_password, role FROM users WHERE username=?"
sql_check_empty = "SELECT COUNT(*) FROM users"


def get_db():
    """
    FastAPI dependency that yields a database connection.
    Connection is closed after the request.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    try:
        yield conn
    finally:
        conn.close()


# Initiate the db
def init_db():
    """Create tables if they do not exist."""
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(sql_create_users_table)
        conn.commit()
    finally:
        conn.close()


def add_user_db(conn: Connection, username: str, hashed_password: str) -> None:
    """
       Insert a new user.

       The first user is assigned the admin role.
       All subsequent users are assigned the user role.

       Raises:
           ValueError: If the username already exists.
       """
    (count,) = conn.execute(sql_check_empty).fetchone()
    role = "admin" if count == 0 else "user"

    try:
        conn.execute(sql_insert_user, (username, hashed_password, role))
    except sqlite3.IntegrityError:
        conn.rollback()
        raise ValueError("Username already exists")
    conn.commit()


def delete_user_db(conn: Connection, username: str) -> None:
    """    Delete a user, username gets checked in authenticate before we delet.    """
    conn.execute(sql_delete_user, (username,))
    conn.commit()


def get_user_by_username(conn: Connection, username: str) -> UserInDB | None:
    """    Return the user as UserInDB form if it exists, otherwise None.    """
    row = conn.execute(sql_get_user_by_username, (username,)).fetchone()
    if row is None:
        return None
        # TODO: introduce a logger later on to log infos that we don't want to show to the user (like invalid username)
    return UserInDB(username=row["username"], hashed_password=row["hashed_password"], role=row["role"])


def list_users_db(conn: Connection) -> list[str]:
    """Return a list of all usernames."""
    rows = conn.execute(sql_get_usernames).fetchall()
    return [row["username"] for row in rows]


def update_user_db(conn: Connection, username: str, role:str) -> None:
    conn.execute(sql_update_user_role, (role, username))
    conn.commit()


# I don't need to get hashed password and row since in get_user_by_username extractz all the field i just need to chose one.
def get_stored_password(conn: Connection, username: str) -> str | None:
    """Return user's hashed password or none."""
    row = conn.execute(sql_get_user_by_username, (username,)).fetchone()
    if row is None:
        return None
    return row["hashed_password"]


def get_role(conn: Connection, username: str) -> str | None:
    """Return the user's role, or None if the user doesn't exist."""
    row = conn.execute(sql_get_user_by_username, (username,)).fetchone()
    if row is None:
        return None
    return row["role"]
