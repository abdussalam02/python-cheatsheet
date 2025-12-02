---
title: 'Empacotamento Python - Folha de Dicas Python'
description: 'Aprenda a empacotar projetos Python usando setup.py e pyproject.toml. Entenda a abordagem moderna para empacotamento Python com as especificações PEP-517, PEP-518 e PEP-660.'
labUrl: 'https://labex.io/pt/labs/python-python-setup-py-633666?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Empacotamento Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-warning>
  <base-warning-title>
    Uma opinião 'controversa'
  </base-warning-title>
  <base-warning-content>
    Usar o `setup.py` para empacotar e distribuir seus pacotes python pode ser bastante desafiador de vez em quando. Ferramentas modernas como <a target="_blank" href="https://python-poetry.org/">Poetry</a> e <a target="_blank" href="https://docs.astral.sh/uv/">UV</a> tornam não apenas o empacotamento **muito mais fácil**, mas também ajudam você a gerenciar suas dependências de uma maneira muito conveniente. O UV é particularmente notável por ser 10-100x mais rápido que as ferramentas tradicionais.
  </base-warning-content>
</base-warning>

Se você deseja mais informações sobre o Poetry, pode ler os seguintes artigos:

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Projetos Python com Poetry e VSCode. Parte 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Projetos Python com Poetry e VSCode. Parte 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Projetos Python com Poetry e VSCode. Parte 3</router-link>

Para um guia abrangente sobre o UV, o gerenciador de pacotes Python ultrarrápido, leia: <router-link to="/blog/python-uv-package-manager">UV: O Gerenciador de Pacotes Python Ultrarrápido</router-link>.

## Introdução

Empacotamento Python é o processo de preparar seu projeto Python para distribuição e instalação. Existem duas abordagens principais: o método tradicional `setup.py` e a abordagem moderna `pyproject.toml` (definida em PEP-517, PEP-518 e PEP-660).

Para um guia abrangente sobre o manuseio de caminhos de arquivos e diretórios, essencial para gerenciar estruturas de projetos, consulte a página <router-link to="/cheatsheet/file-directory-path">Caminhos de Arquivos e Diretórios</router-link>.

## Abordagem Tradicional: setup.py

O arquivo `setup.py` está no centro de um projeto Python tradicional. Ele descreve todos os metadados sobre seu projeto. Existem alguns campos que você pode adicionar a um projeto para dar a ele um rico conjunto de metadados que descrevem o projeto. No entanto, existem apenas três campos obrigatórios: `name`, `version` e `packages`. O campo `name` deve ser exclusivo se você deseja publicar seu pacote no Python Package Index (PyPI). O campo `version` rastreia diferentes lançamentos do projeto. O campo `packages` descreve onde você colocou o código-fonte Python dentro do seu projeto.

Isso permite que você instale facilmente pacotes Python. Muitas vezes, é suficiente escrever:

```bash
python setup.py install
```

e o módulo se instalará.

### Exemplo: setup.py

Nosso `setup.py` inicial também incluirá informações sobre a licença e reutilizará o arquivo README.txt para o campo `long_description`. Isso ficará assim:

```python
# setup.py: define metadados do pacote para distribuição
from distutils.core import setup
setup(
   name='pythonCheatsheet',  # Nome do pacote (deve ser exclusivo no PyPI)
   version='0.1',  # Número da versão
   packages=['pipenv',],  # Lista de pacotes a serem incluídos
   license='MIT',  # Tipo de licença
   long_description=open('README.txt').read(),  # Lê a descrição do arquivo
)
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-packaging-1">
<template #question>
Quais são os três campos obrigatórios em um arquivo <code>setup.py</code>?
</template>

<base-quiz-option value="A">A. name, author, license</base-quiz-option>
<base-quiz-option value="B">B. name, description, packages</base-quiz-option>
<base-quiz-option value="C" correct>C. name, version, packages</base-quiz-option>
<base-quiz-option value="D">D. name, version, license</base-quiz-option>
<base-quiz-answer value="C">Os três campos obrigatórios em <code>setup.py</code> são <code>name</code> (nome do pacote, deve ser exclusivo no PyPI), <code>version</code> (rastreia lançamentos) e <code>packages</code> (descreve onde o código-fonte Python está localizado).</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Abordagem Moderna: pyproject.toml

O arquivo `pyproject.toml` é o padrão moderno para configuração de projetos Python (PEP-517, PEP-518, PEP-660). Ele fornece uma maneira unificada de especificar os requisitos do sistema de compilação e os metadados do projeto em um único formato de arquivo declarativo.

### Benefícios do pyproject.toml

- **Declarativo**: Todos os metadados do projeto em um só lugar
- **Independente do sistema de compilação**: Funciona com setuptools, poetry, flit e outros backends de compilação
- **Sem execução de código**: Mais seguro e previsível do que setup.py
- **Padronizado**: Segue os padrões PEP para melhor suporte de ferramentas

### Exemplo: pyproject.toml

Aqui está um exemplo básico de `pyproject.toml` usando setuptools:

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "pythonCheatsheet"
version = "0.1"
description = "Um pacote de folhas de dicas Python"
readme = "README.txt"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=22.0",
]
```

### Instalação a partir do pyproject.toml

Com `pyproject.toml`, você pode instalar seu pacote usando pip:

```bash
pip install .
```

Ou no modo editável:

```bash
pip install -e .
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-packaging-2">
<template #question>
Qual é a principal vantagem do <code>pyproject.toml</code> sobre o <code>setup.py</code>?
</template>

<base-quiz-option value="A">A. É mais rápido de executar</base-quiz-option>
<base-quiz-option value="B" correct>B. É declarativo, mais seguro (sem execução de código) e segue os padrões PEP</base-quiz-option>
<base-quiz-option value="C">C. Requer menos configuração</base-quiz-option>
<base-quiz-option value="D">D. Só funciona com Python 3.10+</base-quiz-option>
<base-quiz-answer value="B">A abordagem <code>pyproject.toml</code> é declarativa (todos os metadados em um só lugar), mais segura porque não executa código como o <code>setup.py</code> faz, e segue os padrões PEP (PEP-517, PEP-518, PEP-660) para melhor suporte de ferramentas.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Escolhendo a Abordagem Certa

- **Use `setup.py`**: Se você estiver trabalhando com projetos legados ou precisar de controle granular
- **Use `pyproject.toml`**: Para novos projetos (recomendado), pois é o padrão moderno e fornece melhor suporte de ferramentas

Encontre mais informações visitando a [documentação oficial](http://docs.python.org/3.11/install/index.html).

## Links Relevantes

- <router-link to="/cheatsheet/virtual-environments">Ambientes Virtuais</router-link>
- <router-link to="/cheatsheet/file-directory-path">Caminhos de Arquivos e Diretórios</router-link>
- <router-link to="/blog/python-uv-package-manager">UV: O Gerenciador de Pacotes Python Ultrarrápido</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Projetos Python com Poetry e VSCode. Parte 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Projetos Python com Poetry e VSCode. Parte 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Projetos Python com Poetry e VSCode. Parte 3</router-link>
- <router-link to="/builtin/import">import()</router-link>
