---
title: 'Listas y Tuplas de Python - Hoja de Trucos de Python'
description: 'En Python, las Listas son uno de los 4 tipos de datos utilizados para almacenar colecciones de información.'
labUrl: 'https://labex.io/es/labs/python-python-lists-and-tuples-633660?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Listas de Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Las listas son uno de los 4 tipos de datos en Python que se utilizan para almacenar colecciones de datos.

```python
# List: colección ordenada de elementos encerrados entre corchetes
['John', 'Peter', 'Debora', 'Charles']
```

## Obtener valores con índices

```python
# Acceder a elementos de la lista usando el índice (base 0, el primer elemento es el índice 0)
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[0]  # Devuelve el primer elemento: 'table'
```

```output
'table'
```

```python
furniture[1]
```

```output
'chair'
```

```python
furniture[2]
```

```output
'rack'
```

```python
furniture[3]
```

```output
'shelf'
```

## Índices negativos

```python
# Índice negativo: acceder a elementos desde el final de la lista
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[-1]  # Devuelve el último elemento: 'shelf'
```

```output
'shelf'
```

```python
furniture[-3]
```

```output
'chair'
```

```python
f'The {furniture[-1]} is bigger than the {furniture[-3]}'
```

```output
'The shelf is bigger than the chair'
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
¿Qué devuelve <code>furniture[-1]</code> si <code>furniture = ['table', 'chair', 'rack', 'shelf']</code>?
</template>

<base-quiz-option value="A">A. <code>'table'</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>'shelf'</code></base-quiz-option>
<base-quiz-option value="C">C. <code>['shelf']</code></base-quiz-option>
<base-quiz-option value="D">D. <code>IndexError</code></base-quiz-option>
<base-quiz-answer value="B">Los índices negativos acceden a los elementos desde el final de la lista. <code>-1</code> se refiere al último elemento, <code>-2</code> al penúltimo, y así sucesivamente.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Obtener sublistas con Slices

```python
# Slicing: obtener sublista usando la sintaxis [inicio:fin] (el fin es exclusivo)
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[0:4]  # Devuelve los elementos desde el índice 0 hasta el 3 (el 4 excluido)
```

```output
['table', 'chair', 'rack', 'shelf']
```

```python
furniture[1:3]
```

```output
['chair', 'rack']
```

```python
furniture[0:-1]
```

```output
['table', 'chair', 'rack']
```

```python
# Slice desde el principio: omitir el índice de inicio (por defecto es 0)
furniture[:2]  # Devuelve los dos primeros elementos
```

```output
['table', 'chair']
```

```python
# Slice hasta el final: omitir el índice final (por defecto es el final de la lista)
furniture[1:]  # Devuelve todos los elementos desde el índice 1 hasta el final
```

```output
['chair', 'rack', 'shelf']
```

```python
furniture[:]
```

```output
['table', 'chair', 'rack', 'shelf']
```

Dividir la lista completa realizará una copia:

```python
# El slicing crea una copia: [:] crea una copia superficial de la lista
spam = ['cat', 'bat', 'rat', 'elephant']
spam2 = spam[:]  # Crea una copia, no una referencia
spam2
```

```output
['cat', 'bat', 'rat', 'elephant']
```

```python
spam.append('dog')
spam
```

```output
['cat', 'bat', 'rat', 'elephant', 'dog']
```

```python
spam2
```

```output
['cat', 'bat', 'rat', 'elephant']
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
¿Qué crea <code>spam[:]</code> cuando <code>spam</code> es una lista?
</template>

<base-quiz-option value="A">A. Una referencia a la misma lista</base-quiz-option>
<base-quiz-option value="B">B. Una lista vacía</base-quiz-option>
<base-quiz-option value="C" correct>C. Una copia superficial de la lista</base-quiz-option>
<base-quiz-option value="D">D. Una lista invertida</base-quiz-option>
<base-quiz-answer value="C">Dividir la lista completa con <code>[:]</code> crea una copia superficial. Modificar la copia no afectará a la lista original.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Obtener la longitud de una lista con len()

```python
# len() devuelve el número de elementos en una lista
furniture = ['table', 'chair', 'rack', 'shelf']
len(furniture)  # Devuelve 4
```

```output
4
```

## Cambiar valores con índices

```python
# Modificar elementos de la lista asignando nuevos valores a los índices
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[0] = 'desk'  # Reemplazar el primer elemento
furniture
```

```output
['desk', 'chair', 'rack', 'shelf']
```

```python
furniture[2] = furniture[1]
furniture
```

```output
['desk', 'chair', 'chair', 'shelf']
```

```python
furniture[-1] = 'bed'
furniture
```

```output
['desk', 'chair', 'chair', 'bed']
```

## Concatenación y Replicación

```python
# Concatenación de listas: combinar dos listas usando el operador +
[1, 2, 3] + ['A', 'B', 'C']  # Devuelve [1, 2, 3, 'A', 'B', 'C']
```

```output
[1, 2, 3, 'A', 'B', 'C']
```

```python
# Replicación de listas: repetir la lista varias veces usando el operador *
['X', 'Y', 'Z'] * 3  # Devuelve ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
```

```output
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
```

```python
my_list = [1, 2, 3]
my_list = my_list + ['A', 'B', 'C']
my_list
```

```output
[1, 2, 3, 'A', 'B', 'C']
```

## Uso de bucles for con Listas

```python
# Iterar sobre los elementos de la lista usando un bucle for
furniture = ['table', 'chair', 'rack', 'shelf']

for item in furniture:  # Bucle a través de cada elemento
    print(item)
```

```output
table
chair
rack
shelf
```

## Obtener el índice en un bucle con enumerate()

```python
# enumerate() devuelve tanto el índice como el valor en un bucle
furniture = ['table', 'chair', 'rack', 'shelf']

for index, item in enumerate(furniture):  # Obtener índice y elemento juntos
    print(f'index: {index} - item: {item}')
```

```output
index: 0 - item: table
index: 1 - item: chair
index: 2 - item: rack
index: 3 - item: shelf
```

## Bucle en Múltiples Listas con zip()

```python
# zip() combina múltiples listas elemento por elemento en un bucle
furniture = ['table', 'chair', 'rack', 'shelf']
price = [100, 50, 80, 40]

for item, amount in zip(furniture, price):  # Emparejar elementos de ambas listas
    print(f'The {item} costs ${amount}')
```

```output
The table costs $100
The chair costs $50
The rack costs $80
The shelf costs $40
```

## Los operadores in y not in

```python
# Operador in: comprobar si un elemento existe en una lista
'rack' in ['table', 'chair', 'rack', 'shelf']  # Devuelve True
```

```output
True
```

```python
'bed' in ['table', 'chair', 'rack', 'shelf']
```

```output
False
```

```python
furniture = ['table', 'chair', 'rack', 'shelf']
'bed' not in furniture
```

```output
True
```

```python
'rack' not in furniture
```

```output
False
```

## El truco de la asignación múltiple

El truco de la asignación múltiple es un atajo que le permite asignar múltiples variables con los valores de una lista en una sola línea de código. Así que en lugar de hacer esto:

```python
furniture = ['table', 'chair', 'rack', 'shelf']
table = furniture[0]
chair = furniture[1]
rack = furniture[2]
shelf = furniture[3]
```

Podrías escribir esta línea de código:

```python
furniture = ['table', 'chair', 'rack', 'shelf']
table, chair, rack, shelf = furniture

table
```

```output
'table'
```

```python
chair
```

```output
'chair'
```

```python
rack
```

```output
'rack'
```

```python
shelf
```

```output
'shelf'
```

El truco de la asignación múltiple también se puede utilizar para intercambiar los valores en dos variables:

```python
a, b = 'table', 'chair'
a, b = b, a
print(a)
```

```output
chair
```

```python
print(b)
```

```output
table
```

## El método index

El método `index` le permite encontrar el índice de un valor pasando su nombre:

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.index('chair')
```

```output
1
```

## Añadir Valores

### append()

`append` añade un elemento al final de una `list`:

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.append('bed')
furniture
```

```output
['table', 'chair', 'rack', 'shelf', 'bed']
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
¿Qué hace el método <code>append()</code> a una lista?
</template>

<base-quiz-option value="A" correct>A. Añade un elemento al final de la lista</base-quiz-option>
<base-quiz-option value="B">B. Añade un elemento al principio de la lista</base-quiz-option>
<base-quiz-option value="C">C. Reemplaza el último elemento</base-quiz-option>
<base-quiz-option value="D">D. Elimina el último elemento</base-quiz-option>
<base-quiz-answer value="A">El método <code>append()</code> añade un único elemento al final de una lista. Para añadir un elemento en una posición específica, usa <code>insert()</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

### insert()

`insert` añade un elemento a una `list` en una posición dada:

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.insert(1, 'bed')
furniture
```

```output
['table', 'bed', 'chair', 'rack', 'shelf']
```

## Eliminar Valores

### del()

`del` elimina un elemento usando el índice:

```python
furniture = ['table', 'chair', 'rack', 'shelf']
del furniture[2]
furniture
```

```output
['table', 'chair', 'shelf']
```

```python
del furniture[2]
furniture
```

```output
['table', 'chair']
```

### remove()

`remove` elimina un elemento usando su valor real:

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.remove('chair')
furniture
```

```output
['table', 'rack', 'shelf']
```

<base-warning>
  <base-warning-title>
    Eliminación de elementos repetidos
  </base-warning-title>
  <base-warning-content>
    Si el valor aparece varias veces en la lista, solo se eliminará la primera instancia del valor.
  </base-warning-content>
</base-warning>

### pop()

Por defecto, `pop` eliminará y devolverá el último elemento de la lista. También puedes pasar el índice del elemento como parámetro opcional:

```python
animals = ['cat', 'bat', 'rat', 'elephant']

animals.pop()
```

```output
'elephant'
```

```python
animals
```

```output
['cat', 'bat', 'rat']
```

```python
animals.pop(0)
```

```output
'cat'
```

```python
animals
```

```output
['bat', 'rat']
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
¿Qué hace <code>pop()</code> cuando se llama en una lista?
</template>

<base-quiz-option value="A">A. Solo elimina el último elemento</base-quiz-option>
<base-quiz-option value="B" correct>B. Elimina y devuelve un elemento (el último por defecto, o el índice especificado)</base-quiz-option>
<base-quiz-option value="C">C. Solo devuelve el último elemento sin eliminarlo</base-quiz-option>
<base-quiz-option value="D">D. Elimina todos los elementos de la lista</base-quiz-option>
<base-quiz-answer value="B">El método <code>pop()</code> elimina y devuelve un elemento. Por defecto elimina el último elemento, pero puedes pasar un índice para eliminar un elemento específico.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Ordenar valores con sort()

```python
numbers = [2, 5, 3.14, 1, -7]
numbers.sort()
numbers
```

```output
[-7, 1, 2, 3.14, 5]
```

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.sort()
furniture
```

```output
['chair', 'rack', 'shelf', 'table']
```

También puedes pasar `True` para el argumento de palabra clave `reverse` para que `sort()` ordene los valores en orden inverso:

```python
furniture.sort(reverse=True)
furniture
```

```output
['table', 'shelf', 'rack', 'chair']
```

Si necesitas ordenar los valores en orden alfabético normal, pasa `str.lower` para el argumento de palabra clave `key` en la llamada al método sort():

```python
letters = ['a', 'z', 'A', 'Z']
letters.sort(key=str.lower)
letters
```

```output
['a', 'A', 'z', 'Z']
```

Puedes usar la función incorporada `sorted` para devolver una nueva lista:

```python
furniture = ['table', 'chair', 'rack', 'shelf']
sorted(furniture)
```

```output
['chair', 'rack', 'shelf', 'table']
```

## El tipo de dato Tuple

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://stackoverflow.com/questions/1708510/list-vs-tuple-when-to-use-each">Tuplas vs Listas</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    La diferencia clave entre tuplas y listas es que, mientras que las <code>tuples</code> son objetos <i>inmutables</i>, las <code>lists</code> son <i>mutables</i>. Esto significa que las tuplas no se pueden cambiar mientras que las listas sí se pueden modificar. Las tuplas son más eficientes en memoria que las listas.
  </base-disclaimer-content>
</base-disclaimer>

```python
furniture = ('table', 'chair', 'rack', 'shelf')

furniture[0]
```

```output
'table'
```

```python
furniture[1:3]
```

```output
('chair', 'rack')
```

```python
len(furniture)
```

```output
4
```

La principal forma en que las tuplas difieren de las listas es que las tuplas, al igual que las cadenas, son inmutables.

## Conversión entre list() y tuple()

```python
tuple(['cat', 'dog', 5])
```

```output
('cat', 'dog', 5)
```

```python
list(('cat', 'dog', 5))
```

```output
['cat', 'dog', 5]
```

```python
list('hello')
```

```output
['h', 'e', 'l', 'l', 'o']
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
¿Cuál es la principal diferencia entre listas y tuplas en Python?
</template>

<base-quiz-option value="A">A. Las listas solo pueden contener números, las tuplas pueden contener cualquier cosa</base-quiz-option>
<base-quiz-option value="B">B. Las tuplas son más rápidas de crear</base-quiz-option>
<base-quiz-option value="C" correct>C. Las listas son mutables (se pueden cambiar), las tuplas son inmutables (no se pueden cambiar)</base-quiz-option>
<base-quiz-option value="D">D. Las listas usan corchetes cuadrados, las tuplas usan llaves</base-quiz-option>
<base-quiz-answer value="C">Las listas son mutables, lo que significa que puedes modificarlas después de la creación. Las tuplas son inmutables, lo que significa que una vez creadas, no se pueden cambiar. Ambas pueden contener cualquier tipo de dato.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Enlaces relevantes

- <router-link to="/blog/python-data-types">Tipos de Datos de Python: Una Guía Visual para Principiantes</router-link>
- <router-link to="/blog/python-comprehensions-step-by-step">Comprensiones de Python Paso a Paso</router-link>
- <router-link to="/cheatsheet/comprehensions">Comprensiones de Python</router-link>
- <router-link to="/modules/itertools-module">El Módulo itertools</router-link>
- <router-link to="/builtin/list">list()</router-link>
- <router-link to="/builtin/tuple">tuple()</router-link>
- <router-link to="/builtin/len">len()</router-link>
