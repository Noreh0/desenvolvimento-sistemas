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
    resultado = cursor.lastrowid
    conexao.close()
    restaurante.id = resultado
    return resultado


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

def listar_id_restaurante(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT * FROM restaurantes WHERE id = %s
    """, (id,))
    resultado = cursor.fetchone()
    conexao.close()

    id_resultado, nome, categoria, status = resultado
    restaurante = Restaurante(nome, categoria)
    restaurante._ativo = bool(status)
    restaurante.id = id_resultado
    return restaurante

def listar_informacoes(id):
    from repositories import avaliacao_repo, cardapio_repo
    restaurante = listar_id_restaurante(id)
    if restaurante is None:
        return None
    for avaliacao in avaliacao_repo.listar_por_restaurante(id):
        restaurante._avaliacao.append(avaliacao)
    for item in cardapio_repo.listar_por_restaurante(id):
        restaurante._cardapio.append(item)
    return restaurante