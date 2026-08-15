import sqlite3
from sqlite3 import Connection
from pathlib import Path

"""Low-level database access for the `users` table (SQLite)."""
BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "users.db"

# parametrized queries
sql_create = """CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    role TEXT NOT NULL
                )
             """
sql_insert = "INSERT INTO users (username, password, role) VALUES (?, ?, ?)"
sql_delete = "DELETE FROM users WHERE username=?"
sql_select = "SELECT username FROM users"
sql_update = "UPDATE users SET role = ? WHERE username = ?"
sql_check_username = "SELECT * FROM users WHERE username=?"
sql_check_empty = "SELECT COUNT(*) FROM users"


def get_db():
    """
        FastAPI dependency that yields a database connection.
        Connection is closed after the request.
        """
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()

# Initiate the db
def init_db():
    """Create tables if they do not exist."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute(sql_create)
    conn.close()

# Register a new user
def add_user_db (conn: Connection, username: str, password: str):
    """ The first user is always the admin"""
    cur = conn.execute(sql_check_empty)
    (count,) = cur.fetchone()
    role = "admin" if count == 0 else "user"

    """ Insert a user. Raises ValueError if the username already exists. """
    try:
        conn.execute(sql_insert, (username, password, role))
    except sqlite3.IntegrityError as e:
        raise ValueError(str (e))
    conn.commit()

def delete_user_db (conn: Connection, username: str):
    """
    Delete a user, username gets checked in authenticate before we delet.
    """
    conn.execute(sql_delete, (username,))
    conn.commit()

def check_username (conn: Connection, username: str):
    """
    Return the username if it exists, otherwise raise ValueError.
    Used for credential checks without leaking details.
    """
    cur = conn.execute(sql_check_username, (username,))
    row = cur.fetchone()
    if row is None:
        return False
        #TODO: introduce a logger later on to log infos that we don't want to show to the user (like invalid username)
    found_username = row[1]
    return found_username

def list_users_db(conn: Connection) -> list:
    """Return a list of all usernames."""
    cur = conn.execute(sql_select)
    users = cur.fetchall()
    return users

def update_user_db(conn: Connection, username, role):
    conn.execute(sql_update, (role, username))
    conn.commit()
    return True


def get_stored_password(conn: Connection, username):
    """
    Return the stored hashed password for a username.
    Raises ValueError if the password could not be found.
    """
    cur = conn.execute(sql_check_username, (username,))
    row = cur.fetchone()
    if row is None:
        return False
    return row[2]

def get_role(conn: Connection, username):
    cur = conn.execute(sql_check_username, (username,))
    row = cur.fetchone()
    return row[3]