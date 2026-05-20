import sqlite3

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
    print("INFO:     [+] Table created Successfully")
    conn.close()

# Register a new user
def add_user_db (conn, username, pwd):
    try:
        conn.execute(sql_insert, (username, pwd))
    except sqlite3.IntegrityError:
        raise ValueError("Username already exists")
    conn.commit()

def delete_user_db (conn, username):
    if not user_found(conn, username):
        raise ValueError("Invalid Username")
    conn.execute(sql_delete, (username,))
    conn.commit()


def search_user (conn, username):
    cur = conn.cursor()
    cur.execute(sql_check, (username,))
    row = cur.fetchone()
    if row is None:
        raise ValueError("Invalid Username")
    user = row[1]
    return user

def get_users(conn) -> list:
    cur = conn.cursor()
    cur.execute(sql_select)
    users = cur.fetchall()
    print("User: ", users)
    return users

def user_found (conn, username) -> bool:
    cur = conn.cursor()
    cur.execute(sql_check, (username,))
    if cur.fetchone():
        return True
    else:
        return False

def get_stored_pwd(conn, username):
    cur = conn.cursor()
    cur.execute(sql_check, (username,))
    row = cur.fetchone()
    if row is None:
        raise ValueError("Error while retrieving password")
    return row[2]