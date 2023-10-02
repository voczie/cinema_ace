from read_objects import *

def report_all_sessoes(conn):
    print("Todas as Sessões")
    result = read_all_sessoes(conn)
    
    for i in result:
        print("*****************************")
        print(f"ID da Sessão: {i[0]}")
        print(f"Filme: {i[1]}")
        print(f"Data da Sessão: {i[2]}")
        print(f"Número da Sala: {i[3]}")
        print(f"Idioma: {i[4]}")
        print(f"Legendado: {i[5]}") 
        print(f"Classificação: {i[6]}")
        print(f"Sala 3D: {i[7]}")
        print(f"Sala VIP: {i[8]}")
        print("*****************************")

def report_sessoes_disponiveis(conn):
    print("Sessões Disponíveis para a Data Atual")
    result = read_sessoes_disponiveis(conn)
    
    for i in result:
        print("*****************************")
        print(f"ID da Sessão: {i[0]}")
        print(f"Filme: {i[1]}")
        print(f"Data da Sessão: {i[2]}")
        print(f"Número da Sala: {i[3]}")
        print(f"Idioma: {i[4]}")
        print(f"Legendado: {i[5]}") 
        print(f"Classificação: {i[6]}")
        print(f"Sala 3D: {i[7]}")
        print(f"Sala VIP: {i[8]}")
        print("*****************************")

def report_boxoffice(conn):
    print("Ranking de Bilheteria por Filme")
    result = read_boxoffice_by_filme(conn)
    print("*****************************")

    rank = 1
    for i in result:
        print(f"{(rank)} - {i[0]}: {i[1]}")
        rank += 1
    print("*****************************")

def report_profit_by_genero(conn):
    print("Ranking de Lucro por Gênero de Filme")
    result = read_boxoffice_by_genero(conn)
    print("*****************************")

    rank = 1
    for i in result:
        print(f"{(rank)} - {i[0]}: {i[1]}")
        rank += 1
    print("*****************************")