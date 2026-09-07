# Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    def __init__(self, titulo, autor, ano_publicado):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicado = ano_publicado
        self._disponivel = True
    
# Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
    def __str__(self):
        return f"{self._titulo} - {self._autor} - Publicado em {self._ano_publicado} | {self._disponivel}"
# Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
    @property
    def disponivel(self):
        return 'Disponível' if self._disponivel else 'Emprestado'
        
    def emprestar(self):
        self._disponivel = not self._disponivel
    

livro01 = Livro("Linux", "Von Neumman", 1980)
livro02 = Livro("Potugol", "Louco", 2025)
livro01.emprestar()
print(livro01)
print(livro02)