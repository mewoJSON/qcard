import sqlite3
import uuid 

conn = sqlite3.connect('database/data.db', check_same_thread=False)
c = conn.cursor()

# for debugging purposes
# initializes a table, only run once
def create_table() -> None:
    c.execute('''
        CREATE TABLE object (
        id TEXT PRIMARY KEY,
        name TEXT,
        date TEXT,
        creator TEXT,
        location TEXT,
        product TEXT)
        ''')

def insert_user(name, password, email) -> None:
    user_id = str(uuid.uuid4())
    c.execute('''
        INSERT INTO users (id, name, password, email)
        VALUES (?, ?, ?, ?)
        ''', (user_id, name, password, email))
    conn.commit()

def insert_object(creator, date, location, product) -> None:
    user_id = str(uuid.uuid4())
    c.execute('''
        INSERT INTO users (id, creator, date, location, product)
        VALUES (?, ?, ?, ?, ?)
        ''', (user_id, creator, date, location, product))
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
    
def get_game_array():
    c.execute("SELECT name, date, creator, location, product, image FROM object")
    rows = c.fetchall()
    result = [[row[0], row[1], row[2], row[3], row[4], row[5]] for row in rows]
    conn.close()
    print(result)
    return result

get_game_array()