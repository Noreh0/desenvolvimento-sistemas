class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade

class Leitor:
    def __init__(self, nome, idade, proficao):
        self.nome = nome
        self.idade = idade
        self.proficao = proficao
    def __str__(self):
        return f'Meu nome é {self.nome}, tenho {self.idade} anos de idade e trabalho como {self.proficao}.'
    
    @classmethod
    def aniversario(self):
        self.idade += 1
    @property
    def suadacao(self):
        return f'Olá! Meu nome é {self.nome}, atualmente sou {self.proficao}! Obrigado.'

pessoa = Leitor("Heron", 23, "Programador")
print(pessoa)


class ContaBancaria:
    contas = []
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.contas.append(self)
    
    def __str__(self):
        return f"Titular:{self._titular}\nSaldo da conta:R${self._saldo}"

    def alterar_conta(self):
        self._ativo = not self._ativo

    @property
    def ativar_conta(self):
        return "▣" if self._ativo else "▢"


    @classmethod
    def listar_clientes(cls):
        print(f"{"Titular".ljust(25)}|{"Saldo".ljust(27)}|{"Status"}")
        for conta in cls.contas:
            print(f"{conta._titular.ljust(25)}|R${conta._saldo.ljust(25)}|{conta._ativo}")

usuario01 = ContaBancaria("Heron", "1000")

usuario01.alterar_conta()
ContaBancaria.listar_clientes()