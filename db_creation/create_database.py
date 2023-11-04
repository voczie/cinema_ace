import psycopg2

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_PORT = os.getenv('DATABASE_PORT')

conn = psycopg2.connect(user = DATABASE_USER, password = DATABASE_PASSWORD, port = DATABASE_PORT)
conn.autocommit = True

cursor = conn.cursor()
name_database = "CinemAce"

create_database_sql = f"CREATE database {name_database};"

try:
    cursor.execute(create_database_sql)
    print(f"Database {name_database} criada")
except:
    print("Essa database já existe")

conn.close()