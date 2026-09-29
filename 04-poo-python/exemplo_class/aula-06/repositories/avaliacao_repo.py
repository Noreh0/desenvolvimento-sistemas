from models.avaliacao import Avaliacao
from database.db import conectar

def tabela_avaliacao():
    conexao = conectar()
    cursor = conexao.cursor()
    tabela_avaliacoes = """
    CREATE TABLE IF NOT EXISTS avaliacoes(
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_restaurante INT,
        nome_usuario VARCHAR(100) NOT NULL,
        nota_avaliacao DECIMAL(2,1),
        FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id)
    )
    """
    cursor.execute(tabela_avaliacoes)
    conexao.commit()
    conexao.close()

def criar_avaliacao(id_restaurante, avaliacao):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO avaliacoes(id_restaurante, nome_usuario, nota_avaliacao) VALUES (%s,%s,%s)
    """, (id_restaurante, avaliacao._cliente, avaliacao._nota))
    conexao.commit()
    conexao.close()

def listar_por_restaurante(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
            SELECT nome_usuario, nota_avaliacao FROM avaliacoes WHERE id_restaurante = %s
        """,
        (id,)
    )
    resultado = cursor.fetchall()
    conexao.close()
    avaliacoes = []
    for nome, nota in resultado:
        avaliacoes.append(Avaliacao(nome, float(nota)))
    return avaliacoes