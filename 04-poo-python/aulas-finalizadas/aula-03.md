# Aula 03 — Herança em Python: Expandindo o Cardápio
### Projeto guia: "Sabor Express"
### Duração estimada: 4 horas

> Este documento contém apenas o **texto/conteúdo** de cada slide, na ordem de apresentação. O design e a diagramação ficam por sua conta.

---

## Slide 1 — Apresentação da Aula

**Título:** Orientação a Objetos com Python — Aula 03: Herança

- Nas aulas anteriores, construímos e blindamos a classe `Restaurante` (atributos, `@property`, `@classmethod`, `Avaliacao`)
- Hoje o projeto **"Sabor Express"** ganha um **cardápio**
- Vamos aprender o conceito de **herança**, um dos pilares da Orientação a Objetos
- Aula prática: seguimos evoluindo o mesmo código das aulas 01 e 02

---

## Slide 2 — Objetivo da Aula

**O que vamos ver hoje:**

- Como organizar uma nova pasta (`cardapio`) dentro de `modelos`
- Criar a classe base `ItemCardapio`
- Criar as classes `Prato` e `Bebida` que **herdam** de `ItemCardapio`
- Usar `super().__init__()` para reaproveitar o construtor da classe mãe
- Adicionar atributos específicos em cada subclasse
- Relacionar `Prato` e `Bebida` com o `Restaurante`, criando o cardápio

**Ao final da aula você será capaz de:** criar hierarquias de classes usando herança e evitar repetição de código entre classes parecidas.

---

## Slide 3 — Questionamento Provocativo

**Pergunta para a turma:**

> "Se `Prato` e `Bebida` são coisas diferentes, mas ambos têm `nome` e `preço`... vocês recriariam esses dois atributos do zero em cada classe, ou existe um jeito de reaproveitar o que já é comum entre elas?"

- Deixar a turma comentar por 1-2 minutos
- Retomar essa discussão ao apresentar a herança como solução

---

## Slide 4 — Problema do Mundo Real

**Cenário:**

- O "Sabor Express" agora precisa cadastrar itens de cardápio: pratos e bebidas
- Ambos compartilham características em comum: `nome` e `preço`
- Mas cada um também tem particularidades:
  - `Prato` tem uma `descricao`
  - `Bebida` tem um `tamanho`
- **O problema:** se criarmos `Prato` e `Bebida` como classes totalmente separadas, vamos duplicar `nome` e `preço` em cada uma — e se um dia precisarmos mudar essa regra, teremos que alterar em vários lugares
- **A pergunta que fica:** como garantir um padrão comum entre classes parecidas, sem repetir código?

---

## Slide 5 — Conteúdo Técnico: O que é Herança

- **Herança** permite que uma classe (subclasse/filha) herde atributos e comportamentos de outra classe (classe base/mãe)
- Evita repetição de código entre classes que compartilham características
- Mantém um padrão e uma linha de raciocínio consistente entre classes relacionadas
- No nosso projeto: `ItemCardapio` será a classe mãe de `Prato` e `Bebida`

---

## Slide 6 — Conteúdo Técnico: Criando a Classe Base

- Nova pasta `cardapio` dentro de `modelos`, para organizar as classes relacionadas ao cardápio
- Classe `ItemCardapio`: classe base para qualquer item do cardápio
- Construtor `__init__` define os atributos comuns: `_nome` e `_preco`
- Essa classe concentra tudo que **todo** item de cardápio precisa ter

---

## Slide 7 — Conteúdo Técnico: Herdando com `class Filha(Mae)`

- Para herdar de uma classe, importamos a classe base e a colocamos entre parênteses na declaração da subclasse:

```python
class Prato(ItemCardapio):
    ...
```

- Isso indica que `Prato` é uma subclasse de `ItemCardapio` e herda seus atributos e métodos

---

## Slide 8 — Conteúdo Técnico: `super().__init__()`

- Dentro do construtor da subclasse, usamos `super().__init__(nome, preco)` para chamar o construtor da classe mãe
- Isso inicializa os atributos herdados (`_nome`, `_preco`) sem precisar reescrevê-los
- Depois de chamar o `super()`, podemos adicionar atributos específicos da subclasse:
  - `Prato` ganha `descricao`
  - `Bebida` ganha `tamanho`
- Resultado: cada subclasse tem o que é comum (herdado) + o que é específico dela

---

## Slide 9 — Conteúdo Técnico: Relacionando Cardápio e Restaurante

- Na classe `Restaurante`, adicionamos o atributo `_cardapio` (lista vazia) no construtor
- Criamos dois métodos:
  - `adicionar_prato_no_cardapio(prato)`
  - `adicionar_bebida_no_cardapio(bebida)`
- Ambos recebem um objeto (`Prato` ou `Bebida`) e o adicionam à lista `_cardapio` usando `.append()`
- Isso é outro exemplo de **relacionamento entre classes**, como vimos com `Restaurante` e `Avaliacao` na Aula 02

---

## Slide 10 — Exemplo de Arquitetura / Código

**Estrutura de pastas atualizada:**

```
oo-sabor-express/
├── modelos/
│   ├── restaurante.py
│   ├── avaliacao.py
│   └── cardapio/
│       ├── __init__.py
│       ├── item_cardapio.py
│       ├── prato.py
│       └── bebida.py
└── app.py
```

**Trecho de código (item_cardapio.py):**

```python
class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    def __str__(self):
        return self._nome
```

**Trecho de código (prato.py e bebida.py):**

```python
from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao


class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho
```

**Trecho de código (restaurante.py — novos métodos):**

```python
def adicionar_prato_no_cardapio(self, prato):
    self._cardapio.append(prato)

def adicionar_bebida_no_cardapio(self, bebida):
    self._cardapio.append(bebida)
```

---

## Slide 11 — Exemplo Prático 1

**Objetivo:** criar a hierarquia de classes do cardápio

- Criar a pasta `modelos/cardapio`
- Criar a classe `ItemCardapio` com `_nome` e `_preco`
- Criar `Prato(ItemCardapio)` e `Bebida(ItemCardapio)`, usando `super().__init__()`
- Adicionar `descricao` em `Prato` e `tamanho` em `Bebida`

---

## Slide 12 — Exemplo Prático 2

**Objetivo:** instanciar e visualizar os itens

- Adicionar `__str__` em `Prato` e `Bebida` para exibir o nome do item
- No `app.py`, importar `Prato` e `Bebida`
- Criar uma bebida (ex.: "Suco de Melancia") e um prato (ex.: "Pãozinho")
- Imprimir os dois objetos e conferir a saída no terminal

---

## Slide 13 — Exemplo Prático 3

**Objetivo:** conectar o cardápio ao restaurante

- Adicionar `_cardapio` (lista vazia) no construtor de `Restaurante`
- Criar os métodos `adicionar_prato_no_cardapio()` e `adicionar_bebida_no_cardapio()`
- No `app.py`, adicionar a bebida e o prato criados ao `restaurante_praca`
- Desafio extra: imprimir manualmente o conteúdo de `_cardapio` para conferir se os itens foram adicionados

---

## Slide 14 — Importância/Diferença: Conceito

**Sem herança vs. com herança:**

| Classes separadas (sem herança) | Classes com herança |
|---|---|
| `nome` e `preco` repetidos em `Prato` e `Bebida` | `nome` e `preco` definidos uma única vez em `ItemCardapio` |
| Mudar uma regra exige editar várias classes | Mudar a classe mãe reflete em todas as filhas |
| Sem relação explícita entre as classes | Relação clara: `Prato` e `Bebida` **são** `ItemCardapio` |

- Retomar a pergunta do Slide 3: agora a turma consegue explicar por que reaproveitar `nome` e `preco` com herança é melhor que repetir código

---

## Slide 15 — Importância/Diferença: Na Prática Digital

- Herança é usada o tempo todo em sistemas reais: tipos de usuário (Cliente, Funcionário, Administrador herdando de Usuario), tipos de produto, tipos de pagamento, etc.
- Frameworks profissionais (Django, por exemplo) usam herança amplamente — desde models até views baseadas em classe
- Reduz duplicação de código e concentra regras de negócio comuns em um único lugar, facilitando manutenção
- Ajuda equipes a manterem um padrão entre módulos parecidos do sistema

---

## Slide 16 — Estrutura Profissional de Pastas

```
oo-sabor-express/
├── modelos/
│   ├── __init__.py
│   ├── restaurante.py
│   ├── avaliacao.py
│   └── cardapio/
│       ├── __init__.py
│       ├── item_cardapio.py     # classe base (mãe)
│       ├── prato.py             # herda de ItemCardapio
│       └── bebida.py            # herda de ItemCardapio
├── app.py
├── testes/
└── README.md
```

- Subpasta `cardapio/` agrupa tudo que é relacionado ao domínio "itens de cardápio"
- Classe base (`item_cardapio.py`) fica isolada das classes filhas, facilitando localizar o que é comum a todas
- Um domínio cresce (cardápio) sem bagunçar as outras partes do projeto (avaliações, restaurante)

---

## Slide 17 — Atividades

**Atividade 1** — Criar a classe base `Endereco` (ou `Pessoa`, à sua escolha) com atributos comuns, por exemplo `_rua`, `_cidade` (ou `_nome`, `_cpf`).

**Atividade 2** — Criar duas subclasses que herdem dessa classe base (ex.: `EnderecoEntrega(Endereco)` e `EnderecoCobranca(Endereco)`), usando `super().__init__()`.

**Atividade 3** — Adicionar em cada subclasse um atributo específico (ex.: `instrucoes_entrega` em `EnderecoEntrega` e `cnpj_cobranca` em `EnderecoCobranca`).

**Atividade 4** — Implementar `__str__` nas subclasses e instanciar um objeto de cada uma no `app.py`, imprimindo os resultados.

**Atividade 5** — Na classe `Restaurante`, criar um novo método `adicionar_endereco()` (reaproveitando a lógica de `adicionar_prato_no_cardapio()`), guardando os objetos em uma nova lista `_enderecos`.

**Atividade 6 (desafio)** — Juntar tudo: crie no `app.py` um restaurante com pelo menos 1 prato, 1 bebida e 1 endereço associados, e escreva um método `resumo()` na classe `Restaurante` que imprima nome do restaurante, quantidade de itens no cardápio e quantidade de endereços cadastrados.

---

*Fim da sequência de conteúdo da Aula 03.*