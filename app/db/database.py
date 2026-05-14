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
def add_user (username, pwd):
    cur.execute(sql_insert, (username, pwd))
    conn.commit()
    print(username, "added successfuly in table")

def delete_user_db (usrname):
    cur.execute(sql_delete, (usrname,))
    conn.commit()
    print("user deleted successfully")

def search_user (username):
    if user_found:
        pass

    user, stored_pwd = cur.fetchone()
    if user is None:
        print("User nor found")
        return False
    print("User found")
    return user, stored_pwd

def get_users():
    cur.execute(sql_select)
    users = cur.fetchall()
    return users

def user_found (username):
    cur.execute(sql_check, (username,))
    if cur.fetchone():
        return True
    else:
        return False
