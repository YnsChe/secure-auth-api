import sqlite3

from app.cores.hash import hash_password, verify_password

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
def add_user (usrname, pwd):
    hs_pwd = hash_password(pwd)
    cur.execute(sql_insert, (usrname, hs_pwd))
    conn.commit()
    print(usrname, "added successfuly")

def delete_user (usrname):
    cur.execute(sql_delete, (usrname,))
    conn.commit()
    print("user deleted successfully")

def check_user (usrname, pwd):
    cur.execute(sql_check, (usrname,))
    user, stored_pwd = cur.fetchone()
    if user is None:
        print("User is None")
        return None
    vf_pwd = verify_password(stored_pwd, pwd)
    if vf_pwd:
        print("Pssword verified")
    else:
        print("False password! try again")
        return None
    #conn.close()
    print(usrname, "Logged in")
    return user

def get_users():
    cur.execute(sql_select)
    users = cur.fetchall()
    #conn.close()
    return users
