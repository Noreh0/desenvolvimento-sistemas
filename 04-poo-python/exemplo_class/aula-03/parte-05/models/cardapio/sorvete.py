from models.cardapio.item_cardapio import ItemCardapio

class Sorvete(ItemCardapio):
    def __init__(self, nome, preco, sabor):
        super().__init__(nome,preco)
        self.sabor = sabor