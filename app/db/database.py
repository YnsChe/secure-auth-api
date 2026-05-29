import sqlite3
from sqlite3 import Connection

DB_PATH = "users.db"

# parametrized queries
sql_insert = "INSERT INTO users (username, password) VALUES (?, ?)"
sql_delete = "DELETE FROM users WHERE username=?"
sql_select = "SELECT username FROM users"
sql_check = "SELECT * FROM users WHERE username=?"
sql_create = """CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )
             """

def get_db():
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()

# Initiate the db
def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(sql_create)
    conn.close()

# Register a new user
def add_user_db (conn: Connection, username: str, password: str):
    try:
        conn.execute(sql_insert, (username, password))
    except sqlite3.IntegrityError as e:
        raise ValueError(str (e))
    conn.commit()

def delete_user_db (conn: Connection, username: str):
    if not check_username(conn, username):
        raise ValueError("Invalid Username")
    conn.execute(sql_delete, (username,))
    conn.commit()

def check_username (conn: Connection, username: str):
    cur = conn.cursor()
    cur.execute(sql_check, (username,))
    row = cur.fetchone()
    if row is None:
        raise ValueError("Invalid Username")
    found_username = row[1]
    return found_username

def get_users(conn: Connection) -> list:
    cur = conn.cursor()
    cur.execute(sql_select)
    users = cur.fetchall()
    return users

def get_stored_password(conn: Connection, username):
    cur = conn.cursor()
    cur.execute(sql_check, (username,))
    row = cur.fetchone()
    if row is None:
        raise ValueError("Error while retrieving password")
    return row[2]