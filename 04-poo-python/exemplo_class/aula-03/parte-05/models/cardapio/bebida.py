from models.cardapio.item_cardapio import ItemCardapio

# Não importei para gerar um erro --- Bebida(ItemCardapio):
class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho
    def __str__(self):
        return self._nome