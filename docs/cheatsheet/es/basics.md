---
title: 'Fundamentos de Python - Hoja de Trucos de Python'
description: 'Aprenda los conceptos básicos de Python con nuestra guía completa que cubre operadores, tipos de datos, variables, funciones y más. Perfecto para principiantes que aprenden los fundamentos de la programación en Python.'
labUrl: 'https://labex.io/es/labs/python-python-basics-633647?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Conceptos Básicos de Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Todos necesitamos empezar en algún lugar, así que ¿por qué no hacerlo aquí? Esta guía cubre los conceptos básicos fundamentales de Python, incluyendo operadores, tipos de datos, variables y funciones principales.

<base-disclaimer>
<base-disclaimer-title>
Resumen de Conceptos Básicos de Python
</base-disclaimer-title>
<base-disclaimer-content>
Los conceptos básicos de Python que todo principiante debe conocer:

- Variables y tipos básicos
- Operadores y expresiones
- Cadenas (Strings) y métodos comunes
- Listas, tuplas y diccionarios
- Flujo de control básico (if, for, while)
- Funciones simples

</base-disclaimer-content>
</base-disclaimer>

## Operadores Matemáticos

De **mayor** a **menor** precedencia:

| Operadores | Operación       | Ejemplo         |
| ---------- | --------------- | --------------- |
| \*\*       | Exponenciación  | `2 ** 3 = 8`    |
| %          | Módulo/Resto    | `22 % 8 = 6`    |
| //         | División entera | `22 // 8 = 2`   |
| /          | División        | `22 / 8 = 2.75` |
| \*         | Multiplicación  | `3 * 3 = 9`     |
| -          | Resta           | `5 - 2 = 3`     |
| +          | Suma            | `2 + 2 = 4`     |

Ejemplos de expresiones:

```python
# La multiplicación tiene mayor precedencia que la suma
# Así que esto se evalúa como: 2 + (3 * 6) = 2 + 18 = 20
2 + 3 * 6
```

```output
20
```

```python
# Los paréntesis anulan la precedencia de los operadores
# Esto se evalúa como: 5 * 6 = 30
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

<base-quiz>
<base-quiz-question correct="A">
<template #question>
¿Cuál es el resultado de esta expresión de Python?

```python
4 + 2 * 3
```

</template>

<base-quiz-option value="A" correct>A. 10</base-quiz-option>
<base-quiz-option value="B">B. 18</base-quiz-option>
<base-quiz-option value="C">C. 12</base-quiz-option>
<base-quiz-option value="D">D. 20</base-quiz-option>
<base-quiz-answer value="A">La multiplicación tiene mayor precedencia que la suma, por lo que se evalúa como: 4 + (2 \* 3) = 4 + 6 = 10</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Operadores de Asignación Aumentada

| Operador    | Equivalente      |
| ----------- | ---------------- |
| `var += 1`  | `var = var + 1`  |
| `var -= 1`  | `var = var - 1`  |
| `var *= 1`  | `var = var * 1`  |
| `var /= 1`  | `var = var / 1`  |
| `var //= 1` | `var = var // 1` |
| `var %= 1`  | `var = var % 1`  |
| `var **= 1` | `var = var ** 1` |

Ejemplos:

```python
# Asignación aumentada: equivalente a greeting = greeting + ' world!'
greeting = 'Hello'
greeting += ' world!'
greeting
```

```output
'Hello world!'
```

```python
# Incrementar un número en 1
number = 1
number += 1
number
```

```output
2
```

```python
# Replicar elementos de una lista: equivalente a my_list = my_list * 3
my_list = ['item']
my_list *= 3
my_list
```

```output
['item', 'item', 'item']
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
¿Cuál es el valor de <code>x</code> después de ejecutar este código?

```python
x = 5
x += 3
```

</template>

<base-quiz-option value="A">A. 3</base-quiz-option>
<base-quiz-option value="B" correct>B. 8</base-quiz-option>
<base-quiz-option value="C">C. 5</base-quiz-option>
<base-quiz-option value="D">D. 15</base-quiz-option>
<base-quiz-answer value="B">El operador de asignación aumentada <code>+=</code> es equivalente a <code>x = x + 3</code>. Por lo tanto, <code>x</code> comienza en 5, y luego se convierte en 5 + 3 = 8.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Operador Walrus (Morsa)

El Operador Walrus permite la asignación de variables dentro de una expresión mientras devuelve el valor de la variable.

Ejemplo:

```python
# El operador Walrus asigna y devuelve el valor en una sola expresión
# my_var se asigna "Hello World!" y luego se imprime
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

El _Operador Walrus_, u **Operador de Expresión de Asignación**, fue introducido por primera vez en 2018 a través de [PEP 572](https://peps.python.org/pep-0572/), y luego lanzado oficialmente con **Python 3.8** en octubre de 2019.

<base-disclaimer>
  <base-disclaimer-title>
    Sintaxis Semántica y Ejemplos
  </base-disclaimer-title>
  <base-disclaimer-content>
  El <a href="https://peps.python.org/pep-0572/" target="_blank">PEP 572</a> proporciona la sintaxis, semántica y ejemplos para el Operador Walrus.
  </base-disclaimer-content>
</base-disclaimer>

## Tipos de Datos

Comprender los tipos de datos es uno de los conceptos básicos más importantes de Python. Python tiene nueve tipos de datos integrados principales que cubren casi todo lo que necesitarás:

| Tipo de Dato                                               | Ejemplos                                 | Descripción                                  |
| ---------------------------------------------------------- | ---------------------------------------- | -------------------------------------------- |
| **Números**                                                |                                          |                                              |
| <router-link to='/builtin/int'>`int`</router-link>         | `-2, -1, 0, 1, 2, 3, 4, 5`               | Números enteros                              |
| <router-link to='/builtin/float'>`float`</router-link>     | `-1.25, -1.0, -0.5, 0.0, 0.5, 1.0, 1.25` | Números con punto decimal                    |
| <router-link to='/builtin/complex'>`complex`</router-link> | `2+3j, complex(1, 4)`                    | Números con partes real e imaginaria         |
| **Texto**                                                  |                                          |                                              |
| <router-link to='/builtin/str'>`str`</router-link>         | `'a', 'Hello!', "Python"`                | Texto y caracteres                           |
| **Booleano**                                               |                                          |                                              |
| <router-link to='/builtin/bool'>`bool`</router-link>       | `True, False`                            | Valores Verdadero o Falso                    |
| **None**                                                   |                                          |                                              |
| `NoneType`                                                 | `None`                                   | Representa "ningún valor" o "nada"           |
| **Colecciones**                                            |                                          |                                              |
| <router-link to='/builtin/list'>`list`</router-link>       | `[1, 2, 3], ['a', 'b', 'c']`             | Colecciones ordenadas y modificables         |
| <router-link to='/builtin/dict'>`dict`</router-link>       | `{'name': 'Alice', 'age': 30}`           | Pares clave-valor                            |
| <router-link to='/builtin/tuple'>`tuple`</router-link>     | `(1, 2, 3), ('a', 'b')`                  | Colecciones ordenadas e inmutables           |
| <router-link to='/builtin/set'>`set`</router-link>         | `{1, 2, 3}, {'a', 'b', 'c'}`             | Colecciones desordenadas de elementos únicos |

### Ejemplos Rápidos

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

# Colecciones
scores = [85, 92, 78]      # list
person = {'name': 'Bob', 'age': 30}  # dict
coordinates = (10, 20)     # tuple
unique_ids = {1, 2, 3}     # set
```

Para una guía completa con ejemplos visuales y explicaciones detalladas sobre cuándo usar cada tipo, consulte: <router-link to="/blog/python-data-types">Tipos de Datos en Python: Una Guía Visual para Principiantes</router-link>.

## Concatenación y Replicación

Concatenación de cadenas (strings):

```python
# Concatenación de cadenas: las cadenas adyacentes se unen automáticamente
'Alice' 'Bob'
```

```output
'AliceBob'
```

Replicación de cadenas:

```python
# Replicación de cadenas: repite la cadena varias veces
'Alice' * 5
```

```output
'AliceAliceAliceAliceAlice'
```

## Variables

Las variables son una parte fundamental de los conceptos básicos de Python. Puedes nombrar una variable como quieras siempre que obedezca las siguientes reglas:

1. Solo puede ser una palabra.

```python
# mal
my variable = 'Hello'

# bien
var = 'Hello'
```

2. Solo puede usar letras, números y el carácter de guion bajo (`_`).

```python
# mal
%$@variable = 'Hello'

# bien
my_var = 'Hello'

# bien
my_var_2 = 'Hello'
```

3. No puede comenzar con un número.

```python
# esto no funcionará
23_var = 'hello'
```

4. Un nombre de variable que comienza con un guion bajo (`_`) se considera "no útil" (o interno).

```python
# _spam no debe usarse más en el código
_spam = 'Hello'
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
En los conceptos básicos de Python, ¿cuál de los siguientes es un nombre de variable válido?
</template>

<base-quiz-option value="A">A. <code>3value</code></base-quiz-option>
<base-quiz-option value="B">B. <code>user-name</code></base-quiz-option>
<base-quiz-option value="C" correct>C. <code>user_name</code></base-quiz-option>
<base-quiz-option value="D">D. <code>for</code></base-quiz-option>
<base-quiz-answer value="C"><code>user_name</code> es un nombre de variable válido porque solo utiliza letras, números y guiones bajos, y no comienza con un número.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Comentarios

Comentario en línea:

```python
# Este es un comentario
```

Comentario multilínea:

```python
# Este es un
# comentario multilínea
```

Código con un comentario:

```python
a = 1  # inicialización
```

Tenga en cuenta los dos espacios delante del comentario.

Docstring de función:

```python
def foo():
    """
    Este es un docstring de función
    También puedes usar:
    ''' Docstring de Función '''
    """
```

## La Función print()

La función `print()` es uno de los primeros conceptos básicos de Python que aprenderás. Escribe el valor de los argumentos que se le pasan. [...] maneja múltiples argumentos, cantidades de punto flotante y cadenas. Las cadenas se imprimen sin comillas, y se inserta un espacio entre los elementos, para que puedas formatear las cosas de manera agradable:

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

### La palabra clave end

El argumento de palabra clave `end` se puede usar para evitar el salto de línea después de la salida, o para terminar la salida con una cadena diferente:

```python
# Usa el parámetro end para cambiar lo que viene después de cada instrucción print
phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
for word in phrase:
    print(word, end='-')  # Usa '-' en lugar de salto de línea
```

```output
printed-with-a-dash-in-between-
```

### La palabra clave sep

La palabra clave `sep` especifica cómo separar los objetos, si hay más de uno:

```python
# Usa el parámetro sep para especificar el separador entre múltiples argumentos
print('cats', 'dogs', 'mice', sep=',')  # Salida separada por comas
```

```output
cats,dogs,mice
```

## La Función input()

Esta función toma la entrada del usuario y la convierte en una cadena (string):

```python
# input() lee la entrada del usuario y la devuelve como una cadena
print('What is your name?')   # pide su nombre
my_name = input()  # Espera a que el usuario escriba y presione Enter
print('Hi, {}'.format(my_name))
```

```output
What is your name?
Martha
Hi, Martha
```

`input()` también puede establecer un mensaje predeterminado sin usar `print()`:

```python
my_name = input('What is your name? ')  # mensaje predeterminado
print('Hi, {}'.format(my_name))
```

```output
What is your name? Martha
Hi, Martha
```

También es posible usar cadenas formateadas para evitar el uso de .format:

```python
# input() puede mostrar un mensaje de indicación directamente
my_name = input('What is your name? ')  # Indicación y lectura en una sola llamada
print(f'Hi, {my_name}')  # f-string para formateo de cadenas
```

```output
What is your name? Martha
Hi, Martha
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
En los conceptos básicos de Python, ¿qué tipo devuelve `input()`?
</template>

<base-quiz-option value="A">A. int</base-quiz-option>
<base-quiz-option value="B" correct>B. str</base-quiz-option>
<base-quiz-option value="C">C. float</base-quiz-option>
<base-quiz-option value="D">D. Depende de la entrada del usuario</base-quiz-option>
<base-quiz-answer value="B">La función <code>input()</code> siempre devuelve una cadena (string), independientemente de lo que escriba el usuario. Debe convertirla a otros tipos si es necesario.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## La Función len()

Se evalúa al valor entero del número de caracteres en una cadena, lista, diccionario, etc.:

```python
# len() devuelve el número de caracteres en una cadena
len('hello')  # Devuelve 5
```

```output
5
```

```python
# len() devuelve el número de elementos en una lista
len(['cat', 3, 'dog'])  # Devuelve 3 (tres elementos)
```

```output
3
```

<base-warning>
  <base-warning-title>Prueba de Vacío</base-warning-title>
  <base-warning-content>
    La prueba de si las cadenas, listas, diccionarios, etc., están vacíos no debe usar
    <code>len</code>, sino preferir la evaluación booleana directa.
  </base-warning-content>
</base-warning>

Ejemplo de prueba de vacío:

```python
a = [1, 2, 3]

# mal: comprobación de len() innecesaria
if len(a) > 0:  # se evalúa como True
    print("the list is not empty!")
```

```output
the list is not empty!
```

```python
# bien: evaluación booleana directa (forma Pythonica)
if a:  # se evalúa como True si la lista no está vacía
    print("the list is not empty!")
```

```output
the list is not empty!
```

## Las Funciones str(), int(), y float()

Estas funciones le permiten cambiar el tipo de una variable. Por ejemplo, puede transformar de un `integer` o `float` a un `string`:

```python
# Convertir entero a cadena
str(29)  # Devuelve '29'
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

O de una `string` a un `integer` o `float`:

```python
# Convertir cadena a entero
int('11')  # Devuelve 11
```

```output
11
```

```python
# Convertir cadena a flotante
float('3.14')  # Devuelve 3.14
```

```output
3.14
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
¿Cuál es el resultado de este código de Python?

```python
result = int('42')
type(result)
```

</template>

<base-quiz-option value="A">A. <code>str</code></base-quiz-option>
<base-quiz-option value="B">B. <code>float</code></base-quiz-option>
<base-quiz-option value="C" correct>C. <code>int</code></base-quiz-option>
<base-quiz-option value="D">D. <code>NoneType</code></base-quiz-option>
<base-quiz-answer value="C">La función <code>int()</code> convierte una cadena a un entero. Por lo tanto, <code>int('42')</code> devuelve el entero <code>42</code>, y <code>type(42)</code> devuelve <code>int</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Enlaces Relevantes

- <router-link to="/blog/python-data-types">Tipos de Datos en Python: Una Guía Visual para Principiantes</router-link>
- <router-link to="/blog/python-comprehensions-step-by-step">Comprensiones de Python Paso a Paso</router-link>
- <router-link to="/cheatsheet/control-flow">Flujo de Control</router-link>
- <router-link to="/cheatsheet/functions">Funciones</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Listas y Tuplas</router-link>
- <router-link to="/cheatsheet/dictionaries">Diccionarios</router-link>
- <router-link to="/cheatsheet/sets">Conjuntos (Sets)</router-link>
- <router-link to="/cheatsheet/string-formatting">Formato de Cadenas (String Formatting)</router-link>
