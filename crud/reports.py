from read_objects import *

desconto = 0.9

def report_all_sessoes(conn):
    print("Todas as Sessões")
    result = read_all_sessoes(conn)
    
    for i in result:
        preco_desconto = float(((i[10])[3:]).replace(',', '.')) * desconto #Para lidar com o tipo MONEY do PLSQL
        preco_desconto = f"{preco_desconto:.2f}".replace('.', ',') #Substituindo o . do float para , (pois faz mais sentido para nós)
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
        print(f"Bilhetes Disponíveis: {i[9]}")
        print(f"Preço Inteiro: {i[10]}")
        print(f"Preço com Desconto: R$ {preco_desconto}")
        print("*****************************")

def report_sessoes_disponiveis(conn):
    print("Sessões Disponíveis para a Data Atual")
    result = read_sessoes_disponiveis(conn)
    
    for i in result:
        preco_desconto = float(((i[10])[3:]).replace(',', '.')) * desconto #Para lidar com o tipo MONEY do PLSQL
        preco_desconto = f"{preco_desconto:.2f}".replace('.', ',') #Substituindo o . do float para , (pois faz mais sentido para nós)
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
        print(f"Bilhetes Disponíveis: {i[9]}")
        print(f"Preço Inteiro: {i[10]}")
        print(f"Preço com Desconto: R$ {preco_desconto}")
        print("*****************************")

def report_sessoes_por_preco(conn, low_preco, high_preco):
    print(f"Sessões Disponíveis por preços entre R${low_preco} e R${high_preco}")
    result = read_sessoes_by_preco(conn, low_preco, high_preco)
    
    for i in result:
        preco_desconto = float(((i[10])[3:]).replace(',', '.')) * desconto #Para lidar com o tipo MONEY do PLSQL
        preco_desconto = f"{preco_desconto:.2f}".replace('.', ',') #Substituindo o . do float para , (pois faz mais sentido para nós)
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
        print(f"Bilhetes Disponíveis: {i[9]}")
        print(f"Preço Inteiro: {i[10]}")
        print(f"Preço com Desconto: R$ {preco_desconto}")
        print("*****************************")

def report_sessoes_por_categoria(conn, categoria):
    print(f"Sessões Disponíveis na categoria {categoria}")
    result = read_sessoes_by_categoria(conn, categoria)
    
    for i in result:
        preco_desconto = float(((i[10])[3:]).replace(',', '.')) * desconto #Para lidar com o tipo MONEY do PLSQL
        preco_desconto = f"{preco_desconto:.2f}".replace('.', ',') #Substituindo o . do float para , (pois faz mais sentido para nós)
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
        print(f"Bilhetes Disponíveis: {i[9]}")
        print(f"Preço Inteiro: {i[10]}")
        print(f"Preço com Desconto: R$ {preco_desconto}")
        print("*****************************")

def report_sessoes_por_filme_gravado_em_mari(conn):
    print(f"Sessões Disponíveis de Filmes gravados em Mari")
    result = read_sessoes_by_gravado_mari(conn)
    
    for i in result:
        preco_desconto = float(((i[10])[3:]).replace(',', '.')) * desconto #Para lidar com o tipo MONEY do PLSQL
        preco_desconto = f"{preco_desconto:.2f}".replace('.', ',') #Substituindo o . do float para , (pois faz mais sentido para nós)
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
        print(f"Bilhetes Disponíveis: {i[9]}")
        print(f"Preço Inteiro: {i[10]}")
        print(f"Preço com Desconto: R$ {preco_desconto}")
        print("*****************************")

def report_sessoes_esgotando(conn):
    print(f"Sessões Disponíveis que estão quase esgotando")
    result = read_least_than_five_bilhetes(conn)
    
    for i in result:
        preco_desconto = float(((i[10])[3:]).replace(',', '.')) * desconto #Para lidar com o tipo MONEY do PLSQL
        preco_desconto = f"{preco_desconto:.2f}".replace('.', ',') #Substituindo o . do float para , (pois faz mais sentido para nós)
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
        print(f"Bilhetes Disponíveis: {i[9]}!!!!")
        print(f"Preço Inteiro: {i[10]}")
        print(f"Preço com Desconto: R$ {preco_desconto}")
        print("*****************************")

def report_cliente_compras(conn, cpf_cliente):
    result = read_cliente_compras(conn, cpf_cliente)
    print("*****************************")

    compra = 1
    for i in result:
        print(f"{(compra)} - Sessão {i[0]} | {i[1]} | {i[2]}")
        compra += 1
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

def report_profit_by_funcionario(conn):
    print("Ranking de Lucro por Funcionário do CinemAce")
    result = read_sell_by_funcionario(conn)
    print("*****************************")
    rank = 1
    for i in result:
        print(f"{(rank)} - {i[0]}: {i[1]}")
        rank += 1
    print("*****************************")