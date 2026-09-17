# Aula 03 (Melhorada) — Herança e Cardápio Inteligente
### Projeto guia: "Sabor Express"
### Duração estimada: 4 horas

> Este documento contém apenas o **texto/conteúdo** de cada slide, na ordem de apresentação. O design e a diagramação ficam por sua conta.
> Esta versão inclui, além da herança, a refatoração com `isinstance()` e a exibição inteligente do cardápio com `hasattr()`.

---

## Slide 1 — Apresentação da Aula

**Título:** Orientação a Objetos com Python — Aula 03: Herança e Cardápio Inteligente

- Nas aulas anteriores, construímos e blindamos a classe `Restaurante` (atributos, `@property`, `@classmethod`, `Avaliacao`)
- Hoje o projeto **"Sabor Express"** ganha um **cardápio** completo, organizado e inteligente
- Vamos aprender **herança** e como escrever código que se adapta a diferentes tipos de objeto
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
- **Refatorar** os métodos de adicionar itens em um único método, usando `isinstance()`
- Criar `exibir_cardapio()` como `@property`, tratando as diferenças entre os itens com `hasattr()`

**Ao final da aula você será capaz de:** criar hierarquias de classes com herança e escrever métodos genéricos que funcionam para diferentes tipos de objeto, sem duplicar código.

---

## Slide 3 — Questionamento Provocativo

**Pergunta para a turma:**

> "Se `Prato` e `Bebida` são coisas diferentes, mas ambos têm `nome` e `preço`... vocês recriariam esses dois atributos do zero em cada classe? E se amanhã vier uma `Sobremesa`, vocês criariam um método novo só para adicioná-la ao cardápio?"

- Deixar a turma comentar por 1-2 minutos
- Retomar essa discussão ao apresentar a herança e, mais adiante, o método unificado `adicionar_no_cardapio()`

---

## Slide 4 — Problema do Mundo Real

**Cenário:**

- O "Sabor Express" agora precisa cadastrar itens de cardápio: pratos e bebidas (e, no futuro, sobremesas, combos, etc.)
- Ambos compartilham características em comum: `nome` e `preço`
- Mas cada um também tem particularidades:
  - `Prato` tem uma `descricao`
  - `Bebida` tem um `tamanho`
- **Problema 1:** se criarmos `Prato` e `Bebida` como classes totalmente separadas, vamos duplicar `nome` e `preço` em cada uma
- **Problema 2:** se criarmos um método de adicionar item para cada tipo (`adicionar_prato_no_cardapio()`, `adicionar_bebida_no_cardapio()`...), o código não escala — cada novo tipo de item exige um novo método
- **Problema 3:** ao exibir o cardápio, como mostrar a descrição só para pratos e o tamanho só para bebidas, sem um monte de `if` explícito checando o tipo?
- **A pergunta que fica:** como escrever um código que se adapta a diferentes tipos de item sem crescer descontroladamente?

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
- Primeira versão: dois métodos separados — `adicionar_prato_no_cardapio(prato)` e `adicionar_bebida_no_cardapio(bebida)`
- Ambos recebem um objeto e o adicionam à lista `_cardapio` usando `.append()`
- Isso funciona, mas repete lógica — vamos melhorar isso a seguir

---

## Slide 10 — Conteúdo Técnico: Refatorando com `isinstance()`

- **Refatorar** = melhorar a estrutura do código sem mudar o que ele faz
- Unificamos os dois métodos em um só: `adicionar_no_cardapio(item)`
- Usamos `isinstance(item, ItemCardapio)` para verificar se o item é uma instância de `ItemCardapio` **ou de qualquer classe filha** (`Prato`, `Bebida`, e futuramente `Sobremesa`, etc.)
- Vantagem: não é mais necessário criar um método novo para cada tipo de item — a herança garante que tudo que é `ItemCardapio` passa pela mesma verificação
- Isso simplifica o código e facilita a manutenção conforme o cardápio cresce

---

## Slide 11 — Conteúdo Técnico: Exibindo o Cardápio com `hasattr()`

- Criamos `exibir_cardapio()` como uma `@property` (propriedade de leitura) dentro de `Restaurante`
- Usamos `enumerate()` para numerar os itens do cardápio a partir de 1
- Para cada item, exibimos o `nome` e o `preco` (comuns a todos)
- Para exibir os dados **específicos** (descrição do prato, tamanho da bebida), usamos `hasattr(item, 'nome_do_atributo')`:
  - Verifica se aquele objeto possui determinado atributo antes de tentar acessá-lo
  - Evita erro ao tentar mostrar `descricao` em uma `Bebida` (que não tem esse atributo) ou `tamanho` em um `Prato`
- Resultado: um cardápio completo, com os detalhes certos para cada tipo de item, sem precisar checar `if isinstance(item, Prato)` item por item

---

## Slide 12 — Exemplo de Arquitetura / Código

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

**Trecho de código (item_cardapio.py, prato.py e bebida.py):**

```python
class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    def __str__(self):
        return self._nome


class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao


class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho
```

**Trecho de código (restaurante.py — método unificado e exibição):**

```python
from modelos.cardapio.item_cardapio import ItemCardapio

def adicionar_no_cardapio(self, item):
    if isinstance(item, ItemCardapio):
        self._cardapio.append(item)

@property
def exibir_cardapio(self):
    print(f'Cardápio de {self.nome}')
    for indice, item in enumerate(self._cardapio, start=1):
        linha = f'{indice}. {item._nome} - R$ {item._preco}'
        if hasattr(item, '_descricao'):
            linha += f' | Descrição: {item._descricao}'
        if hasattr(item, '_tamanho'):
            linha += f' | Tamanho: {item._tamanho}'
        print(linha)
```

---

## Slide 13 — Exemplo Prático 1

**Objetivo:** criar a hierarquia de classes do cardápio

- Criar a pasta `modelos/cardapio`
- Criar a classe `ItemCardapio` com `_nome` e `_preco`
- Criar `Prato(ItemCardapio)` e `Bebida(ItemCardapio)`, usando `super().__init__()`
- Adicionar `descricao` em `Prato` e `tamanho` em `Bebida`, e um `__str__` que retorna o nome

---

## Slide 14 — Exemplo Prático 2

**Objetivo:** unificar a adição de itens com `isinstance()`

- Criar `_cardapio` (lista vazia) no construtor de `Restaurante`
- Criar o método único `adicionar_no_cardapio(item)`, validando com `isinstance(item, ItemCardapio)`
- No `app.py`, instanciar uma bebida e um prato e adicioná-los ao `restaurante_praca` usando o novo método
- Testar o que acontece ao tentar adicionar algo que **não** é um `ItemCardapio` (ex: uma string)

---

## Slide 15 — Exemplo Prático 3

**Objetivo:** exibir o cardápio de forma inteligente

- Criar a `@property` `exibir_cardapio()` na classe `Restaurante`
- Usar `enumerate()` para numerar os itens a partir de 1
- Usar `hasattr()` para mostrar `descricao` apenas em pratos e `tamanho` apenas em bebidas
- Testar no `app.py`, chamando `restaurante_praca.exibir_cardapio`

---

## Slide 16 — Importância/Diferença: Conceito

**Sem herança/isinstance vs. com herança/isinstance:**

| Abordagem sem herança e sem `isinstance()` | Abordagem com herança e `isinstance()` |
|---|---|
| `nome` e `preco` repetidos em cada classe de item | Definidos uma única vez em `ItemCardapio` |
| Um método de "adicionar" para cada tipo de item | Um único método `adicionar_no_cardapio()` para qualquer item |
| Cada novo tipo de item exige alterar vários lugares | Novo tipo de item só precisa herdar de `ItemCardapio` |
| `if`/`else` explícito para tratar cada tipo na exibição | `hasattr()` verifica dinamicamente o que aquele objeto tem |

- Retomar a pergunta do Slide 3: agora a turma consegue explicar por que herança + `isinstance()` evita ter que criar um método novo para cada tipo de item (como a `Sobremesa` do exemplo)

---

## Slide 17 — Importância/Diferença: Na Prática Digital

- Herança é usada o tempo todo em sistemas reais: tipos de usuário (Cliente, Funcionário, Administrador herdando de Usuario), tipos de produto, tipos de pagamento, etc.
- `isinstance()` é comum em bibliotecas e frameworks para validar tipos antes de processar dados, evitando erros em tempo de execução
- `hasattr()` é usado sempre que um sistema precisa lidar com objetos "parecidos, mas não iguais" — muito comum em cardápios, formulários dinâmicos e integrações com APIs externas
- Frameworks profissionais (Django, por exemplo) usam herança amplamente — desde models até views baseadas em classe
- Reduz duplicação de código e concentra regras de negócio comuns em um único lugar, facilitando manutenção

---

## Slide 18 — Estrutura Profissional de Pastas

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
- Métodos genéricos (`adicionar_no_cardapio`) ficam na classe que "recebe" os itens (`Restaurante`), não espalhados pelo projeto

---

## Slide 19 — Atividades

**Atividade 1** — Criar a classe base `Endereco` com atributos comuns, por exemplo `_rua` e `_cidade`.

**Atividade 2** — Criar duas subclasses que herdem dessa classe base (ex.: `EnderecoEntrega(Endereco)` e `EnderecoCobranca(Endereco)`), usando `super().__init__()` e adicionando um atributo específico em cada (`instrucoes_entrega` e `cnpj_cobranca`).

**Atividade 3** — Na classe `Restaurante`, criar uma lista `_enderecos` e um único método `adicionar_endereco(endereco)` que usa `isinstance(endereco, Endereco)` para validar antes de adicionar (assim como fizemos com `adicionar_no_cardapio()`).

**Atividade 4** — Criar uma nova classe `Sobremesa(ItemCardapio)` com um atributo específico `sabor`, e adicionar uma sobremesa ao cardápio usando o método `adicionar_no_cardapio()` já existente — sem alterar esse método.

**Atividade 5** — Atualizar a `@property` `exibir_cardapio()` para também exibir o `sabor` quando o item for uma `Sobremesa`, usando `hasattr()`.

**Atividade 6 (desafio)** — No `app.py`, monte um cenário completo: um restaurante com pelo menos 1 prato, 1 bebida, 1 sobremesa e 2 endereços (entrega e cobrança). Crie um método `resumo()` na classe `Restaurante` que imprima o nome do restaurante, a quantidade de itens no cardápio (usando `len(self._cardapio)`) e a quantidade de endereços cadastrados.

---

*Fim da sequência de conteúdo da Aula 03 (versão melhorada).*