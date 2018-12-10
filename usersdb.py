import sqlite3

conn = sqlite3.connect('flask.db')

c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, email VARCHAR, password TEXT)")

def data_entry():
    c.execute("INSERT INTO users VALUES(null, 'rodrigo', 'rodrigocamarena@hotmail.es', '12345')")
    conn.commit()
    c.close()
    conn.close()

def print_table():
    c.execute("SELECT * FROM users")
    results = c.fetchall()
    for i in results:
        print(i[0])
        print(i[1])
        print(i[2])
        print(i[3])
def variable_entry():
    name = 'rodrigo89'
    password = '1234567'
    email = 'kamarena78@gmail.com'

    c.execute("INSERT INTO users (id, username, email, password) VALUES (NULL, ?, ?, ?)", (name, email, password))
    conn.commit()



print_table()


