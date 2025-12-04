---
title: 'Списки и Кортежи Python - Шпаргалка по Python'
description: 'В Python списки — это один из 4 типов данных, используемых для хранения коллекций.'
labUrl: 'https://labex.io/ru/labs/python-python-lists-and-tuples-633660?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Списки Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Списки — это один из 4 типов данных в Python, используемых для хранения коллекций данных.

```python
# Список: упорядоченная коллекция элементов, заключенных в квадратные скобки
['John', 'Peter', 'Debora', 'Charles']
```

## Получение значений по индексам

```python
# Доступ к элементам списка с использованием индекса (начиная с 0, первый элемент имеет индекс 0)
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[0]  # Возвращает первый элемент: 'table'
```

```output
'table'
```

```python
furniture[1]
```

```output
'chair'
```

```python
furniture[2]
```

```output
'rack'
```

```python
furniture[3]
```

```output
'shelf'
```

## Отрицательные индексы

```python
# Отрицательный индекс: доступ к элементам с конца списка
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[-1]  # Возвращает последний элемент: 'shelf'
```

```output
'shelf'
```

```python
furniture[-3]
```

```output
'chair'
```

```python
f'The {furniture[-1]} is bigger than the {furniture[-3]}'
```

```output
'The shelf is bigger than the chair'
```

<BaseQuiz id="cheatsheet-lists-and-tuples-1" correct="B">
<template #question>
Что вернет <code>furniture[-1]</code>, если <code>furniture = ['table', 'chair', 'rack', 'shelf']</code>?
</template>

<BaseQuizOption value="A">A. <code>'table'</code></BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>'shelf'</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>['shelf']</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>IndexError</code></BaseQuizOption>
<BaseQuizAnswer>Отрицательные индексы обращаются к элементам с конца списка. <code>-1</code> относится к последнему элементу, <code>-2</code> — к предпоследнему и так далее.</BaseQuizAnswer>
</BaseQuiz>

## Получение подсписков с помощью срезов (Slices)

```python
# Срез: получение подсписка с использованием синтаксиса [start:end] (end не включается)
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[0:4]  # Возвращает элементы с индекса 0 по 3 (4 исключается)
```

```output
['table', 'chair', 'rack', 'shelf']
```

```python
furniture[1:3]
```

```output
['chair', 'rack']
```

```python
furniture[0:-1]
```

```output
['table', 'chair', 'rack']
```

```python
# Срез от начала: пропустить начальный индекс (по умолчанию 0)
furniture[:2]  # Возвращает первые два элемента
```

```output
['table', 'chair']
```

```python
# Срез до конца: пропустить конечный индекс (по умолчанию до конца списка)
furniture[1:]  # Возвращает все элементы с индекса 1 до конца
```

```output
['chair', 'rack', 'shelf']
```

```python
furniture[:]
```

```output
['table', 'chair', 'rack', 'shelf']
```

Создание среза всего списка выполнит копирование:

```python
# Срез создает копию: [:] создает неглубокую копию списка
spam = ['cat', 'bat', 'rat', 'elephant']
spam2 = spam[:]  # Создать копию, а не ссылку
spam2
```

```output
['cat', 'bat', 'rat', 'elephant']
```

```python
spam.append('dog')
spam
```

```output
['cat', 'bat', 'rat', 'elephant', 'dog']
```

```python
spam2
```

```output
['cat', 'bat', 'rat', 'elephant']
```

<BaseQuiz id="cheatsheet-lists-and-tuples-2" correct="C">
<template #question>
Что создает <code>spam[:]</code>, когда <code>spam</code> — это список?
</template>

<BaseQuizOption value="A">A. Ссылка на тот же список</BaseQuizOption>
<BaseQuizOption value="B">B. Пустой список</BaseQuizOption>
<BaseQuizOption value="C" correct>C. Неглубокая копия списка</BaseQuizOption>
<BaseQuizOption value="D">D. Перевернутый список</BaseQuizOption>
<BaseQuizAnswer>Создание среза всего списка с помощью <code>[:]</code> создает неглубокую копию. Изменение копии не повлияет на исходный список.</BaseQuizAnswer>
</BaseQuiz>

## Получение длины списка с помощью len()

```python
# len() возвращает количество элементов в списке
furniture = ['table', 'chair', 'rack', 'shelf']
len(furniture)  # Возвращает 4
```

```output
4
```

## Изменение значений по индексам

```python
# Изменение элементов списка путем присвоения новых значений индексам
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[0] = 'desk'  # Заменить первый элемент
furniture
```

```output
['desk', 'chair', 'rack', 'shelf']
```

```python
furniture[2] = furniture[1]
furniture
```

```output
['desk', 'chair', 'chair', 'shelf']
```

```python
furniture[-1] = 'bed'
furniture
```

```output
['desk', 'chair', 'chair', 'bed']
```

## Объединение и повторение

```python
# Объединение списков: объединение двух списков с помощью оператора +
[1, 2, 3] + ['A', 'B', 'C']  # Возвращает [1, 2, 3, 'A', 'B', 'C']
```

```output
[1, 2, 3, 'A', 'B', 'C']
```

```python
# Повторение списка: повторение списка несколько раз с помощью оператора *
['X', 'Y', 'Z'] * 3  # Возвращает ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
```

```output
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
```

```python
my_list = [1, 2, 3]
my_list = my_list + ['A', 'B', 'C']
my_list
```

```output
[1, 2, 3, 'A', 'B', 'C']
```

## Использование циклов for со списками

```python
# Итерация по элементам списка с помощью цикла for
furniture = ['table', 'chair', 'rack', 'shelf']

for item in furniture:  # Цикл по каждому элементу
    print(item)
```

```output
table
chair
rack
shelf
```

## Получение индекса в цикле с помощью enumerate()

```python
# enumerate() возвращает и индекс, и значение в цикле
furniture = ['table', 'chair', 'rack', 'shelf']

for index, item in enumerate(furniture):  # Получить индекс и элемент вместе
    print(f'index: {index} - item: {item}')
```

```output
index: 0 - item: table
index: 1 - item: chair
index: 2 - item: rack
index: 3 - item: shelf
```

## Цикл по нескольким спискам с помощью zip()

```python
# zip() объединяет несколько списков попарно в цикле
furniture = ['table', 'chair', 'rack', 'shelf']
price = [100, 50, 80, 40]

for item, amount in zip(furniture, price):  # Сопоставить элементы из обоих списков
    print(f'The {item} costs ${amount}')
```

```output
The table costs $100
The chair costs $50
The rack costs $80
The shelf costs $40
```

## Операторы in и not in

```python
# Оператор in: проверка наличия элемента в списке
'rack' in ['table', 'chair', 'rack', 'shelf']  # Возвращает True
```

```output
True
```

```python
'bed' in ['table', 'chair', 'rack', 'shelf']
```

```output
False
```

```python
furniture = ['table', 'chair', 'rack', 'shelf']
'bed' not in furniture
```

```output
True
```

```python
'rack' not in furniture
```

```output
False
```

## Трюк с множественным присваиванием

Трюк с множественным присваиванием — это ярлык, который позволяет присвоить несколько переменных значениям из списка в одной строке кода. Вместо того чтобы делать так:

```python
furniture = ['table', 'chair', 'rack', 'shelf']
table = furniture[0]
chair = furniture[1]
rack = furniture[2]
shelf = furniture[3]
```

Вы можете написать эту строку кода:

```python
furniture = ['table', 'chair', 'rack', 'shelf']
table, chair, rack, shelf = furniture

table
```

```output
'table'
```

```python
chair
```

```output
'chair'
```

```python
rack
```

```output
'rack'
```

```python
shelf
```

```output
'shelf'
```

Трюк с множественным присваиванием также можно использовать для обмена значениями двух переменных:

```python
a, b = 'table', 'chair'
a, b = b, a
print(a)
```

```output
chair
```

```python
print(b)
```

```output
table
```

## Метод index

Метод `index` позволяет найти индекс значения, передав его имя:

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.index('chair')
```

```output
1
```

## Добавление значений

### append()

`append` добавляет элемент в конец `list`:

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.append('bed')
furniture
```

```output
['table', 'chair', 'rack', 'shelf', 'bed']
```

<BaseQuiz id="cheatsheet-lists-and-tuples-3" correct="A">
<template #question>
Что делает метод <code>append()</code> со списком?
</template>

<BaseQuizOption value="A" correct>A. Добавляет элемент в конец списка</BaseQuizOption>
<BaseQuizOption value="B">B. Добавляет элемент в начало списка</BaseQuizOption>
<BaseQuizOption value="C">C. Заменяет последний элемент</BaseQuizOption>
<BaseQuizOption value="D">D. Удаляет последний элемент</BaseQuizOption>
<BaseQuizAnswer>Метод <code>append()</code> добавляет один элемент в конец списка. Чтобы добавить элемент в определенную позицию, используйте <code>insert()</code>.</BaseQuizAnswer>
</BaseQuiz>

### insert()

`insert` добавляет элемент в `list` в заданную позицию:

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.insert(1, 'bed')
furniture
```

```output
['table', 'bed', 'chair', 'rack', 'shelf']
```

## Удаление значений

### del

`del` удаляет элемент по индексу:

```python
furniture = ['table', 'chair', 'rack', 'shelf']
del furniture[2]
furniture
```

```output
['table', 'chair', 'shelf']
```

```python
del furniture[2]
furniture
```

```output
['table', 'chair']
```

### remove()

`remove` удаляет элемент по его фактическому значению:

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.remove('chair')
furniture
```

```output
['table', 'rack', 'shelf']
```

<base-warning>
  <base-warning-title>
    Удаление повторяющихся элементов
  </base-warning-title>
  <base-warning-content>
    Если значение встречается в списке несколько раз, будет удален только первый экземпляр этого значения.
  </base-warning-content>
</base-warning>

### pop()

По умолчанию `pop` удаляет и возвращает последний элемент списка. Вы также можете передать индекс элемента в качестве необязательного параметра:

```python
animals = ['cat', 'bat', 'rat', 'elephant']

animals.pop()
```

```output
'elephant'
```

```python
animals
```

```output
['cat', 'bat', 'rat']
```

```python
animals.pop(0)
```

```output
'cat'
```

```python
animals
```

```output
['bat', 'rat']
```

<BaseQuiz id="cheatsheet-lists-and-tuples-4" correct="B">
<template #question>
Что делает <code>pop()</code> при вызове для списка?
</template>

<BaseQuizOption value="A">A. Только удаляет последний элемент</BaseQuizOption>
<BaseQuizOption value="B" correct>B. Удаляет и возвращает элемент (по умолчанию последний элемент или указанный индекс)</BaseQuizOption>
<BaseQuizOption value="C">C. Только возвращает последний элемент, не удаляя его</BaseQuizOption>
<BaseQuizOption value="D">D. Удаляет все элементы из списка</BaseQuizOption>
<BaseQuizAnswer>Метод <code>pop()</code> удаляет и возвращает элемент. По умолчанию он удаляет последний элемент, но вы можете передать индекс, чтобы удалить определенный элемент.</BaseQuizAnswer>
</BaseQuiz>

## Сортировка значений с помощью sort()

```python
numbers = [2, 5, 3.14, 1, -7]
numbers.sort()
numbers
```

```output
[-7, 1, 2, 3.14, 5]
```

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.sort()
furniture
```

```output
['chair', 'rack', 'shelf', 'table']
```

Вы также можете передать `True` для именованного аргумента `reverse`, чтобы `sort()` отсортировал значения в обратном порядке:

```python
furniture.sort(reverse=True)
furniture
```

```output
['table', 'shelf', 'rack', 'chair']
```

Если вам нужно отсортировать значения в обычном алфавитном порядке, передайте `str.lower` для именованного аргумента `key` в вызове метода `sort()`:

```python
letters = ['a', 'z', 'A', 'Z']
letters.sort(key=str.lower)
letters
```

```output
['a', 'A', 'z', 'Z']
```

Вы можете использовать встроенную функцию `sorted`, чтобы вернуть новый список:

```python
furniture = ['table', 'chair', 'rack', 'shelf']
sorted(furniture)
```

```output
['chair', 'rack', 'shelf', 'table']
```

## Тип данных Tuple

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://stackoverflow.com/questions/1708510/list-vs-tuple-when-to-use-each">Кортежи против Списков</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Ключевое различие между кортежами и списками заключается в том, что, хотя <code>кортежи</code> являются <i>неизменяемыми</i> объектами, <code>списки</code> являются <i>изменяемыми</i>. Это означает, что кортежи нельзя изменять, в то время как списки можно изменять. Кортежи более эффективны по памяти, чем списки.
  </base-disclaimer-content>
</base-disclaimer>

```python
furniture = ('table', 'chair', 'rack', 'shelf')

furniture[0]
```

```output
'table'
```

```python
furniture[1:3]
```

```output
('chair', 'rack')
```

```python
len(furniture)
```

```output
4
```

Основное отличие кортежей от списков заключается в том, что кортежи, как и строки, неизменяемы.

## Преобразование между list() и tuple()

```python
tuple(['cat', 'dog', 5])
```

```output
('cat', 'dog', 5)
```

```python
list(('cat', 'dog', 5))
```

```output
['cat', 'dog', 5]
```

```python
list('hello')
```

```output
['h', 'e', 'l', 'l', 'o']
```

<BaseQuiz id="cheatsheet-lists-and-tuples-5" correct="C">
<template #question>
Каково основное различие между списками и кортежами в Python?
</template>

<BaseQuizOption value="A">A. Списки могут содержать только числа, кортежи могут содержать что угодно</BaseQuizOption>
<BaseQuizOption value="B">B. Кортежи создаются быстрее</BaseQuizOption>
<BaseQuizOption value="C" correct>C. Списки изменяемы (могут быть изменены), кортежи неизменяемы (не могут быть изменены)</BaseQuizOption>
<BaseQuizOption value="D">D. Списки используют квадратные скобки, кортежи используют фигурные скобки</BaseQuizOption>
<BaseQuizAnswer>Списки изменяемы, что означает, что вы можете изменять их после создания. Кортежи неизменяемы, что означает, что после создания их нельзя изменить. Оба могут содержать любые типы данных.</BaseQuizAnswer>
</BaseQuiz>

## Связанные ссылки

- <router-link to="/blog/python-data-types">Типы данных Python: Наглядное руководство для начинающих</router-link>
- <router-link to="/blog/python-comprehensions-step-by-step">Понимание Python шаг за шагом</router-link>
- <router-link to="/cheatsheet/comprehensions">Понимание Python</router-link>
- <router-link to="/modules/itertools-module">Модуль itertools</router-link>
- <router-link to="/builtin/list">list()</router-link>
- <router-link to="/builtin/tuple">tuple()</router-link>
- <router-link to="/builtin/len">len()</router-link>
