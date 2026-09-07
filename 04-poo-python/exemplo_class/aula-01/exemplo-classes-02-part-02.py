class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):#Serve para retornar informações claras e compreensíveis para quem usa o programa, especialmente em String.
        return self.nome
        
    def listar_restaurante():
        for restaurante in Restaurante.restaurantes:
            print(f'Restaurante: {restaurante.nome}. Categoria: {restaurante.categoria}')
restaurante_01 = Restaurante("Madá Pizzaria", "Italiana")
restaurante_01 = Restaurante("Vinigucci Pizzaria", "Italiana")

Restaurante.listar_restaurante()


# print(restaurantes)
# print(restaurante_01)
# print(dir(restaurante_01))
# print(restaurante_01)
# print(vars(restaurante_01))
# print(restaurante_01.ativo) #Mostra somente esse atributo
# print(f"\nRestaurante: {restaurante_01.nome} \nCategoria: {restaurante_01.categoria}")


