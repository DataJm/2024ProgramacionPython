'''
ORM
Object-Relational Mapping

Vamos a interactuar con la base de datos utilizando Objetos de Python.
Esto evita escribir código SQL manualmente,
tiene la ventaja de que sólo escribiriemos código python,
tiene la ventaja de la portabilidad entre bases de datos SQL (SQAlchemy
traduce el código Python a cualquiera que sea tu base de datos SQL)
'''

import sqlalchemy

# 1er Objeto importante : Engine
# Importamos el engine
from sqlalchemy import create_engine

engine = create_engine('sqlite:///mascotas.sqlite')

# 2do objeto importante: Base
# Importamos la base
# 'Base' mapea los objetos hacia la base de datos

# NOTA: Usaremos por ahora una base "declarativa"
# Construiremos manualmente la base (y los objetos)
# más adelante veremos como crear en automático estos objetos

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float

# 2do objeto importante de SQLAlchemy
Base = declarative_base()

class Pet(Base):
    __tablename__ = 'mascotas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    tipo = Column(String)

# Con esta línea de código se crea la tabla
Base.metadata.create_all(engine)

mascota1 = Pet(nombre='Orejas', tipo='Conejo')
mascota2 = Pet(nombre='Manchas', tipo='Perro')
mascota3 = Pet(nombre='Bigotes', tipo='Gato')

# 3er Objeto importante: Session
# El session controla las consultas (query) a la BD

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

session.add(mascota1)
session.add(mascota2)
session.add(mascota3)

# Cuando vamos a terminar las operaciones de Escritura, Actualización o Eliminación
# debemos hacer commit de los cambios
session.commit()

# FINALIZAR
# Cerramos todos los objetos para garantizar que no queda ninguna sesión abierta en la base de datos
session.close()
engine.dispose()
