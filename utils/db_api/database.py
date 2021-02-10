from gino import Gino
from gino.schema import GinoSchemaVisitor
from psycopg2 import connect
from psycopg2._psycopg import OperationalError
from data.config import DATABASE, PGUSER, PGPASSWORD, ip, PGPORT
from data.config import POSTGRES_URI

db = Gino()


def create_connection_for_create_db(db_name):
    connection = None
    try:
        connection = connect(
            database=db_name,
            user=PGUSER,
            password=PGPASSWORD,
            host=ip,
            port=PGPORT,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def create_database_for_create_db(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def create_datab():
    if create_connection_for_create_db(DATABASE):
        pass
    else:
        connection = create_connection_for_create_db("postgres")
        create_database_query_for_create_db = f"CREATE DATABASE {DATABASE}"
        create_database_for_create_db(connection, create_database_query_for_create_db)


# Документация
# http://gino.fantix.pro/en/latest/tutorials/tutorial.html

async def create_db():
    # Устанавливаем связь с базой данных
    await db.set_bind(POSTGRES_URI)
    db.gino: GinoSchemaVisitor

    # Создаем таблицы
    await db.gino.create_all()
