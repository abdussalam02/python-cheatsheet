---
title: 'Conjuntos de Python - Hoja de Trucos de Python'
description: 'Python incluye varios tipos de datos integrados para ayudarnos a organizar nuestra información. Estas estructuras incluyen listas, diccionarios, tuplas y conjuntos.'
labUrl: 'https://labex.io/es/labs/python-python-sets-633665?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Conjuntos de Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Python viene equipado con varios tipos de datos incorporados para ayudarnos a organizar nuestros datos. Estas estructuras incluyen listas, diccionarios, tuplas y **conjuntos** (sets).

<base-disclaimer>
  <base-disclaimer-title>
    De la <a target="_blank" href="https://docs.python.org/3/tutorial/datastructures.html#sets">documentación</a> de Python 3
  </base-disclaimer-title>
  <base-disclaimer-content>
    Un conjunto es una colección desordenada sin elementos duplicados. Los usos básicos incluyen la prueba de pertenencia y la eliminación de entradas duplicadas.
  </base-disclaimer-content>
</base-disclaimer>

Lea <router-link to="/blog/python-sets-what-why-how">Python Sets: What, Why and How</router-link> para una referencia más profunda.

## Inicialización de un conjunto

Hay dos formas de crear conjuntos: usando llaves `{}` y la función incorporada `set()`

<base-warning>
  <base-warning-title>
    Conjuntos Vacíos
  </base-warning-title>
  <base-warning-content>
    Al crear un conjunto, asegúrese de no usar llaves vacías <code>{}</code> o, en su lugar, obtendrá un diccionario vacío.
  </base-warning-content>
</base-warning>

```python
# Crear conjunto usando llaves o la función set()
s = {1, 2, 3}  # Usando llaves
s = set([1, 2, 3])  # Usando el constructor set()

# Advertencia: {} vacío crea un diccionario, no un conjunto
s = {}  # esto creará un diccionario en lugar de un conjunto
type(s)  # Devuelve <class 'dict'>
```

```output
<class 'dict'>
```

## Colecciones desordenadas de elementos únicos

Un conjunto elimina automáticamente todos los valores duplicados.

```python
# Los conjuntos eliminan automáticamente los duplicados
s = {1, 2, 3, 2, 3, 4}  # Se eliminan los duplicados
s  # Devuelve {1, 2, 3, 4}
```

```output
{1, 2, 3, 4}
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
¿Qué sucede cuando crea un conjunto con valores duplicados?
</template>

<base-quiz-option value="A" correct>A. Los duplicados se eliminan automáticamente</base-quiz-option>
<base-quiz-option value="B">B. Se genera un error</base-quiz-option>
<base-quiz-option value="C">C. El conjunto conserva todos los duplicados</base-quiz-option>
<base-quiz-option value="D">D. Solo se conserva la primera ocurrencia</base-quiz-option>
<base-quiz-answer value="A">Los conjuntos eliminan automáticamente los valores duplicados. Un conjunto es una colección desordenada sin elementos duplicados.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Y como tipo de dato desordenado, no se puede indexar.

```python
s = {1, 2, 3}
s[0]
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
```

## set add y update

Usando el método `add()` podemos agregar un solo elemento al conjunto.

```python
# Método add(): agregar un solo elemento al conjunto
s = {1, 2, 3}
s.add(4)  # Agregar elemento 4
s
```

```output
{1, 2, 3, 4}
```

Y con `update()`, múltiples elementos:

```python
# Método update(): agregar múltiples elementos de un iterable
s = {1, 2, 3}
s.update([2, 3, 4, 5, 6])  # Agregar múltiples elementos (duplicados ignorados)
s
```

```output
{1, 2, 3, 4, 5, 6}
```

## set remove y discard

Ambos métodos eliminarán un elemento del conjunto, pero `remove()` generará un `key error` si el valor no existe.

```python
# Método remove(): eliminar elemento, genera KeyError si no se encuentra
s = {1, 2, 3}
s.remove(3)  # Eliminar elemento 3
s
```

```output
{1, 2}
```

```python
s.remove(3)
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 3
```

`discard()` no generará ningún error.

```python
# Método discard(): eliminar elemento, sin error si no se encuentra
s = {1, 2, 3}
s.discard(3)  # Eliminar elemento 3 (seguro, sin error si falta)
s
```

```output
{1, 2}
```

```python
s.discard(3)
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
¿Cuál es la diferencia entre los métodos <code>remove()</code> y <code>discard()</code> para conjuntos?
</template>

<base-quiz-option value="A">A. <code>remove()</code> elimina un elemento, <code>discard()</code> elimina todos</base-quiz-option>
<base-quiz-option value="B">B. No hay diferencia</base-quiz-option>
<base-quiz-option value="C" correct>C. <code>remove()</code> genera un error si el elemento no existe, <code>discard()</code> no lo hace</base-quiz-option>
<base-quiz-option value="D">D. <code>remove()</code> es más rápido</base-quiz-option>
<base-quiz-answer value="C">Ambos métodos eliminan un elemento de un conjunto, pero <code>remove()</code> genera un <code>KeyError</code> si el elemento no existe, mientras que <code>discard()</code> no hace nada si el elemento falta.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## set union

`union()` o `|` crearán un nuevo conjunto con todos los elementos de los conjuntos proporcionados.

```python
# union(): combinar todos los elementos de múltiples conjuntos (sin duplicados)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.union(s2)  # o 's1 | s2' - devuelve {1, 2, 3, 4, 5}
```

```output
{1, 2, 3, 4, 5}
```

## set intersection

`intersection()` o `&` devolverán un conjunto con solo los elementos que son comunes a todos ellos.

```python
# intersection(): devolver elementos comunes a todos los conjuntos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
s1.intersection(s2, s3)  # o 's1 & s2 & s3' - devuelve {3}
```

```output
{3}
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
¿Qué devuelve <code>intersection()</code> para los conjuntos?
</template>

<base-quiz-option value="A">A. Todos los elementos de todos los conjuntos</base-quiz-option>
<base-quiz-option value="B" correct>B. Solo los elementos que son comunes a todos los conjuntos</base-quiz-option>
<base-quiz-option value="C">C. Elementos en el primer conjunto pero no en los otros</base-quiz-option>
<base-quiz-option value="D">D. Elementos en cualquiera de los conjuntos pero no en ambos</base-quiz-option>
<base-quiz-answer value="B">El método <code>intersection()</code> devuelve un conjunto que contiene solo los elementos que están presentes en todos los conjuntos que se comparan.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## set difference

`difference()` o `-` devolverán solo los elementos que son únicos para el primer conjunto (conjunto invocado).

```python
# difference(): devolver elementos en el primer conjunto pero no en otros
s1 = {1, 2, 3}
s2 = {2, 3, 4}

s1.difference(s2)  # o 's1 - s2' - devuelve {1}
```

```output
{1}
```

```python
s2.difference(s1) # o 's2 - s1'
```

```output
{4}
```

## set symmetric_difference

`symmetric_difference()` o `^` devolverán todos los elementos que no son comunes entre ellos.

```python
# symmetric_difference(): devolver elementos en cualquiera de los conjuntos, pero no en ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1.symmetric_difference(s2)  # o 's1 ^ s2' - devuelve {1, 4}
```

```output
{1, 4}
```

<base-quiz>
<base-quiz-question correct="D">
<template #question>
¿Qué devuelve <code>symmetric_difference()</code> para dos conjuntos?
</template>

<base-quiz-option value="A">A. Todos los elementos de ambos conjuntos</base-quiz-option>
<base-quiz-option value="B">B. Solo los elementos comunes a ambos conjuntos</base-quiz-option>
<base-quiz-option value="C">C. Elementos en el primer conjunto pero no en el segundo</base-quiz-option>
<base-quiz-option value="D" correct>D. Elementos en cualquiera de los conjuntos, pero no en ambos</base-quiz-option>
<base-quiz-answer value="D">El método <code>symmetric_difference()</code> devuelve un conjunto que contiene elementos que están en cualquiera de los conjuntos, pero no en ambos conjuntos.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Enlaces relevantes

- <router-link to="/blog/python-data-types">Publicación del Blog Tipos de Datos de Python</router-link>
- <router-link to="/blog/python-sets-what-why-how">Python Sets: What, Why and How</router-link>
- <router-link to="/cheatsheet/dictionaries">Diccionarios de Python</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Listas y Tuplas de Python</router-link>
