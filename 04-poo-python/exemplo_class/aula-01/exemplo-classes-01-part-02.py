class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_01 = Restaurante("Madá Pizzaria", "Italiana")
restaurantes = [restaurante_01]

# print(restaurantes)
# print(restaurante_01)
print(dir(restaurante_01))
print(restaurante_01)
# print(vars(restaurante_01))
# print(restaurante_01.ativo) #Mostra somente esse atributo
# print(f"\nRestaurante: {restaurante_01.nome} \nCategoria: {restaurante_01.categoria}")


