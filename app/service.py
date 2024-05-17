import psycopg2

conn = psycopg2.connect(host='db', port=5432, user='postgres',
                        password='postgres', dbname='db')

def lista_pedidos():
    cur = conn.cursor()
    cur.execute('SELECT * FROM PEDIDOS')
    data = cur.fetchall()
    cur.close()
    if data == []:
        return {"message": "Nenhum pedido encontrado"}
    return [{"ID": row[0], "USUARIO": row[1], "EMAIL": row[2], "DESCRICAO": row[3]} for row in data]

def pedido_id(id: int):
    cur = conn.cursor()
    cur.execute('SELECT * FROM PEDIDOS WHERE ID = %s', (id,))
    data = cur.fetchall()
    cur.close()
    if data == []:
        return {"message": "Pedido não encontrado"}
    return [{"ID": row[0], "USUARIO": row[1], "EMAIL": row[2], "DESCRICAO": row[3]} for row in data]

def delete_pedido(id: int):
    cur = conn.cursor()
    cur.execute("DELETE FROM PEDIDOS WHERE ID = %s", (id,))
    conn.commit()
    cur.close()
    return

def cria_pedido(usuario: str, email: str, descricao: str):
    cur = conn.cursor()
    cur.execute('INSERT INTO PEDIDOS (USUARIO, EMAIL, DESCRICAO) VALUES (%s, %s, %s)', (usuario, email, descricao))
    conn.commit()
    cur.close()
    return

