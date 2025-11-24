---
title: 'Ambientes Virtuais Python - Folha de Dicas Python'
description: 'O uso de um Ambiente Virtual é testar código Python em ambientes encapsulados e também evitar preencher a instalação base do Python com bibliotecas que podemos usar para apenas um projeto.'
labUrl: 'https://labex.io/pt/labs/python-python-virtual-environments-633669?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Ambiente Virtual
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

O uso de um Ambiente Virtual é para testar código python em ambientes encapsulados e também para evitar preencher a instalação base do Python com bibliotecas que podemos usar para apenas um projeto.

## venv

`venv` é o módulo da biblioteca padrão para criar ambientes virtuais no Python 3.3+. Ele é embutido no Python, então nenhuma instalação é necessária.

1. Criar um ambiente virtual

```bash
python -m venv venv
```

Ou em alguns sistemas:

```bash
python3 -m venv venv
```

Isso cria um diretório `venv` na sua pasta atual contendo o ambiente virtual.

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Qual comando é usado para criar um ambiente virtual usando <code>venv</code>?
</template>

<base-quiz-option value="A" correct>A. <code>python -m venv venv</code></base-quiz-option>
<base-quiz-option value="B">B. <code>python create venv</code></base-quiz-option>
<base-quiz-option value="C">C. <code>venv create</code></base-quiz-option>
<base-quiz-option value="D">D. <code>python venv new</code></base-quiz-option>
<base-quiz-answer value="A">O comando <code>python -m venv venv</code> cria um ambiente virtual. O flag <code>-m</code> executa o módulo venv, e <code>venv</code> no final é o nome do diretório a ser criado.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

2. Ativar o ambiente virtual

No Linux/macOS:

```bash
source venv/bin/activate
```

No Windows:

```bash
venv\Scripts\activate
```

Uma vez ativado, você verá `(venv)` no início do seu prompt de comando, indicando que o ambiente virtual está ativo.

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Como você ativa um ambiente virtual no Linux/macOS?
</template>

<base-quiz-option value="A">A. <code>activate venv</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>source venv/bin/activate</code></base-quiz-option>
<base-quiz-option value="C">C. <code>venv activate</code></base-quiz-option>
<base-quiz-option value="D">D. <code>python venv activate</code></base-quiz-option>
<base-quiz-answer value="B">No Linux/macOS, você ativa um ambiente virtual usando <code>source venv/bin/activate</code>. No Windows, você usaria <code>venv\Scripts\activate</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

3. Instalar pacotes

Com o ambiente virtual ativado, instale pacotes usando pip:

```bash
pip install package_name
```

Pacotes instalados serão específicos para este ambiente virtual.

4. Desativar o ambiente virtual

Para sair do ambiente virtual:

```bash
deactivate
```

O prefixo `(venv)` desaparecerá do seu prompt de comando.

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Qual é o principal propósito de usar um ambiente virtual?
</template>

<base-quiz-option value="A" correct>A. Isolar as dependências do projeto e evitar preencher a instalação base do Python</base-quiz-option>
<base-quiz-option value="B">B. Fazer o Python rodar mais rápido</base-quiz-option>
<base-quiz-option value="C">C. Criptografar código Python</base-quiz-option>
<base-quiz-option value="D">D. Compilar Python para código de máquina</base-quiz-option>
<base-quiz-answer value="A">Ambientes virtuais permitem que você teste código Python em ambientes encapsulados e evite preencher a instalação base do Python com bibliotecas que podem ser usadas apenas para um projeto. Isso ajuda a gerenciar dependências por projeto.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## virtualenv

1. Instalar virtualenv

```bash
pip install virtualenv
```

1. Instalar virtualenvwrapper-win (Windows)

```bash
pip install virtualenvwrapper-win
```

Uso:

1. Criar um Ambiente Virtual chamado `HelloWorld`

```bash
mkvirtualenv HelloWorld
```

Tudo o que instalarmos agora será específico para este projeto. E disponível para os projetos que conectarmos a este ambiente.

1. Definir Diretório do Projeto

Para vincular nosso virtualenv ao nosso diretório de trabalho atual, simplesmente digitamos:

```bash
setprojectdir .
```

1. Desativar

Para mudar para outra coisa na linha de comando, digite `deactivate` para desativar seu ambiente.

```bash
deactivate
```

Note como os parênteses desaparecem.

1. Workon

Abra o prompt de comando e digite `workon HelloWorld` para ativar o ambiente e mover para a pasta raiz do seu projeto

```bash
workon HelloWorld
```

## Poetry

<base-disclaimer>
  <base-disclaimer-title>
    Do <a href="https://python-poetry.org/">site do Poetry</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Poetry é uma ferramenta para gerenciamento de dependências e empacotamento em Python. Ele permite que você declare as bibliotecas das quais seu projeto depende e as gerenciará (instalará/atualizará) para você.
  </base-disclaimer-content>
</base-disclaimer>

1. Instalar Poetry

```bash
pip install --user poetry
```

2. Criar um novo projeto

```bash
poetry new my-project
```

Isso criará um diretório my-project:

```plaintext
my-project
├── pyproject.toml
├── README.rst
├── poetry_demo
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_poetry_demo.py
```

O arquivo pyproject.toml orquestrará seu projeto e suas dependências:

```toml
[tool.poetry]
name = "my-project"
version = "0.1.0"
description = ""
authors = ["your name <your@mail.com>"]

[tool.poetry.dependencies]
python = "*"

[tool.poetry.dev-dependencies]
pytest = "^3.4"
```

3. Pacotes

Para adicionar dependências ao seu projeto, você pode especificá-las na seção tool.poetry.dependencies:

```toml
[tool.poetry.dependencies]
pendulum = "^1.4"
```

Além disso, em vez de modificar o arquivo pyproject.toml manualmente, você pode usar o comando add e ele encontrará automaticamente uma restrição de versão adequada.

```bash
poetry add pendulum
```

Para instalar as dependências listadas em pyproject.toml:

```bash
poetry install
```

Para remover dependências:

```bash
poetry remove pendulum
```

Para mais informações, consulte a [documentação](https://poetry.eustace.io/docs/) ou leia aqui:

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Projetos Python com Poetry e VSCode. Parte 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Projetos Python com Poetry e VSCode. Parte 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Projetos Python com Poetry e VSCode. Parte 3</router-link>

## Pipenv

<base-disclaimer>
  <base-disclaimer-title>
    Do <a target="_blank" href="https://pipenv.pypa.io/en/latest/">site do Pipenv</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Pipenv é uma ferramenta que visa trazer o melhor de todos os mundos de empacotamento (bundler, composer, npm, cargo, yarn, etc.) para o mundo Python. O Windows é um cidadão de primeira classe, em nosso mundo.
  </base-disclaimer-content>
</base-disclaimer>

1. Instalar pipenv

```bash
pip install pipenv
```

2. Entre no diretório do seu Projeto e instale os Pacotes para seu projeto

```bash
cd my_project
pipenv install <package>
```

Pipenv instalará seu pacote e criará um Pipfile para você no diretório do seu projeto. O Pipfile é usado para rastrear quais dependências seu projeto precisa caso você precise reinstalá-las.

3. Desinstalar Pacotes

```bash
pipenv uninstall <package>
```

4. Ativar o Ambiente Virtual associado ao seu projeto Python

```bash
pipenv shell
```

5. Sair do Ambiente Virtual

```bash
exit
```

Encontre mais informações e um vídeo em [docs.pipenv.org](https://docs.pipenv.org/).

## Anaconda

<base-disclaimer>
  <base-disclaimer-title>
    <a target="k" href="https://anaconda.com/">Anaconda</a> é outra ferramenta popular para gerenciar pacotes python.
  </base-disclaimer-title>
  <base-disclaimer-content>
    Onde pacotes, notebooks, projetos e ambientes são compartilhados. Seu lugar para hospedagem pública gratuita de pacotes conda.
  </base-disclaimer-content>
</base-disclaimer>

Uso:

1. Criar um Ambiente Virtual

```bash
conda create -n HelloWorld
```

2. Para usar o Ambiente Virtual, ative-o por:

```bash
conda activate HelloWorld
```

Tudo o que for instalado agora será específico para o projeto HelloWorld

3. Sair do Ambiente Virtual

```bash
conda deactivate
```

## UV

<base-disclaimer>
  <base-disclaimer-title>
    Da <a target="_blank" href="https://docs.astral.sh/uv/">Documentação do UV</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    UV é um instalador e resolvedor de pacotes Python extremamente rápido, projetado como um substituto direto para os fluxos de trabalho pip e pip-tools. UV é 10-100x mais rápido que pip e fornece gerenciamento unificado de pacotes, criação de ambiente virtual e gerenciamento de versão Python.
  </base-disclaimer-content>
</base-disclaimer>

1. Instalar UV

```bash
# Usando curl (Linux/macOS)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Usando pip ou pipx
pip install uv
```

2. Criar um novo projeto com ambiente virtual

```bash
uv init my-project
cd my-project
```

3. Adicionar dependências

```bash
uv add requests
```

4. Executar comandos no ambiente do projeto

```bash
uv run python script.py
```

5. Ativar o ambiente virtual manualmente (opcional)

```bash
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

UV gerencia automaticamente ambientes virtuais, versões Python e dependências com velocidade e conveniência excepcionais.

## Links Relevantes

- <router-link to="/cheatsheet/packaging">Empacotamento</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Projetos Python com Poetry e VSCode. Parte 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Projetos Python com Poetry e VSCode. Parte 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Projetos Python com Poetry e VSCode. Parte 3</router-link>
- <router-link to="/blog/python-uv-package-manager">UV: O Gerenciador de Pacotes Python Relâmpago</router-link>
- <router-link to="/builtin/import">import()</router-link>
