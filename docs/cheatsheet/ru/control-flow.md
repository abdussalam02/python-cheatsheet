---
title: 'Управление потоком Python - Шпаргалка по Python'
description: 'Управление потоком — это порядок, в котором выполняются или оцениваются отдельные операторы, инструкции или вызовы функций. Управление потоком программы Python регулируется условными операторами, циклами и вызовами функций.'
labUrl: 'https://labex.io/ru/labs/python-python-control-flow-633651?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Управление потоком Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    Управление потоком Python
  </base-disclaimer-title>
  <base-disclaimer-content>
  Управление потоком — это порядок, в котором выполняются или оцениваются отдельные операторы, инструкции или вызовы функций. Управление потоком программы Python регулируется условными операторами, циклами и вызовами функций.
  </base-disclaimer-content>
</base-disclaimer>

## Операторы сравнения

| Оператор | Значение         |
| -------- | ---------------- |
| `==`     | Равно            |
| `!=`     | Не равно         |
| `<`      | Меньше чем       |
| `>`      | Больше чем       |
| `<=`     | Меньше или равно |
| `>=`     | Больше или равно |

Эти операторы возвращают `True` или `False` в зависимости от предоставленных вами значений.

Примеры:

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

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Чему равно выражение <code>'hello' == 'Hello'</code>?
</template>

<base-quiz-option value="A">A. <code>True</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>False</code></base-quiz-option>
<base-quiz-option value="C">C. <code>None</code></base-quiz-option>
<base-quiz-option value="D">D. Вызывает ошибку</base-quiz-option>
<base-quiz-answer value="B">Сравнение строк в Python чувствительно к регистру. <code>'hello'</code> и <code>'Hello'</code> — разные строки, поэтому сравнение возвращает <code>False</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Логические операторы

Существует три логических оператора: `and`, `or` и `not`.
В порядке приоритета, от высшего к низшему: `not`, `and` и `or`.

Таблица истинности для оператора `and`:

| Выражение         | Возвращает |
| ----------------- | ---------- |
| `True and True`   | `True`     |
| `True and False`  | `False`    |
| `False and True`  | `False`    |
| `False and False` | `False`    |

Таблица истинности для оператора `or`:

| Выражение        | Возвращает |
| ---------------- | ---------- |
| `True or True`   | `True`     |
| `True or False`  | `True`     |
| `False or True`  | `True`     |
| `False or False` | `False`    |

Таблица истинности для оператора `not`:

| Выражение   | Возвращает |
| ----------- | ---------- |
| `not True`  | `False`    |
| `not False` | `True`     |

## Смешивание операторов

Вы можете смешивать логические операторы и операторы сравнения:

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

Вы также можете использовать несколько логических операторов в одном выражении вместе с операторами сравнения:

```python
2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
```

```output
True
```

```python
# В приведенном ниже операторе сначала выполняется 3 < 4 and 5 > 5, что дает False
# Затем 5 > 4 возвращает True, поэтому результат после True or False будет True
5 > 4 or 3 < 4 and 5 > 5
```

```output
True
```

```python
# Теперь сначала выполняется выражение в скобках, поэтому True and False возвращает False.
(5 > 4 or 3 < 4) and 5 > 5
```

```output
False
```

## Операторы if

Оператор `if` оценивает выражение, и если это выражение равно `True`, он выполняет следующий блок кода с отступом:

```python
# оператор if: выполнить блок кода, когда условие истинно
name = 'Debora'

if name == 'Debora':  # Проверить, равно ли имя 'Debora'
   print('Hi, Debora')  # Эта строка выполняется, если условие True
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

Оператор `else` выполняется только в том случае, если оценка выражений `if` и всех выражений `elif` равна `False`:

```python
# if-else: выполнить разный код в зависимости от условия
name = 'Debora'

if name == 'George':
   print('Hi, George.')
else:  # Выполняется, если условие if ложно
   print('You are not George')
```

```output
You are not George
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Когда выполняется блок <code>else</code> в операторе if-else?
</template>

<base-quiz-option value="A">A. Всегда</base-quiz-option>
<base-quiz-option value="B" correct>B. Только когда условие <code>if</code> (и все условия <code>elif</code>, если они есть) равны <code>False</code></base-quiz-option>
<base-quiz-option value="C">C. Только когда условие <code>if</code> равно <code>True</code></base-quiz-option>
<base-quiz-option value="D">D. Никогда</base-quiz-option>
<base-quiz-answer value="B">Блок <code>else</code> выполняется только тогда, когда условие <code>if</code> и все условия <code>elif</code> (если таковые имеются) оцениваются как <code>False</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Только после того, как выражение оператора `if` окажется `False`, оператор `elif` будет оценен и выполнен:

```python
# if-elif: проверка нескольких условий по порядку
name = 'George'

if name == 'Debora':
   print('Hi Debora!')
elif name == 'George':  # Проверяется, только если предыдущее условие ложно
   print('Hi George!')
```

```output
Hi George!
```

части `elif` и `else` являются необязательными.

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

## Тернарный условный оператор

Многие языки программирования имеют тернарный оператор, который определяет условное выражение. Наиболее распространенное использование — создание краткого, простого оператора присваивания с условием. Другими словами, он предлагает однострочный код для вычисления первого выражения, если условие истинно, и в противном случае вычисляет второе выражение.

```plaintext
<expression1> if <condition> else <expression2>
```

Пример:

```python
age = 15

# этот оператор if:
if age < 18:
   print('kid')
else:
   print('adult')
```

```output
kid
```

```python
# Тернарный оператор: однострочное условное выражение
# Синтаксис: значение_если_истинно if условие else значение_если_ложно
print('kid' if age < 18 else 'adult')
```

```output
kid
```

Тернарные операторы могут быть соединены в цепочку:

```python
age = 15

# этот тернарный оператор:
print('kid' if age < 13 else 'teen' if age < 18 else 'adult')
```

```output
teen
```

```python
# эквивалентен этому оператору if:
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

## Оператор Switch-Case

<base-disclaimer>
  <base-disclaimer-title>
    Операторы Switch-Case
  </base-disclaimer-title>
  <base-disclaimer-content>
  В языках программирования оператор switch — это тип механизма управления выбором, используемый для изменения потока управления выполнением программы путем поиска и сопоставления значения переменной или выражения.
  </base-disclaimer-content>
</base-disclaimer>

Операторы _Switch-Case_, или **Структурное сопоставление шаблонов (Structural Pattern Matching)**, были впервые представлены в 2020 году через [PEP 622](https://peps.python.org/pep-0622/) и официально выпущены с **Python 3.10** в сентябре 2022 года.

<base-disclaimer>
  <base-disclaimer-title>
    Официальное руководство
  </base-disclaimer-title>
  <base-disclaimer-content>
  [PEP 636](https://peps.python.org/pep-0636/) предоставляет официальное руководство по сопоставлению шаблонов Python или операторам Switch-Case.
  </base-disclaimer-content>
</base-disclaimer>

### Сопоставление отдельных значений

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

### Сопоставление с шаблоном или (or Pattern)

В этом примере символ вертикальной черты (`|` или `or`) позволяет Python возвращать один и тот же ответ для двух или более случаев.

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

### Сопоставление по длине итерируемого объекта

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

### Значение по умолчанию

Символ подчеркивания (`_`) используется для определения случая по умолчанию:

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

### Сопоставление встроенных классов

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

### Защита операторов Match-Case (Guarding)

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

## Операторы цикла while

Оператор while используется для повторяющегося выполнения до тех пор, пока выражение истинно:

```python
# цикл while: повторять код, пока условие истинно
spam = 0
while spam < 5:  # Продолжать, пока spam меньше 5
    print('Hello, world.')
    spam = spam + 1  # Увеличить счетчик, чтобы избежать бесконечного цикла
```

```output
Hello, world.
Hello, world.
Hello, world.
Hello, world.
Hello, world.
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Что делает цикл <code>while</code>?
</template>

<base-quiz-option value="A" correct>A. Повторяет код, пока условие <code>True</code></base-quiz-option>
<base-quiz-option value="B">B. Выполняет код ровно один раз</base-quiz-option>
<base-quiz-option value="C">C. Выполняет код фиксированное количество раз</base-quiz-option>
<base-quiz-option value="D">D. Пропускает выполнение кода</base-quiz-option>
<base-quiz-answer value="A">Цикл <code>while</code> многократно выполняет блок кода, пока условие оценивается как <code>True</code>. Когда условие становится <code>False</code>, цикл останавливается.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Операторы break

Если выполнение достигает оператора `break`, оно немедленно выходит из блока цикла `while`:

```python
# оператор break: немедленно выйти из цикла при обнаружении
while True:  # Бесконечный цикл
    name = input('Please type your name: ')
    if name == 'your name':
        break  # Немедленно выйти из цикла

print('Thank you!')
```

```output
Please type your name: your name
Thank you!
```

## Операторы continue

Когда выполнение программы достигает оператора `continue`, выполнение программы немедленно переходит к началу цикла.

```python
# оператор continue: пропустить оставшуюся часть итерации цикла и начать следующую итерацию
while True:
    name = input('Who are you? ')
    if name != 'Joe':
        continue  # Перейти к следующей итерации, не запрашивать пароль
    password = input('Password? (It is a fish.): ')
    if password == 'swordfish':
        break  # Выйти из цикла, когда пароль верен

print('Access granted.')
```

```output
Who are you? Charles
Who are you? Debora
Who are you? Joe
Password? (It is a fish.): swordfish
Access granted.
```

## Цикл For

Цикл `for` перебирает `list`, `tuple`, `dictionary`, `set` или `string`:

```python
# цикл for: итерация по каждому элементу в последовательности
pets = ['Bella', 'Milo', 'Loki']
for pet in pets:  # Цикл по каждому питомцу в списке
    print(pet)  # Печать имени каждого питомца
```

```output
Bella
Milo
Loki
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
Что перебирает цикл <code>for</code>?
</template>

<base-quiz-option value="A">A. Только числа</base-quiz-option>
<base-quiz-option value="B">B. Только строки</base-quiz-option>
<base-quiz-option value="C" correct>C. Любая итерируемая последовательность (список, кортеж, словарь, множество и т. д.)</base-quiz-option>
<base-quiz-option value="D">D. Только списки</base-quiz-option>
<base-quiz-answer value="C">Цикл <code>for</code> может перебирать любую итерируемую последовательность, включая списки, кортежи, словари, множества, строки и другие итерируемые объекты.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Функция range()

Функция `range()` возвращает последовательность чисел. Она начинается с 0, увеличивается на 1 и останавливается перед указанным числом:

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

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Что генерирует <code>range(5)</code>?
</template>

<base-quiz-option value="A">A. Числа от 1 до 5</base-quiz-option>
<base-quiz-option value="B" correct>B. Числа от 0 до 4</base-quiz-option>
<base-quiz-option value="C">C. Числа от 0 до 5</base-quiz-option>
<base-quiz-option value="D">D. Пять случайных чисел</base-quiz-option>
<base-quiz-answer value="B">Функция <code>range(5)</code> генерирует числа от 0 до 4 (всего 5 чисел). Конечное значение не включается, поэтому она останавливается, не достигая 5.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Функция `range()` также может изменять свои 3 значения по умолчанию. Первые два будут значениями `start` (начало) и `stop` (конец), а третье будет аргументом `step` (шаг). Шаг — это величина, на которую увеличивается переменная после каждой итерации.

```python
# range(start, stop, step)
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

Вы даже можете использовать отрицательное число в качестве аргумента `step`, чтобы цикл `for` считал в обратном порядке, а не по возрастанию.

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

## Оператор For else

Это позволяет указать оператор для выполнения в случае полного выполнения цикла. Это полезно только тогда, когда в цикле может произойти условие `break`:

```python
for i in [1, 2, 3, 4, 5]:
   if i == 3:
       break
else:
   print("only executed when no item is equal to 3")
```

## Завершение программы с помощью sys.exit()

Функция `exit()` позволяет завершить работу Python.

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

## Связанные ссылки

- <router-link to="/cheatsheet/basics">Основы</router-link>
- <router-link to="/cheatsheet/functions">Функции</router-link>
- <router-link to="/cheatsheet/exception-handling">Обработка исключений</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Списки и кортежи</router-link>
- <router-link to="/cheatsheet/sets">Множества</router-link>
- <router-link to="/cheatsheet/dictionaries">Словари</router-link>
- <router-link to="/cheatsheet/comprehensions">Генераторы (Comprehensions)</router-link>
