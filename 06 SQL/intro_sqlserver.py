import sqlalchemy
from sqlalchemy import create_engine, text
from config import usuario, password
import pyodbc
from sqlalchemy.engine import URL

connection_string = (
    "Driver={SQL Server};"
    "Server=MXW20125004,65074;"
    "Database=BDCOBPROCESO;"
    "Trusted_Connection=yes;")
print(connection_string)

connection_url = URL.create(
    "mssql+pyodbc", 
    query={"odbc_connect": connection_string}
)
engine = create_engine(connection_url)

sql = text("select * from DBO.MX_TW_USUARIOS ")


with engine.connect() as conn:
    resultados = conn.execute(sql)

    for row in resultados:
        print(row)

