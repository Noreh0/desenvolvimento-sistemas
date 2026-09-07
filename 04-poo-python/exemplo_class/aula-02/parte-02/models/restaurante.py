
# Criamos o import do modelo de avaliação
from models.avaliacao import Avaliacao
class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):#Serve para retornar informações claras e compreensíveis para quem usa o programa, especialmente em String.
        return self.nome
    @classmethod
    def listar_restaurante():
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:                                  #ljust não funciona para float, então por isso transformamos em string
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return "▣" if self._ativo else "▢"

    def alterar_conta(self):
        self._ativo = not self._ativo
    # Criamos uma função importando as avaliações dos clientes, podendo agora criar uma avaliação para o restaurante
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property #permite ler cada uma das avaliações para cada restaurante
    # Função criada para calcular a média das notas dos restaurantes
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        notas_somadas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(notas_somadas/quantidade_notas, 1)
        return media