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

def read_boxoffice_by_filme(conn):
    cursor = conn.cursor()

    query = "SELECT fi.nome, SUM(bi.valor_compra) FROM bilhetes bi INNER JOIN sessoes se ON bi.sessao_id = se.id INNER JOIN filmes fi ON se.filme_id = fi.id GROUP BY fi.nome ORDER BY SUM(bi.valor_compra) DESC;"

    cursor.execute(query)

    result = cursor.fetchall()
    return result


def read_boxoffice_by_genero(conn):
    cursor = conn.cursor()

    query = "SELECT ge.nome, SUM(bi.valor_compra) FROM bilhetes bi INNER JOIN sessoes se ON bi.sessao_id = se.id INNER JOIN generos_filmes gf ON se.filme_id = gf.filme_id INNER JOIN generos ge ON gf.genero_id = ge.id GROUP BY ge.nome ORDER BY SUM(bi.valor_compra) DESC;"

    cursor.execute(query)

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

    
