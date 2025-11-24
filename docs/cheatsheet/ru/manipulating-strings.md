---
title: 'Манипуляции со строками - Шпаргалка Python'
description: "Символ экранирования создается вводом обратной косой черты \\, за которой следует вставляемый символ."
labUrl: 'https://labex.io/ru/labs/python-python-string-manipulation-633668?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Манипулирование строками
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## Escape characters

Символ экранирования создается путем ввода обратной косой черты `\` за которым следует символ, который вы хотите вставить.

| Символ экранирования | Выводится как                     |
| -------------------- | --------------------------------- |
| `\'`                 | Одинарная кавычка                 |
| `\"`                 | Двойная кавычка                   |
| `\t`                 | Табуляция                         |
| `\n`                 | Новая строка (перенос строки)     |
| `\\`                 | Обратная косая черта              |
| `\b`                 | Забой (Backspace)                 |
| `\ooo`               | Восьмеричное значение             |
| `\r`                 | Возврат каретки (Carriage Return) |

```python
# Escape characters: use backslash to insert special characters
# \n = newline, \' = single quote
print("Hello there!\nHow are you?\nI\'m doing fine.")
```

```output
Hello there!
How are you?
I'm doing fine.
```

## Raw strings

Сырая строка (raw string) полностью игнорирует все символы экранирования и выводит любую обратную косую черту, которая появляется в строке.

```python
# Raw string (r prefix): treats backslashes as literal characters
print(r"Hello there!\nHow are you?\nI\'m doing fine.")  # \n printed literally
```

```output
Hello there!\nHow are you?\nI\'m doing fine.
```

Сырые строки в основном используются для определения <router-link to="/cheatsheet/regular-expressions">регулярных выражений</router-link>.

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Что делает сырая строка (с префиксом <code>r</code>) в Python?
</template>

<base-quiz-option value="A">A. Преобразует все символы в верхний регистр</base-quiz-option>
<base-quiz-option value="B" correct>B. Обрабатывает обратные косые черты как литеральные символы, игнорируя последовательности экранирования</base-quiz-option>
<base-quiz-option value="C">C. Удаляет все пробелы</base-quiz-option>
<base-quiz-option value="D">D. Меняет строку на обратную</base-quiz-option>
<base-quiz-answer value="B">Сырые строки (с префиксом <code>r</code>) обрабатывают обратные косые черты как литеральные символы, поэтому последовательности экранирования, такие как <code>\n</code>, не интерпретируются.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Multiline Strings

```python
print(
"""Dear Alice,

Eve's cat has been arrested for catnapping,
cat burglary, and extortion.

Sincerely,
Bob"""
)
```

```output
Dear Alice,

Eve's cat has been arrested for catnapping,
cat burglary, and extortion.

Sincerely,
Bob
```

## Indexing and Slicing strings

    H   e   l   l   o       w   o   r   l   d    !
    0   1   2   3   4   5   6   7   8   9   10   11

### Indexing

```python
# String indexing: access characters by position (0-based)
spam = 'Hello world!'

spam[0]  # Returns first character: 'H'
```

```output
'H'
```

```python
spam[4]
```

```output
'o'
```

```python
spam[-1]
```

```output
'!'
```

### Slicing

```python
# String slicing: extract substring using [start:end] syntax
spam = 'Hello world!'

spam[0:5]  # Returns characters from index 0 to 4: 'Hello'
```

```output
'Hello'
```

```python
spam[:5]
```

```output
'Hello'
```

```python
spam[6:]
```

```output
'world!'
```

```python
spam[6:-1]
```

```output
'world'
```

```python
spam[:-1]
```

```output
'Hello world'
```

```python
spam[::-1]
```

```output
'!dlrow olleH'
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
Что делает <code>spam[::-1]</code> со строкой?
</template>

<base-quiz-option value="A">A. Возвращает первый символ</base-quiz-option>
<base-quiz-option value="B">B. Возвращает последний символ</base-quiz-option>
<base-quiz-option value="C" correct>C. Меняет строку на обратную</base-quiz-option>
<base-quiz-option value="D">D. Удаляет все символы</base-quiz-option>
<base-quiz-answer value="C">Срез <code>[::-1]</code> меняет строку на обратную, проходя по всем символам в обратном порядке. Шаг <code>-1</code> означает "двигаться назад".</base-quiz-answer>
</base-quiz-question>
</base-quiz>

```python
fizz = spam[0:5]
fizz
```

```output
'Hello'
```

## The in and not in operators

```python
'Hello' in 'Hello World'
```

```output
True
```

```python
'Hello' in 'Hello'
```

```output
True
```

```python
'HELLO' in 'Hello World'
```

```output
False
```

```python
'' in 'spam'
```

```output
True
```

```python
'cats' not in 'cats and dogs'
```

```output
False
```

## upper(), lower() and title()

Преобразует строку в верхний, нижний регистр и регистр заголовка:

```python
greet = 'Hello world!'
greet.upper()
```

```output
'HELLO WORLD!'
```

```python
greet.lower()
```

```output
'hello world!'
```

```python
greet.title()
```

```output
'Hello World!'
```

## isupper() and islower() methods

Возвращает `True` или `False` после оценки, находится ли строка в верхнем или нижнем регистре:

```python
spam = 'Hello world!'
spam.islower()
```

```output
False
```

```python
spam.isupper()
```

```output
False
```

```python
'HELLO'.isupper()
```

```output
True
```

```python
'abc12345'.islower()
```

```output
True
```

```python
'12345'.islower()
```

```output
False
```

```python
'12345'.isupper()
```

```output
False
```

## The isX string methods

| Метод       | Описание                                                                                                                           |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| isalpha()   | возвращает `True`, если строка состоит только из букв.                                                                             |
| isalnum()   | возвращает `True`, если строка состоит только из букв и цифр.                                                                      |
| isdecimal() | возвращает `True`, если строка состоит только из цифр.                                                                             |
| isspace()   | возвращает `True`, если строка состоит только из пробелов, табуляций и символов новой строки.                                      |
| istitle()   | возвращает `True`, если строка состоит только из слов, начинающихся с заглавной буквы, за которой следуют только строчные символы. |

## startswith() and endswith()

```python
'Hello world!'.startswith('Hello')
```

```output
True
```

```python
'Hello world!'.endswith('world!')
```

```output
True
```

```python
'abc123'.startswith('abcdef')
```

```output
False
```

```python
'abc123'.endswith('12')
```

```output
False
```

```python
'Hello world!'.startswith('Hello world!')
```

```output
True
```

```python
'Hello world!'.endswith('Hello world!')
```

```output
True
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Что возвращает <code>startswith()</code>?
</template>

<base-quiz-option value="A" correct>A. <code>True</code>, если строка начинается с указанной подстроки, <code>False</code> в противном случае</base-quiz-option>
<base-quiz-option value="B">B. Подстрока, соответствующая началу</base-quiz-option>
<base-quiz-option value="C">C. Индекс, с которого начинается подстрока</base-quiz-option>
<base-quiz-option value="D">D. Новая строка без префикса</base-quiz-option>
<base-quiz-answer value="A">Метод <code>startswith()</code> возвращает булево значение: <code>True</code>, если строка начинается с указанной подстроки, <code>False</code> в противном случае.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## join() and split()

### join()

Метод `join()` принимает все элементы итерируемого объекта, такого как <router-link to="/cheatsheet/lists-and-tuples">список</router-link>, <router-link to="/cheatsheet/dictionaries">словарь</router-link>, <router-link to="/cheatsheet/lists-and-tuples#the-tuple-data-type">кортеж</router-link> или <router-link to="/cheatsheet/sets">множество</router-link>, и объединяет их в строку. Вы также можете указать разделитель.

```python
''.join(['My', 'name', 'is', 'Simon'])
```

```output
'MynameisSimon'
```

```python
', '.join(['cats', 'rats', 'bats'])
```

```output
'cats, rats, bats'
```

```python
' '.join(['My', 'name', 'is', 'Simon'])
```

```output
'My name is Simon'
```

```python
'ABC'.join(['My', 'name', 'is', 'Simon'])
```

```output
'MyABCnameABCisABCSimon'
```

### split()

Метод `split()` разделяет `строку` на `список`. По умолчанию он использует пробелы для разделения элементов, но вы также можете указать другой символ по вашему выбору:

```python
'My name is Simon'.split()
```

```output
['My', 'name', 'is', 'Simon']
```

```python
'MyABCnameABCisABCSimon'.split('ABC')
```

```output
['My', 'name', 'is', 'Simon']
```

```python
'My name is Simon'.split('m')
```

```output
['My na', 'e is Si', 'on']
```

```python
' My  name is  Simon'.split()
```

```output
['My', 'name', 'is', 'Simon']
```

```python
' My  name is  Simon'.split(' ')
```

```output
['', 'My', '', 'name', 'is', '', 'Simon']
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Что возвращает <code>split()</code> при вызове на строке?
</template>

<base-quiz-option value="A">A. Строку</base-quiz-option>
<base-quiz-option value="B" correct>B. Список строк</base-quiz-option>
<base-quiz-option value="C">C. Кортеж строк</base-quiz-option>
<base-quiz-option value="D">D. Словарь</base-quiz-option>
<base-quiz-answer value="B">Метод <code>split()</code> разделяет строку на список подстрок. По умолчанию он разделяет по пробелам, но вы можете указать другой разделитель.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Justifying text with rjust(), ljust() and center()

```python
'Hello'.rjust(10)
```

```output
'     Hello'
```

```python
'Hello'.rjust(20)
```

```output
'               Hello'
```

```python
'Hello World'.rjust(20)
```

```output
'         Hello World'
```

```python
'Hello'.ljust(10)
```

```output
'Hello     '
```

```python
'Hello'.center(20)
```

```output
'       Hello       '
```

Необязательный второй аргумент для `rjust()` и `ljust()` укажет символ заполнения, отличный от пробела:

```python
'Hello'.rjust(20, '*')
```

```output
'***************Hello'
```

```python
'Hello'.ljust(20, '-')
```

```output
'Hello---------------'
```

```python
'Hello'.center(20, '=')
```

```output
'=======Hello========'
```

## Removing whitespace with strip(), rstrip(), and lstrip()

```python
spam = '    Hello World     '
spam.strip()
```

```output
'Hello World'
```

```python
spam.lstrip()
```

```output
'Hello World     '
```

```python
spam.rstrip()
```

```output
'    Hello World'
```

```python
spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')
```

```output
'BaconSpamEggs'
```

## The Count Method

Подсчитывает количество вхождений данного символа или подстроки в строке, к которой он применяется. Можно опционально указать начальный и конечный индексы.

```python
sentence = 'one sheep two sheep three sheep four'
sentence.count('sheep')
```

```output
3
```

```python
sentence.count('e')
```

```output
9
```

```python
# returns count of e after 'one sh' i.e 6 chars since beginning of string
sentence.count('e', 6)
```

```output
8
```

```python
sentence.count('e', 7)
```

```output
7
```

## Replace Method

Заменяет все вхождения заданной подстроки другой подстрокой. Можно опционально указать третий аргумент для ограничения количества замен. Возвращает новую строку.

```python
text = "Hello, world!"
text.replace("world", "planet")
```

```output
'Hello, planet!'
```

```python
fruits = "apple, banana, cherry, apple"
fruits.replace("apple", "orange", 1)
```

```output
'orange, banana, cherry, apple'
```

```python
sentence = "I like apples, Apples are my favorite fruit"
sentence.replace("apples", "oranges")
```

```output
'I like oranges, Apples are my favorite fruit'
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
Что возвращает метод <code>replace()</code>?
</template>

<base-quiz-option value="A">A. Изменяет исходную строку</base-quiz-option>
<base-quiz-option value="B">B. Возвращает <code>None</code></base-quiz-option>
<base-quiz-option value="C" correct>C. Возвращает новую строку с внесенными заменами</base-quiz-option>
<base-quiz-option value="D">D. Возвращает список замененных строк</base-quiz-option>
<base-quiz-answer value="C">Метод <code>replace()</code> возвращает новую строку со всеми заменами старой подстроки на новую. Исходная строка не изменяется.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Relevant links

- <router-link to="/builtin/format">format()</router-link>
- <router-link to="/builtin/len">len()</router-link>
- <router-link to="/builtin/str">str()</router-link>
- <router-link to="/builtin/repr">repr()</router-link>
- <router-link to="/builtin/input">input()</router-link>
- <router-link to="/cheatsheet/string-formatting">Форматирование строк</router-link>
- <router-link to="/cheatsheet/regular-expressions">Регулярные выражения</router-link>
