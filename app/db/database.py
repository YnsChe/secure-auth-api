import sqlite3

conn = sqlite3.connect('users.db')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")
print("INFO:     [+] Table created Successfuly")
conn.close()

def add_user (usrname, pwd):
    conn1 = sqlite3.connect('users.db')
    cur1 = conn1.cursor()
    cur1.execute("INSERT INTO users (username, password) VALUES (?, ?)", (usrname, pwd))
    conn1.commit()
    print("User added successfuly")
    conn1.close()

def delete_user (usrname):
    conn2 = sqlite3.connect('users.db')
    cur2 = conn2.cursor()
    cur2.execute("DELETE FROM users WHERE username=?", (usrname,))
    conn2.commit()
    print("user deleted successfully")
    conn2.close()

def check_user (usrname, pwd):
    conn3 = sqlite3.connect('users.db')
    cur3 = conn3.cursor()
    cur3.execute("SELECT * FROM users WHERE username=? AND password=?", (usrname, pwd))
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
    cur4.execute("SELECT username FROM users")
    users = cur4.fetchall()
    conn4.close()
    return users