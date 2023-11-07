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

# create_object_filmes(conn)
# create_object_generos(conn)
# create_object_generos_filmes(conn)
# create_object_pessoas(conn)
# create_object_salas(conn)
# create_object_sessoes(conn)
# create_object_bilhetes(conn)
# create_object_view_lista_all_sessoes(conn)

# result = read_filme_by_name(conn, "Monstro")
# print(result)

# update_sala_sessao(conn, 13, 3)

# delete_sessao(conn, 9)

# report_all_sessoes(conn)
# report_boxoffice(conn)
# report_profit_by_genero(conn)
# report_sessoes_disponiveis(conn)
# report_profit_by_funcionario(conn)
# report_sessoes_por_preco(conn, 12, 25)
# report_sessoes_por_categoria(conn, 'Acao')
# report_sessoes_por_filme_gravado_em_mari(conn)
# report_sessoes_esgotando(conn)
report_cliente_compras(conn, '11649047444')

conn.close()