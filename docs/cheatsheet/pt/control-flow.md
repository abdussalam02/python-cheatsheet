---
title: 'Fluxo de Controle Python - Folha de Dicas Python'
description: 'O fluxo de controle é a ordem em que instruções individuais, comandos ou chamadas de função são executados ou avaliados. O fluxo de controle de um programa Python é regulado por instruções condicionais, loops e chamadas de função.'
labUrl: 'https://labex.io/pt/labs/python-python-control-flow-633651?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Fluxo de Controle em Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    Fluxo de controle em Python
  </base-disclaimer-title>
  <base-disclaimer-content>
  O fluxo de controle é a ordem em que instruções individuais, comandos ou chamadas de função são executados ou avaliados. O fluxo de controle de um programa Python é regulado por instruções condicionais, loops e chamadas de função.
  </base-disclaimer-content>
</base-disclaimer>

## Operadores de Comparação

| Operador | Significado      |
| -------- | ---------------- |
| `==`     | Igual a          |
| `!=`     | Diferente de     |
| `<`      | Menor que        |
| `>`      | Maior que        |
| `<=`     | Menor ou igual a |
| `>=`     | Maior ou igual a |

Estes operadores avaliam para True ou False dependendo dos valores que você lhes atribui.

Exemplos:

```python
42 == 42
```

```output
True
```

```python
40 == 42
```

```output
False
```

```python
'hello' == 'hello'
```

```output
True
```

```python
'hello' == 'Hello'
```

```output
False
```

```python
'dog' != 'cat'
```

```output
True
```

```python
42 == 42.0
```

```output
True
```

```python
42 == '42'
```

```output
False
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-control-flow-1">
<template #question>
A que avalia <code>'hello' == 'Hello'</code>?
</template>

<base-quiz-option value="A">A. <code>True</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>False</code></base-quiz-option>
<base-quiz-option value="C">C. <code>None</code></base-quiz-option>
<base-quiz-option value="D">D. Levanta um erro</base-quiz-option>
<base-quiz-answer value="B">A comparação de strings em Python diferencia maiúsculas de minúsculas. <code>'hello'</code> e <code>'Hello'</code> são strings diferentes, então a comparação retorna <code>False</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Operadores Booleanos

Existem três operadores booleanos: `and`, `or` e `not`.
Na ordem de precedência, do mais alto para o mais baixo, eles são `not`, `and` e `or`.

Tabela de Verdade do Operador `and`:

| Expressão         | Avalia para |
| ----------------- | ----------- |
| `True and True`   | `True`      |
| `True and False`  | `False`     |
| `False and True`  | `False`     |
| `False and False` | `False`     |

Tabela de Verdade do Operador `or`:

| Expressão        | Avalia para |
| ---------------- | ----------- |
| `True or True`   | `True`      |
| `True or False`  | `True`      |
| `False or True`  | `True`      |
| `False or False` | `False`     |

Tabela de Verdade do Operador `not`:

| Expressão   | Avalia para |
| ----------- | ----------- |
| `not True`  | `False`     |
| `not False` | `True`      |

## Misturando Operadores

Você pode misturar operadores booleanos e de comparação:

```python
(4 < 5) and (5 < 6)
```

```output
True
```

```python
(4 < 5) and (9 < 6)
```

```output
False
```

```python
(1 == 2) or (2 == 2)
```

```output
True
```

Além disso, você pode misturar e usar múltiplos operadores booleanos em uma expressão, juntamente com os operadores de comparação:

```python
2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
```

```output
True
```

```python
# Na instrução abaixo, 3 < 4 and 5 > 5 é executado primeiro, avaliando para False
# Então, 5 > 4 retorna True, então o resultado após True or False é True
5 > 4 or 3 < 4 and 5 > 5
```

```output
True
```

```python
# Agora, a instrução entre parênteses é executada primeiro, então True and False retorna False.
(5 > 4 or 3 < 4) and 5 > 5
```

```output
False
```

## Instruções if

A instrução `if` avalia uma expressão e, se essa expressão for `True`, executa o código indentado seguinte:

```python
# instrução if: execute o bloco de código quando a condição for True
name = 'Debora'

if name == 'Debora':  # Verifica se o nome é igual a 'Debora'
   print('Hi, Debora')  # Esta linha é executada se a condição for True
```

```output
Hi, Debora
```

```python
if name != 'George':
   print('You are not George')
```

```output
You are not George
```

A instrução `else` é executada somente se a avaliação da expressão `if` e de todas as expressões `elif` forem `False`:

```python
# if-else: execute código diferente com base na condição
name = 'Debora'

if name == 'George':
   print('Hi, George.')
else:  # Executa se a condição if for False
   print('You are not George')
```

```output
You are not George
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-control-flow-2">
<template #question>
Quando o bloco <code>else</code> é executado em uma instrução if-else?
</template>

<base-quiz-option value="A">A. Sempre</base-quiz-option>
<base-quiz-option value="B" correct>B. Somente quando a condição <code>if</code> (e todas as condições <code>elif</code>, se presentes) forem <code>False</code></base-quiz-option>
<base-quiz-option value="C">C. Somente quando a condição <code>if</code> for <code>True</code></base-quiz-option>
<base-quiz-option value="D">D. Nunca</base-quiz-option>
<base-quiz-answer value="B">O bloco <code>else</code> é executado somente quando a condição <code>if</code> e todas as condições <code>elif</code> (se houver) avaliam para <code>False</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Somente depois que a expressão da instrução `if` for `False`, a instrução `elif` é avaliada e executada:

```python
# if-elif: verifica múltiplas condições em sequência
name = 'George'

if name == 'Debora':
   print('Hi Debora!')
elif name == 'George':  # Verificado somente se a condição anterior for False
   print('Hi George!')
```

```output
Hi George!
```

as partes `elif` e `else` são opcionais.

```python
name = 'Antony'

if name == 'Debora':
   print('Hi Debora!')
elif name == 'George':
   print('Hi George!')
else:
   print('Who are you?')
```

```output
Who are you?
```

## Operador Condicional Ternário

Muitas linguagens de programação possuem um operador ternário, que define uma expressão condicional. O uso mais comum é criar uma instrução de atribuição condicional simples e concisa. Em outras palavras, oferece código em uma linha para avaliar a primeira expressão se a condição for verdadeira e, caso contrário, avalia a segunda expressão.

```plaintext
<expression1> if <condition> else <expression2>
```

Exemplo:

```python
age = 15

# esta instrução if:
if age < 18:
   print('kid')
else:
   print('adult')
```

```output
kid
```

```python
# Operador ternário: expressão condicional em uma linha
# Sintaxe: valor_se_verdadeiro if condição else valor_se_falso
print('kid' if age < 18 else 'adult')
```

```output
kid
```

Operadores ternários podem ser encadeados:

```python
age = 15

# este operador ternário:
print('kid' if age < 13 else 'teen' if age < 18 else 'adult')
```

```output
teen
```

```python
# é equivalente a esta instrução if:
if age < 13:
    print('kid')
else:
    if age < 18:
        print('teen')
    else:
        print('adult')
```

```output
teen
```

## Instrução Switch-Case

<base-disclaimer>
  <base-disclaimer-title>
    Instruções Switch-Case
  </base-disclaimer-title>
  <base-disclaimer-content>
  Em linguagens de programação de computador, uma instrução switch é um tipo de mecanismo de controle de seleção usado para permitir que o valor de uma variável ou expressão mude o fluxo de controle da execução do programa através de pesquisa e mapeamento.
  </base-disclaimer-content>
</base-disclaimer>

As instruções _Switch-Case_, ou **Structural Pattern Matching**, foram introduzidas pela primeira vez em 2020 através da [PEP 622](https://peps.python.org/pep-0622/), e depois oficialmente lançadas com o **Python 3.10** em setembro de 2022.

<base-disclaimer>
  <base-disclaimer-title>
    Tutorial Oficial
  </base-disclaimer-title>
  <base-disclaimer-content>
  A <a href="https://peps.python.org/pep-0636/" target="_blank">PEP 636</a> fornece um tutorial oficial para o Pattern Matching do Python ou instruções Switch-Case.
  </base-disclaimer-content>
</base-disclaimer>

### Correspondência de valores únicos

```python
response_code = 201
match response_code:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 300:
        print("Multiple Choices")
    case 307:
        print("Temporary Redirect")
    case 404:
        print("404 Not Found")
    case 500:
        print("Internal Server Error")
    case 502:
        print("502 Bad Gateway")
```

```output
Created
```

### Correspondência com o Padrão or

Neste exemplo, o caractere pipe (`|` ou `or`) permite que o python retorne a mesma resposta para dois ou mais casos.

```python
response_code = 502
match response_code:
    case 200 | 201:
        print("OK")
    case 300 | 307:
        print("Redirect")
    case 400 | 401:
        print("Bad Request")
    case 500 | 502:
        print("Internal Server Error")
```

```output
Internal Server Error
```

### Correspondência pelo comprimento de um Iterável

```python
today_responses = [200, 300, 404, 500]
match today_responses:
    case [a]:
            print(f"One response today: {a}")
    case [a, b]:
            print(f"Two responses today: {a} and {b}")
    case [a, b, *rest]:
            print(f"All responses: {a}, {b}, {rest}")
```

```output
All responses: 200, 300, [404, 500]
```

### Valor Padrão

O símbolo de sublinhado (`_`) é usado para definir um caso padrão:

```python
response_code = 800
match response_code:
    case 200 | 201:
        print("OK")
    case 300 | 307:
        print("Redirect")
    case 400 | 401:
        print("Bad Request")
    case 500 | 502:
        print("Internal Server Error")
    case _:
        print("Invalid Code")
```

```output
Invalid Code
```

### Correspondência de Classes Nativas

```python
response_code = "300"
match response_code:
    case int():
            print('Code is a number')
    case str():
            print('Code is a string')
    case _:
            print('Code is neither a string nor a number')
```

```output
Code is a string
```

### Protegendo Instruções Match-Case

```python
response_code = 300
match response_code:
    case int() if response_code > 99 and response_code < 500:
            print('Code is a valid number')
    case _:
            print('Code is an invalid number')
```

```output
Code is a valid number
```

## Instruções de Loop while

A instrução while é usada para execução repetida enquanto uma expressão for `True`:

```python
# loop while: repete o código enquanto a condição for True
spam = 0
while spam < 5:  # Continua enquanto spam for menor que 5
    print('Hello, world.')
    spam = spam + 1  # Incrementa o contador para evitar loop infinito
```

```output
Hello, world.
Hello, world.
Hello, world.
Hello, world.
Hello, world.
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-control-flow-3">
<template #question>
O que um loop <code>while</code> faz?
</template>

<base-quiz-option value="A" correct>A. Repete o código enquanto a condição for <code>True</code></base-quiz-option>
<base-quiz-option value="B">B. Executa o código exatamente uma vez</base-quiz-option>
<base-quiz-option value="C">C. Executa o código um número fixo de vezes</base-quiz-option>
<base-quiz-option value="D">D. Pula a execução do código</base-quiz-option>
<base-quiz-answer value="A">Um loop <code>while</code> executa repetidamente um bloco de código enquanto a condição for avaliada como <code>True</code>. Quando a condição se torna <code>False</code>, o loop para.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Instruções break

Se a execução atingir uma instrução `break`, ela sai imediatamente da cláusula do loop `while`:

```python
# instrução break: sai do loop imediatamente quando encontrada
while True:  # Loop infinito
    name = input('Please type your name: ')
    if name == 'your name':
        break  # Sai do loop imediatamente

print('Thank you!')
```

```output
Please type your name: your name
Thank you!
```

## Instruções continue

Quando a execução do programa atinge uma instrução `continue`, a execução do programa salta imediatamente de volta para o início do loop.

```python
# instrução continue: pula o restante da iteração do loop e inicia a próxima iteração
while True:
    name = input('Who are you? ')
    if name != 'Joe':
        continue  # Pula para a próxima iteração, não pede a senha
    password = input('Password? (It is a fish.): ')
    if password == 'swordfish':
        break  # Sai do loop quando a senha estiver correta

print('Access granted.')
```

```output
Who are you? Charles
Who are you? Debora
Who are you? Joe
Password? (It is a fish.): swordfish
Access granted.
```

## Loop For

O loop `for` itera sobre uma `list`, `tuple`, `dictionary`, `set` ou `string`:

```python
# loop for: itera sobre cada item em uma sequência
pets = ['Bella', 'Milo', 'Loki']
for pet in pets:  # Itera sobre cada pet na lista
    print(pet)  # Imprime cada nome de pet
```

```output
Bella
Milo
Loki
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-control-flow-4">
<template #question>
Sobre o que um loop <code>for</code> itera?
</template>

<base-quiz-option value="A">A. Apenas números</base-quiz-option>
<base-quiz-option value="B">B. Apenas strings</base-quiz-option>
<base-quiz-option value="C" correct>C. Qualquer sequência iterável (lista, tupla, dicionário, conjunto, string, etc.)</base-quiz-option>
<base-quiz-option value="D">D. Apenas listas</base-quiz-option>
<base-quiz-answer value="C">Um loop <code>for</code> pode iterar sobre qualquer sequência iterável, incluindo listas, tuplas, dicionários, conjuntos, strings e outros objetos iteráveis.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## A função range()

A função `range()` retorna uma sequência de números. Ela começa em 0, incrementa em 1 e para antes de um número especificado:

```python
for i in range(5):
    print(f'Will stop at 5! or 4? ({i})')
```

```output
Will stop at 5! or 4? (0)
Will stop at 5! or 4? (1)
Will stop at 5! or 4? (2)
Will stop at 5! or 4? (3)
Will stop at 5! or 4? (4)
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-control-flow-5">
<template #question>
O que <code>range(5)</code> gera?
</template>

<base-quiz-option value="A">A. Números de 1 a 5</base-quiz-option>
<base-quiz-option value="B" correct>B. Números de 0 a 4</base-quiz-option>
<base-quiz-option value="C">C. Números de 0 a 5</base-quiz-option>
<base-quiz-option value="D">D. Cinco números aleatórios</base-quiz-option>
<base-quiz-answer value="B">A função <code>range(5)</code> gera números de 0 a 4 (5 números no total). O valor de parada é exclusivo, então para antes de atingir 5.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

A função `range()` também pode modificar seus 3 argumentos padrão. Os dois primeiros serão os valores de `start` e `stop`, e o terceiro será o argumento `step`. O passo é a quantidade pela qual a variável é aumentada após cada iteração.

```python
# range(start, stop, step)
for i in range(0, 10, 2):
   print(i)
```

```output
0
2
4
6
8
```

Você pode até usar um número negativo para o argumento step para fazer o loop for contar regressivamente em vez de progressivamente.

```python
for i in range(5, -1, -1):
    print(i)
```

```output
5
4
3
2
1
0
```

## Declaração For else

Isso permite especificar uma instrução a ser executada no caso de o loop completo ter sido executado. Só é útil quando uma condição `break` pode ocorrer no loop:

```python
for i in [1, 2, 3, 4, 5]:
   if i == 3:
       break
else:
   print("only executed when no item is equal to 3")
```

## Encerrando um Programa com sys.exit()

A função `exit()` permite sair do Python.

```python
import sys

while True:
    feedback = input('Type exit to exit: ')
    if feedback == 'exit':
        print(f'You typed {feedback}.')
        sys.exit()
```

```output
Type exit to exit: open
Type exit to exit: close
Type exit to exit: exit
You typed exit.
```

## Links Relevantes

- <router-link to="/cheatsheet/basics">Básicos</router-link>
- <router-link to="/cheatsheet/functions">Funções</router-link>
- <router-link to="/cheatsheet/exception-handling">Tratamento de Exceções</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Listas e Tuplas</router-link>
- <router-link to="/cheatsheet/sets">Conjuntos</router-link>
- <router-link to="/cheatsheet/dictionaries">Dicionários</router-link>
- <router-link to="/cheatsheet/comprehensions">Compreensões</router-link>
