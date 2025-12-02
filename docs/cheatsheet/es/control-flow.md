---
title: 'Flujo de Control en Python - Hoja de Trucos'
description: 'El flujo de control es el orden en que se ejecutan o evalúan las sentencias, instrucciones o llamadas a funciones individuales. El flujo de control de un programa Python se regula mediante sentencias condicionales, bucles y llamadas a funciones.'
labUrl: 'https://labex.io/es/labs/python-python-control-flow-633651?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Flujo de Control de Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    Flujo de control de Python
  </base-disclaimer-title>
  <base-disclaimer-content>
  El flujo de control es el orden en que se ejecutan o evalúan las sentencias, instrucciones o llamadas a funciones individuales. El flujo de control de un programa Python se regula mediante sentencias condicionales, bucles y llamadas a funciones.
  </base-disclaimer-content>
</base-disclaimer>

## Operadores de Comparación

| Operador | Significado       |
| -------- | ----------------- |
| `==`     | Igual a           |
| `!=`     | Distinto de       |
| `<`      | Menor que         |
| `>`      | Mayor que         |
| `<=`     | Menor o igual que |
| `>=`     | Mayor o igual que |

Estos operadores se evalúan como True o False dependiendo de los valores que se les asignen.

Ejemplos:

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

<BaseQuiz id="cheatsheet-control-flow-1" correct="B">
<template #question>
¿A qué se evalúa <code>'hello' == 'Hello'</code>?
</template>

<BaseQuizOption value="A">A. <code>True</code></BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>False</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>None</code></BaseQuizOption>
<BaseQuizOption value="D">D. Lanza un error</BaseQuizOption>
<BaseQuizAnswer>La comparación de cadenas en Python distingue entre mayúsculas y minúsculas. <code>'hello'</code> y <code>'Hello'</code> son cadenas diferentes, por lo que la comparación devuelve <code>False</code>.</BaseQuizAnswer>
</BaseQuiz>

## Operadores Booleanos

Hay tres operadores booleanos: `and`, `or` y `not`.
En orden de precedencia, de mayor a menor son `not`, `and` y `or`.

Tabla de Verdad del Operador `and`:

| Expresión         | Se evalúa como |
| ----------------- | -------------- |
| `True and True`   | `True`         |
| `True and False`  | `False`        |
| `False and True`  | `False`        |
| `False and False` | `False`        |

Tabla de Verdad del Operador `or`:

| Expresión        | Se evalúa como |
| ---------------- | -------------- |
| `True or True`   | `True`         |
| `True or False`  | `True`         |
| `False or True`  | `True`         |
| `False or False` | `False`        |

Tabla de Verdad del Operador `not`:

| Expresión   | Se evalúa como |
| ----------- | -------------- |
| `not True`  | `False`        |
| `not False` | `True`         |

## Mezcla de Operadores

Puedes mezclar operadores booleanos y de comparación:

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

También puedes usar múltiples operadores booleanos en una expresión, junto con los operadores de comparación:

```python
2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
```

```output
True
```

```python
# En la siguiente sentencia, 3 < 4 and 5 > 5 se ejecuta primero evaluando a False
# Luego 5 > 4 devuelve True, por lo que el resultado después de True or False es True
5 > 4 or 3 < 4 and 5 > 5
```

```output
True
```

```python
# Ahora, la sentencia entre paréntesis se ejecuta primero, por lo que True and False devuelve False.
(5 > 4 or 3 < 4) and 5 > 5
```

```output
False
```

## Sentencias if

La sentencia `if` evalúa una expresión, y si esa expresión es `True`, ejecuta el siguiente código indentado:

```python
# sentencia if: ejecuta el bloque de código cuando la condición es True
name = 'Debora'

if name == 'Debora':  # Comprueba si name es igual a 'Debora'
   print('Hi, Debora')  # Esta línea se ejecuta si la condición es True
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

La sentencia `else` se ejecuta solo si la evaluación de las expresiones `if` y todas las expresiones `elif` son `False`:

```python
# if-else: ejecuta código diferente basado en la condición
name = 'Debora'

if name == 'George':
   print('Hi, George.')
else:  # Se ejecuta si la condición if es False
   print('You are not George')
```

```output
You are not George
```

<BaseQuiz id="cheatsheet-control-flow-2" correct="B">
<template #question>
¿Cuándo se ejecuta el bloque <code>else</code> en una sentencia if-else?
</template>

<BaseQuizOption value="A">A. Siempre</BaseQuizOption>
<BaseQuizOption value="B" correct>B. Solo cuando la condición <code>if</code> (y todas las condiciones <code>elif</code> si están presentes) son <code>False</code></BaseQuizOption>
<BaseQuizOption value="C">C. Solo cuando la condición <code>if</code> es <code>True</code></BaseQuizOption>
<BaseQuizOption value="D">D. Nunca</BaseQuizOption>
<BaseQuizAnswer>El bloque <code>else</code> se ejecuta solo cuando la condición <code>if</code> y todas las condiciones <code>elif</code> (si las hay) se evalúan como <code>False</code>.</BaseQuizAnswer>
</BaseQuiz>

Solo después de que la expresión de la sentencia `if` sea `False`, se evalúa y ejecuta la sentencia `elif`:

```python
# if-elif: comprueba múltiples condiciones en secuencia
name = 'George'

if name == 'Debora':
   print('Hi Debora!')
elif name == 'George':  # Se comprueba solo si la condición anterior es False
   print('Hi George!')
```

```output
Hi George!
```

Las partes `elif` y `else` son opcionales.

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

## Operador Condicional Ternario

Muchos lenguajes de programación tienen un operador ternario, que define una expresión condicional. El uso más común es crear una sentencia de asignación condicional simple y concisa. En otras palabras, ofrece código en una sola línea para evaluar la primera expresión si la condición es verdadera, y si no, evalúa la segunda expresión.

```plaintext
<expresión1> if <condición> else <expresión2>
```

Ejemplo:

```python
age = 15

# esta sentencia if:
if age < 18:
   print('kid')
else:
   print('adult')
```

```output
kid
```

```python
# Operador ternario: expresión condicional en una sola línea
# Sintaxis: valor_si_verdadero if condición else valor_si_falso
print('kid' if age < 18 else 'adult')
```

```output
kid
```

Los operadores ternarios se pueden encadenar:

```python
age = 15

# este operador ternario:
print('kid' if age < 13 else 'teen' if age < 18 else 'adult')
```

```output
teen
```

```python
# es equivalente a esta sentencia if:
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

## Sentencia Switch-Case

<base-disclaimer>
  <base-disclaimer-title>
    Sentencias Switch-Case
  </base-disclaimer-title>
  <base-disclaimer-content>
  En los lenguajes de programación de computadoras, una sentencia switch es un tipo de mecanismo de control de selección utilizado para permitir que el valor de una variable o expresión cambie el flujo de control de la ejecución del programa mediante búsqueda y mapeo.
  </base-disclaimer-content>
</base-disclaimer>

Las sentencias _Switch-Case_, o **Coincidencia Estructural de Patrones** (Structural Pattern Matching), se introdujeron por primera vez en 2020 a través de [PEP 622](https://peps.python.org/pep-0622/), y luego se lanzaron oficialmente con **Python 3.10** en septiembre de 2022.

<base-disclaimer>
  <base-disclaimer-title>
    Tutorial Oficial
  </base-disclaimer-title>
  <base-disclaimer-content>
  El <a href="https://peps.python.org/pep-0636/" target="_blank">PEP 636</a> proporciona un tutorial oficial para la coincidencia de patrones de Python o sentencias Switch-Case.
  </base-disclaimer-content>
</base-disclaimer>

### Coincidencia de valores únicos

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

### Coincidencia con el Patrón or

En este ejemplo, el carácter de barra vertical (`|` u `or`) permite a Python devolver la misma respuesta para dos o más casos.

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

### Coincidencia por la longitud de un Iterable

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

### Valor por defecto

El símbolo de guion bajo (`_`) se utiliza para definir un caso por defecto:

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

### Coincidencia de Clases Incorporadas

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

### Declaraciones Match-Case con Guardia (Guard)

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

## Sentencias de Bucle while

La sentencia while se utiliza para la ejecución repetida mientras una expresión sea `True`:

```python
# bucle while: repite el código mientras la condición sea True
spam = 0
while spam < 5:  # Continúa mientras spam sea menor que 5
    print('Hello, world.')
    spam = spam + 1  # Incrementa el contador para evitar un bucle infinito
```

```output
Hello, world.
Hello, world.
Hello, world.
Hello, world.
Hello, world.
```

<BaseQuiz id="cheatsheet-control-flow-3" correct="A">
<template #question>
¿Qué hace un bucle <code>while</code>?
</template>

<BaseQuizOption value="A" correct>A. Repite código mientras la condición sea <code>True</code></BaseQuizOption>
<BaseQuizOption value="B">B. Ejecuta el código exactamente una vez</BaseQuizOption>
<BaseQuizOption value="C">C. Ejecuta el código un número fijo de veces</BaseQuizOption>
<BaseQuizOption value="D">D. Omite la ejecución del código</BaseQuizOption>
<BaseQuizAnswer>Un bucle <code>while</code> ejecuta repetidamente un bloque de código mientras la condición se evalúe como <code>True</code>. Cuando la condición se vuelve <code>False</code>, el bucle se detiene.</BaseQuizAnswer>
</BaseQuiz>

## Sentencias break

Si la ejecución alcanza una sentencia `break`, sale inmediatamente de la cláusula del bucle `while`:

```python
# sentencia break: sale del bucle inmediatamente cuando se encuentra
while True:  # Bucle infinito
    name = input('Please type your name: ')
    if name == 'your name':
        break  # Sale del bucle inmediatamente

print('Thank you!')
```

```output
Please type your name: your name
Thank you!
```

## Sentencias continue

Cuando la ejecución del programa alcanza una sentencia `continue`, la ejecución del programa salta inmediatamente al inicio del bucle.

```python
# sentencia continue: omite el resto de la iteración del bucle e inicia la siguiente iteración
while True:
    name = input('Who are you? ')
    if name != 'Joe':
        continue  # Salta a la siguiente iteración, no pidas la contraseña
    password = input('Password? (It is a fish.): ')
    if password == 'swordfish':
        break  # Sale del bucle cuando la contraseña es correcta

print('Access granted.')
```

```output
Who are you? Charles
Who are you? Debora
Who are you? Joe
Password? (It is a fish.): swordfish
Access granted.
```

## Bucle For

El bucle `for` itera sobre una `list`, `tuple`, `dictionary`, `set` o `string`:

```python
# bucle for: itera sobre cada elemento en una secuencia
pets = ['Bella', 'Milo', 'Loki']
for pet in pets:  # Itera sobre cada mascota en la lista
    print(pet)  # Imprime cada nombre de mascota
```

```output
Bella
Milo
Loki
```

<BaseQuiz id="cheatsheet-control-flow-4" correct="C">
<template #question>
¿Sobre qué itera un bucle <code>for</code>?
</template>

<BaseQuizOption value="A">A. Solo números</BaseQuizOption>
<BaseQuizOption value="B">B. Solo cadenas</BaseQuizOption>
<BaseQuizOption value="C" correct>C. Cualquier secuencia iterable (lista, tupla, diccionario, conjunto, cadena, etc.)</BaseQuizOption>
<BaseQuizOption value="D">D. Solo listas</BaseQuizOption>
<BaseQuizAnswer>Un bucle <code>for</code> puede iterar sobre cualquier secuencia iterable, incluyendo listas, tuplas, diccionarios, conjuntos, cadenas y otros objetos iterables.</BaseQuizAnswer>
</BaseQuiz>

## La función range()

La función `range()` devuelve una secuencia de números. Comienza desde 0, incrementa en 1 y se detiene antes de un número especificado:

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

<BaseQuiz id="cheatsheet-control-flow-5" correct="B">
<template #question>
¿Qué genera <code>range(5)</code>?
</template>

<BaseQuizOption value="A">A. Números del 1 al 5</BaseQuizOption>
<BaseQuizOption value="B" correct>B. Números del 0 al 4</BaseQuizOption>
<BaseQuizOption value="C">C. Números del 0 al 5</BaseQuizOption>
<BaseQuizOption value="D">D. Cinco números aleatorios</BaseQuizOption>
<BaseQuizAnswer>La función <code>range(5)</code> genera números del 0 al 4 (5 números en total). El valor de parada es exclusivo, por lo que se detiene antes de llegar a 5.</BaseQuizAnswer>
</BaseQuiz>

La función `range()` también puede modificar sus 3 argumentos predeterminados. Los dos primeros serán los valores de `start` (inicio) y `stop` (parada), y el tercero será el argumento `step` (paso). El paso es la cantidad en que se incrementa la variable después de cada iteración.

```python
# range(inicio, parada, paso)
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

Incluso puedes usar un número negativo para el argumento `step` para hacer que el bucle `for` cuente hacia atrás en lugar de hacia adelante.

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

## Sentencia For else

Esto permite especificar una sentencia para ejecutar en caso de que se haya ejecutado el bucle completo. Solo es útil cuando una condición `break` puede ocurrir en el bucle:

```python
for i in [1, 2, 3, 4, 5]:
   if i == 3:
       break
else:
   print("only executed when no item is equal to 3")
```

## Finalizar un Programa con sys.exit()

La función `exit()` permite salir de Python.

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

## Enlaces relevantes

- <router-link to="/cheatsheet/basics">Básicos</router-link>
- <router-link to="/cheatsheet/functions">Funciones</router-link>
- <router-link to="/cheatsheet/exception-handling">Manejo de Excepciones</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Listas y Tuplas</router-link>
- <router-link to="/cheatsheet/sets">Conjuntos</router-link>
- <router-link to="/cheatsheet/dictionaries">Diccionarios</router-link>
- <router-link to="/cheatsheet/comprehensions">Comprensiones</router-link>
