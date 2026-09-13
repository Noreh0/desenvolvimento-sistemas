from models.cardapio.item_cardapio import ItemCardapio

# Não importei para gerar um erro --- Bebida(ItemCardapio):
class Bebida:
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho