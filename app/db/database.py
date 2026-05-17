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

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cur = conn.cursor()

# Initiate the db
def init_db():
    cur.execute(sql_create)
    print("INFO:     [+] Table created Successfuly")

def close_db():
    conn.close()
    return {"Connection closed"}

# Register a new user
def add_user_db (username, pwd):
    cur.execute(sql_check, (username,))
    try:
        cur.execute(sql_insert, (username, pwd))
    except sqlite3.IntegrityError:
        raise ValueError("User already exists")
    conn.commit()
    print(username, "added successfuly in table")

def delete_user_db (username):
    if not user_found(username):
        raise ValueError("User not found")
    cur.execute(sql_delete, (username,))
    conn.commit()
    print("user deleted successfully")


def search_user (username):
    if not user_found(username):
        print("User not found")
        return None
    cur.execute(sql_check, (username,))
    user, stored_pwd = cur.fetchone()[1:3]
    print("User found")
    return user, stored_pwd

def get_users() -> list:
    print("Entred get_users")
    cur.execute(sql_select)
    users = cur.fetchall()
    return users

def user_found (username) -> bool:
    cur.execute(sql_check, (username,))
    if cur.fetchone():
        return True
    else:
        return False
