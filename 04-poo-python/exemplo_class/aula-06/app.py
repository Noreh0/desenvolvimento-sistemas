from functools import wraps
from flask import Flask, render_template

from repositories.restaurante_repo import tabela_restaurante, criar_restaurante, listar_restaurantes
from models.restaurante import Restaurante

la_mafia = Restaurante("La Mafia","Italiana")

def main():
    # tabela_restaurante()
    # criar_restaurante(la_mafia)
    listar_restaurantes()

if __name__ == '__main__':
    main()