---
title: 'Декораторы Python - Шпаргалка по Python'
description: 'Декоратор Python — это синтаксис, обеспечивающий краткий и многократно используемый способ расширения функциональности функции или класса.'
labUrl: 'https://labex.io/ru/labs/python-python-decorators-633654?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Декораторы Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Декоратор Python предоставляет лаконичный и многократно используемый способ расширения
функции или класса. Прочтите сопутствующую статью <router-link to="/blog/python-decorators-for-beginners">Декораторы Python: Простые шаблоны для улучшения вашего кода</router-link> для практических примеров и шаблонов.

## Базовый декоратор

Декоратор в своей простейшей форме — это функция, которая принимает другую
функцию в качестве аргумента и возвращает обертку (wrapper). Следующий пример
показывает создание декоратора и его использование.

```python
# Декоратор: функция, которая принимает другую функцию и возвращает обертку
def your_decorator(func):
  def wrapper():
    # Сделать что-то до вызова func...
    print("Before func!")
    func()  # Вызвать исходную функцию
    # Сделать что-то после вызова func...
    print("After func!")
  return wrapper  # Вернуть функцию-обертку

# @your_decorator — это синтаксический сахар для: foo = your_decorator(foo)
@your_decorator
def foo():
  print("Hello World!")

foo()  # Вызывает wrapper, который вызывает foo с дополнительным поведением
```

```output
Before func!
Hello World!
After func!
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-decorators-1">
<template #question>
Что такое декоратор в Python?
</template>

<base-quiz-option value="A" correct>A. Функция, которая принимает другую функцию и возвращает функцию-обертку</base-quiz-option>
<base-quiz-option value="B">B. Особый тип класса</base-quiz-option>
<base-quiz-option value="C">C. Встроенное ключевое слово Python</base-quiz-option>
<base-quiz-option value="D">D. Способ удаления функций</base-quiz-option>
<base-quiz-answer value="A">Декоратор — это функция, которая принимает другую функцию в качестве аргумента и возвращает функцию-обертку. Синтаксис <code>@</code> является синтаксическим сахаром, который применяет декоратор к функции.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Декоратор для функции с параметрами

```python
# Декоратор, который работает с функциями, имеющими параметры
def your_decorator(func):
  def wrapper(*args,**kwargs):  # Принимает любые аргументы
    # Сделать что-то до вызова func...
    print("Before func!")
    func(*args,**kwargs)  # Передать аргументы исходной функции
    # Сделать что-то после вызова func...
    print("After func!")
  return wrapper

@your_decorator
def foo(bar):
  print("My name is " + bar)

foo("Jack")  # Аргументы передаются через wrapper
```

```output
Before func!
My name is Jack
After func!
```

## Шаблон для базового декоратора

Этот шаблон полезен для большинства вариантов использования декораторов. Он применим к функциям
с параметрами или без них, а также с возвращаемым значением или без него.

```python
import functools

# Шаблон декоратора с лучшими практиками: сохраняет метаданные функции и возвращаемое значение
def your_decorator(func):
  @functools.wraps(func)  # Сохраняет имя функции, docstring и т. д.
  def wrapper(*args,**kwargs):
    # Сделать что-то до вызова func...
    result = func(*args,**kwargs)  # Вызвать функцию и захватить возвращаемое значение
    # Сделать что-то после вызова func..
    return result  # Вернуть возвращаемое значение исходной функции
  return wrapper
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-decorators-2">
<template #question>
Что делает <code>@functools.wraps(func)</code> в декораторе?
</template>

<base-quiz-option value="A">A. Заставляет декоратор выполняться быстрее</base-quiz-option>
<base-quiz-option value="B" correct>B. Сохраняет метаданные исходной функции (имя, docstring и т. д.)</base-quiz-option>
<base-quiz-option value="C">C. Предотвращает вызов функции</base-quiz-option>
<base-quiz-option value="D">D. Преобразует функцию в класс</base-quiz-option>
<base-quiz-answer value="B">Декоратор <code>@functools.wraps(func)</code> сохраняет метаданные исходной функции (такие как ее имя и docstring) в функции-обертке. Это считается лучшей практикой при написании декораторов.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Декоратор с параметрами

Вы также можете определить параметры для использования декоратором.

```python
import functools

# Фабрика декораторов: возвращает декоратор на основе параметров
def your_decorator(arg):
  def decorator(func):
    @functools.wraps(func)  # Сохранить метаданные функции
    def wrapper(*args,**kwargs):
      # Сделать что-то до вызова func, возможно, используя arg...
      result = func(*args,**kwargs)
      # Сделать что-то после вызова func, возможно, используя arg...
      return result
    return wrapper
  return decorator  # Вернуть фактическую функцию-декоратор
```

Чтобы использовать этот декоратор:

```python
# Использование декоратора с параметрами: @your_decorator(arg='x') вызывает your_decorator('x')
# который возвращает декоратор, который затем применяется к foo
@your_decorator(arg = 'x')
def foo(bar):
  return bar
```

## Декораторы на основе классов

Чтобы декорировать метод класса, вы должны определить декоратор внутри класса. Когда
методу передается только неявный аргумент `self`, без каких-либо явных
дополнительных аргументов, вы должны создать отдельный декоратор только для этих методов
без каких-либо дополнительных аргументов. Пример этого показан ниже, когда вы хотите
перехватывать и выводить исключения определенным образом.

```python
# Декоратор метода класса: определяется внутри класса
class DecorateMyMethod:

  # Декоратор статического метода для методов, имеющих только параметр 'self'
  def decorator_for_class_method_with_no_args(method):
    def wrapper_for_class_method(self):  # Принимает только self
      try:
        return method(self)  # Вызвать исходный метод
      except Exception as e:
        print("\nWARNING: Please make note of the following:\n")
        print(e)
    return wrapper_for_class_method

  def __init__(self,succeed:bool):
    self.succeed = succeed

  @decorator_for_class_method_with_no_args
  def class_action(self):
    if self.succeed:
      print("You succeeded by choice.")
    else:
      raise Exception("Epic fail of your own creation.")

test_succeed = DecorateMyMethod(True)
test_succeed.class_action()
```

```output
You succeeded by choice.
```

```python
test_fail = DecorateMyMethod(False)
test_fail.class_action()
```

```output
Exception: Epic fail of your own creation.
```

Декоратор также может быть определен как класс вместо метода. Это полезно для
поддержания и обновления состояния, как в следующем примере, где мы подсчитываем
количество вызовов метода:

```python
# Декоратор на основе класса: поддерживает состояние между вызовами
class CountCallNumber:

  def __init__(self, func):
    self.func = func  # Сохранить декорируемую функцию
    self.call_number = 0  # Инициализировать счетчик вызовов

  def __call__(self, *args, **kwargs):  # Делает экземпляр вызываемым
    self.call_number += 1  # Увеличить счетчик
    print("This is execution number " + str(self.call_number))
    return self.func(*args, **kwargs)  # Вызвать исходную функцию

@CountCallNumber  # Создает экземпляр CountCallNumber
def say_hi(name):
  print("Hi! My name is " + name)

say_hi("Jack")  # Вызывает CountCallNumber.__call__()
```

```output
This is execution number 1
Hi! My name is Jack
```

```python
say_hi("James")
```

```output
This is execution number 2
Hi! My name is James
```

<base-disclaimer>
  <base-disclaimer-title>
    Пример подсчета
  </base-disclaimer-title>
  <base-disclaimer-content>
  Этот пример подсчета вдохновлен <a href="https://youtu.be/HGOBQPFzWKo?si=IUvFzeQbzTmeEgKV" target="_blank">видеоуроком Патрика Лобера на YouTube</a>.
  </base-disclaimer-content>
</base-disclaimer>

## Связанные ссылки

- <router-link to="/blog/python-decorators-for-beginners">Декораторы Python: Простые шаблоны для улучшения вашего кода</router-link>
- <router-link to="/blog/python-easy-args-kwargs">Python \*args и \*\*kwargs: Простое объяснение</router-link>
- <router-link to="/cheatsheet/functions">Функции</router-link>
- <router-link to="/cheatsheet/args-and-kwargs">Args и Kwargs</router-link>
- <router-link to="/builtin/classmethod">classmethod()</router-link>
- <router-link to="/builtin/staticmethod">staticmethod()</router-link>
- <router-link to="/builtin/property">property()</router-link>
- <router-link to="/builtin/callable">callable()</router-link>
