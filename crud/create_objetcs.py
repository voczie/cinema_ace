import datetime

def create_object_filmes(conn):
    cursor = conn.cursor()

    data_required = {"Extenso":"Nome, Data de Estreia, Pais de Origem, Duracao, Direcao e Faixa Etaria",
                     "Tabela":"nome, data_estreia, pais_origem, duracao, direcao, faixa_etaria"}
    
    nome, data_estreia, pais_origem, duracao, direcao, faixa_etaria = input(f"Digite, separados por um |, o {data_required['Extenso']}: \n").split("|")
    
    query = (f'''INSERT INTO filmes({data_required['Tabela']}) VALUES (%s, %s, %s, %s, %s, %s)''')

    try:
        cursor.execute(query, (nome, data_estreia, pais_origem, duracao, direcao, faixa_etaria,))
    except:
        print("Erro ao inserir dados")
        conn.rollback()
        return
    
    conn.commit()

def create_object_generos(conn):
    cursor = conn.cursor()

    nome = input(f"Digite o nome do genero: \n")
    
    query = (f'''INSERT INTO generos(nome) VALUES (%s)''')
    
    try:    
        cursor.execute(query, (nome,))
    except:
        print("Erro ao inserir dados")
        conn.rollback()
        return
    
    conn.commit()

def create_object_generos_filmes(conn):
    cursor = conn.cursor()

    data_required = {"Extenso":"ID do Filme, ID do Genero",
                     "Tabela":"filme_id, genero_id"}
    
    filme_id, genero_id = input(f"Digite, separados por um |, o {data_required['Extenso']}: \n").split("|")
    
    query = (f'''INSERT INTO generos_filmes({data_required['Tabela']}) VALUES (%s, %s)''')
    
    try:    
        cursor.execute(query, (filme_id, genero_id,))
    except:
        print("Erro ao inserir dados")
        conn.rollback()
        return
    
    conn.commit()

def create_object_salas(conn):
    cursor = conn.cursor()

    data_required = {"Extenso":"Numero de Cadeiras, Tamanho da Tela, Capacidade Maxima de Pessoas, Exibe 3D, Sala VIP",
                     "Tabela":"numero_cadeiras, tamanho_tela, capacidade_maxima, tridimensional, vip"}
    
    numero_cadeiras, tamanho_tela, capacidade_maxima, tridimensional, vip = input(f"Digite, separados por um |, o {data_required['Extenso']}: \n").split("|")
    
    query = (f'''INSERT INTO salas({data_required['Tabela']}) VALUES (%s, %s, %s, %s, %s)''')
    
    try:    
        cursor.execute(query, (numero_cadeiras, tamanho_tela, capacidade_maxima, tridimensional, vip,))
    except:
        print("Erro ao inserir dados")
        conn.rollback()
        return
    
    conn.commit()

def create_object_sessoes(conn):
    cursor = conn.cursor()

    data_required = {"Extenso":"ID do Filme, Numero da Sala, Data de Exibicao, Faixa de Audio, Legendado",
                     "Tabela":"filme_id, numero_sala, data, faixa_audio, legenda"}
    
    filme_id, numero_sala, data, faixa_audio, legenda = input(f"Digite, separados por um |, o {data_required['Extenso']}: \n").split("|")

    query = (f'''INSERT INTO sessoes({data_required['Tabela']}) VALUES (%s, %s, %s, %s, %s)''')
    
    try:
        cursor.execute(query, (filme_id, numero_sala, data, faixa_audio, legenda,))
    except:
        print("Erro ao inserir dados")
        conn.rollback()
        return
    
    conn.commit()

def create_object_bilhetes(conn):
    cursor = conn.cursor()

    data_required = {"Extenso":"ID da Sessao, Valor da Compra",
                     "Tabela":"sessao_id, data_compra, valor_compra"}
    
    sessao_id, valor_compra = input(f"Digite, separados por um |, o {data_required['Extenso']}: \n").split("|")
    data_compra = datetime.datetime.now()

    query = (f'''INSERT INTO bilhetes({data_required['Tabela']}) VALUES (%s, %s, %s)''')
    
    try:
        cursor.execute(query, (sessao_id, data_compra, valor_compra))
    except:
        print("Erro ao inserir dados")
        conn.rollback()
        return
    
    conn.commit()