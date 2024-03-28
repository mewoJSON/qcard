import sqlite3
import uuid 

conn = sqlite3.connect('static/database.db', check_same_thread=False)
c = conn.cursor()

# for debugging purposes
# initializes a table, only run once
def create_table() -> None:
    c.execute('''
        CREATE TABLE users (
        id TEXT PRIMARY KEY,
        name TEXT,
        password TEXT,
        email TEXT)
        ''')

def insert_user(name, password, email) -> None:
    user_id = str(uuid.uuid4())
    c.execute('''
        INSERT INTO users (id, name, password, email)
        VALUES (?, ?, ?, ?)
        ''', (user_id, name, password, email))
    conn.commit()

def user_in_database(email) -> bool: 
    c.execute(f'''SELECT EXISTS(SELECT 1 FROM users WHERE email = ?)''', (email,))
    fetch = c.fetchone()[0]
    return bool(fetch)

# this is awful and just for test purposes
def password_check(email, password) -> bool:
    c.execute(f'''SELECT password FROM users WHERE email = ?''', (email,))
    pswd = c.fetchone()[0] # sob
    return True if pswd == password else False
    
# uncomment this 
# create_table()