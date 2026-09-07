# Aula 02 — Propriedades, Encapsulamento e Organização de Projetos em POO com Python
### Projeto guia: "Sabor Express"
### Duração estimada: 4 horas

> Este documento contém apenas o **texto/conteúdo** de cada slide, na ordem de apresentação. O design e a diagramação ficam por sua conta.

---

## Slide 1 — Apresentação da Aula

**Título:** Orientação a Objetos com Python — Aula 02: Propriedades, Encapsulamento e Organização de Código

- Na aula passada criamos a classe `Restaurante`, com atributos, construtor, `__str__` e métodos próprios
- Hoje vamos deixar essa classe mais **profissional, protegida e organizada**
- Continuamos com o projeto **"Sabor Express"**
- Aula prática: vamos evoluir o mesmo código da Aula 01

---

## Slide 2 — Objetivo da Aula

**O que vamos ver hoje:**

- O decorador `@property` para controlar como um atributo é lido
- Atributos protegidos (`_underscore`) e por que proteger dados
- `@classmethod` e a diferença entre métodos de classe e de instância
- Como separar o projeto em múltiplos arquivos (`restaurante.py` e `app.py`) usando `import`
- Criar uma nova classe `Avaliacao` e relacioná-la com `Restaurante`
- Calcular e exibir a média de avaliações formatada no terminal

**Ao final da aula você será capaz de:** proteger dados de uma classe, organizar um projeto em múltiplos arquivos e relacionar duas classes entre si.

---

## Slide 3 — Questionamento Provocativo

**Pergunta para a turma:**

> "Se qualquer parte do código pode alterar `restaurante.ativo = 'batata'` sem nenhum controle... o que pode dar errado em um sistema real com várias pessoas mexendo no mesmo código?"

- Deixar a turma comentar por 1-2 minutos
- Retomar essa discussão quando falarmos de atributos protegidos e `@property`

---

## Slide 4 — Problema do Mundo Real

**Cenário:**

- O "Sabor Express" está crescendo: agora os restaurantes recebem **avaliações de clientes**
- Precisamos:
  - Impedir que qualquer trecho do código altere `_ativo` ou `_nota` de forma descontrolada
  - Exibir o status `ativo` de um jeito mais amigável (não só `True`/`False`)
  - Calcular automaticamente a média das avaliações de cada restaurante
  - Manter o projeto organizado à medida que ele cresce (mais de uma classe, mais de um arquivo)
- **A pergunta que fica:** como fazer tudo isso sem transformar o código em uma bagunça incontrolável?

---

## Slide 5 — Conteúdo Técnico: `@property`

- `@property` transforma um método em algo que se comporta como um **atributo** (sem usar `()`)
- Permite controlar **como um valor é exibido** ou calculado na hora da leitura
- Exemplo de uso: em vez de mostrar `True`/`False` para `ativo`, exibir um emoji indicando o status
- A lógica fica escondida dentro do método, mas o uso continua simples: `restaurante.ativo`

---

## Slide 6 — Conteúdo Técnico: Atributos Protegidos

- Prefixo `_` (underscore) no nome do atributo, como `self._ativo`, indica um **atributo protegido**
- Sinaliza para quem for usar a classe: "não altere isso diretamente, use um método ou property"
- Não impede tecnicamente o acesso, mas é a convenção usada pela comunidade Python
- Trabalha em conjunto com `@property`: a leitura/escrita passa a ser controlada pela classe

---

## Slide 7 — Conteúdo Técnico: `@classmethod` vs Métodos de Instância

- `@classmethod` indica que um método pertence à **classe**, não a uma instância específica
- Usa `cls` no lugar de `self` como primeiro parâmetro
- Exemplo: `listar_restaurantes()` vira um `@classmethod`, usando `cls` em vez do nome fixo da classe
- Já um método de instância, como `alternar_estado()`, atua sobre **um objeto específico**, alterando seu estado (`_ativo`)
- Diferença resumida:
  - `@classmethod` → afeta ou lê algo da classe como um todo
  - Método de instância → afeta um objeto individual

---

## Slide 8 — Conteúdo Técnico: Organização em Múltiplos Arquivos

- Separar a definição da classe (`modelos/restaurante.py`) da lógica principal (`app.py`)
- Uso do `import` para reaproveitar código: `from modelos.restaurante import Restaurante`
- Isso permite criar objetos e usar métodos (`listar_restaurantes()`, `alternar_estado()`) no `app.py`
- Sobre a pasta `__pycache__` e arquivos `.pyc`:
  - Gerados automaticamente pelo Python
  - Guardam o código já compilado em bytecode
  - Servem para otimizar a performance na execução de módulos importados

---

## Slide 9 — Conteúdo Técnico: Relacionando Classes (`Avaliacao`)

- Criamos uma nova classe `Avaliacao` (em `avaliacao.py`) com `__init__(self, cliente, nota)`
- Atributos `_cliente` e `_nota` protegidos, pois são dados sensíveis
- Na classe `Restaurante`, adicionamos um atributo `_avaliacoes` (lista vazia) no construtor
- Método `receber_avaliacao(cliente, nota)`:
  - Cria um objeto `Avaliacao`
  - Adiciona esse objeto à lista `_avaliacoes` do restaurante
- Isso é um **relacionamento entre classes**: um `Restaurante` guarda uma lista de objetos `Avaliacao`

---

## Slide 10 — Exemplo de Arquitetura / Código

**Estrutura de pastas atualizada:**

```
oo-sabor-express/
├── modelos/
│   ├── restaurante.py
│   ├── avaliacao.py
│   └── __init__.py
└── app.py
```

**Trecho de código (restaurante.py):**

```python
from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    @property
    def ativo(self):
        return '[x]' if self._ativo else '[ ]'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        soma = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        media = soma / len(self._avaliacoes)
        return round(media, 1)

    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(
                restaurante.nome.ljust(20)
                + restaurante.categoria.ljust(15)
                + restaurante.ativo.ljust(5)
                + str(restaurante.media_avaliacoes).ljust(5)
            )
```

---

## Slide 11 — Exemplo Prático 1

**Objetivo:** proteger e formatar o atributo `ativo`

- Alterar o atributo `ativo` da classe `Restaurante` para `_ativo`
- Criar uma `@property` chamada `ativo` que retorna um emoji/símbolo diferente para ativo/inativo
- Testar imprimindo o status de dois restaurantes diferentes

---

## Slide 12 — Exemplo Prático 2

**Objetivo:** `@classmethod` e `alternar_estado()`

- Transformar `listar_restaurantes()` em `@classmethod`, usando `cls`
- Criar o método `alternar_estado()` para alternar `_ativo` de um objeto
- Separar o projeto em `restaurante.py` e `app.py`, usando `import` para trazer a classe

---

## Slide 13 — Exemplo Prático 3

**Objetivo:** criar `Avaliacao` e calcular a média

- Criar a classe `Avaliacao` com `_cliente` e `_nota`
- Adicionar `_avaliacoes` e `receber_avaliacao()` na classe `Restaurante`
- Criar o método/`@property` `media_avaliacoes()`
- Adicionar a coluna de avaliação em `listar_restaurantes()`, convertendo a média para `str()` antes do `.ljust()`

---

## Slide 14 — Importância/Diferença: Conceito

**Atributo público vs. atributo protegido + `@property`:**

| Atributo público direto | Atributo protegido + `@property` |
|---|---|
| Qualquer código altera sem controle | Acesso e alteração passam por métodos |
| Sem validação nem formatação | Pode validar, formatar ou calcular na leitura |
| Difícil rastrear onde o dado mudou | Centraliza a regra em um único lugar |

**`@classmethod` vs método de instância:**

- `@classmethod` pertence à classe (ex.: listar todos os restaurantes)
- Método de instância pertence a um objeto específico (ex.: alternar o estado de UM restaurante)

- Retomar a pergunta do Slide 3 com a turma: agora dá pra explicar por que o encapsulamento evita bagunça

---

## Slide 15 — Importância/Diferença: Na Prática Digital

- Encapsulamento (`_atributo` + `@property`) é usado em praticamente todo sistema profissional: bancos, e-commerces, ERPs
- Evita bugs causados por alterações diretas e não controladas de dados sensíveis
- Projetos reais sempre separam classes em módulos/arquivos (nunca tudo em um arquivo só) — facilita trabalho em equipe e manutenção
- Relacionar classes (como `Restaurante` e `Avaliacao`) é a base de sistemas reais: pedidos, usuários, produtos, avaliações sempre se conectam entre si

---

## Slide 16 — Estrutura Profissional de Pastas

```
oo-sabor-express/
├── modelos/
│   ├── __init__.py
│   ├── restaurante.py       # classe Restaurante (encapsulada)
│   └── avaliacao.py         # classe Avaliacao
├── app.py                   # ponto de entrada, cria objetos e testa funcionalidades
├── testes/                  # testes automatizados (próximas aulas)
└── README.md
```

- `modelos/` concentra as regras de negócio (classes)
- `app.py` é responsável por "usar" as classes, não por defini-las
- Separação de responsabilidades = projeto mais fácil de manter e escalar

---

## Slide 17 — Atividades

**Atividade 1** — Na classe `Produto` (criada na Aula 01), proteger o atributo `disponivel` com `_` e criar uma `@property` que retorna "Disponível" ou "Indisponível".

**Atividade 2** — Criar um método de instância `alternar_disponibilidade()` na classe `Produto`, similar ao `alternar_estado()` do `Restaurante`.

**Atividade 3** — Transformar o método `listar_produtos()` em `@classmethod`, usando `cls` em vez do nome fixo da classe.

**Atividade 4** — Criar a classe `Avaliacao` de produto (`_cliente`, `_nota`) e um método `receber_avaliacao()` na classe `Produto`, guardando as avaliações em `_avaliacoes`.

**Atividade 5** — Criar a `@property` `media_avaliacoes` na classe `Produto`, seguindo os mesmos passos usados no `Restaurante` (soma, contagem, média, arredondamento).

**Atividade 6 (desafio)** — Separar as classes `Produto` e `Avaliacao` em arquivos próprios dentro de `modelos/`, e criar um `app.py` que importa ambas, cria objetos e exibe a listagem de produtos com nome, preço, disponibilidade e média de avaliação alinhados com `.ljust()`.

---

*Fim da sequência de conteúdo da Aula 02.*