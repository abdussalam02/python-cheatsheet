---
title: 'Обработка исключений Python - Шпаргалка по Python'
description: 'В Python обработка исключений — это процесс реагирования на возникновение исключений.'
labUrl: 'https://labex.io/ru/labs/python-python-exception-handling-633656?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Обработка исключений в Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikipedia.org/wiki/Exception_handling">Обработка исключений</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    В вычислениях и компьютерном программировании обработка исключений — это процесс реагирования на возникновение исключений — аномальных или исключительных условий, требующих специальной обработки.
  </base-disclaimer-content>
</base-disclaimer>

В Python есть много [встроенных исключений](https://docs.python.org/3/library/exceptions.html), которые вызываются, когда программа сталкивается с ошибкой, и большинство внешних библиотек, таких как популярная [Requests](https://requests.readthedocs.io/en/latest), включают свои [пользовательские исключения](https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions), с которыми нам придется иметь дело.

## Базовая обработка исключений

Нельзя делить на ноль, это математическая истина, и если вы попытаетесь сделать это в Python, интерпретатор вызовет встроенное исключение [ZeroDivisionError](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError):

```python
def divide(dividend , divisor):
    print(dividend / divisor)

divide(dividend=10, divisor=5)
```

```output
2
```

```python
divide(dividend=10, divisor=0)
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

Предположим, мы не хотим, чтобы наше выполнение программы останавливалось или чтобы пользователю выводился непонятный ему результат. Скажем, мы хотим напечатать полезное и понятное сообщение, тогда нам нужно **_обработать_** исключение с помощью ключевых слов `try` и `except`:

```python
# try-except: обрабатывать исключения корректно
def divide(dividend , divisor):
    try:  # Попытаться выполнить этот код
        print(dividend / divisor)
    except ZeroDivisionError:  # Перехватить конкретный тип исключения
        print('You can not divide by 0')

divide(dividend=10, divisor=5)
```

```output
2
```

```python
divide(dividend=10, divisor=0)
```

```output
You can not divide by 0
```

<BaseQuiz id="cheatsheet-exception-handling-1" correct="A">
<template #question>
Какие ключевые слова используются для обработки исключений в Python?
</template>

<BaseQuizOption value="A" correct>A. <code>try</code> и <code>except</code></BaseQuizOption>
<BaseQuizOption value="B">B. <code>catch</code> и <code>handle</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>error</code> и <code>rescue</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>if</code> и <code>else</code></BaseQuizOption>
<BaseQuizAnswer>Python использует <code>try</code> для обозначения кода, который может вызвать исключение, и <code>except</code> для обработки конкретных возникающих исключений.</BaseQuizAnswer>
</BaseQuiz>

## Обработка нескольких исключений с помощью одного блока исключений

Вы также можете обрабатывать несколько исключений в одной строке, как показано ниже, без необходимости создавать несколько блоков исключений.

```python
# Обработка нескольких исключений в одном блоке except
def divide(dividend , divisor):
    try:
        if (dividend == 10):
          var = 'str' + 1  # Это вызовет TypeError
        else:
          print(dividend / divisor)
    except (ZeroDivisionError, TypeError) as error:  # Перехват нескольких типов исключений
        print(error)  # Вывод сообщения об ошибке

divide(dividend=20, divisor=5)
```

```output
4
```

```python
divide(dividend=10, divisor=5)
```

```output
can only concatenate str (not "int") to str
```

```python
divide(dividend=10, divisor=0)
```

```output
division by zero
```

<BaseQuiz id="cheatsheet-exception-handling-2" correct="B">
<template #question>
Можно ли обрабатывать несколько типов исключений в одном блоке <code>except</code>?
</template>

<BaseQuizOption value="A">A. Нет, для каждого типа исключения необходимо использовать отдельные блоки <code>except</code></BaseQuizOption>
<BaseQuizOption value="B" correct>B. Да, поместив их в кортеж, например <code>except (Exception1, Exception2)</code></BaseQuizOption>
<BaseQuizOption value="C">C. Да, но только если они связаны</BaseQuizOption>
<BaseQuizOption value="D">D. Нет, Python этого не поддерживает</BaseQuizOption>
<BaseQuizAnswer>Вы можете обрабатывать несколько типов исключений в одном блоке <code>except</code>, поместив их в кортеж: <code>except (ZeroDivisionError, TypeError) as error:</code></BaseQuizAnswer>
</BaseQuiz>

## Код finally при обработке исключений

Код внутри секции `finally` всегда выполняется, независимо от того, было ли вызвано исключение или нет:

```python
# Блок finally: выполняется всегда, независимо от исключений
def divide(dividend , divisor):
    try:
        print(dividend / divisor)
    except ZeroDivisionError:
        print('You can not divide by 0')
    finally:  # Выполняется всегда, даже если произошло исключение
        print('Execution finished')

divide(dividend=10, divisor=5)
```

```output
2.0
Execution finished
```

```python
divide(dividend=10, divisor=0)
```

```output
You can not divide by 0
Execution finished
```

<BaseQuiz id="cheatsheet-exception-handling-3" correct="C">
<template #question>
Когда выполняется блок <code>finally</code>?
</template>

<BaseQuizOption value="A">A. Только когда возникает исключение</BaseQuizOption>
<BaseQuizOption value="B">B. Только когда исключение не возникает</BaseQuizOption>
<BaseQuizOption value="C" correct>C. Всегда, независимо от того, произошло исключение или нет</BaseQuizOption>
<BaseQuizOption value="D">D. Никогда</BaseQuizOption>
<BaseQuizAnswer>Блок <code>finally</code> выполняется всегда, независимо от того, произошло исключение или нет. Он полезен для кода очистки, который должен быть выполнен независимо от результата.</BaseQuizAnswer>
</BaseQuiz>

## Пользовательские исключения

Пользовательские исключения инициализируются путем создания `class`, который наследуется от базового класса `Exception` Python, и вызываются с помощью ключевого слова `raise`:

```python
# Пользовательское исключение: создается путем наследования от класса Exception
class MyCustomException(Exception):
    pass

raise MyCustomException  # Вызов пользовательского исключения
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyCustomException
```

Чтобы объявить сообщение пользовательского исключения, вы можете передать его в качестве параметра:

```python
class MyCustomException(Exception):
    pass

raise MyCustomException('A custom message for my custom exception')
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyCustomException: A custom message for my custom exception
```

Обработка пользовательского исключения такая же, как и любой другой:

```python
try:
    raise MyCustomException('A custom message for my custom exception')
except MyCustomException:
    print('My custom exception was raised')
```

```output
My custom exception was raised
```

<BaseQuiz id="cheatsheet-exception-handling-4" correct="A">
<template #question>
Как создать пользовательское исключение в Python?
</template>

<BaseQuizOption value="A" correct>A. Создать класс, который наследуется от класса <code>Exception</code></BaseQuizOption>
<BaseQuizOption value="B">B. Использовать декоратор <code>@exception</code></BaseQuizOption>
<BaseQuizOption value="C">C. Вызвать <code>Exception.create()</code></BaseQuizOption>
<BaseQuizOption value="D">D. Импортировать его из специального модуля</BaseQuizOption>
<BaseQuizAnswer>Пользовательские исключения создаются путем определения класса, который наследуется от базового класса <code>Exception</code>. Затем их можно вызывать и обрабатывать так же, как и встроенные исключения.</BaseQuizAnswer>
</BaseQuiz>

## Соответствующие ссылки

- <router-link to="/cheatsheet/control-flow">Control Flow</router-link>
- <router-link to="/builtin/breakpoint">breakpoint()</router-link>
- <router-link to="/builtin/isinstance">isinstance()</router-link>
- <router-link to="/builtin/issubclass">issubclass()</router-link>
