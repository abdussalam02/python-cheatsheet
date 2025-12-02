---
title: 'Генераторы Python - Шпаргалка по Python'
description: 'Генераторы списков предоставляют краткий способ создания списков'
labUrl: 'https://labex.io/ru/labs/python-python-comprehensions-633649?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Генераторы Python (Comprehensions)
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Генераторы списков (List Comprehensions) — это особый синтаксис, который позволяет создавать списки из других списков и невероятно полезен при работе с числами и одним или двумя уровнями вложенных циклов `for`.

<base-disclaimer>
  <base-disclaimer-title>
    Из руководства Python 3 <a target="_blank" href="https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions">tutorial</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Генераторы списков предоставляют краткий способ создания списков. [...] или для создания подпоследовательности тех элементов, которые удовлетворяют определенному условию.
  </base-disclaimer-content>
</base-disclaimer>

Прочтите <router-link to="/blog/python-comprehensions-step-by-step">Python Comprehensions: A step by step Introduction</router-link> для более подробного введения.

## Генератор списка (List comprehension)

Вот как мы создаем новый список из существующей коллекции с помощью цикла `For Loop`:

```python
# Традиционный подход: создание списка с помощью цикла for
names = ['Charles', 'Susan', 'Patrick', 'George']

new_list = []
for n in names:
    new_list.append(n)

new_list
```

```output
['Charles', 'Susan', 'Patrick', 'George']
```

А вот как мы делаем то же самое с помощью генератора списка (List Comprehension):

```python
# Генератор списка: краткий способ создания нового списка
# Синтаксис: [expression for item in iterable]
names = ['Charles', 'Susan', 'Patrick', 'George']

new_list = [n for n in names]  # Создать список со всеми именами
new_list
```

```output
['Charles', 'Susan', 'Patrick', 'George']
```

<BaseQuiz id="cheatsheet-comprehensions-1" correct="A">
<template #question>
What is the basic syntax of a list comprehension?
</template>

<BaseQuizOption value="A" correct>A. <code>[expression for item in iterable]</code></BaseQuizOption>
<BaseQuizOption value="B">B. <code>(expression for item in iterable)</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>{expression for item in iterable}</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>expression for item in iterable</code></BaseQuizOption>
<BaseQuizAnswer>List comprehensions use square brackets <code>[]</code> with the syntax <code>[expression for item in iterable]</code>. This creates a new list by applying the expression to each item.</BaseQuizAnswer>
</BaseQuiz>

Мы можем сделать то же самое с числами:

```python
# Вложенный генератор списка: создание кортежей из двух диапазонов
# Эквивалентно вложенным циклам for
n = [(a, b) for a in range(1, 3) for b in range(1, 3)]
n
```

```output
[(1, 1), (1, 2), (2, 1), (2, 2)]
```

## Добавление условий

Если мы хотим, чтобы `new_list` содержал только имена, начинающиеся с 'C', с помощью цикла `for` мы бы сделали это так:

```python
# Традиционный подход: фильтрация с условием if
names = ['Charles', 'Susan', 'Patrick', 'George', 'Carol']

new_list = []
for n in names:
    if n.startswith('C'):  # Фильтрация имен, начинающихся с 'C'
        new_list.append(n)

print(new_list)
```

```output
['Charles', 'Carol']
```

В генераторе списка мы добавляем оператор `if` в конец:

```python
# Генератор списка с условием: фильтрация элементов
# Синтаксис: [expression for item in iterable if condition]
new_list = [n for n in names if n.startswith('C')]
print(new_list)
```

```output
['Charles', 'Carol']
```

<BaseQuiz id="cheatsheet-comprehensions-2" correct="B">
<template #question>
Where does the <code>if</code> condition go in a list comprehension?
</template>

<BaseQuizOption value="A">A. Before the <code>for</code> keyword</BaseQuizOption>
<BaseQuizOption value="B" correct>B. After the <code>for</code> clause</BaseQuizOption>
<BaseQuizOption value="C">C. Inside the expression</BaseQuizOption>
<BaseQuizOption value="D">D. Before the square brackets</BaseQuizOption>
<BaseQuizAnswer>In a list comprehension, the <code>if</code> condition comes after the <code>for</code> clause: <code>[expression for item in iterable if condition]</code>. This filters items based on the condition.</BaseQuizAnswer>
</BaseQuiz>

Чтобы использовать оператор `if-else` в генераторе списка:

```python
# Генератор списка с if-else: условное выражение
# Синтаксис: [expression_if_true if condition else expression_if_false for item in iterable]
nums = [1, 2, 3, 4, 5, 6]
new_list = [num*2 if num % 2 == 0 else num for num in nums]  # Удвоить четные числа
print(new_list)
```

```output
[1, 4, 3, 8, 5, 12]
```

<base-disclaimer>
  <base-disclaimer-title>
    Генераторы множеств и словарей (Set and Dict comprehensions)
  </base-disclaimer-title>
  <base-disclaimer-content>
    Основы генераторов списков также применимы к <b>множествам</b> (sets) и <b>словарям</b> (dictionaries).
  </base-disclaimer-content>
</base-disclaimer>

## Генератор множества (Set comprehension)

```python
# Генератор множества: создание множества с использованием синтаксиса генератора
# Синтаксис: {expression for item in iterable}
b = {"abc", "def"}
{s.upper() for s in b}  # Преобразовать все строки в верхний регистр
```

```output
{"ABC", "DEF"}
```

## Генератор словаря (Dict comprehension)

```python
# Генератор словаря: поменять местами ключи и значения
# Синтаксис: {key_expression: value_expression for item in iterable}
c = {'name': 'Pooka', 'age': 5}
{v: k for k, v in c.items()}  # Поменять местами пары ключ-значение
```

```output
{'Pooka': 'name', 5: 'age'}
```

<BaseQuiz id="cheatsheet-comprehensions-3" correct="C">
<template #question>
What syntax is used for dictionary comprehensions?
</template>

<BaseQuizOption value="A">A. <code>[key: value for item in iterable]</code></BaseQuizOption>
<BaseQuizOption value="B">B. <code>(key: value for item in iterable)</code></BaseQuizOption>
<BaseQuizOption value="C" correct>C. <code>{key_expression: value_expression for item in iterable}</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>{key, value for item in iterable}</code></BaseQuizOption>
<BaseQuizAnswer>Dictionary comprehensions use curly braces <code>{}</code> with the syntax <code>{key_expression: value_expression for item in iterable}</code>, similar to list comprehensions but with key-value pairs.</BaseQuizAnswer>
</BaseQuiz>

Генератор списка может быть создан из словаря:

```python
# Генератор списка из словаря: создание отформатированных строк
c = {'name': 'Pooka', 'age': 5}
["{}:{}".format(k.upper(), v) for k, v in c.items()]  # Формат как "KEY:value"
```

```output
['NAME:Pooka', 'AGE:5']
```

## Связанные ссылки

- <router-link to="/blog/python-comprehensions-step-by-step">Python Comprehensions: A step by step Introduction</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Python Lists and Tuples</router-link>
- <router-link to="/cheatsheet/sets">Python Sets</router-link>
- <router-link to="/cheatsheet/dictionaries">Python Dictionaries</router-link>
- <router-link to="/blog/python-sets-what-why-how">Python Sets: What, Why and How</router-link>
- <router-link to="/blog/python-data-types">Python Data Types Blog Post</router-link>
