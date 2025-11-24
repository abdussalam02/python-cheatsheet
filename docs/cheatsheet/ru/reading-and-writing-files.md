---
title: 'Чтение и запись файлов - Шпаргалка по Python'
description: 'Для чтения/записи в файл в Python используйте оператор with, который автоматически закроет файл и позаботится об управлении ресурсами.'
labUrl: 'https://labex.io/ru/labs/python-python-reading-and-writing-files-633663?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Чтение и запись файлов
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Для более подробного изучения манипуляций с путями к файлам и каталогам см. страницу <router-link to="/cheatsheet/file-directory-path">Пути к файлам и каталогам</router-link>.

## Процесс чтения/записи файлов

Для чтения/записи в файл в Python рекомендуется использовать оператор `with`, который автоматически закроет файл после завершения работы, управляя доступными ресурсами.

## Открытие и чтение файлов

Функция `open` открывает файл и возвращает соответствующий файловый объект.

```python
# Чтение файла с использованием оператора 'with': автоматически закрывает файл по завершении
with open('/home/labex/project/hi.txt') as hello_file:
    hello_content = hello_file.read()  # Читает все содержимое файла

hello_content
```

```output
'Hello World!'
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Каково основное преимущество использования оператора <code>with</code> при открытии файлов?
</template>

<base-quiz-option value="A" correct>A. Файл автоматически закрывается по завершении, даже если возникает ошибка</base-quiz-option>
<base-quiz-option value="B">B. Файлы открываются быстрее</base-quiz-option>
<base-quiz-option value="C">C. Файлы можно открывать одновременно в режиме чтения и записи</base-quiz-option>
<base-quiz-option value="D">D. Файлы автоматически сжимаются</base-quiz-option>
<base-quiz-answer value="A">Оператор <code>with</code> гарантирует, что файл будет автоматически закрыт при выходе из блока, даже если возникает исключение. Это помогает правильно управлять ресурсами.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Альтернативно, вы можете использовать метод _readlines()_, чтобы получить список строковых значений из файла, по одной строке для каждой строки текста:

```python
# Метод readlines(): возвращает список строк, по одной на строку
with open('sonnet29.txt') as sonnet_file:
    sonnet_file.readlines()  # Возвращает список, где каждая строка является строкой
```

```output
['When, in disgrace with fortune and men's eyes,\n',
 ' I all alone beweep my  outcast state,\n',
 "And trouble deaf heaven with my bootless cries,\n",
 "And look upon myself and curse my fate,']
```

Вы также можете итерироваться по файлу построчно:

```python
# Итерация по файлу построчно (эффективно по памяти для больших файлов)
with open('sonnet29.txt') as sonnet_file:
    for line in sonnet_file:  # Файловый объект итерируем
        print(line, end='')  # Печать без дополнительного перевода строки
```

```output
When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,
```

## Запись в файлы

```python
# Запись в файл: режим 'w' перезаписывает существующий файл
with open('bacon.txt', 'w') as bacon_file:  # 'w' = режим записи
    bacon_file.write('Hello world!\n')  # Возвращает количество записанных символов
```

```output
13
```

```python
# Добавление в файл: режим 'a' добавляет содержимое в конец существующего файла
with open('bacon.txt', 'a') as bacon_file:  # 'a' = режим добавления
    bacon_file.write('Bacon is not a vegetable.')
```

```output
25
```

```python
with open('bacon.txt') as bacon_file:
    content = bacon_file.read()

print(content)
```

```output
Hello world!
Bacon is not a vegetable.
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
В чем разница между открытием файла в режиме <code>'w'</code> и режиме <code>'a'</code>?
</template>

<base-quiz-option value="A">A. <code>'w'</code> для чтения, <code>'a'</code> для записи</base-quiz-option>
<base-quiz-option value="B" correct>B. <code>'w'</code> перезаписывает файл, <code>'a'</code> добавляет в конец файла</base-quiz-option>
<base-quiz-option value="C">C. <code>'w'</code> для Windows, <code>'a'</code> для Apple</base-quiz-option>
<base-quiz-option value="D">D. Разницы нет</base-quiz-option>
<base-quiz-answer value="B">Режим <code>'w'</code> открывает файл для записи и перезаписывает любое существующее содержимое. Режим <code>'a'</code> открывает файл для добавления, добавляя новое содержимое в конец файла.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Связанные ссылки

- <router-link to="/cheatsheet/file-directory-path">Пути к файлам и каталогам</router-link>
- <router-link to="/cheatsheet/json-yaml">JSON и YAML</router-link>
- <router-link to="/blog/python-pathlib-essentials">10 основных операций с файловой системой, которые должен знать каждый разработчик</router-link>
- <router-link to="/builtin/open">open()</router-link>
- <router-link to="/builtin/print">print()</router-link>
