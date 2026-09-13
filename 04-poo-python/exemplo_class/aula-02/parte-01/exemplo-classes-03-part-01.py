class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):#Serve para retornar informações claras e compreensíveis para quem usa o programa, especialmente em String.
        return self.nome
        
    def listar_restaurante():
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'inativo' if self._ativo else 'ativo'
restaurante_01 = Restaurante("Madá Pizzaria", "Italiana")
restaurante_01 = Restaurante("Vinigucci Pizzaria", "Italiana")

Restaurante.listar_restaurante()


print(restaurante_01)
# print(restaurante_01)
# print(dir(restaurante_01))
# print(restaurante_01)
# print(vars(restaurante_01))
# print(restaurante_01.ativo) #Mostra somente esse atributo
# print(f"\nRestaurante: {restaurante_01.nome} \nCategoria: {restaurante_01.categoria}")


