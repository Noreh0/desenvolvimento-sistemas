from models.cardapio.item_cardapio import ItemCardapio

class Sorvete(ItemCardapio):
    def __init__(self, nome, preco, sabor):
        super().__init__(nome,preco)
        self.sabor = sabor
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.1)