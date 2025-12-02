---
title: 'Дата-классы Python - Шпаргалка по Python'
description: 'Дата-классы — это классы Python, предназначенные для хранения объектов данных. Этот модуль предоставляет декоратор и функции для автоматического добавления сгенерированных специальных методов, таких как __init__() и __repr__(), к классам, определенным пользователем.'
labUrl: 'https://labex.io/ru/labs/python-python-dataclasses-633652?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Dataclasses Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

`Dataclasses` — это классы Python, но они подходят для хранения объектов данных.
Этот модуль предоставляет декоратор и функции для автоматического добавления сгенерированных специальных методов, таких как `__init__()` и `__repr__()`, в пользовательские классы.

## Особенности

1. Они хранят данные и представляют определенный тип данных. Например, число. Для тех, кто знаком с ORM, экземпляр модели — это объект данных. Он представляет определенный вид сущности. Он содержит атрибуты, которые определяют или представляют эту сущность.

2. Их можно сравнивать с другими объектами того же типа. Например, число может быть больше, меньше или равно другому числу.

Python 3.7 предоставляет декоратор `dataclass`, который используется для преобразования класса в dataclass.

```python
class Number:
    def __init__(self, val):
        self.val = val

obj = Number(2)
obj.val
```

```output
2
```

с dataclass

```python
# Dataclass: автоматически генерирует методы __init__ и __repr__
from dataclasses import dataclass

@dataclass  # Декоратор преобразует класс в dataclass
class Number:
    val: int  # Обязательная аннотация типа

obj = Number(2)  # __init__ создается автоматически
obj.val
```

```output
2
```

## Значения по умолчанию

Легко добавить значения по умолчанию для полей вашего класса данных.

```python
# Dataclass со значениями по умолчанию: поля со значениями по умолчанию должны следовать за обязательными полями
@dataclass
class Product:
    name: str        # Обязательное поле
    count: int = 0   # Необязательное поле со значением по умолчанию
    price: float = 0.0  # Необязательное поле со значением по умолчанию

obj = Product("Python")  # Требуется только name, остальные используют значения по умолчанию
obj.name
```

```output
Python
```

```python
obj.count
```

```output
0
```

```python
obj.price
```

```output
0.0
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-dataclasses-1">
<template #question>
В dataclass, где должны располагаться поля со значениями по умолчанию?
</template>

<base-quiz-option value="A">A. Перед полями без значений по умолчанию</base-quiz-option>
<base-quiz-option value="B" correct>B. После полей без значений по умолчанию</base-quiz-option>
<base-quiz-option value="C">C. Это не имеет значения</base-quiz-option>
<base-quiz-option value="D">D. В отдельном разделе</base-quiz-option>
<base-quiz-answer value="B">В dataclasses поля со значениями по умолчанию должны следовать за полями без значений по умолчанию. Это связано с тем, что Python должен знать порядок обязательных и необязательных параметров для сгенерированного метода <code>**init**</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Подсказки типов (Type hints)

Обязательно указывать тип данных в dataclass. Однако, если вы предпочитаете не указывать тип данных, используйте `typing.Any`.

```python
from dataclasses import dataclass
from typing import Any

@dataclass
class WithoutExplicitTypes:
   name: Any
   value: Any = 42
```

## Связанные ссылки

- <router-link to="/cheatsheet/oop-basics">Основы ООП</router-link>
- <router-link to="/cheatsheet/decorators">Декораторы</router-link>
- <router-link to="/blog/python-data-types">Статья в блоге о типах данных Python</router-link>
- <router-link to="/builtin/object">object()</router-link>
- <router-link to="/builtin/repr">repr()</router-link>
- <router-link to="/builtin/type">type()</router-link>
