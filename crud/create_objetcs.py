import datetime
from read_objects import read_cap_max_sala, read_qnt_bilhetes_disponivel,read_flamenguista_onepiece_sousa, read_preco
from update_objects import update_qnt_bilhetes_disponivel

def create_object_filmes(conn):
    cursor = conn.cursor()

    data_required = {"Extenso":"Nome, Data de Estreia, Pais de Origem, Duracao, Direcao, Faixa Etaria e Se foi gravado em Mari",
                     "Tabela":"nome, data_estreia, pais_origem, duracao, direcao, faixa_etaria, gravado_mari"}
    
    nome, data_estreia, pais_origem, duracao, direcao, faixa_etaria, gravado_mari = input(f"Digite, separados por um |, o {data_required['Extenso']}: \n").split("|")
    
    query = (f'''INSERT INTO filmes({data_required['Tabela']}) VALUES (%s, %s, %s, %s, %s, %s, %s)''')

    try:
        cursor.execute(query, (nome, data_estreia, pais_origem, duracao, direcao, faixa_etaria, gravado_mari))
    except Exception as exc:
        print("Erro ao inserir dados")
        print(exc)
        conn.rollback()
        return
    
    conn.commit()

def create_object_generos(conn):
    cursor = conn.cursor()

    nome = input(f"Digite o nome do genero: \n")
    
    query = (f'''INSERT INTO generos(nome) VALUES (%s)''')
    
    try:    
        cursor.execute(query, (nome,))
    except Exception as exc:
        print("Erro ao inserir dados")
        print(exc)
        conn.rollback()
        return
    
    conn.commit()

def create_object_generos_filmes(conn):
    cursor = conn.cursor()

    data_required = {"Extenso":"ID do Filme, Nome do Genero",
                     "Tabela":"filme_id, genero"}
    
    filme_id, genero = input(f"Digite, separados por um |, o {data_required['Extenso']}: \n").split("|")
    
    query = (f'''INSERT INTO generos_filmes({data_required['Tabela']}) VALUES (%s, %s)''')
    
    try:    
        cursor.execute(query, (filme_id, genero,))
    except Exception as exc:
        print("Erro ao inserir dados. Voce digitou o nome do genero certo?")
        print(exc)
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
    except Exception as exc:
        print("Erro ao inserir dados")
        print(exc)
        conn.rollback()
        return
    
    conn.commit()

def create_object_sessoes(conn):
    cursor = conn.cursor()

    data_required = {"Extenso":"ID do Filme, Numero da Sala, Data de Exibicao, Faixa de Audio, Legendado, Preco Inteiro",
                     "Tabela":"filme_id, numero_sala, data, faixa_audio, legenda, qnt_bilhetes_disponivel, preco_inteira"}
    
    filme_id, numero_sala, data, faixa_audio, legenda, preco_inteira = input(f"Digite, separados por um |, o {data_required['Extenso']}: \n").split("|")
    
    qnt_bilhetes_disponivel = read_cap_max_sala(conn, numero_sala)

    query = (f'''INSERT INTO sessoes({data_required['Tabela']}) VALUES (%s, %s, %s, %s, %s, %s, %s)''')
    
    try:
        cursor.execute(query, (filme_id, numero_sala, data, faixa_audio, legenda, qnt_bilhetes_disponivel, preco_inteira,))
    except Exception as exc:
        print("Erro ao inserir dados")
        print(exc)
        conn.rollback()
        return
    
    conn.commit()

def create_object_pessoas(conn):
    cursor = conn.cursor()

    data_required = {"Extenso":"CPF, Nome, Idade, Login, Senha e Se é funcionário",
                     "Tabela":"cpf, nome, idade, login, senha"}
    
    cpf, nome, idade, login, senha, is_funcionario = input(f"Digite, separados por um |, o {data_required['Extenso']}: \n").split("|")

    query = (f'''INSERT INTO pessoas({data_required['Tabela']}) VALUES (%s, %s, %s, %s, %s)''')    

    try:
        cursor.execute(query, (cpf, nome, idade, login, senha,))
    except Exception as exc:
        print("Erro ao inserir dados")
        print(exc)
        conn.rollback()
        return

    if is_funcionario == '1':
        create_object_funcionarios(conn, cpf)
    else:
        create_object_clientes(conn, cpf)

    conn.commit()

def create_object_funcionarios(conn, cpf):
    cursor = conn.cursor()

    data_required = {"Extenso":"CPF e Salario",
                    "Tabela":"cpf, salario"}

    salario = input("Funcionario, digite seu salario: \n")
    query = (f'''INSERT INTO funcionarios({data_required['Tabela']}) VALUES (%s, %s)''')

    try:
        cursor.execute(query, (cpf, salario,))
    except Exception as exc:
        print("Erro ao inserir dados do Funcionario")
        print(exc)
        conn.rollback()
        return

def create_object_clientes(conn, cpf):
    cursor = conn.cursor()

    data_required = {"Extenso":"CPF, Torcedor do Flamengo, Assiste One Piece e Sousense",
                    "Tabela":"cpf, flamenguista, assiste_onepiece, sousense"}

    flamenguista, assiste_onepiece, sousense = input("Informe, usando 0 para Falso e 1 para Verdadeiro e separados por um | se você torce para o Flamengo, assiste One Piece ou nasceu em Sousa-PB: \n").split("|")
    query = (f'''INSERT INTO clientes({data_required['Tabela']}) VALUES (%s, %s, %s, %s)''')

    try:
        cursor.execute(query, (cpf, flamenguista, assiste_onepiece, sousense,))
    except Exception as exc:
        print("Erro ao inserir dados do Cliente")
        print(exc)
        conn.rollback()
        return
             
def create_object_bilhetes(conn):
    cursor = conn.cursor()

    data_required = {"Extenso":"ID da Sessao, Funcionario Vendedor, Cliente",
                     "Tabela":"sessao_id, funcionario_vendedor_id, cliente_id, preco_pago, tipo_pagamento, data_compra, compra_concluida"}
    
    sessao_id, funcionario_vendedor_id, cliente_id = input(f"Digite, separados por um |, o {data_required['Extenso']}: \n").split("|")
    data_compra = datetime.datetime.now()
    compra_concluida = '0'

    if read_qnt_bilhetes_disponivel(conn, sessao_id) <= 0:
        print("Sessao lotada :(")
        return
    if read_flamenguista_onepiece_sousa(conn, cliente_id).count(True) >= 1:
        preco_pago = read_preco(conn, sessao_id, True)
    else:
        preco_pago = read_preco(conn, sessao_id)
        preco_pago = preco_pago[0]

    tipos_pagamento = ["pix", "cartao", "boleto","berries"]
    tipo_pagamento = input(f"O valor do bilhete é {preco_pago}. Qual sera a forma de pagamento? \n")
    if tipo_pagamento.lower() in tipos_pagamento:
        compra_concluida = '1'
    else:
        print("Erro na hora de efetuar a compra")
        return
    
    query = (f'''INSERT INTO bilhetes({data_required['Tabela']}) VALUES (%s, %s, %s, %s, %s, %s, %s)''')
    
    try:
        cursor.execute(query, (sessao_id, funcionario_vendedor_id, cliente_id, preco_pago, tipo_pagamento, data_compra, compra_concluida))
    except Exception as exc:
        print("Erro ao inserir dados")
        print(exc)
        conn.rollback()
        return

    update_qnt_bilhetes_disponivel(conn, sessao_id)

    conn.commit()

def create_object_view_lista_all_sessoes(conn):
    cursor = conn.cursor()

    query = '''CREATE OR REPLACE VIEW public.all_sessoes AS SELECT se.id, fi.nome, se.data, sa.numero_sala, se.faixa_audio, se.legenda, fi.faixa_etaria, sa.tridimensional, sa.vip, se.qnt_bilhetes_disponivel, se.preco_inteira  FROM sessoes as se INNER JOIN filmes as fi ON fi.id = se.filme_id INNER JOIN salas as sa ON sa.numero_sala = se.numero_sala ORDER BY se.data ASC;'''

    cursor.execute(query)
    
    conn.commit()