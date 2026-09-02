# Aula 03 — Templates, Arquivos Estáticos e Novas Páginas no Django
### Sequência de conteúdo para montagem dos slides (duração total: 4h)

---

## SLIDE 1 — Apresentação da Aula

**Título:** Django na Prática: Templates, Estilo Visual e Novas Páginas

**Texto de apoio:**
Na Aula 02 vocês criaram o app "galeria" e fizeram a primeira página aparecer com `HttpResponse`. Hoje vamos deixar esse código profissional de verdade: separar o HTML da lógica Python, aplicar o layout oficial do projeto, carregar CSS e imagens, e criar uma segunda página navegável.

**Fala do professor (script sugerido):**
"Hoje o projeto sai do 'texto simples na tela' e vira uma aplicação com cara de produto real: com layout, estilo e mais de uma página."

---

## SLIDE 2 — Objetivo da Aula

**Título:** O que vamos aprender hoje

**Tópicos:**
- Entender por que não devemos escrever HTML dentro do `HttpResponse`
- Configurar a pasta de templates no `settings.py`
- Usar a função `render` para renderizar arquivos HTML
- Organizar templates por app (`templates/galeria`)
- Configurar e carregar arquivos estáticos (CSS e imagens)
- Rodar o `collectstatic`
- Usar as tags `{% load static %}` e `{% static %}`
- Criar uma nova página (`produtos.html`) com sua própria view e rota

---

## SLIDE 3 — Pergunta Provocativa

**Título:** Antes de começar, pense...

**Pergunta central:**
"Por que é ruim escrever todo o HTML da página dentro de uma string de Python, no meio da lógica do sistema?"

**Perguntas de apoio (para gerar debate em sala):**
- O que aconteceria se uma pessoa do time de design precisasse editar o texto de uma página, mas o HTML estivesse escondido dentro de código Python?
- Um site sem nenhum CSS carregado é uma boa experiência para o usuário final?
- Por que sites reais têm várias páginas em vez de uma única tela?

**Orientação ao professor:** deixe a turma responder antes de revelar a próxima parte da aula.

---

## SLIDE 4 — O Problema do Mundo Real

**Título:** Os problemas que esta aula resolve

**Texto de apoio:**
Aplicações reais em produção precisam de:
- **Separação de responsabilidades:** designers e devs de front-end trabalham no HTML/CSS sem precisar mexer na lógica Python
- **Identidade visual:** um site sem estilo (CSS) e sem imagens carregadas transmite pouca credibilidade e prejudica a experiência do usuário
- **Navegação:** usuários esperam poder clicar e ir de uma página para outra dentro do mesmo site

**Gancho para a próxima parte:**
"O Django resolve tudo isso com um sistema de templates, arquivos estáticos e roteamento entre páginas. Vamos ver como funciona na prática."

---

## SLIDE 5 — Conteúdo Técnico: Templates

**Título:** Separando HTML da lógica Python

**Pontos-chave:**
- Escrever HTML dentro do `HttpResponse` funciona, mas não escala e mistura responsabilidades
- A solução do Django é o sistema de **templates**: arquivos `.html` isolados em uma pasta própria
- A função `render()` substitui o `HttpResponse`, conectando a view a um arquivo HTML

**Fluxo lógico:**
1. Configurar no `settings.py` onde o Django deve procurar os templates
2. Criar a pasta `templates` e o arquivo HTML
3. Trocar `HttpResponse` por `render` na view

---

## SLIDE 6 — Sequência de Configuração: Templates

**Título:** Sequência lógica de configuração (parte 1)

**Passo a passo, na ordem de uso:**

1. Abrir `setup > settings.py` e localizar a seção `TEMPLATES`
2. Configurar `'DIRS': [os.path.join(BASE_DIR, 'templates')]`
   → Informa ao Django onde procurar os arquivos HTML do projeto
3. Criar a pasta `templates` na raiz do projeto (ex: dentro de `alura-space`)
4. Criar o arquivo `index.html` dentro dessa pasta, com um `<h1>` e um `<p>`
5. Em `galeria > views.py`, importar e usar a função `render` no lugar do `HttpResponse`:

```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

---

## SLIDE 7 — Exemplo de Arquitetura: Templates Organizados por App

**Título:** Organizando templates dentro de cada app

**Boa prática apresentada:**
- Mover `index.html` para dentro de uma subpasta com o nome do app: `templates/galeria/index.html`
- Atualizar a referência no `views.py` para `'galeria/index.html'`

**Por que isso importa:** em projetos com muitos apps, cada um mantém seus próprios templates organizados, evitando conflitos de nomes de arquivos entre apps diferentes.

**Exemplo de estrutura:**
```
alura-space/
├── templates/
│   └── galeria/
│       ├── index.html
│       └── produtos.html
```

---

## SLIDE 8 — Exemplo Prático 1 (mão na massa)

**Título:** Vamos praticar juntos: renderizando o primeiro template

**Passo a passo para reproduzir ao vivo:**
1. Configurar `DIRS` no `settings.py`
2. Criar a pasta `templates/galeria`
3. Criar o `index.html` com o conteúdo do projeto Alura Space (layout fornecido)
4. Atualizar a view `index` para usar `render` apontando para `'galeria/index.html'`
5. Testar no navegador e confirmar que o layout aparece (ainda sem CSS)

---

## SLIDE 9 — Conteúdo Técnico: Arquivos Estáticos

**Título:** Carregando CSS e imagens no Django

**Pontos-chave:**
- Arquivos estáticos = CSS, imagens, ícones, JavaScript
- O Django precisa ser configurado para saber onde procurar e onde reunir esses arquivos
- Duas configurações principais no `settings.py`:
  - `STATICFILES_DIRS` → onde o Django **procura** os arquivos estáticos durante o desenvolvimento (ex: `setup/static`)
  - `STATIC_ROOT` → para onde o Django **coleta** todos os arquivos estáticos (usado em produção)

---

## SLIDE 10 — Sequência de Configuração: Arquivos Estáticos

**Título:** Sequência lógica de configuração (parte 2)

**Passo a passo, na ordem de uso:**

1. Criar a pasta `static` dentro de `setup`
2. Mover os arquivos CSS e outros ativos visuais para essa pasta
3. Configurar `STATICFILES_DIRS` e `STATIC_ROOT` no `settings.py`
4. Rodar `python manage.py collectstatic`
   → Reúne todos os arquivos estáticos configurados nos diretórios definidos
5. No `index.html`, adicionar `{% load static %}` no topo do arquivo
6. Trocar os caminhos fixos de CSS/imagens pela tag `{% static 'caminho/do/arquivo.css' %}`

---

## SLIDE 11 — Exemplo de Código: Usando Arquivos Estáticos no Template

**Título:** Exemplo de arquitetura — template com static

**Exemplo de código (`index.html`):**
```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <img src="{% static 'img/logo.png' %}" alt="Logo">
    ...
</body>
</html>
```

**Destaque para comentar:** a tag `{% static %}` precisa ser usada em **cada** referência a um arquivo estático — logo, ícone de busca, ícones da barra lateral, banner, fotos da página. Um atalho útil em editores como o VS Code é selecionar múltiplos trechos ao mesmo tempo (tecla `Alt`) para editar tudo de uma vez.

---

## SLIDE 12 — Exemplo Prático 2

**Título:** Vamos praticar juntos: aplicando o CSS ao layout

**Passo a passo:**
1. Configurar `STATICFILES_DIRS` e `STATIC_ROOT`
2. Rodar `collectstatic`
3. Adicionar `{% load static %}` no `index.html`
4. Substituir os caminhos de CSS e imagens pela tag `{% static %}`
5. Recarregar o navegador e confirmar que o layout está estilizado

---

## SLIDE 13 — Exemplo Prático 3

**Título:** Vamos praticar juntos: criando a página "produtos"

**Passo a passo:**
1. Criar o arquivo `produtos.html` dentro de `templates/galeria`
2. Em `galeria/views.py`, criar a função `produtos` que renderiza `'galeria/produtos.html'`
3. Em `galeria/urls.py`, adicionar a rota `path('produtos/', produtos)`
4. Testar acessando diretamente `/produtos/` no navegador
5. Observar e discutir o erro ao clicar no link da página inicial (o Django não processa `.html` na URL) — deixar como gancho para a próxima aula

---

## SLIDE 14 — Django x Outros Modelos (Conceito)

**Título:** Por que separar templates e estáticos faz diferença?

**Comparação conceitual:**
- **HTML dentro do código Python (HttpResponse):** mistura lógica de negócio com apresentação, difícil de manter e de dividir entre equipes
- **Templates isolados:** separam claramente "o que o sistema faz" (views) de "como o sistema aparece" (templates), seguindo o princípio de separação de responsabilidades presente na própria arquitetura MVT
- **Arquivos estáticos versionados à parte:** permitem que o CSS/JS evolua sem impactar a lógica de backend, e facilitam otimizações (cache, CDN) em produção

---

## SLIDE 15 — Django x Outros Modelos (Prática Digital)

**Título:** Impacto na prática do dia a dia

**Pontos para discussão:**
- Times de front-end e back-end conseguem trabalhar em paralelo quando HTML/CSS estão isolados da lógica Python
- Sites com identidade visual completa (CSS, imagens) têm maior credibilidade e retenção de usuários
- Projetos com páginas organizadas em templates por app ficam mais fáceis de escalar conforme o produto cresce (novas páginas, novos apps)

---

## SLIDE 16 — Estrutura Profissional de Pastas (Atualizada)

**Título:** Como organizar templates e estáticos em um projeto Django

**Sugestão de estrutura:**
```
alura-space/
├── venv/
├── .env
├── setup/
│   ├── settings.py        → TEMPLATES (DIRS), STATICFILES_DIRS, STATIC_ROOT
│   ├── static/              → CSS, imagens, ícones do projeto
│   └── urls.py
├── templates/
│   └── galeria/
│       ├── index.html
│       └── produtos.html
├── galeria/
│   ├── views.py             → funções index e produtos, usando render()
│   ├── urls.py               → rotas '' e 'produtos/'
│   └── models.py
├── manage.py
└── requirements.txt
```

**Boas práticas a destacar:**
- Templates organizados por app, dentro de uma pasta com o nome do app
- Arquivos estáticos centralizados em `setup/static`, coletados com `collectstatic`
- Cada nova página segue o mesmo padrão: HTML em `templates`, função em `views.py`, rota em `urls.py`

---

## SLIDE 17 — Fechamento e Transição para Atividades

**Título:** Recapitulando o que vimos

**Resumo rápido:**
- Configuração da pasta de templates e uso de `render`
- Organização de templates por app
- Configuração e coleta de arquivos estáticos (`collectstatic`)
- Uso das tags `{% load static %}` e `{% static %}`
- Criação de uma nova página com view e rota próprias

**Frase de transição:** "Agora é a vez de vocês aplicarem tudo isso, deixando o próprio projeto com layout, estilo e mais de uma página."

---

## SLIDE 18 — Atividades

**Título:** Hora de praticar

1. **Atividade 1:** Configure a pasta `templates` no `settings.py` e crie um `index.html` simples com `<h1>` e `<p>`.
2. **Atividade 2:** Atualize a view `index` para usar `render` no lugar de `HttpResponse`, apontando para o novo template.
3. **Atividade 3:** Mova o `index.html` para dentro de uma subpasta com o nome do seu app (ex: `templates/galeria`) e ajuste a referência na view.
4. **Atividade 4:** Configure `STATICFILES_DIRS` e `STATIC_ROOT`, crie a pasta `static`, adicione um arquivo CSS simples e rode `collectstatic`.
5. **Atividade 5:** No `index.html`, adicione `{% load static %}` e conecte o CSS criado usando a tag `{% static %}`, confirmando a mudança visual no navegador.
6. **Atividade 6 (desafio integrador):** Crie uma nova página `sobre.html` com sua própria view `sobre` e rota `sobre/`, aplicando o mesmo CSS carregado na Atividade 5 — depois explique, com suas palavras, por que reaproveitar o mesmo arquivo estático entre páginas diferentes é uma boa prática (conecta as atividades 3, 4, 5 e 6).

**Orientação ao professor:** as atividades 1 a 3 constroem a base de templates; as atividades 4 e 5 tratam de estilo visual; a atividade 6 retoma tudo, exigindo que o aluno replique o padrão aprendido em uma página nova, de forma independente.

---

*Fim da sequência da Aula 03 — pronto para ser transformado em slides.*