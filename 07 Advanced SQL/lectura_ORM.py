# Cargar dependencias
import sqlalchemy
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

# Explorar la base de datos
# Qué tablas tengo ? 

# 1er Objeto importante: engine
engine = create_engine('sqlite:///mascotas.sqlite')

# inspector
# Este objeto nos ayuda a explorar la base de datos
# por ejemplo: listas las tablas

inspector = inspect(engine)
tables = inspector.get_table_names()
print(tables)

# Imprimir la metadata de una tabla
columnas = inspector.get_columns('mascotas')
# print(columnas)

# El método get_columns regresa una lista
# de diccionarios. Por lo tanto
# lo común es iterar para imprimir los metadatos
# que nos interesan

for c in columnas:
    print(f"Nombre: {c['name']}, tipo: {c['type']}")

# 2do Objeto importante: Base
# En esta ocación veremos como "copiar" la
# estructura de la tabla de la base de datos

Base = automap_base()
Base.prepare(engine, reflect=True)

# Copiamos la estructura de los objetos(tablas)
# directamente de "Base"
Pet = Base.classes.mascotas

# Lo que resulta es:
# tenemos de nuevo la clase "Pet" pero esta vez
# no la escribimos manualmente, la copiamos
# de la base de datos

# mascota1 = Pet(nombre='Fideo', tipo='Gato')
# Session = sessionmaker(bind=engine)
# session = Session()
# session.add(mascota1)
# session.commit()
# session.close()
# engine.dispose()

# 3er objeto importante: Session
Session = sessionmaker(bind=engine)
session = Session()

# select * from table mascotas
resultados = session.query(Pet).all()

# Cada fila de los resultados del query
# están en "row"
# Dentro de row, tengo las propiedades ( columnas )
# a las que puedo acceder usando notación de punto
for row in resultados:
    print(row.nombre)

# select * from table mascotas where tipo='Gato'
resultados = session.query(Pet).filter(Pet.tipo=='Gato').all()
for row in resultados:
    print(f'{row.nombre}, {row.tipo}')

# select tipo, count(tipo) from table mascotas group by tipo
# Para construir este query, necesito importar
# las funciones de SQL
from sqlalchemy import func

resultados = session.query(Pet.tipo, func.count(Pet.tipo)).group_by(Pet.tipo).all()
for tipo, count in resultados:
    print(f'{tipo}: {count}')

session.close()
engine.dispose()

# Filtros con tiempo
# Para fechas especificas usamos la notacion : YYYY-MM-DD
# resultados = session.query(Pet).filter(Pet.date>='2024-01-01').all()

# Es posible usar objetos de tiempo de python:

# current_time = datetime.datetime.utcnow()

# ten_weeks_ago = current_time - datetime.timedelta(weeks=10)

# subjects_within_the_last_ten_weeks = session.query(Pet).filter(
#     Pet.date > ten_weeks_ago).all()








