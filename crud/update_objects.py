def update_hora_sessao(conn, id_sessao, nova_hora):
    cursor = conn.cursor()

    query = "UPDATE sessoes SET data = %s WHERE id = %s"
    
    try:
        cursor.execute(query, (nova_hora, id_sessao,))
    except:
        print("Erro ao inserir dados")
        conn.rollback()
        return
    
    print(f"Sessão de ID {id_sessao} atualizada com sucesso!")
    conn.commit()

def update_sala_sessao(conn, id_sessao, nova_sala):
    cursor = conn.cursor()

    query = "UPDATE sessoes SET numero_sala = %s WHERE id = %s"
    
    try:
        cursor.execute(query, (nova_sala, id_sessao,))
    except:
        print("Erro ao inserir dados")
        conn.rollback()
        return
    
    print(f"Sessão de ID {id_sessao} atualizada com sucesso!")
    conn.commit()

# FUNÇÃO SÓ DE TESTE, NÃO DEVEMOS ALTERAR O ID DOS OBJETOS
def update_filme_id(conn, id_filme, novo_id):
    cursor = conn.cursor()

    query = "UPDATE filmes  SET id = %s WHERE id = %s"
    
    try:
        cursor.execute(query, (novo_id, id_filme,))
    except:
        print("Erro ao inserir dados")
        conn.rollback()
        return
    
    print(f"Filme de antigo ID {id_filme} e novo ID {novo_id} atualizado com sucesso!")
    conn.commit()