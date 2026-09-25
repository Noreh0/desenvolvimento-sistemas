from database.db import conectar
from models.restaurante import Restaurante

def tabela_restaurante():
    conexao = conectar()
    cursor = conexao.cursor()
    tabela_restaurante = """
    CREATE TABLE IF NOT EXISTS restaurantes(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome_restaurante VARCHAR(100) NOT NULL,
        categoria_restaurante VARCHAR(100) NOT NULL,
        restaurante_ativo BOOLEAN DEFAULT FALSE NOT NULL
    )
    """
    cursor.execute(tabela_restaurante)
    conexao.commit()
    conexao.close()


def criar_restaurante(restaurante):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
            INSERT INTO restaurantes(nome_restaurante, categoria_restaurante) \
            VALUES (%s, %s)
        """, (restaurante.nome, restaurante.categoria)
    )
    conexao.commit()
    conexao.close()


def listar_restaurantes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
            SELECT * FROM restaurantes
        """
    )
    restaurantes_busca = cursor.fetchall()
    conexao.commit()
    conexao.close()
    restaurantes = []
    for id_banco, nome, categoria, ativo in restaurantes_busca:
        restaurante = Restaurante(nome, categoria)
        restaurante._ativo = bool(ativo)
        restaurante.id = id_banco
        restaurantes.append(restaurante)
    return restaurantes
