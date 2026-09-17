from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

japa_food = Restaurante("Japa", "Japonesa")
saque_japa = Bebida("Saque de uva", 16.99, "Grande")
pastel_flango = Prato("Pastel de flango", 18.99, "Pastel de carne de flango da sacada")
japa_food.adicionar_no_cardapio(pastel_flango)
japa_food.adicionar_no_cardapio(saque_japa)



def main():
    japa_food.exibir_cardapio

if __name__ == '__main__':
    main()