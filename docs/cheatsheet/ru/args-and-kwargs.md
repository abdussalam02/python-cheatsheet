---
title: 'Python Args и Kwargs – Шпаргалка по Python'
description: 'Args и kwargs могут показаться сложными, но на самом деле их легко понять. Они придают функциям гибкость и улучшают читаемость кода.'
labUrl: 'https://labex.io/ru/labs/python-python-args-and-kwargs-633646?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Аргументы и Kwargs Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a href="https://docs.python.org/3/tutorial/index.html">Python args and kwargs Made Easy</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    <code>*args</code> и <code>**kwargs</code> могут показаться пугающими, но правда в том, что их не так уж сложно понять, и они могут наделить ваши функции большой гибкостью.
  </base-disclaimer-content>
</base-disclaimer>

Прочтите статью <router-link to="/blog/python-easy-args-kwargs">Python \*args и \*\*kwargs Made Easy</router-link> для более глубокого введения.

## Args и Kwargs

`*args` и `**kwargs` позволяют передавать неопределенное количество позиционных и именованных аргументов при вызове функции.

```python
# Define a function that accepts any number of positional and keyword arguments
def some_function(*args, **kwargs):
    pass

# Call with any number of positional arguments
some_function(arg1, arg2, arg3)

# Call with any number of keyword arguments
some_function(key1=arg1, key2=arg2, key3=arg3)

# Call with both positional and keyword arguments
some_function(arg, key1=arg1)

# Or call with no arguments at all
some_function()
```

<base-warning>
  <base-warning-title>
    Python conventions
  </base-warning-title>
  <base-warning-content>
    Слова <code>*args</code> и <code>**kwargs</code> являются соглашениями. Они не навязываются интерпретатором, но считаются хорошей практикой в сообществе Python.
  </base-warning-content>
</base-warning>

## args

Вы можете получить доступ к _аргументам_ через переменную `args`:

```python
# *args collects positional arguments into a tuple
def some_function(*args):
    print(f'Arguments passed: {args} as {type(args)}')

# Pass multiple arguments - they'll be collected into args tuple
some_function('arg1', 'arg2', 'arg3')
```

```output
Arguments passed: ('arg1', 'arg2', 'arg3') as <class 'tuple'>
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
В какой тип данных собираются аргументы <code>*args</code>?
</template>

<base-quiz-option value="A">A. Список</base-quiz-option>
<base-quiz-option value="B" correct>B. Кортеж (tuple)</base-quiz-option>
<base-quiz-option value="C">C. Словарь</base-quiz-option>
<base-quiz-option value="D">D. Множество (set)</base-quiz-option>
<base-quiz-answer value="B">Параметр <code>\*args</code> собирает позиционные аргументы в кортеж. Это позволяет функции принимать любое количество позиционных аргументов.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## kwargs

Именованные аргументы (keywords) доступны через переменную `kwargs`:

```python
# **kwargs collects keyword arguments into a dictionary
def some_function(**kwargs):
    print(f'keywords: {kwargs} as {type(kwargs)}')

# Pass keyword arguments - they'll be collected into kwargs dict
some_function(key1='arg1', key2='arg2')
```

```output
keywords: {'key1': 'arg1', 'key2': 'arg2'} as <class 'dict'>
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
В какой тип данных собираются аргументы <code>**kwargs</code>?
</template>

<base-quiz-option value="A">A. Список</base-quiz-option>
<base-quiz-option value="B">B. Кортеж (tuple)</base-quiz-option>
<base-quiz-option value="C" correct>C. Словарь</base-quiz-option>
<base-quiz-option value="D">D. Множество (set)</base-quiz-option>
<base-quiz-answer value="C">Параметр <code>\*\*kwargs</code> собирает именованные аргументы в словарь. Это позволяет функции принимать любое количество именованных аргументов.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Relevant links

- <router-link to="/cheatsheet/functions">Функции</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Списки и Кортежи</router-link>
- <router-link to="/cheatsheet/dictionaries">Словари Python</router-link>
- <router-link to="/blog/python-easy-args-kwargs">Python \*args и \*\*kwargs Made Easy</router-link>
- <router-link to="/builtin/tuple">tuple()</router-link>
- <router-link to="/builtin/dict">dict()</router-link>
