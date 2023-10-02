def delete_filme(conn, id_filme):
    cursor = conn.cursor()

    query = "DELETE FROM filmes WHERE id = %s"
    
    try:
        cursor.execute(query, (id_filme,))
    except:
        print("Erro ao inserir dados")
        conn.rollback()
        return
    
    print(f"Filme de ID {id_filme} deletado com sucesso!")
    conn.commit()

def delete_genero(conn, id_genero):
    cursor = conn.cursor()

    query = "DELETE FROM generos WHERE id = %s"

    try:
        cursor.execute(query, (id_genero,))
    except:
        print("Erro ao inserir dados")
        conn.rollback()
        return
    
    print(f"Genero de ID {id_genero} deletado com sucesso!")
    conn.commit()

def delete_genero_filme(conn, id_filme, id_genero):
    cursor = conn.cursor()

    query = "DELETE FROM generos_filmes WHERE filme_id = %s AND genero_id = %s"

    try:
        cursor.execute(query, (id_filme, id_genero))
    except:
        print("Erro ao inserir dados")
        conn.rollback()
        return
    
    print(f"Genero-Filme de IDs {id_filme}, {id_genero} deletado com sucesso!")
    conn.commit()

def delete_sala(conn, id_sala):
    cursor = conn.cursor()

    query = "DELETE FROM salas WHERE id = %s"

    try:
        cursor.execute(query, (id_sala,))
    except:
        print("Erro ao inserir dados")
        conn.rollback()
        return
    
    print(f"Sala de ID {id_sala} deletada com sucesso!")
    conn.commit()

def delete_sessao(conn, id_sessao):
    cursor = conn.cursor()

    query = "DELETE FROM sessoes WHERE id = %s"
    
    try:
        cursor.execute(query, (id_sessao,))
    except:
        print("Erro ao inserir dados")
        conn.rollback()
        return
    
    print(f"Sessão de ID {id_sessao} deletada com sucesso!")
    conn.commit()

def delete_bilhete(conn, id_bilhete):
    cursor = conn.cursor()

    query = "DELETE FROM bilhetes WHERE id = %s"
    
    try:
        cursor.execute(query, (id_bilhete,))
    except:
        print("Erro ao inserir dados")
        conn.rollback()
        return
    
    print(f"Bilhete de ID {id_bilhete} deletado com sucesso!")
    conn.commit()