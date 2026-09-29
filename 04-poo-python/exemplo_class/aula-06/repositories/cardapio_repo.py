from database.db import conectar
from models.cardapio.prato import Prato
from models.cardapio.bebida import Bebida


def tabela_cardapio():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS cardapio(
                id INT AUTO_INCREMENT PRIMARY KEY,
                id_restaurante INT,
                nome VARCHAR(255) NOT NULL,
                preco FLOAT(6,2) NOT NULL,
                tipo VARCHAR(30),
                descricao TEXT,
                tamanho VARCHAR(50),
                FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id)
            )
        """
    )
    conexao.commit()
    conexao.close()

def criar_item(id_restaurante, item):
    if isinstance(item, Prato):
        tipo_item = 'Prato'
        descricao = item.descricao
        tamanho = None
    elif isinstance(item, Bebida):
        tipo_item = 'Bebida'
        descricao = None
        tamanho = item.tamanho
            
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO cardapio(id_restaurante, nome, preco, tipo, descricao. tamanho) VALUES (%s,%s,%s,%s,%s, %s)
    """, (id_restaurante, item.nome, item.preco, tipo_item, descricao, tamanho))

    conexao.commit()
    conexao.close()

def listar_por_restaurante(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
            SELECT nome, preco, tipo, descricao, tamanho FROM cardapio WHERE id_restaurante = %s
        """, (id,)
    )
    resultado = cursor.fetchall()
    conexao.close()
    cardapio = []
    for nome_item, preco_item, tipo_item, descricao, tamanho in resultado:
        preco = float(preco_item)
        if tipo_item == 'Prato':
            cardapio.append(Prato(nome_item, preco, descricao))
        elif tipo_item == "Bebida":
            cardapio.append(Bebida(nome_item, preco, tamanho))
    return cardapio