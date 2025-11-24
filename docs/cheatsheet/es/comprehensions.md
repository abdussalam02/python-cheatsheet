---
title: 'Comprensiones de Python - Hoja de Trucos de Python'
description: 'Las comprensiones de listas ofrecen una forma concisa de crear listas'
labUrl: 'https://labex.io/es/labs/python-python-comprehensions-633649?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Comprensiones de Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Las Comprensiones de Listas son un tipo especial de sintaxis que nos permite crear listas a partir de otras listas, y son increíblemente útiles cuando se trabaja con números y con uno o dos niveles de bucles for anidados.

<base-disclaimer>
  <base-disclaimer-title>
    Del tutorial de Python 3 <a target="_blank" href="https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions">aquí</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Las comprensiones de listas proporcionan una forma concisa de crear listas. [...] o para crear una subsecuencia de aquellos elementos que satisfacen una cierta condición.
  </base-disclaimer-content>
</base-disclaimer>

Lea <router-link to="/blog/python-comprehensions-step-by-step">Comprensiones de Python: Una introducción paso a paso</router-link> para una introducción más profunda.

## Comprensión de listas

Así es como creamos una nueva lista a partir de una colección existente con un Bucle For:

```python
# Enfoque tradicional: crear lista usando un bucle for
names = ['Charles', 'Susan', 'Patrick', 'George']

new_list = []
for n in names:
    new_list.append(n)

new_list
```

```output
['Charles', 'Susan', 'Patrick', 'George']
```

Y así es como hacemos lo mismo con una Comprensión de Listas:

```python
# Comprensión de listas: forma concisa de crear una nueva lista
# Sintaxis: [expresión for elemento in iterable]
names = ['Charles', 'Susan', 'Patrick', 'George']

new_list = [n for n in names]  # Crear lista con todos los nombres
new_list
```

```output
['Charles', 'Susan', 'Patrick', 'George']
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
¿Cuál es la sintaxis básica de una comprensión de listas?
</template>

<base-quiz-option value="A" correct>A. <code>[expresión for elemento in iterable]</code></base-quiz-option>
<base-quiz-option value="B">B. <code>(expresión for elemento in iterable)</code></base-quiz-option>
<base-quiz-option value="C">C. <code>{expresión for elemento in iterable}</code></base-quiz-option>
<base-quiz-option value="D">D. <code>expresión for elemento in iterable</code></base-quiz-option>
<base-quiz-answer value="A">Las comprensiones de listas usan corchetes <code>[]</code> con la sintaxis <code>[expresión for elemento in iterable]</code>. Esto crea una nueva lista aplicando la expresión a cada elemento.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Podemos hacer lo mismo con números:

```python
# Comprensión de lista anidada: crear tuplas a partir de dos rangos
# Equivalente a bucles for anidados
n = [(a, b) for a in range(1, 3) for b in range(1, 3)]
n
```

```output
[(1, 1), (1, 2), (2, 1), (2, 2)]
```

## Añadir condicionales

Si queremos que `new_list` contenga solo los nombres que comienzan con C, con un bucle for, lo haríamos así:

```python
# Enfoque tradicional: filtrar con condición if
names = ['Charles', 'Susan', 'Patrick', 'George', 'Carol']

new_list = []
for n in names:
    if n.startswith('C'):  # Filtrar nombres que comienzan con 'C'
        new_list.append(n)

print(new_list)
```

```output
['Charles', 'Carol']
```

En una Comprensión de Listas, añadimos la sentencia `if` al final:

```python
# Comprensión de listas con condición: filtrar elementos
# Sintaxis: [expresión for elemento in iterable if condición]
new_list = [n for n in names if n.startswith('C')]
print(new_list)
```

```output
['Charles', 'Carol']
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
¿Dónde va la condición <code>if</code> en una comprensión de listas?
</template>

<base-quiz-option value="A">A. Antes de la palabra clave <code>for</code></base-quiz-option>
<base-quiz-option value="B" correct>B. Después de la cláusula <code>for</code></base-quiz-option>
<base-quiz-option value="C">C. Dentro de la expresión</base-quiz-option>
<base-quiz-option value="D">D. Antes de los corchetes</base-quiz-option>
<base-quiz-answer value="B">En una comprensión de listas, la condición <code>if</code> viene después de la cláusula <code>for</code>: <code>[expresión for elemento in iterable if condición]</code>. Esto filtra elementos basándose en la condición.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Para usar una sentencia `if-else` en una Comprensión de Listas:

```python
# Comprensión de listas con if-else: expresión condicional
# Sintaxis: [expresión_si_verdadero if condición else expresión_si_falso for elemento in iterable]
nums = [1, 2, 3, 4, 5, 6]
new_list = [num*2 if num % 2 == 0 else num for num in nums]  # Duplicar números pares
print(new_list)
```

```output
[1, 4, 3, 8, 5, 12]
```

<base-disclaimer>
  <base-disclaimer-title>
    Comprensiones de conjuntos y diccionarios
  </base-disclaimer-title>
  <base-disclaimer-content>
    Los conceptos básicos de las comprensiones de `list` también se aplican a los <b>conjuntos</b> y <b>diccionarios</b>.
  </base-disclaimer-content>
</base-disclaimer>

## Comprensión de conjuntos

```python
# Comprensión de conjuntos: crear un conjunto usando sintaxis de comprensión
# Sintaxis: {expresión for elemento in iterable}
b = {"abc", "def"}
{s.upper() for s in b}  # Convertir todas las cadenas a mayúsculas
```

```output
{"ABC", "DEF"}
```

## Comprensión de diccionarios

```python
# Comprensión de diccionarios: intercambiar claves y valores
# Sintaxis: {expresión_clave: expresión_valor for elemento in iterable}
c = {'name': 'Pooka', 'age': 5}
{v: k for k, v in c.items()}  # Invertir pares clave-valor
```

```output
{'Pooka': 'name', 5: 'age'}
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
¿Qué sintaxis se utiliza para las comprensiones de diccionarios?
</template>

<base-quiz-option value="A">A. <code>[clave: valor for elemento in iterable]</code></base-quiz-option>
<base-quiz-option value="B">B. <code>(clave: valor for elemento in iterable)</code></base-quiz-option>
<base-quiz-option value="C" correct>C. <code>{expresión_clave: expresión_valor for elemento in iterable}</code></base-quiz-option>
<base-quiz-option value="D">D. <code>{clave, valor for elemento in iterable}</code></base-quiz-option>
<base-quiz-answer value="C">Las comprensiones de diccionarios usan llaves <code>{}</code> con la sintaxis <code>{expresión_clave: expresión_valor for elemento in iterable}</code>, similar a las comprensiones de listas pero con pares clave-valor.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Se puede generar una comprensión de listas a partir de un diccionario:

```python
# Comprensión de listas a partir de un diccionario: crear cadenas formateadas
c = {'name': 'Pooka', 'age': 5}
["{}:{}".format(k.upper(), v) for k, v in c.items()]  # Formatear como "CLAVE:valor"
```

```output
['NAME:Pooka', 'AGE:5']
```

## Enlaces relevantes

- <router-link to="/blog/python-comprehensions-step-by-step">Comprensiones de Python: Una introducción paso a paso</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Listas y Tuplas de Python</router-link>
- <router-link to="/cheatsheet/sets">Conjuntos de Python</router-link>
- <router-link to="/cheatsheet/dictionaries">Diccionarios de Python</router-link>
- <router-link to="/blog/python-sets-what-why-how">Conjuntos de Python: Qué, Por qué y Cómo</router-link>
- <router-link to="/blog/python-data-types">Publicación del Blog sobre Tipos de Datos de Python</router-link>
