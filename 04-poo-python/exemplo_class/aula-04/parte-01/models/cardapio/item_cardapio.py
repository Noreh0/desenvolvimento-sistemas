from abc import ABC, abstractmethod
# importamos o métod abstrato - algo genérico para usar nos filhos - ABC = Abstract Class

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
    
    @abstractmethod
    def aplicar_desconto(self):
        pass