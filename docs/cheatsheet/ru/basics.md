---
title: 'Основы Python - Шпаргалка по Python'
description: 'Изучите основы Python с помощью нашего подробного руководства, охватывающего операторы, типы данных, переменные, функции и многое другое. Идеально подходит для начинающих, изучающих основы программирования на Python.'
labUrl: 'https://labex.io/ru/labs/python-python-basics-633647?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Основы Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Всем нам нужно с чего-то начинать, так почему бы не начать здесь. Это руководство охватывает фундаментальные основы Python, включая операторы, типы данных, переменные и основные функции.

<base-disclaimer>
<base-disclaimer-title>
Обзор основ Python
</base-disclaimer-title>
<base-disclaimer-content>
Основные основы Python, которые должен знать каждый новичок:

- Переменные и базовые типы
- Операторы и выражения
- Строки и общие методы
- Списки, кортежи и словари
- Базовый поток управления (if, for, while)
- Простые функции

</base-disclaimer-content>
</base-disclaimer>

## Математические операторы

От **наивысшего** к **низшему** приоритету:

| Операторы | Операция              | Пример          |
| --------- | --------------------- | --------------- |
| \*\*      | Возведение в степень  | `2 ** 3 = 8`    |
| %         | Остаток от деления    | `22 % 8 = 6`    |
| //        | Целочисленное деление | `22 // 8 = 2`   |
| /         | Деление               | `22 / 8 = 2.75` |
| \*        | Умножение             | `3 * 3 = 9`     |
| -         | Вычитание             | `5 - 2 = 3`     |
| +         | Сложение              | `2 + 2 = 4`     |

Примеры выражений:

```python
# Умножение имеет более высокий приоритет, чем сложение
# Поэтому это вычисляется как: 2 + (3 * 6) = 2 + 18 = 20
2 + 3 * 6
```

```output
20
```

```python
# Скобки переопределяют приоритет операторов
# Это вычисляется как: 5 * 6 = 30
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
<base-quiz-question correct="A" id="cheatsheet-basics-1">
<template #question>
Каков результат этого выражения Python?

```python
4 + 2 * 3
```

</template>

<base-quiz-option value="A" correct>A. 10</base-quiz-option>
<base-quiz-option value="B">B. 18</base-quiz-option>
<base-quiz-option value="C">C. 12</base-quiz-option>
<base-quiz-option value="D">D. 20</base-quiz-option>
<base-quiz-answer value="A">Умножение имеет более высокий приоритет, чем сложение, поэтому это вычисляется как: 4 + (2 \* 3) = 4 + 6 = 10</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Операторы присваивания с расширением

| Оператор    | Эквивалент       |
| ----------- | ---------------- |
| `var += 1`  | `var = var + 1`  |
| `var -= 1`  | `var = var - 1`  |
| `var *= 1`  | `var = var * 1`  |
| `var /= 1`  | `var = var / 1`  |
| `var //= 1` | `var = var // 1` |
| `var %= 1`  | `var = var % 1`  |
| `var **= 1` | `var = var ** 1` |

Примеры:

```python
# Присваивание с расширением: эквивалентно greeting = greeting + ' world!'
greeting = 'Hello'
greeting += ' world!'
greeting
```

```output
'Hello world!'
```

```python
# Увеличить число на 1
number = 1
number += 1
number
```

```output
2
```

```python
# Повторение элементов списка: эквивалентно my_list = my_list * 3
my_list = ['item']
my_list *= 3
my_list
```

```output
['item', 'item', 'item']
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-basics-2">
<template #question>
Каково значение <code>x</code> после выполнения этого кода?

```python
x = 5
x += 3
```

</template>

<base-quiz-option value="A">A. 3</base-quiz-option>
<base-quiz-option value="B" correct>B. 8</base-quiz-option>
<base-quiz-option value="C">C. 5</base-quiz-option>
<base-quiz-option value="D">D. 15</base-quiz-option>
<base-quiz-answer value="B">Оператор присваивания с расширением <code>+=</code> эквивалентен <code>x = x + 3</code>. Таким образом, <code>x</code> начинается с 5, а затем становится 5 + 3 = 8.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Оператор "Морж" (Walrus Operator)

Оператор "Морж" позволяет присваивать переменные внутри выражения, возвращая при этом значение переменной

Пример:

```python
# Оператор "Морж" присваивает и возвращает значение в одном выражении
# my_var присваивается "Hello World!" и затем выводится на печать
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

Оператор _"Морж"_, или **Оператор выражения присваивания**, был впервые представлен в 2018 году через [PEP 572](https://peps.python.org/pep-0572/), а затем официально выпущен с **Python 3.8** в октябре 2019 года.

<base-disclaimer>
  <base-disclaimer-title>
    Синтаксическая семантика и примеры
  </base-disclaimer-title>
  <base-disclaimer-content>
  [PEP 572](https://peps.python.org/pep-0572/) предоставляет синтаксис, семантику и примеры для оператора "Морж".
  </base-disclaimer-content>
</base-disclaimer>

## Типы данных

Понимание типов данных — одна из самых важных основ Python. В Python есть девять основных встроенных типов данных, которые охватывают почти все, что вам понадобится:

| Тип данных                                                 | Примеры                                  | Описание                                       |
| ---------------------------------------------------------- | ---------------------------------------- | ---------------------------------------------- |
| **Числа**                                                  |                                          |                                                |
| <router-link to='/builtin/int'>`int`</router-link>         | `-2, -1, 0, 1, 2, 3, 4, 5`               | Целые числа                                    |
| <router-link to='/builtin/float'>`float`</router-link>     | `-1.25, -1.0, -0.5, 0.0, 0.5, 1.0, 1.25` | Числа с десятичной точкой                      |
| <router-link to='/builtin/complex'>`complex`</router-link> | `2+3j, complex(1, 4)`                    | Числа с действительной и мнимой частями        |
| **Текст**                                                  |                                          |                                                |
| <router-link to='/builtin/str'>`str`</router-link>         | `'a', 'Hello!', "Python"`                | Текст и символы                                |
| **Булевы**                                                 |                                          |                                                |
| <router-link to='/builtin/bool'>`bool`</router-link>       | `True, False`                            | Значения Истина или Ложь                       |
| **None**                                                   |                                          |                                                |
| `NoneType`                                                 | `None`                                   | Обозначает "нет значения" или "ничего"         |
| **Коллекции**                                              |                                          |                                                |
| <router-link to='/builtin/list'>`list`</router-link>       | `[1, 2, 3], ['a', 'b', 'c']`             | Упорядоченные, изменяемые коллекции            |
| <router-link to='/builtin/dict'>`dict`</router-link>       | `{'name': 'Alice', 'age': 30}`           | Пары ключ-значение                             |
| <router-link to='/builtin/tuple'>`tuple`</router-link>     | `(1, 2, 3), ('a', 'b')`                  | Упорядоченные, неизменяемые коллекции          |
| <router-link to='/builtin/set'>`set`</router-link>         | `{1, 2, 3}, {'a', 'b', 'c'}`             | Неупорядоченные коллекции уникальных элементов |

### Краткие примеры

```python
# Числа
age = 25                    # int
price = 19.99              # float
coordinate = 2 + 3j        # complex

# Текст
name = "Alice"             # str

# Булевы
is_student = True          # bool

# None
result = None              # NoneType

# Коллекции
scores = [85, 92, 78]      # list
person = {'name': 'Bob', 'age': 30}  # dict
coordinates = (10, 20)     # tuple
unique_ids = {1, 2, 3}     # set
```

Для всеобъемлющего руководства с визуальными примерами и подробными объяснениями о том, когда использовать каждый тип, см.: <router-link to="/blog/python-data-types">Типы данных Python: Визуальное руководство для начинающих</router-link>.

## Конкатенация и повторение

Конкатенация строк:

```python
# Конкатенация строк: смежные строки автоматически объединяются
'Alice' 'Bob'
```

```output
'AliceBob'
```

Повторение строк:

```python
# Повторение строк: повторить строку несколько раз
'Alice' * 5
```

```output
'AliceAliceAliceAliceAlice'
```

## Переменные

Переменные — это фундаментальная часть основ Python. Вы можете назвать переменную как угодно, если она подчиняется следующим правилам:

1. Она может состоять только из одного слова.

```python
# плохо
my variable = 'Hello'

# хорошо
var = 'Hello'
```

2. Она может содержать только буквы, цифры и символ подчеркивания (`_`).

```python
# плохо
%$@variable = 'Hello'

# хорошо
my_var = 'Hello'

# хорошо
my_var_2 = 'Hello'
```

3. Она не может начинаться с цифры.

```python
# это не сработает
23_var = 'hello'
```

4. Имя переменной, начинающееся с подчеркивания (`_`), считается "неиспользуемым".

```python
# _spam не следует использовать снова в коде
_spam = 'Hello'
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-basics-3">
<template #question>
В основах Python, какое из следующих имен является допустимым именем переменной?
</template>

<base-quiz-option value="A">A. <code>3value</code></base-quiz-option>
<base-quiz-option value="B">B. <code>user-name</code></base-quiz-option>
<base-quiz-option value="C" correct>C. <code>user_name</code></base-quiz-option>
<base-quiz-option value="D">D. <code>for</code></base-quiz-option>
<base-quiz-answer value="C"><code>user_name</code> является допустимым именем переменной, поскольку оно использует только буквы, цифры и подчеркивания и не начинается с цифры.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Комментарии

Встроенный комментарий:

```python
# Это комментарий
```

Многострочный комментарий:

```python
# Это
# многострочный комментарий
```

Код с комментарием:

```python
a = 1  # инициализация
```

Обратите внимание на два пробела перед комментарием.

Строка документации функции:

```python
def foo():
    """
    Это строка документации функции
    Вы также можете использовать:
    ''' Строка документации функции '''
    """
```

## Функция print()

Функция `print()` — одна из первых основ Python, которую вы изучите. Она выводит значение переданного ей аргумента(ов). [...] она обрабатывает несколько аргументов, числа с плавающей запятой и строки. Строки печатаются без кавычек, и между элементами вставляется пробел, так что вы можете красиво форматировать вывод:

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

### Ключевое слово end

Ключевой аргумент `end` можно использовать, чтобы избежать перехода на новую строку после вывода, или завершить вывод другой строкой:

```python
# Используйте параметр end, чтобы изменить то, что идет после каждого оператора print
phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
for word in phrase:
    print(word, end='-')  # Используем '-' вместо новой строки
```

```output
printed-with-a-dash-in-between-
```

### Ключевое слово sep

Ключевое слово `sep` определяет, как разделять объекты, если их несколько:

```python
# Используйте параметр sep, чтобы указать разделитель между несколькими аргументами
print('cats', 'dogs', 'mice', sep=',')  # Вывод с разделителем-запятой
```

```output
cats,dogs,mice
```

## Функция input()

Эта функция принимает ввод от пользователя и преобразует его в строку:

```python
# input() считывает ввод пользователя и возвращает его в виде строки
print('What is your name?')   # запрашиваем имя
my_name = input()  # Ожидаем, пока пользователь введет текст и нажмет Enter
print('Hi, {}'.format(my_name))
```

```output
What is your name?
Martha
Hi, Martha
```

`input()` также может отображать сообщение-подсказку без использования `print()`:

```python
my_name = input('What is your name? ')  # сообщение-подсказка
print('Hi, {}'.format(my_name))
```

```output
What is your name? Martha
Hi, Martha
```

Также возможно использовать форматированные строки, чтобы избежать использования .format:

```python
# input() может отображать сообщение-подсказку напрямую
my_name = input('What is your name? ')  # Подсказка и чтение в одном вызове
print(f'Hi, {my_name}')  # f-строка для форматирования строк
```

```output
What is your name? Martha
Hi, Martha
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-basics-4">
<template #question>
В основах Python, какой тип возвращает `input()`?
</template>

<base-quiz-option value="A">A. int</base-quiz-option>
<base-quiz-option value="B" correct>B. str</base-quiz-option>
<base-quiz-option value="C">C. float</base-quiz-option>
<base-quiz-option value="D">D. Зависит от ввода пользователя</base-quiz-option>
<base-quiz-answer value="B">Функция <code>input()</code> всегда возвращает строку, независимо от того, что вводит пользователь. Вам нужно преобразовать ее в другой тип, если это необходимо.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Функция len()

Оценивается в целое число, равное количеству символов в строке, списке, словаре и т. д.:

```python
# len() возвращает количество символов в строке
len('hello')  # Возвращает 5
```

```output
5
```

```python
# len() возвращает количество элементов в списке
len(['cat', 3, 'dog'])  # Возвращает 3 (три элемента)
```

```output
3
```

<base-warning>
  <base-warning-title>Проверка на пустоту</base-warning-title>
  <base-warning-content>
    Проверку на пустоту строк, списков, словарей и т. д. не следует выполнять с помощью
    <code>len</code>, а лучше предпочесть прямую булеву оценку.
  </base-warning-content>
</base-warning>

Пример проверки на пустоту:

```python
a = [1, 2, 3]

# плохо: ненужная проверка len()
if len(a) > 0:  # оценивается как True
    print("the list is not empty!")
```

```output
the list is not empty!
```

```python
# хорошо: прямая булева оценка (Pythonic способ)
if a:  # оценивается как True, если список не пуст
    print("the list is not empty!")
```

```output
the list is not empty!
```

## Функции str(), int() и float()

Эти функции позволяют изменять тип переменной. Например, вы можете преобразовать `integer` или `float` в `string`:

```python
# Преобразовать целое число в строку
str(29)  # Возвращает '29'
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

Или из `string` в `integer` или `float`:

```python
# Преобразовать строку в целое число
int('11')  # Возвращает 11
```

```output
11
```

```python
# Преобразовать строку в число с плавающей точкой
float('3.14')  # Возвращает 3.14
```

```output
3.14
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-basics-5">
<template #question>
Каков результат этого кода Python?

```python
result = int('42')
type(result)
```

</template>

<base-quiz-option value="A">A. <code>str</code></base-quiz-option>
<base-quiz-option value="B">B. <code>float</code></base-quiz-option>
<base-quiz-option value="C" correct>C. <code>int</code></base-quiz-option>
<base-quiz-option value="D">D. <code>NoneType</code></base-quiz-option>
<base-quiz-answer value="C">Функция <code>int()</code> преобразует строку в целое число. Таким образом, <code>int('42')</code> возвращает целое число <code>42</code>, а <code>type(42)</code> возвращает <code>int</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Связанные ссылки

- <router-link to="/blog/python-data-types">Типы данных Python: Визуальное руководство для начинающих</router-link>
- <router-link to="/blog/python-comprehensions-step-by-step">Пошаговое руководство по генераторам Python</router-link>
- <router-link to="/cheatsheet/control-flow">Поток управления</router-link>
- <router-link to="/cheatsheet/functions">Функции</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Списки и кортежи</router-link>
- <router-link to="/cheatsheet/dictionaries">Словари</router-link>
- <router-link to="/cheatsheet/sets">Множества</router-link>
- <router-link to="/cheatsheet/string-formatting">Форматирование строк</router-link>
