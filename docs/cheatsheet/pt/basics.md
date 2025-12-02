---
title: 'Básico de Python - Folha de Dicas Python'
description: 'Aprenda o básico de Python com nosso guia completo cobrindo operadores, tipos de dados, variáveis, funções e mais. Perfeito para iniciantes que estudam os fundamentos da programação Python.'
labUrl: 'https://labex.io/pt/labs/python-python-basics-633647?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Básicos de Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Todos precisamos começar em algum lugar, então que tal começar por aqui. Este guia cobre os fundamentos básicos do Python, incluindo operadores, tipos de dados, variáveis e funções principais.

<base-disclaimer>
<base-disclaimer-title>
Visão Geral dos Fundamentos do Python
</base-disclaimer-title>
<base-disclaimer-content>
Os fundamentos básicos do Python que todo iniciante deve saber:

- Variáveis e tipos básicos
- Operadores e expressões
- Strings e métodos comuns
- Listas, tuplas e dicionários
- Fluxo de controle básico (if, for, while)
- Funções simples

</base-disclaimer-content>
</base-disclaimer>

## Operadores Matemáticos

De **maior** para **menor** precedência:

| Operadores | Operação        | Exemplo         |
| ---------- | --------------- | --------------- |
| \*\*       | Exponenciação   | `2 ** 3 = 8`    |
| %          | Módulo/Resto    | `22 % 8 = 6`    |
| //         | Divisão inteira | `22 // 8 = 2`   |
| /          | Divisão         | `22 / 8 = 2.75` |
| \*         | Multiplicação   | `3 * 3 = 9`     |
| -          | Subtração       | `5 - 2 = 3`     |
| +          | Adição          | `2 + 2 = 4`     |

Exemplos de expressões:

```python
# A multiplicação tem precedência maior que a adição
# Então isso é avaliado como: 2 + (3 * 6) = 2 + 18 = 20
2 + 3 * 6
```

```output
20
```

```python
# Parênteses anulam a precedência dos operadores
# Isso é avaliado como: 5 * 6 = 30
(2 + 3) * 6
```

```output
30
```

```python
2 ** 8
```

```output
256
```

```python
23 // 7
```

```output
3
```

```python
23 % 7
```

```output
2
```

```python
(5 - 1) * ((7 + 1) / (3 - 1))
```

```output
16.0
```

<BaseQuiz id="cheatsheet-basics-1" correct="A">
<template #question>
Qual é o resultado desta expressão Python?

```python
4 + 2 * 3
```

</template>

<BaseQuizOption value="A" correct>A. 10</BaseQuizOption>
<BaseQuizOption value="B">B. 18</BaseQuizOption>
<BaseQuizOption value="C">C. 12</BaseQuizOption>
<BaseQuizOption value="D">D. 20</BaseQuizOption>
<BaseQuizAnswer>A multiplicação tem precedência maior que a adição, então isso é avaliado como: 4 + (2 \* 3) = 4 + 6 = 10</BaseQuizAnswer>
</BaseQuiz>

## Operadores de Atribuição Aumentada

| Operador    | Equivalente      |
| ----------- | ---------------- |
| `var += 1`  | `var = var + 1`  |
| `var -= 1`  | `var = var - 1`  |
| `var *= 1`  | `var = var * 1`  |
| `var /= 1`  | `var = var / 1`  |
| `var //= 1` | `var = var // 1` |
| `var %= 1`  | `var = var % 1`  |
| `var **= 1` | `var = var ** 1` |

Exemplos:

```python
# Atribuição aumentada: equivalente a greeting = greeting + ' world!'
greeting = 'Hello'
greeting += ' world!'
greeting
```

```output
'Hello world!'
```

```python
# Incrementa um número em 1
number = 1
number += 1
number
```

```output
2
```

```python
# Replica elementos da lista: equivalente a my_list = my_list * 3
my_list = ['item']
my_list *= 3
my_list
```

```output
['item', 'item', 'item']
```

<BaseQuiz id="cheatsheet-basics-2" correct="B">
<template #question>
Qual é o valor de <code>x</code> após executar este código?

```python
x = 5
x += 3
```

</template>

<BaseQuizOption value="A">A. 3</BaseQuizOption>
<BaseQuizOption value="B" correct>B. 8</BaseQuizOption>
<BaseQuizOption value="C">C. 5</BaseQuizOption>
<BaseQuizOption value="D">D. 15</BaseQuizOption>
<BaseQuizAnswer>O operador de atribuição aumentada <code>+=</code> é equivalente a <code>x = x + 3</code>. Então <code>x</code> começa como 5, e depois se torna 5 + 3 = 8.</BaseQuizAnswer>
</BaseQuiz>

## Operador Walrus

O Operador Walrus permite a atribuição de variáveis dentro de uma expressão, retornando o valor da variável

Exemplo:

```python
# O operador Walrus atribui e retorna o valor em uma única expressão
# my_var recebe "Hello World!" e depois é impresso
print(my_var:="Hello World!")
```

```output
Hello World!
```

```python
my_var="Yes"
print(my_var)
```

```output
Yes
```

```python
print(my_var:="Hello")
```

```output
Hello
```

O _Operador Walrus_, ou **Operador de Expressão de Atribuição**, foi introduzido pela primeira vez em 2018 através do [PEP 572](https://peps.python.org/pep-0572/), e depois lançado oficialmente com o **Python 3.8** em outubro de 2019.

<base-disclaimer>
  <base-disclaimer-title>
    Sintaxe Semântica & Exemplos
  </base-disclaimer-title>
  <base-disclaimer-content>
  O <a href="https://peps.python.org/pep-0572/" target="_blank">PEP 572</a> fornece a sintaxe, semântica e exemplos para o Operador Walrus.
  </base-disclaimer-content>
</base-disclaimer>

## Tipos de Dados

Compreender os tipos de dados é um dos fundamentos básicos mais importantes do Python. O Python tem nove tipos de dados principais integrados que cobrem quase tudo o que você precisará:

| Tipo de Dado                                               | Exemplos                                 | Descrição                              |
| ---------------------------------------------------------- | ---------------------------------------- | -------------------------------------- |
| **Números**                                                |                                          |                                        |
| <router-link to='/builtin/int'>`int`</router-link>         | `-2, -1, 0, 1, 2, 3, 4, 5`               | Números inteiros                       |
| <router-link to='/builtin/float'>`float`</router-link>     | `-1.25, -1.0, -0.5, 0.0, 0.5, 1.0, 1.25` | Números com pontos decimais            |
| <router-link to='/builtin/complex'>`complex`</router-link> | `2+3j, complex(1, 4)`                    | Números com partes real e imaginária   |
| **Texto**                                                  |                                          |                                        |
| <router-link to='/builtin/str'>`str`</router-link>         | `'a', 'Hello!', "Python"`                | Texto e caracteres                     |
| **Booleano**                                               |                                          |                                        |
| <router-link to='/builtin/bool'>`bool`</router-link>       | `True, False`                            | Valores Verdadeiro ou Falso            |
| **None**                                                   |                                          |                                        |
| `NoneType`                                                 | `None`                                   | Representa "nenhum valor" ou "nada"    |
| **Coleções**                                               |                                          |                                        |
| <router-link to='/builtin/list'>`list`</router-link>       | `[1, 2, 3], ['a', 'b', 'c']`             | Coleções ordenadas e mutáveis          |
| <router-link to='/builtin/dict'>`dict`</router-link>       | `{'name': 'Alice', 'age': 30}`           | Pares chave-valor                      |
| <router-link to='/builtin/tuple'>`tuple`</router-link>     | `(1, 2, 3), ('a', 'b')`                  | Coleções ordenadas e imutáveis         |
| <router-link to='/builtin/set'>`set`</router-link>         | `{1, 2, 3}, {'a', 'b', 'c'}`             | Coleções não ordenadas de itens únicos |

### Exemplos Rápidos

```python
# Números
age = 25                    # int
price = 19.99              # float
coordinate = 2 + 3j        # complex

# Texto
name = "Alice"             # str

# Booleano
is_student = True          # bool

# None
result = None              # NoneType

# Coleções
scores = [85, 92, 78]      # list
person = {'name': 'Bob', 'age': 30}  # dict
coordinates = (10, 20)     # tuple
unique_ids = {1, 2, 3}     # set
```

Para um guia abrangente com exemplos visuais e explicações detalhadas sobre quando usar cada tipo, consulte: <router-link to="/blog/python-data-types">Tipos de Dados em Python: Um Guia Visual para Iniciantes</router-link>.

## Concatenação e Replicação

Concatenação de strings:

```python
# Concatenação de strings: strings adjacentes são unidas automaticamente
'Alice' 'Bob'
```

```output
'AliceBob'
```

Replicação de strings:

```python
# Replicação de string: repete a string múltiplas vezes
'Alice' * 5
```

```output
'AliceAliceAliceAliceAlice'
```

## Variáveis

Variáveis são uma parte fundamental dos conceitos básicos do Python. Você pode nomear uma variável como quiser, desde que obedeça às seguintes regras:

1. Pode ser apenas uma palavra.

```python
# ruim
my variable = 'Hello'

# bom
var = 'Hello'
```

2. Pode usar apenas letras, números e o caractere sublinhado (`_`).

```python
# ruim
%$@variable = 'Hello'

# bom
my_var = 'Hello'

# bom
my_var_2 = 'Hello'
```

3. Não pode começar com um número.

```python
# isso não funcionará
23_var = 'hello'
```

4. Nomes de variáveis que começam com um sublinhado (`_`) são considerados "não úteis".

```python
# _spam não deve ser usado novamente no código
_spam = 'Hello'
```

<BaseQuiz id="cheatsheet-basics-3" correct="C">
<template #question>
Nos fundamentos do Python, qual dos seguintes é um nome de variável válido?
</template>

<BaseQuizOption value="A">A. <code>3value</code></BaseQuizOption>
<BaseQuizOption value="B">B. <code>user-name</code></BaseQuizOption>
<BaseQuizOption value="C" correct>C. <code>user_name</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>for</code></BaseQuizOption>
<BaseQuizAnswer><code>user_name</code> é um nome de variável válido porque usa apenas letras, números e sublinhados, e não começa com um número.</BaseQuizAnswer>
</BaseQuiz>

## Comentários

Comentário em linha:

```python
# Este é um comentário
```

Comentário de múltiplas linhas:

```python
# Este é um
# comentário de múltiplas linhas
```

Código com um comentário:

```python
a = 1  # inicialização
```

Observe os dois espaços antes do comentário.

Docstring de função:

```python
def foo():
    """
    Este é um docstring de função
    Você também pode usar:
    ''' Docstring da Função '''
    """
```

## A Função print()

A função `print()` é um dos primeiros conceitos básicos do Python que você aprenderá. Ela escreve o valor do(s) argumento(s) que recebe. [...] ela lida com múltiplos argumentos, quantidades de ponto flutuante e strings. As strings são impressas sem aspas, e um espaço é inserido entre os itens, para que você possa formatar as coisas de forma agradável:

```python
print('Hello world!')
```

```output
Hello world!
```

```python
a = 1
print('Hello world!', a)
```

```output
Hello world! 1
```

### A palavra-chave end

O argumento de palavra-chave `end` pode ser usado para evitar a nova linha após a saída, ou terminar a saída com uma string diferente:

```python
# Use o parâmetro end para mudar o que vem depois de cada instrução print
phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
for word in phrase:
    print(word, end='-')  # Use '-' em vez de nova linha
```

```output
printed-with-a-dash-in-between-
```

### A palavra-chave sep

A palavra-chave `sep` especifica como separar os objetos, se houver mais de um:

```python
# Use o parâmetro sep para especificar o separador entre múltiplos argumentos
print('cats', 'dogs', 'mice', sep=',')  # Saída separada por vírgula
```

```output
cats,dogs,mice
```

## A Função input()

Esta função recebe a entrada do usuário e a converte em uma string:

```python
# input() lê a entrada do usuário e a retorna como uma string
print('What is your name?')   # pergunta o nome
my_name = input()  # Espera o usuário digitar e pressionar Enter
print('Hi, {}'.format(my_name))
```

```output
What is your name?
Martha
Hi, Martha
```

`input()` também pode definir uma mensagem padrão sem usar `print()`:

```python
my_name = input('What is your name? ')  # mensagem padrão
print('Hi, {}'.format(my_name))
```

```output
What is your name? Martha
Hi, Martha
```

Também é possível usar strings formatadas para evitar o uso de .format:

```python
# input() pode exibir uma mensagem de prompt diretamente
my_name = input('What is your name? ')  # Prompt e leitura em uma única chamada
print(f'Hi, {my_name}')  # f-string para formatação de string
```

```output
What is your name? Martha
Hi, Martha
```

<BaseQuiz id="cheatsheet-basics-4" correct="B">
<template #question>
Nos fundamentos do Python, que tipo `input()` retorna?
</template>

<BaseQuizOption value="A">A. int</BaseQuizOption>
<BaseQuizOption value="B" correct>B. str</BaseQuizOption>
<BaseQuizOption value="C">C. float</BaseQuizOption>
<BaseQuizOption value="D">D. Depende da entrada do usuário</BaseQuizOption>
<BaseQuizAnswer>A função <code>input()</code> sempre retorna uma string, independentemente do que o usuário digita. Você precisa convertê-la para outros tipos, se necessário.</BaseQuizAnswer>
</BaseQuiz>

## A Função len()

Avalia-se como o valor inteiro do número de caracteres em uma string, lista, dicionário, etc.:

```python
# len() retorna o número de caracteres em uma string
len('hello')  # Retorna 5
```

```output
5
```

```python
# len() retorna o número de itens em uma lista
len(['cat', 3, 'dog'])  # Retorna 3 (três itens)
```

```output
3
```

<base-warning>
  <base-warning-title>Teste de Vazio</base-warning-title>
  <base-warning-content>
    O teste de vazio de strings, listas, dicionários, etc., não deve usar
    <code>len</code>, mas sim preferir a avaliação booleana direta.
  </base-warning-content>
</base-warning>

Exemplo de teste de vazio:

```python
a = [1, 2, 3]

# ruim: verificação len() desnecessária
if len(a) > 0:  # avalia como True
    print("the list is not empty!")
```

```output
the list is not empty!
```

```python
# bom: avaliação booleana direta (maneira Pythonica)
if a:  # avalia como True se a lista não estiver vazia
    print("the list is not empty!")
```

```output
the list is not empty!
```

## As Funções str(), int(), e float()

Essas funções permitem que você altere o tipo de variável. Por exemplo, você pode transformar de um `integer` ou `float` para uma `string`:

```python
# Converter inteiro para string
str(29)  # Retorna '29'
```

```output
'29'
```

```python
str(-3.14)
```

```output
'-3.14'
```

Ou de uma `string` para um `integer` ou `float`:

```python
# Converter string para inteiro
int('11')  # Retorna 11
```

```output
11
```

```python
# Converter string para float
float('3.14')  # Retorna 3.14
```

```output
3.14
```

<BaseQuiz id="cheatsheet-basics-5" correct="C">
<template #question>
Qual é o resultado deste código Python?

```python
result = int('42')
type(result)
```

</template>

<BaseQuizOption value="A">A. <code>str</code></BaseQuizOption>
<BaseQuizOption value="B">B. <code>float</code></BaseQuizOption>
<BaseQuizOption value="C" correct>C. <code>int</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>NoneType</code></BaseQuizOption>
<BaseQuizAnswer>A função <code>int()</code> converte uma string em um inteiro. Portanto, <code>int('42')</code> retorna o inteiro <code>42</code>, e <code>type(42)</code> retorna <code>int</code>.</BaseQuizAnswer>
</BaseQuiz>

## Links Relevantes

- <router-link to="/blog/python-data-types">Tipos de Dados em Python: Um Guia Visual para Iniciantes</router-link>
- <router-link to="/blog/python-comprehensions-step-by-step">Compreensões em Python Passo a Passo</router-link>
- <router-link to="/cheatsheet/control-flow">Fluxo de Controle</router-link>
- <router-link to="/cheatsheet/functions">Funções</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Listas e Tuplas</router-link>
- <router-link to="/cheatsheet/dictionaries">Dicionários</router-link>
- <router-link to="/cheatsheet/sets">Sets</router-link>
- <router-link to="/cheatsheet/string-formatting">Formatação de Strings</router-link>
