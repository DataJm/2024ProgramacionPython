'''
TODO:

Enviar la data del archivo audi.csv a una base
de datos
'''
import sqlite3
import csv
import os

csv_path = os.path.join('..', 'datos', '03audi.csv')

with open(csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    values = [] 

    for row in csv_reader:
        modelo = row[0]
        precio = row[2]
        values.append(f'{(modelo,precio)}')

    values = ",".join(values)

print(values)
# Conexion a BD
conn = sqlite3.connect("audi.sqlite")
cur = conn.cursor()

cur.execute('''
CREATE TABLE inventario(
    model VARCHAR(30) NOT NULL,
    price VARCHAR(10) NOT NULL
)
''')

cur.execute(f'''
INSERT INTO inventario (model, price)
VALUES {values};
)
''')

conn.commit()
conn.close()



