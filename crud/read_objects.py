import datetime

def read_objects(table_name, conn, only_first = False):
    table_names = ['filmes', 'generos', 'generos_filme', 'salas', 'sessoes', 'bilhetes', 'pessoas', 'clientes', 'funcionarios']
    if table_name not in table_names:
        print(f"Tabela {table_name} nao existe")
        return
    
    cursor = conn.cursor()

    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)

    if only_first:
        result = cursor.fetchone()
    else:
        result = cursor.fetchall()
    
    return result

def read_filme_by_name(conn, name, exact_name = False):
    cursor = conn.cursor()

    if not exact_name: 
        name = "%" + name + "%"

    query = "SELECT * FROM filmes WHERE nome like %s;"
    cursor.execute(query, (name,))

    result = cursor.fetchall()
    return result

def read_all_sessoes(conn):
    cursor = conn.cursor()

    query = "SELECT * FROM public.all_sessoes ORDER BY data ASC;"
    cursor.execute(query)
    
    result = cursor.fetchall()
    return result

def read_sessoes_disponiveis(conn):
    cursor = conn.cursor()

    query = "SELECT * FROM public.all_sessoes WHERE data > %s ORDER BY data ASC;"

    cursor.execute(query, (datetime.date.today(),))
    
    result = cursor.fetchall()
    return result

def read_sessoes_by_preco(conn, low_preco, high_preco):
    cursor = conn.cursor()

    query = "SELECT * FROM public.all_sessoes WHERE preco_inteira BETWEEN %s::money AND %s::money"

    cursor.execute(query, (low_preco, high_preco,))
   
    result = cursor.fetchall()
    return result

def read_sessoes_by_gravado_mari(conn):
    cursor = conn.cursor()

    query = "SELECT se.id, fi.nome, se.data, sa.numero_sala, se.faixa_audio, se.legenda, fi.faixa_etaria, sa.tridimensional, sa.vip, se.qnt_bilhetes_disponivel, se.preco_inteira  FROM sessoes as se INNER JOIN filmes as fi ON fi.id = se.filme_id INNER JOIN salas as sa ON sa.numero_sala = se.numero_sala WHERE fi.gravado_mari"

    cursor.execute(query)
    result = cursor.fetchall()
    return result

def read_sessoes_by_categoria(conn, categoria):
    cursor = conn.cursor()

    query = "SELECT se.id, fi.nome, se.data, sa.numero_sala, se.faixa_audio, se.legenda, fi.faixa_etaria, sa.tridimensional, sa.vip, se.qnt_bilhetes_disponivel, se.preco_inteira  FROM sessoes as se INNER JOIN filmes as fi ON fi.id = se.filme_id INNER JOIN salas as sa ON sa.numero_sala = se.numero_sala INNER JOIN generos_filmes as gf ON fi.id = gf.filme_id WHERE gf.genero ILIKE %s"

    cursor.execute(query, (categoria,))
    result = cursor.fetchall()
    return result

def read_least_than_five_bilhetes(conn):
    cursor = conn.cursor()

    query = "SELECT * FROM public.all_sessoes WHERE qnt_bilhetes_disponivel < 5"

    cursor.execute(query)
    result = cursor.fetchall()
    return result

def read_boxoffice_by_filme(conn):
    cursor = conn.cursor()

    query = "SELECT fi.nome, SUM(bi.preco_pago) FROM bilhetes bi INNER JOIN sessoes se ON bi.sessao_id = se.id INNER JOIN filmes fi ON se.filme_id = fi.id GROUP BY fi.nome ORDER BY SUM(bi.preco_pago) DESC;"

    cursor.execute(query)

    result = cursor.fetchall()
    return result


def read_boxoffice_by_genero(conn):
    cursor = conn.cursor()

    query = "SELECT ge.nome, SUM(bi.preco_pago) FROM bilhetes bi INNER JOIN sessoes se ON bi.sessao_id = se.id INNER JOIN generos_filmes gf ON se.filme_id = gf.filme_id INNER JOIN generos ge ON gf.genero = ge.nome GROUP BY ge.nome ORDER BY SUM(bi.preco_pago) DESC;"

    cursor.execute(query)

    result = cursor.fetchall()
    return result

def read_cliente_compras(conn, cpf_cliente):
    cursor = conn.cursor()

    query = "SELECT se.id, fi.nome, se.data FROM bilhetes AS bi INNER JOIN sessoes AS se ON bi.sessao_id = se.id INNER JOIN filmes AS fi ON se.filme_id = fi.id WHERE bi.cliente_id = %s"

    cursor.execute(query, (cpf_cliente,))

    result = cursor.fetchall()
    return result

def read_cap_max_sala(conn, num_sala):
    cursor = conn.cursor()

    query = "SELECT sa.capacidade_maxima FROM salas sa WHERE sa.numero_sala = %s"
    
    cursor.execute(query, (num_sala,))

    result = cursor.fetchone()
    return result[0]

def read_qnt_bilhetes_disponivel(conn, id_sessao):
    cursor = conn.cursor()

    query = "SELECT se.qnt_bilhetes_disponivel FROM sessoes se WHERE se.id = %s"

    cursor.execute(query, (id_sessao,))

    result = cursor.fetchone()
    return result[0]

def read_flamenguista_onepiece_sousa(conn, id_cliente):
    cursor = conn.cursor()

    query = "SELECT cli.flamenguista, cli.assiste_onepiece, cli.sousense FROM clientes cli WHERE cli.cpf LIKE %s;"

    cursor.execute(query, (id_cliente,))

    result = cursor.fetchone()
    return result

def read_preco(conn, id_sessao, desconto = False):
    cursor = conn.cursor()

    query = "SELECT se.preco_inteira FROM sessoes se WHERE se.id = %s"

    cursor.execute(query, (id_sessao,))

    result = cursor.fetchone()

    if desconto:
        porcentagem_desconto = 0.9
        result = float(((result[0])[3:]).replace(',', '.')) * porcentagem_desconto #Para lidar com o tipo MONEY do PLSQL
        result = f"{result:.2f}".replace('.', ',') #Substituindo o . do float para , (pois faz mais sentido para nós)

    return result

def read_sell_by_funcionario(conn):
    cursor = conn.cursor()

    query = "SELECT pe.nome, SUM(bi.preco_pago) FROM bilhetes AS bi INNER JOIN pessoas AS pe ON bi.funcionario_vendedor_id = pe.cpf GROUP BY pe.nome ORDER BY SUM(bi.preco_pago) DESC"

    cursor.execute(query)

    result = cursor.fetchall()
    return result