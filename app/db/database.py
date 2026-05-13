import sqlite3
from app.cores.hash import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///users.db')


# parametrized queries against SQL Injection
sql_insert = "INSERT INTO users (username, password) VALUES (?, ?)"
sql_delete = "DELETE FROM users WHERE username=?"
sql_select = "SELECT username FROM users"
sql_check = "SELECT * FROM users WHERE username=? AND password=?"

def init():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT UNIQUE,
        password TEXT NOT NULL
    )
    """)
    conn.close()
    print("INFO:     [+] Database created Successfuly")

def add_user (usrname, pwd):
    with engine.connect() as conn:
        result = conn.execute(sql_insert, (usrname, pwd))
    conn1 = sqlite3.connect('users.db')
    cur1 = conn1.cursor()
    pwd = hash_password(pwd)
    cur1.execute(sql_insert, (usrname, pwd))
    conn1.commit()
    print("User added successfuly")
    conn1.close()

def insert (username, pwd):
    conn1 = sqlite3.connect('users.db')
    cur1 = conn1.cursor()
    pwd = hash_password(pwd)
    cur1.execute(sql_insert, (username, pwd))

def delete_user (usrname):
    conn2 = sqlite3.connect('users.db')
    cur2 = conn2.cursor()
    cur2.execute(sql_delete, (usrname,))
    conn2.commit()
    print("user deleted successfully")
    conn2.close()

def check_user (usrname, pwd):
    conn3 = sqlite3.connect('users.db')
    cur3 = conn3.cursor()
    cur3.execute(sql_check, (usrname, pwd))
    user = cur3.fetchone()
    if user is None:
        print("User not found")
        conn3.close()
        return None
    conn3.close()
    print("User found")
    return user

def get_users():
    conn4 = sqlite3.connect('users.db')
    cur4 = conn4.cursor()
    cur4.execute(sql_select)
    users = cur4.fetchall()
    conn4.close()
    return users