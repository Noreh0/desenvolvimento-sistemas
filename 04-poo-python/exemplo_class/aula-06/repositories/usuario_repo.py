from models.usuario import Usuario
from database.db import conectar

def tabela_usuario():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuario(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(254) NOT NULL, 
        email VARCHAR(254) NOT NULL,
        senha_hash VARCHAR(254) NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def criar_usuario(usuario):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
            INSERT INTO usuario(nome, email, senha_hash) VALUES (%s,%s,%s)
        """, (usuario.nome, usuario.email, usuario._senha_hash)
    )
    conexao.commit()
    id_usuario = cursor.lastrowid
    conexao.close()
    usuario.id = id_usuario
    return id_usuario

def buscar_email(email):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
            SELECT * FROM usuario WHERE email = %s
        """, (email,)
    )
    resultado = cursor.fetchone()
    conexao.close()
    if resultado is None:
        return None
    id_usuario, nome, email, senha_hash = resultado
    usuario = Usuario(nome, email, senha_hash)
    usuario.id = id_usuario
    return usuario

def buscar_id(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
            SELECT * FROM usuario WHERE id = %s
        """, (id,)
    )
    conexao.close()
    resultado = cursor.fetchone()
    if resultado is None:
        return None
    id_usuario, nome, email, senha_hash = resultado
    usuario = Usuario(nome, email, senha_hash)
    usuario.id = id_usuario
    return usuario