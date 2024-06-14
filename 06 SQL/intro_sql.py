import sqlite3

conn = sqlite3.connect("pets.sqlite")

cur = conn.cursor()

cur.execute('''
CREATE TABLE pets(
    name VARCHAR(30) NOT NULL,
    pet_type VARCHAR(10) NOT NULL            
)
''')

conn.commit()

conn.close()