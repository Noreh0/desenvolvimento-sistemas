# Comandos:
# python -m venv venv
# .\venv\Scripts\activate
#  pip install mysql-connector-python

# pyrefly: ignore [missing-import]
import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1234",
        database = "ifood2"
    )
    return conexao
# inserir - parte 03 oficial



def criar_avaliacao(id_restaurante, nome_usuario, nota_avaliacao):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO avaliacoes(id_restaurante, nome_usuario, nota_avaliacao) \
        VALUES (%s, %s, %s)
    """, (int(id_restaurante), nome_usuario, float(nota_avaliacao)))
    conexao.commit()
    conexao.close()

def listar_avaliacoes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT avaliacoes.id, restaurantes.nome_restaurante, avaliacoes.nome_usuario, avaliacoes.nota_avaliacao
        FROM avaliacoes
        JOIN restaurantes ON avaliacoes.id_restaurante = restaurantes.id 
    """)
    avaliacoes = cursor.fetchall()
    for avaliacao in avaliacoes:
        print(avaliacao)
    conexao.commit()
    conexao.close()
    