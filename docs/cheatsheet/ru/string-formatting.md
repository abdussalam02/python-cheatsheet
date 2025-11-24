---
title: 'Форматирование строк Python - Шпаргалка Python'
description: 'Если вы используете Python 3.6+, форматированные строки f-strings — рекомендуемый способ форматирования строк.'
labUrl: 'https://labex.io/ru/labs/python-python-string-formatting-633667?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Форматирование строк Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    Из <a href="https://docs.python.org/3/library/stdtypes.html?highlight=sprintf#printf-style-string-formatting">документации Python 3</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Операции форматирования, описанные здесь (<b>оператор %</b>), демонстрируют ряд особенностей, которые приводят к ряду распространенных ошибок [...]. Использование более новых <a href="#formatted-string-literals-or-f-strings">литералов строк с форматированием</a> [...] помогает избежать этих ошибок. Эти альтернативы также предоставляют более мощные, гибкие и расширяемые подходы к форматированию текста.
  </base-disclaimer-content>
</base-disclaimer>

## % operator

<base-warning>
  <base-warning-title>
    Предпочитайте строковые литералы
  </base-warning-title>
  <base-warning-content>
    Для нового кода настоятельно рекомендуется использовать <a href="#strformat">str.format</a> или <a href="#formatted-string-literals-or-f-strings">литералы строк с форматированием</a> (Python 3.6+) вместо оператора <code>%</code>.
  </base-warning-content>
</base-warning>

```python
# % operator: форматирование строк старого стиля (не рекомендуется для нового кода)
name = 'Pete'
'Hello %s' % name  # %s = строковый заполнитель
```

```output
"Hello Pete"
```

Мы можем использовать спецификатор формата `%d` для преобразования целочисленного значения в строку:

```python
num = 5
'I have %d apples' % num
```

```output
"I have 5 apples"
```

## str.format

В Python 3 был представлен новый способ форматирования строк, который позже был обратно портирован в Python 2.7. Это делает синтаксис форматирования строк более упорядоченным.

```python
# Метод str.format(): современное форматирование строк (Python 2.7+)
name = 'John'
age = 20

"Hello I'm {}, my age is {}".format(name, age)  # {} = заполнитель
```

```output
"Hello I'm John, my age is 20"
```

```python
"Hello I'm {0}, my age is {1}".format(name, age)
```

```output
"Hello I'm John, my age is 20"
```

## Литералы строк с форматированием или f-строки

Если вы используете Python 3.6+, строковые `f-строки` являются рекомендуемым способом форматирования строк.

<base-disclaimer>
  <base-disclaimer-title>
    Из <a href="https://docs.python.org/3/reference/lexical_analysis.html#f-strings">документации Python 3</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Литерал строки с форматированием, или f-строка, — это строковый литерал, которому предшествует префикс <code>f</code> или <code>F</code>. Эти строки могут содержать поля для замены, которые представляют собой выражения, ограниченные фигурными скобками {}. В то время как другие строковые литералы всегда имеют постоянное значение, форматированные строки на самом деле являются выражениями, вычисляемыми во время выполнения.
  </base-disclaimer-content>
</base-disclaimer>

```python
# f-string: рекомендуемый способ форматирования строк (Python 3.6+)
name = 'Elizabeth'
f'Hello {name}!'  # префикс f позволяет использовать выражения в {}
```

```output
'Hello Elizabeth!'
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Какой префикс используется для f-строк в Python?
</template>

<base-quiz-option value="A">A. <code>fmt</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>f</code> или <code>F</code></base-quiz-option>
<base-quiz-option value="C">C. <code>format</code></base-quiz-option>
<base-quiz-option value="D">D. <code>str</code></base-quiz-option>
<base-quiz-answer value="B">F-строки предваряются префиксом <code>f</code> или <code>F</code> перед открывающей кавычкой. Они позволяют встраивать выражения в фигурные скобки <code>{}</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

В них даже можно выполнять встроенные вычисления:

```python
# f-строки поддерживают выражения: могут включать вычисления внутри {}
a = 5
b = 10
f'Five plus ten is {a + b} and not {2 * (a + b)}.'  # Вычисляет выражения
```

```output
'Five plus ten is 15 and not 30.'
```

### Многострочные f-строки

```python
name = 'Robert'
messages = 12
(
f'Hi, {name}. '
f'You have {messages} unread messages'
)
```

```output
'Hi, Robert. You have 12 unread messages'
```

### Спецификатор =

Это выведет выражение и его значение:

```python
# Спецификатор =: выводит как имя переменной, так и значение (Python 3.8+)
from datetime import datetime
now = datetime.now().strftime("%b/%d/%Y - %H:%M:%S")
f'date and time: {now=}'  # Выводит "now='Nov/14/2022 - 20:50:01'"
```

```output
"date and time: now='Nov/14/2022 - 20:50:01'"
```

### Добавление пробелов или символов

```python
name = 'Robert'
f"{name.upper() = :-^20}"
```

```output
'name.upper() = -------ROBERT-------'
```

```python
f"{name.upper() = :^20}"
```

```output
'name.upper() =        ROBERT       '
```

```python
f"{name.upper() = :20}"
```

```output
'name.upper() = ROBERT              '
```

## Форматирование цифр

Добавление разделителя тысяч

```python
a = 10000000
f"{a:,}"
```

```output
'10,000,000'
```

Округление

```python
a = 3.1415926
f"{a:.2f}"
```

```output
'3.14'
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
Что делает <code>f"{a:.2f}"</code>?
</template>

<base-quiz-option value="A">A. Округляет число до ближайшего целого</base-quiz-option>
<base-quiz-option value="B">B. Форматирует как процент</base-quiz-option>
<base-quiz-option value="C" correct>C. Форматирует число как число с плавающей точкой с 2 знаками после запятой</base-quiz-option>
<base-quiz-option value="D">D. Преобразует в экспоненциальную нотацию</base-quiz-option>
<base-quiz-answer value="C">Спецификатор формата <code>:.2f</code> форматирует число как число с плавающей точкой с ровно 2 знаками после запятой. <code>.2</code> указывает точность, а <code>f</code> означает формат float.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Отображение в виде процента

```python
a = 0.816562
f"{a:.2%}"
```

```output
'81.66%'
```

### Таблица форматирования чисел

| Число      | Формат  | Вывод     | Описание                                               |
| ---------- | ------- | --------- | ------------------------------------------------------ |
| 3.1415926  | {:.2f}  | 3.14      | Формат float, 2 знака после запятой                    |
| 3.1415926  | {:+.2f} | +3.14     | Формат float, 2 знака после запятой, со знаком         |
| -1         | {:+.2f} | -1.00     | Формат float, 2 знака после запятой, со знаком         |
| 2.71828    | {:.0f}  | 3         | Формат float без знаков после запятой                  |
| 4          | {:0>2d} | 04        | Дополнение нулями (дополнение слева, ширина 2)         |
| 4          | {:x<4d} | 4xxx      | Дополнение символами x (дополнение справа, ширина 4)   |
| 10         | {:x<4d} | 10xx      | Дополнение символами x (дополнение справа, ширина 4)   |
| 1000000    | {:,}    | 1,000,000 | Формат числа с запятой в качестве разделителя          |
| 0.35       | {:.2%}  | 35.00%    | Формат процента                                        |
| 1000000000 | {:.2e}  | 1.00e+09  | Экспоненциальная нотация                               |
| 11         | {:11d}  | 11        | Выравнивание по правому краю (по умолчанию, ширина 10) |
| 11         | {:<11d} | 11        | Выравнивание по левому краю (ширина 10)                |
| 11         | {:^11d} | 11        | Выравнивание по центру (ширина 10)                     |

## Строки-шаблоны (Template Strings)

Более простой и менее мощный механизм, но он рекомендуется при работе со строками, генерируемыми пользователями. Благодаря своей меньшей сложности строковые шаблоны являются более безопасным выбором.

```python
from string import Template
name = 'Elizabeth'
t = Template('Hey $name!')
t.substitute(name=name)
```

```output
'Hey Elizabeth!'
```

## Связанные ссылки

- <router-link to="/cheatsheet/manipulating-strings">Манипулирование строками</router-link>
- <router-link to="/blog/python-data-types">Статья в блоге о типах данных Python</router-link>
- <router-link to="/builtin/format">format()</router-link>
- <router-link to="/builtin/print">print()</router-link>
- <router-link to="/builtin/str">str()</router-link>
- <router-link to="/builtin/repr">repr()</router-link>
- <router-link to="/builtin/ascii">ascii()</router-link>
