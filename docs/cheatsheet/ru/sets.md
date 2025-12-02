---
title: 'Множества Python - Шпаргалка по Python'
description: 'Python оснащен несколькими встроенными типами данных для организации информации. Эти структуры включают списки, словари, кортежи и множества.'
labUrl: 'https://labex.io/ru/labs/python-python-sets-633665?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Множества Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Python оснащен несколькими встроенными типами данных, которые помогают нам организовывать наши данные. Эти структуры включают списки (lists), словари (dictionaries), кортежи (tuples) и **множества (sets)**.

<base-disclaimer>
  <base-disclaimer-title>
    Из <a target="_blank" href="https://docs.python.org/3/tutorial/datastructures.html#sets">документации Python 3</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Множество — это неупорядоченная коллекция без повторяющихся элементов. Основные варианты использования включают проверку членства и устранение дублирующихся записей.
  </base-disclaimer-content>
</base-disclaimer>

Прочтите <router-link to="/blog/python-sets-what-why-how">Python Sets: What, Why and How</router-link> для более глубокого справочного материала.

## Инициализация множества

Существует два способа создания множеств: с использованием фигурных скобок `{}` и встроенной функции `set()`.

<base-warning>
  <base-warning-title>
    Пустые множества
  </base-warning-title>
  <base-warning-content>
    При создании множества убедитесь, что вы не используете пустые фигурные скобки <code>{}</code>, иначе вместо множества вы получите пустой словарь.
  </base-warning-content>
</base-warning>

```python
# Create set using curly braces or set() function
s = {1, 2, 3}  # Using curly braces
s = set([1, 2, 3])  # Using set() constructor

# Warning: empty {} creates a dictionary, not a set
s = {}  # this will create a dictionary instead of a set
type(s)  # Returns <class 'dict'>
```

```output
<class 'dict'>
```

## Неупорядоченные коллекции уникальных элементов

Множество автоматически удаляет все повторяющиеся значения.

```python
# Sets automatically remove duplicates
s = {1, 2, 3, 2, 3, 4}  # Duplicates are removed
s  # Returns {1, 2, 3, 4}
```

```output
{1, 2, 3, 4}
```

<BaseQuiz id="cheatsheet-sets-1" correct="A">
<template #question>
What happens when you create a set with duplicate values?
</template>

<BaseQuizOption value="A" correct>A. Duplicates are automatically removed</BaseQuizOption>
<BaseQuizOption value="B">B. An error is raised</BaseQuizOption>
<BaseQuizOption value="C">C. The set keeps all duplicates</BaseQuizOption>
<BaseQuizOption value="D">D. Only the first occurrence is kept</BaseQuizOption>
<BaseQuizAnswer>Sets automatically remove duplicate values. A set is an unordered collection with no duplicate elements.</BaseQuizAnswer>
</BaseQuiz>

И как неупорядоченный тип данных, они не могут быть проиндексированы.

```python
s = {1, 2, 3}
s[0]
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
```

## Добавление и обновление множества (set add and update)

Используя метод `add()`, мы можем добавить один элемент в множество.

```python
# add() method: add a single element to the set
s = {1, 2, 3}
s.add(4)  # Add element 4
s
```

```output
{1, 2, 3, 4}
```

А с помощью `update()` можно добавить несколько элементов:

```python
# update() method: add multiple elements from an iterable
s = {1, 2, 3}
s.update([2, 3, 4, 5, 6])  # Add multiple elements (duplicates ignored)
s
```

```output
{1, 2, 3, 4, 5, 6}
```

## Удаление элемента из множества (set remove and discard)

Оба метода удалят элемент из множества, но `remove()` вызовет ошибку `key error`, если значение не существует.

```python
# remove() method: remove element, raises KeyError if not found
s = {1, 2, 3}
s.remove(3)  # Remove element 3
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

`discard()` не вызовет никаких ошибок.

```python
# discard() method: remove element, no error if not found
s = {1, 2, 3}
s.discard(3)  # Remove element 3 (safe, no error if missing)
s
```

```output
{1, 2}
```

```python
s.discard(3)
```

<BaseQuiz id="cheatsheet-sets-2" correct="C">
<template #question>
What is the difference between <code>remove()</code> and <code>discard()</code> methods for sets?
</template>

<BaseQuizOption value="A">A. <code>remove()</code> removes one element, <code>discard()</code> removes all</BaseQuizOption>
<BaseQuizOption value="B">B. There is no difference</BaseQuizOption>
<BaseQuizOption value="C" correct>C. <code>remove()</code> raises an error if element doesn't exist, <code>discard()</code> does not</BaseQuizOption>
<BaseQuizOption value="D">D. <code>remove()</code> is faster</BaseQuizOption>
<BaseQuizAnswer>Both methods remove an element from a set, but <code>remove()</code> raises a <code>KeyError</code> if the element doesn't exist, while <code>discard()</code> does nothing if the element is missing.</BaseQuizAnswer>
</BaseQuiz>

## Объединение множеств (set union)

`union()` или `|` создаст новое множество со всеми элементами из предоставленных множеств.

```python
# union(): combine all elements from multiple sets (no duplicates)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.union(s2)  # or 's1 | s2' - returns {1, 2, 3, 4, 5}
```

```output
{1, 2, 3, 4, 5}
```

## Пересечение множеств (set intersection)

`intersection()` или `&` вернет множество, содержащее только те элементы, которые являются общими для всех множеств.

```python
# intersection(): return elements common to all sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
s1.intersection(s2, s3)  # or 's1 & s2 & s3' - returns {3}
```

```output
{3}
```

<BaseQuiz id="cheatsheet-sets-3" correct="B">
<template #question>
What does <code>intersection()</code> return for sets?
</template>

<BaseQuizOption value="A">A. All elements from all sets</BaseQuizOption>
<BaseQuizOption value="B" correct>B. Only elements that are common to all sets</BaseQuizOption>
<BaseQuizOption value="C">C. Elements in the first set but not in others</BaseQuizOption>
<BaseQuizOption value="D">D. Elements in either set but not both</BaseQuizOption>
<BaseQuizAnswer>The <code>intersection()</code> method returns a set containing only elements that are present in all the sets being compared.</BaseQuizAnswer>
</BaseQuiz>

## Разность множеств (set difference)

`difference()` или `-` вернет только те элементы, которые уникальны для первого множества (множества, к которому применяется метод).

```python
# difference(): return elements in first set but not in others
s1 = {1, 2, 3}
s2 = {2, 3, 4}

s1.difference(s2)  # or 's1 - s2' - returns {1}
```

```output
{1}
```

```python
s2.difference(s1) # or 's2 - s1'
```

```output
{4}
```

## Симметричная разность множеств (set symmetric_difference)

`symmetric_difference()` или `^` вернет все элементы, которые не являются общими для множеств.

```python
# symmetric_difference(): return elements in either set, but not both
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1.symmetric_difference(s2)  # or 's1 ^ s2' - returns {1, 4}
```

```output
{1, 4}
```

<BaseQuiz id="cheatsheet-sets-4" correct="D">
<template #question>
What does <code>symmetric_difference()</code> return for two sets?
</template>

<BaseQuizOption value="A">A. All elements from both sets</BaseQuizOption>
<BaseQuizOption value="B">B. Only elements common to both sets</BaseQuizOption>
<BaseQuizOption value="C">C. Elements in the first set but not in the second</BaseQuizOption>
<BaseQuizOption value="D" correct>D. Elements in either set, but not in both</BaseQuizOption>
<BaseQuizAnswer>The <code>symmetric_difference()</code> method returns a set containing elements that are in either set, but not in both sets.</BaseQuizAnswer>
</BaseQuiz>

## Связанные ссылки

- <router-link to="/blog/python-data-types">Python Data Types Blog Post</router-link>
- <router-link to="/blog/python-sets-what-why-how">Python Sets: What, Why and How</router-link>
- <router-link to="/cheatsheet/dictionaries">Python Dictionaries</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Python Lists and Tuples</router-link>
