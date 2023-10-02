import datetime

def read_objects(table_name, conn, only_first = False):
    table_names = ['filmes', 'generos', 'generos_filme', 'salas', 'sessoes', 'bilhetes']
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

    query = "SELECT se.id, fi.nome, se.data, sa.id, se.faixa_audio, se.legenda, fi.faixa_etaria, sa.tridimensional, sa.vip FROM sessoes as se INNER JOIN filmes as fi ON fi.id = se.filme_id INNER JOIN salas as sa ON sa.id = se.numero_sala ORDER BY se.data ASC;"
    cursor.execute(query)
    
    result = cursor.fetchall()
    return result

def read_sessoes_disponiveis(conn):
    cursor = conn.cursor()

    query = "SELECT se.id, fi.nome, se.data, sa.id, se.faixa_audio, se.legenda, fi.faixa_etaria, sa.tridimensional, sa.vip FROM sessoes as se INNER JOIN filmes as fi ON fi.id = se.filme_id INNER JOIN salas as sa ON sa.id = se.numero_sala WHERE se.data > %s ORDER BY se.data ASC;"

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