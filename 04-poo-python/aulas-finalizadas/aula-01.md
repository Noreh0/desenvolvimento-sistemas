# Aula 01 — Introdução à Programação Orientada a Objetos com Python
### Projeto guia: "Sabor Express"
### Duração estimada: 4 horas

> Este documento contém apenas o **texto/conteúdo** de cada slide, na ordem de apresentação. O design e a diagramação ficam por sua conta.

---

## Slide 1 — Apresentação da Aula

**Título:** Orientação a Objetos com Python — Aula 01: Classes e Objetos

- Bem-vindos(as) à primeira aula do módulo de Programação Orientada a Objetos (POO)
- Vamos aprender usando um projeto prático: o sistema **"Sabor Express"**
- Aula 100% prática: menos teoria solta, mais mão na massa
- Pré-requisitos: lógica de programação básica em Python (variáveis, funções, listas)

---

## Slide 2 — Objetivo da Aula

**O que vamos ver hoje:**

- O que é uma **classe** e o que é um **objeto**
- Como criar atributos e instanciar objetos
- O método construtor `__init__` e o papel do `self`
- O método especial `__str__`
- Como criar métodos próprios dentro de uma classe
- Como estruturar um projeto Python de forma profissional

**Ao final da aula você será capaz de:** modelar uma entidade do mundo real como uma classe em Python e manipular seus objetos.

---

## Slide 3 — Questionamento Provocativo

**Pergunta para a turma:**

> "Se vocês já sabem usar variáveis, listas e dicionários para guardar dados... por que precisamos de mais um jeito de organizar informação?"

- Deixar a turma responder/discutir por 1-2 minutos
- Anotar as respostas no quadro/chat para retomar no final da aula (quando compararmos POO com dicionários)

---

## Slide 4 — Problema do Mundo Real

**Cenário:**

- Imagine que o "Sabor Express" precisa cadastrar dezenas de restaurantes parceiros
- Cada restaurante tem nome, categoria e status (ativo ou não)
- Se usarmos apenas dicionários soltos, corremos o risco de:
  - Esquecer de preencher um campo
  - Escrever o nome da chave errado (`'nome'` vs `'Nome'`)
  - Não ter um jeito padronizado de exibir ou comparar restaurantes
- **A pergunta que fica:** como garantir que todo restaurante cadastrado no sistema siga sempre a mesma estrutura, com os mesmos dados obrigatórios?
- É esse problema que a Orientação a Objetos resolve

---

## Slide 5 — Conteúdo Técnico: O que é uma Classe

- Uma **classe** é uma abstração do mundo real: um "molde" que agrupa características (atributos) de uma entidade
- No projeto Sabor Express, vamos modelar um restaurante com:
  - `nome` (string)
  - `categoria` (string)
  - `ativo` (booleano)
- Sintaxe em Python:
  - Palavra reservada `class`
  - Nome da classe com inicial maiúscula (convenção)
  - Dois pontos `:` e corpo indentado

---

## Slide 6 — Conteúdo Técnico: Objetos (Instâncias)

- Um **objeto** é uma representação concreta da classe (uma instância)
- Para criar um objeto: nome da classe + parênteses, atribuído a uma variável
- Podemos criar quantos objetos quisermos a partir da mesma classe
- Cada objeto guarda seus próprios valores, independentes dos demais

---

## Slide 7 — Conteúdo Técnico: Construtor `__init__` e `self`

- `__init__` é o **método construtor**: roda automaticamente quando o objeto é criado
- Garante que todo objeto já nasça com os atributos preenchidos
- `self` é o primeiro parâmetro de qualquer método de instância e representa **o próprio objeto**
- Analogia: assim como passamos parâmetros para uma função, passamos valores para o construtor
- Vantagem sobre dicionários: com `__init__` definido, **não é possível** criar um objeto sem fornecer os dados obrigatórios → mais consistência

---

## Slide 8 — Conteúdo Técnico: `__str__` e Métodos Especiais

- Métodos especiais em Python têm `__` (dois underlines) antes e depois do nome
- `__str__` define como o objeto será exibido quando impresso ou convertido para texto
- Sem `__str__`, o `print()` mostra apenas o endereço de memória do objeto
- Com `__str__`, escolhemos quais informações mostrar (nome, categoria, etc.) — facilita debug e leitura do código

---

## Slide 9 — Conteúdo Técnico: Métodos Próprios

- Além dos métodos especiais, podemos criar **nossos próprios métodos**
- Usamos `def` dentro da classe, seguindo a convenção `snake_case`
- Exemplo de uso: um método que percorre e lista todos os restaurantes já cadastrados
- A classe pode manter uma lista de todas as instâncias criadas, atualizada dentro do `__init__`

---

## Slide 10 — Exemplo de Arquitetura / Código

**Estrutura de pastas do projeto:**

```
oo-sabor-express/
└── modelos/
    └── restaurante.py
```

**Código da classe (restaurante.py):**

```python
class Restaurante:
    restaurantes = []  # lista de todas as instâncias

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} - {self.categoria}'

    def listar_restaurantes(self):
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | Ativo: {restaurante.ativo}')
```

---

## Slide 11 — Exemplo Prático 1

**Objetivo:** criar a classe e os primeiros objetos

- Criar a pasta `oo-sabor-express/modelos/restaurante.py`
- Escrever a classe `Restaurante` com `__init__` (nome, categoria, ativo)
- Criar dois objetos: `restaurante_praca` e `restaurante_pizza`
- Usar `print()` para ver o resultado sem e com `__str__`

---

## Slide 12 — Exemplo Prático 2

**Objetivo:** inspecionar e comparar objetos

- Usar `vars(restaurante_praca)` para ver os atributos em formato de dicionário
- Usar `dir(restaurante_praca)` para ver todos os atributos/métodos disponíveis
- Alterar o valor de `ativo` para `True` em um dos objetos e verificar com `vars()`

---

## Slide 13 — Exemplo Prático 3

**Objetivo:** criar e usar um método próprio

- Adicionar o método `listar_restaurantes()` à classe
- Criar 3 ou mais objetos `Restaurante`
- Chamar `Restaurante.listar_restaurantes()` (ou pela instância) e observar a saída
- Desafio extra: adicionar um novo atributo (ex: `nota_media`) e refletir no `__str__`

---

## Slide 14 — Importância/Diferença: Conceito

**POO vs. estruturas soltas (dicionários/listas):**

| Dicionário / variáveis soltas | Classe (POO) |
|---|---|
| Sem garantia de estrutura fixa | Estrutura padronizada e obrigatória |
| Fácil esquecer um campo | `__init__` obriga o preenchimento |
| Sem comportamento embutido | Métodos ligam dados + comportamento |
| Difícil de escalar/manter | Organiza o crescimento do sistema |

- Retomar a pergunta do Slide 3 com a turma: agora dá pra responder com propriedade

---

## Slide 15 — Importância/Diferença: Na Prática Digital

- POO é o paradigma dominante em sistemas de médio/grande porte no mercado
- Frameworks amplamente usados (Django, Flask com classes, FastAPI, sistemas de e-commerce, apps bancários) são construídos sobre POO
- Facilita trabalho em equipe: cada pessoa desenvolvedora mexe em uma classe/módulo sem quebrar o resto
- Base para conceitos avançados que vêm depois: herança, polimorfismo, encapsulamento

---

## Slide 16 — Estrutura Profissional de Pastas

```
oo-sabor-express/
├── modelos/
│   ├── restaurante.py       # classes do domínio (Restaurante, Produto, Pedido...)
│   └── __init__.py
├── main.py                  # ponto de entrada da aplicação
├── testes/                  # testes automatizados (próximas aulas)
└── README.md                # documentação do projeto
```

- `modelos/`: guarda as classes que representam entidades do mundo real
- Separar por responsabilidade facilita manutenção e localização do código
- Convenção que se repete em projetos profissionais reais (inclusive em frameworks)

---

## Slide 17 — Atividades

**Atividade 1** — Criar a classe `Produto` com atributos `nome`, `preco` e `disponivel`, usando `__init__`.

**Atividade 2** — Criar 3 objetos da classe `Produto` e imprimir cada um usando `__str__` (defina o `__str__` também).

**Atividade 3** — Criar um método `aplicar_desconto(self, percentual)` na classe `Produto` que altera o `preco`.

**Atividade 4** — Adicionar à classe `Produto` uma lista de classe `produtos` (igual ao exemplo do `Restaurante`) e um método `listar_produtos()`.

**Atividade 5** — Integrar as duas classes: criar uma classe `Pedido` que recebe um `Restaurante` e uma lista de `Produto` (reaproveitar os objetos criados nas atividades anteriores).

**Atividade 6 (desafio)** — Usando `vars()` e `dir()`, investigar e listar, em formato de texto, todos os atributos de instância de um objeto `Pedido` criado na Atividade 5.

---

*Fim da sequência de conteúdo da Aula 01.*