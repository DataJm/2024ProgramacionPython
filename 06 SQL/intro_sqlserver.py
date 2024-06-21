import sqlalchemy
from sqlalchemy import create_engine, text
from config import usuario, password
import pyodbc
from sqlalchemy.engine import URL

# SQL Server
connection_string = (
    "Driver={SQL Server};"
    "Server=MXW20125004,65074;"
    "Database=BDCOBPROCESO;"
    "Trusted_Connection=yes;")

connection_url = URL.create(
    "mssql+pyodbc", 
    query={"odbc_connect": connection_string}
)
engine = create_engine(connection_url)

# SQLite
# engine = create_engine('sqlite:///pets.sqlite')

# -------------------------------------------------
# Cómo consumir de la base de datos
# Una vez que tenemos el engine...


# Preparamos nuestro raw SQL
sql = text("select * from DBO.MX_TW_USUARIOS")

'''
En las últimas versiones de SQLAlchemy, se modificó la forma de mandar
raw sql para que sea explítica la apertura y cierre de la conexión a la base de
datos
'''
with engine.connect() as conn:
    resultados = conn.execute(sql)

    for row in resultados:
        print(row)