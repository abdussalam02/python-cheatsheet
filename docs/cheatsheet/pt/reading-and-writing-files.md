---
title: 'Leitura e Escrita de Arquivos - Guia Rápido Python'
description: "Para ler/escrever em um arquivo no Python, utilize a instrução 'with', que fechará o arquivo automaticamente após o uso, gerenciando os recursos disponíveis."
labUrl: 'https://labex.io/pt/labs/python-python-reading-and-writing-files-633663?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Leitura e Escrita de Arquivos
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Para um olhar mais aprofundado sobre a manipulação de caminhos de arquivos e diretórios, consulte a página <router-link to="/cheatsheet/file-directory-path">Caminhos de Arquivos e Diretórios</router-link>.

## O processo de Leitura/Escrita de arquivos

Para ler/escrever em um arquivo em Python, você desejará usar a instrução `with`, que fechará o arquivo para você depois de terminar, gerenciando os recursos disponíveis.

## Abrindo e lendo arquivos

A função `open` abre um arquivo e retorna um objeto de arquivo correspondente.

```python
# Read file using 'with' statement: automatically closes file when done
with open('/home/labex/project/hi.txt') as hello_file:
    hello_content = hello_file.read()  # Read entire file content

hello_content
```

```output
'Hello World!'
```

<BaseQuiz id="cheatsheet-reading-and-writing-files-1" correct="A">
<template #question>
What is the main advantage of using the <code>with</code> statement when opening files?
</template>

<BaseQuizOption value="A" correct>A. O arquivo é fechado automaticamente quando terminado, mesmo que ocorra um erro</BaseQuizOption>
<BaseQuizOption value="B">B. Arquivos abrem mais rápido</BaseQuizOption>
<BaseQuizOption value="C">C. Arquivos podem ser abertos em modo de leitura e escrita simultaneamente</BaseQuizOption>
<BaseQuizOption value="D">D. Arquivos são automaticamente compactados</BaseQuizOption>
<BaseQuizAnswer>A instrução <code>with</code> garante que o arquivo seja fechado automaticamente quando o bloco for encerrado, mesmo que ocorra uma exceção. Isso ajuda a gerenciar os recursos adequadamente.</BaseQuizAnswer>
</BaseQuiz>

Alternativamente, você pode usar o método _readlines()_ para obter uma lista de valores de string do arquivo, uma string para cada linha de texto:

```python
# readlines() method: returns list of strings, one per line
with open('sonnet29.txt') as sonnet_file:
    sonnet_file.readlines()  # Returns list with each line as a string
```

```output
['When, in disgrace with fortune and men's eyes,\n',
 ' I all alone beweep my  outcast state,\n',
 "And trouble deaf heaven with my bootless cries,\n",
 "And look upon myself and curse my fate,']
```

Você também pode iterar sobre o arquivo linha por linha:

```python
# Iterate through file line by line (memory efficient for large files)
with open('sonnet29.txt') as sonnet_file:
    for line in sonnet_file:  # File object is iterable
        print(line, end='')  # Print without extra newline
```

```output
When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,
```

## Escrevendo em arquivos

```python
# Write to file: 'w' mode overwrites existing file
with open('bacon.txt', 'w') as bacon_file:  # 'w' = write mode
    bacon_file.write('Hello world!\n')  # Returns number of characters written
```

```output
13
```

```python
# Append to file: 'a' mode appends to existing file
with open('bacon.txt', 'a') as bacon_file:  # 'a' = append mode
    bacon_file.write('Bacon is not a vegetable.')
```

```output
25
```

```python
with open('bacon.txt') as bacon_file:
    content = bacon_file.read()

print(content)
```

```output
Hello world!
Bacon is not a vegetable.
```

<BaseQuiz id="cheatsheet-reading-and-writing-files-2" correct="B">
<template #question>
What is the difference between opening a file with mode <code>'w'</code> and mode <code>'a'</code>?
</template>

<BaseQuizOption value="A">A. <code>'w'</code> é para leitura, <code>'a'</code> é para escrita</BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>'w'</code> sobrescreve o arquivo, <code>'a'</code> anexa ao arquivo</BaseQuizOption>
<BaseQuizOption value="C">C. <code>'w'</code> é para Windows, <code>'a'</code> é para Apple</BaseQuizOption>
<BaseQuizOption value="D">D. Não há diferença</BaseQuizOption>
<BaseQuizAnswer>O modo <code>'w'</code> abre o arquivo para escrita e sobrescreve qualquer conteúdo existente. O modo <code>'a'</code> abre o arquivo para anexar, adicionando novo conteúdo ao final do arquivo.</BaseQuizAnswer>
</BaseQuiz>

## Links relevantes

- <router-link to="/cheatsheet/file-directory-path">Caminhos de Arquivos e Diretórios</router-link>
- <router-link to="/cheatsheet/json-yaml">JSON e YAML</router-link>
- <router-link to="/blog/python-pathlib-essentials">10 Operações Essenciais do Sistema de Arquivos que Todo Desenvolvedor Deve Conhecer</router-link>
- <router-link to="/builtin/open">open()</router-link>
- <router-link to="/builtin/print">print()</router-link>
