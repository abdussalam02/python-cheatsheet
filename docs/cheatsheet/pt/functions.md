---
title: 'Funções Python - Guia Rápido Python'
description: 'Em Python, uma função é um bloco de código organizado usado para executar uma única tarefa.'
labUrl: 'https://labex.io/pt/labs/python-python-functions-633658?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Funções Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikiversity.org/wiki/Programming_Fundamentals/Functions">Programação de Funções</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Uma função é um bloco de código organizado que é usado para executar uma única tarefa. Elas fornecem melhor modularidade para sua aplicação e reutilização.
  </base-disclaimer-content>
</base-disclaimer>

## Argumentos de Função

Uma função pode receber `argumentos` e `valores de retorno`:

No exemplo a seguir, a função **say_hello** recebe o argumento "name" e imprime uma saudação:

```python
# Define uma função que aceita um argumento
def say_hello(name):
   print(f'Hello {name}')

# Chama a função com um argumento de string
say_hello('Carlos')
```

```output
Hello Carlos
```

```python
say_hello('Wanda')
```

```output
Hello Wanda
```

```python
say_hello('Rose')
```

```output
Hello Rose
```

## Argumentos de Palavra-Chave (Keyword Arguments)

Para melhorar a legibilidade do código, devemos ser o mais explícitos possível. Podemos conseguir isso em nossas funções usando `Keyword Arguments`:

```python
# Função com múltiplos parâmetros
def say_hi(name, greeting):
   print(f"{greeting} {name}")

# Argumentos posicionais: a ordem importa
say_hi('John', 'Hello')
```

```output
Hello John
```

```python
# Argumentos de palavra-chave: a ordem não importa, mais legível
say_hi(name='Anna', greeting='Hi')
```

```output
Hi Anna
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-functions-1">
<template #question>
Qual é a principal vantagem de usar argumentos de palavra-chave em funções Python?
</template>

<base-quiz-option value="A">A. Eles são executados mais rapidamente</base-quiz-option>
<base-quiz-option value="B">B. Eles usam menos memória</base-quiz-option>
<base-quiz-option value="C" correct>C. Eles melhoram a legibilidade do código e a ordem não importa</base-quiz-option>
<base-quiz-option value="D">D. Eles previnem erros</base-quiz-option>
<base-quiz-answer value="C">Argumentos de palavra-chave melhoram a legibilidade do código ao deixar claro o que cada argumento representa, e eles permitem que você passe argumentos em qualquer ordem.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Valores de Retorno

Ao criar uma função usando a instrução `def`, você pode especificar qual deve ser o valor de retorno com uma instrução `return`. Uma instrução de retorno consiste no seguinte:

- A palavra-chave `return`.

- O valor ou expressão que a função deve retornar.

```python
# Função que retorna um valor usando a instrução return
def sum_two_numbers(number_1, number_2):
   return number_1 + number_2

# Chama a função e armazena o valor retornado
result = sum_two_numbers(7, 8)
print(result)
```

```output
15
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-functions-2">
<template #question>
Qual palavra-chave é usada para retornar um valor de uma função em Python?
</template>

<base-quiz-option value="A" correct>A. <code>return</code></base-quiz-option>
<base-quiz-option value="B">B. <code>output</code></base-quiz-option>
<base-quiz-option value="C">C. <code>yield</code></base-quiz-option>
<base-quiz-option value="D">D. <code>exit</code></base-quiz-option>
<base-quiz-answer value="A">A palavra-chave <code>return</code> é usada para retornar um valor de uma função. Se nenhuma instrução return for usada, a função retorna <code>None</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Escopo Local e Global

- O código no escopo global não pode usar nenhuma variável local.

- No entanto, um escopo local pode acessar variáveis globais.

- O código no escopo local de uma função não pode usar variáveis em nenhum outro escopo local.

- Você pode usar o mesmo nome para variáveis diferentes se elas estiverem em escopos diferentes. Ou seja, pode haver uma variável local chamada spam e uma variável global também chamada spam.

```python
# Variável global: acessível em todos os lugares
global_variable = 'I am available everywhere'

def some_function():
    print(global_variable)  # Pode acessar a variável global
    # Variável local: só existe dentro desta função
    local_variable = "only available within this function"
    print(local_variable)

# Isso levantará NameError: local_variable não existe no escopo global
print(local_variable)
```

```output
Traceback (most recent call last):
  File "<stdin>", line 10, in <module>
NameError: name 'local_variable' is not defined
```

## A Declaração global

Se você precisar modificar uma variável global de dentro de uma função, use a instrução global:

```python
# Usa a palavra-chave 'global' para modificar a variável global de dentro da função
def spam():
    global eggs  # Declara que estamos modificando a variável global
    eggs = 'spam'  # Isso altera a variável global

eggs = 'global'
spam()  # A função modifica a variável global
print(eggs)  # Imprime 'spam', não 'global'
```

```output
spam
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-functions-3">
<template #question>
Qual palavra-chave você deve usar dentro de uma função para modificar uma variável global?
</template>

<base-quiz-option value="A">A. <code>nonlocal</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>global</code></base-quiz-option>
<base-quiz-option value="C">C. <code>extern</code></base-quiz-option>
<base-quiz-option value="D">D. Nenhuma palavra-chave necessária</base-quiz-option>
<base-quiz-answer value="B">A palavra-chave <code>global</code> deve ser usada dentro de uma função para modificar uma variável global. Sem ela, o Python criará uma variável local em vez disso.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Existem quatro regras para saber se uma variável está em um escopo local ou global:

1. Se uma variável estiver sendo usada no escopo global (ou seja, fora de todas as funções), ela é sempre uma variável global.

1. Se houver uma instrução global para essa variável em uma função, ela é uma variável global.

1. Caso contrário, se a variável for usada em uma instrução de atribuição na função, ela é uma variável local.

1. Mas se a variável não for usada em uma instrução de atribuição, ela é uma variável global.

## Funções Lambda

Em Python, uma função lambda é uma função anônima de linha única, que pode ter qualquer número de argumentos, mas pode ter apenas uma expressão.

<base-disclaimer>
  <base-disclaimer-title>
    Do <a target="_blank" href="https://docs.python.org/3/library/ast.html?highlight=lambda#function-and-class-definitions">Tutorial do Python 3</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    lambda é uma definição de função mínima que pode ser usada dentro de uma expressão. Diferente de FunctionDef, body contém um único nó.
  </base-disclaimer-content>
</base-disclaimer>

<base-warning>
  <base-warning-title>
    Expressão de linha única
  </base-warning-title>
  <base-warning-content>
    Funções Lambda só podem avaliar uma expressão, como uma única linha de código.
  </base-warning-content>
</base-warning>

Esta função:

```python
# Definição de função regular
def add(x, y):
    return x + y

add(5, 3)
```

```output
8
```

É equivalente à função _lambda_:

```python
# Função Lambda: função anônima definida em uma linha
# Sintaxe: lambda argumentos: expressão
add = lambda x, y: x + y
add(5, 3)
```

```output
8
```

<base-quiz>
<base-quiz-question correct="D" id="cheatsheet-functions-4">
<template #question>
O que é uma função lambda em Python?
</template>

<base-quiz-option value="A">A. Uma função que só pode ser chamada uma vez</base-quiz-option>
<base-quiz-option value="B">B. Uma função que não recebe argumentos</base-quiz-option>
<base-quiz-option value="C">C. Uma função que retorna múltiplos valores</base-quiz-option>
<base-quiz-option value="D" correct>D. Uma função anônima de linha única que pode ter qualquer número de argumentos, mas apenas uma expressão</base-quiz-option>
<base-quiz-answer value="D">Uma função lambda é uma função anônima de linha única definida usando a palavra-chave <code>lambda</code>. Ela pode aceitar qualquer número de argumentos, mas pode conter apenas uma única expressão.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Assim como as funções aninhadas regulares, as lambdas também funcionam como fechamentos lexicais (closures):

```python
# Fechamento Lambda: função lambda que captura variável do escopo externo
def make_adder(n):
    return lambda x: x + n  # Lambda captura 'n' da função externa

# Cria funções que adicionam valores diferentes
plus_3 = make_adder(3)  # Retorna lambda que adiciona 3
plus_5 = make_adder(5)  # Retorna lambda que adiciona 5

plus_3(4)  # Retorna 4 + 3 = 7
```

```output
7
```

```python
plus_5(4)
```

```output
9
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-functions-5">
<template #question>
O que um fechamento lambda permite que você faça?
</template>

<base-quiz-option value="A" correct>A. Capturar variáveis do escopo externo</base-quiz-option>
<base-quiz-option value="B">B. Modificar variáveis globais sem a palavra-chave global</base-quiz-option>
<base-quiz-option value="C">C. Retornar múltiplos valores</base-quiz-option>
<base-quiz-option value="D">D. Executar código de forma assíncrona</base-quiz-option>
<base-quiz-answer value="A">Fechamentos lambda permitem que funções lambda capturem e usem variáveis de seu escopo circundante, de forma semelhante às funções aninhadas regulares.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Links Relevantes

- <router-link to="/blog/python-easy-args-kwargs">\*args e \*\*kwargs explicados</router-link>
- <router-link to="/cheatsheet/args-and-kwargs">Args e Kwargs</router-link>
- <router-link to="/cheatsheet/decorators">Decorators</router-link>
- <router-link to="/cheatsheet/control-flow">Fluxo de Controle</router-link>
- <router-link to="/cheatsheet/basics">Noções Básicas</router-link>
- <router-link to="/builtin">Funções Built-in</router-link>
