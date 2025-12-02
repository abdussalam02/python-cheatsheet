---
title: 'Python JSON e YAML - Folha de Dicas Python'
description: 'JSON (JavaScript Object Notation) é um formato leve para armazenar e transportar dados. JSON é frequentemente usado quando dados são enviados de um servidor para uma página web.'
labUrl: 'https://labex.io/pt/labs/python-python-json-and-yaml-633659?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
JSON e YAML
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## JSON

JSON significa JavaScript Object Notation e é um formato leve para armazenar e transportar dados. JSON é frequentemente usado quando dados são enviados de um servidor para uma página web.

```python
# Read JSON file: json.load() parses JSON from file object
import json
with open("filename.json", "r") as f:  # Abrir arquivo no modo de leitura
    content = json.load(f)  # Analisar JSON e retornar dict/list Python
```

Escreva um arquivo JSON com:

```python
# Write JSON file: json.dump() writes Python object as JSON
import json

content = {"name": "Joe", "age": 20}
with open("filename.json", "w") as f:  # Abrir arquivo no modo de escrita
    json.dump(content, f, indent=2)  # Escrever JSON com indentação de 2 espaços
```

<BaseQuiz id="cheatsheet-json-yaml-1" correct="B">
<template #question>
Qual função é usada para escrever um dicionário Python em um arquivo JSON?
</template>

<BaseQuizOption value="A">A. <code>json.write()</code></BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>json.dump()</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>json.save()</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>json.export()</code></BaseQuizOption>
<BaseQuizAnswer>A função <code>json.dump()</code> escreve um objeto Python (como um dicionário) em um arquivo JSON. <code>json.load()</code> é usada para ler arquivos JSON.</BaseQuizAnswer>
</BaseQuiz>

## YAML

Comparado ao JSON, o YAML permite uma manutenibilidade humana muito melhor e dá a capacidade de adicionar comentários. É uma escolha conveniente para arquivos de configuração onde um humano terá que editar.

Existem duas bibliotecas principais que permitem acesso a arquivos YAML:

- [PyYaml](https://pypi.python.org/pypi/PyYAML)
- [Ruamel.yaml](https://pypi.python.org/pypi/ruamel.yaml)

Instale-as usando `pip install` no seu ambiente virtual.

A primeira é mais fácil de usar, mas a segunda, Ruamel, implementa muito melhor a especificação YAML, e permite, por exemplo, modificar um conteúdo YAML sem alterar comentários.

Abra um arquivo YAML com:

```python
# Read YAML file using ruamel.yaml library
from ruamel.yaml import YAML

with open("filename.yaml") as f:
    yaml=YAML()  # Criar instância do analisador YAML
    yaml.load(f)  # Analisar YAML e retornar dict/list Python
```

<BaseQuiz id="cheatsheet-json-yaml-2" correct="C">
<template #question>
Qual é uma vantagem do YAML sobre o JSON?
</template>

<BaseQuizOption value="A">A. Arquivos YAML são menores</BaseQuizOption>
<BaseQuizOption value="B">B. YAML é mais rápido de analisar</BaseQuizOption>
<BaseQuizOption value="C" correct>C. YAML permite comentários e é mais legível por humanos</BaseQuizOption>
<BaseQuizOption value="D">D. YAML é embutido no Python</BaseQuizOption>
<BaseQuizAnswer>YAML permite comentários e é mais legível por humanos do que JSON, tornando-o uma escolha conveniente para arquivos de configuração que os humanos precisam editar.</BaseQuizAnswer>
</BaseQuiz>

## Anyconfig

[Anyconfig](https://pypi.python.org/pypi/anyconfig) é um pacote muito útil, permitindo abstrair completamente o formato subjacente do arquivo de configuração. Ele permite carregar um dicionário Python de JSON, YAML, TOML, e assim por diante.

Instale-o com:

```bash
pip install anyconfig
```

Uso:

```python
# anyconfig: load configuration files in various formats (JSON, YAML, TOML, etc.)
import anyconfig
conf1 = anyconfig.load("/path/to/foo/conf.d/a.yml")  # Detecta o formato automaticamente
```

<BaseQuiz id="cheatsheet-json-yaml-3" correct="A">
<template #question>
O que a biblioteca anyconfig permite que você faça?
</template>

<BaseQuizOption value="A" correct>A. Carregar arquivos de configuração em vários formatos (JSON, YAML, TOML) sem especificar o formato</BaseQuizOption>
<BaseQuizOption value="B">B. Converter entre diferentes formatos de configuração</BaseQuizOption>
<BaseQuizOption value="C">C. Validar a sintaxe do arquivo de configuração</BaseQuizOption>
<BaseQuizOption value="D">D. Criptografar arquivos de configuração</BaseQuizOption>
<BaseQuizAnswer>A biblioteca anyconfig abstrai o formato subjacente do arquivo de configuração, permitindo carregar dicionários Python de JSON, YAML, TOML e outros formatos sem a necessidade de saber qual formato está sendo usado.</BaseQuizAnswer>
</BaseQuiz>

## Relevant links

- <router-link to="/cheatsheet/reading-and-writing-files">Leitura e Escrita de Arquivos</router-link>
- <router-link to="/cheatsheet/dictionaries">Dicionários Python</router-link>
- <router-link to="/modules/json-module">O Módulo json</router-link>
- <router-link to="/blog/python-pathlib-essentials">10 Operações Essenciais do Sistema de Arquivos que Todo Desenvolvedor Deve Conhecer</router-link>
- <router-link to="/builtin/open">open()</router-link>
- <router-link to="/builtin/dict">dict()</router-link>
