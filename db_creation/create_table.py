import psycopg2
from db_creation.create_sqls import tables_sqls

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT')

conn = psycopg2.connect(database = DATABASE_NAME, user = DATABASE_USER, password = DATABASE_PASSWORD,
                        host = DATABASE_HOST, port = DATABASE_PORT)
cursor = conn.cursor()

name_tables = ["filmes", "generos", "generos_filmes", "salas", "sessoes", "pessoas", "funcionarios", "clientes" "bilhetes"]

for table in name_tables:
    cursor.execute(f"DROP TABLE IF EXISTS {table} CASCADE")

for sql in tables_sqls:
    try:
        cursor.execute(sql)
        print(f"Tabela criada com sucesso ")
    except:
        print("Falha ao criar a tabela")
        break

conn.commit()

conn.close()