import psycopg2
import sys
import os
from dotenv import load_dotenv

sys.path.append('crud')
load_dotenv()

DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT')

from crud.create_objetcs import *
from crud.read_objects import *
from crud.update_objects import *
from crud.delete_objects import *
from crud.reports import *

print(DATABASE_HOST)

conn = psycopg2.connect(database = DATABASE_NAME, user = DATABASE_USER, password = DATABASE_PASSWORD,
                        host = DATABASE_HOST, port = DATABASE_PORT)

# result = read_objects('filmes', conn)
# print(result)
# create_object_filmes(conn)
# result = read_movie_by_name(conn, "Monstros")
# print(result)
# report_all_sessoes()
# create_object_sessoes(conn)
# report_sessoes_disponiveis(conn)
# report_boxoffice(conn)

# create_object_generos_filmes(conn)
# create_object_generos(conn)
# create_object_bilhetes(conn)
# report_profit_by_genero(conn)

# delete_bilhete(conn, 2)
# delete_genero(conn, 11)
# delete_filme(conn, 8)
# update_hora_sessao(conn, 2, '01/10/2023 03:00:00')
# update_filme_id(conn, 5, 666)

conn.close()