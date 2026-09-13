#Aula POO 04 From e Imports

# O From ele vai servir para importar uma biblioteca ou aquivo de um lugar
from models.restaurante import Restaurante

japa_food = Restaurante("Japa", "Japonesa")
korean_food = Restaurante("Korean", "Coreana")
marmita_fresca = Restaurante("Marmifrex", "Brasileira")

marmita_fresca.alterar_conta()
#Agora podemos criar avaliações
marmita_fresca.receber_avaliacao("Heron", 7.5)

# Criada para poder executarmos aqui na app, todo o arquivo que criarmos
def main():
    Restaurante.listar_restaurante()
# Essa validação serve para verificar se estamos na aplicação principal
if __name__ == '__main__':
    main()
# Cria o pycache após executar, para exemplificar que estamos realizando a conexão entre os models da aplicação/funções