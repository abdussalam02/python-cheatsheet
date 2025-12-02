---
title: 'Python JSON и YAML - Справочник Python'
description: 'JSON (JavaScript Object Notation) — это легкий формат для хранения и передачи данных. JSON часто используется при отправке данных с сервера на веб-страницу.'
labUrl: 'https://labex.io/ru/labs/python-python-json-and-yaml-633659?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
JSON и YAML
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## JSON

JSON (JavaScript Object Notation) — это легковесный формат для хранения и передачи данных. JSON часто используется, когда данные отправляются с сервера на веб-страницу.

```python
# Read JSON file: json.load() parses JSON from file object
import json
with open("filename.json", "r") as f:  # Открыть файл в режиме чтения
    content = json.load(f)  # Разобрать JSON и вернуть Python dict/list
```

Запись JSON-файла с помощью:

```python
# Write JSON file: json.dump() writes Python object as JSON
import json

content = {"name": "Joe", "age": 20}
with open("filename.json", "w") as f:  # Открыть файл в режиме записи
    json.dump(content, f, indent=2)  # Записать JSON с отступом в 2 пробела
```

<BaseQuiz id="cheatsheet-json-yaml-1" correct="B">
<template #question>
Какая функция используется для записи словаря Python в файл JSON?
</template>

<BaseQuizOption value="A">A. <code>json.write()</code></BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>json.dump()</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>json.save()</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>json.export()</code></BaseQuizOption>
<BaseQuizAnswer>Функция <code>json.dump()</code> записывает объект Python (например, словарь) в файл JSON. <code>json.load()</code> используется для чтения файлов JSON.</BaseQuizAnswer>
</BaseQuiz>

## YAML

По сравнению с JSON, YAML обеспечивает гораздо лучшую читаемость для человека и дает возможность добавлять комментарии. Это удобный выбор для конфигурационных файлов, которые будут редактироваться человеком.

Существуют две основные библиотеки, предоставляющие доступ к файлам YAML:

- [PyYaml](https://pypi.python.org/pypi/PyYAML)
- [Ruamel.yaml](https://pypi.python.org/pypi/ruamel.yaml)

Установите их с помощью `pip install` в вашей виртуальной среде.

Первая проще в использовании, но вторая, Ruamel, гораздо лучше реализует спецификацию YAML и позволяет, например, изменять содержимое YAML без изменения комментариев.

Открытие файла YAML с помощью:

```python
# Read YAML file using ruamel.yaml library
from ruamel.yaml import YAML

with open("filename.yaml") as f:
    yaml=YAML()  # Создать экземпляр парсера YAML
    yaml.load(f)  # Разобрать YAML и вернуть Python dict/list
```

<BaseQuiz id="cheatsheet-json-yaml-2" correct="C">
<template #question>
Какое одно из преимуществ YAML перед JSON?
</template>

<BaseQuizOption value="A">A. Файлы YAML меньше</BaseQuizOption>
<BaseQuizOption value="B">B. YAML быстрее разбирается</BaseQuizOption>
<BaseQuizOption value="C" correct>C. YAML допускает комментарии и более читаем для человека</BaseQuizOption>
<BaseQuizOption value="D">D. YAML встроен в Python</BaseQuizOption>
<BaseQuizAnswer>YAML допускает комментарии и более читаем для человека, чем JSON, что делает его удобным выбором для конфигурационных файлов, которые должны редактироваться людьми.</BaseQuizAnswer>
</BaseQuiz>

## Anyconfig

[Anyconfig](https://pypi.python.org/pypi/anyconfig) — очень удобный пакет, позволяющий полностью абстрагировать базовый формат конфигурационного файла. Он позволяет загружать словарь Python из JSON, YAML, TOML и других форматов.

Установите его с помощью:

```bash
pip install anyconfig
```

Использование:

```python
# anyconfig: load configuration files in various formats (JSON, YAML, TOML, etc.)
import anyconfig
conf1 = anyconfig.load("/path/to/foo/conf.d/a.yml")  # Автоматическое определение формата
```

<BaseQuiz id="cheatsheet-json-yaml-3" correct="A">
<template #question>
Что позволяет делать библиотека anyconfig?
</template>

<BaseQuizOption value="A" correct>A. Загружать конфигурационные файлы в различных форматах (JSON, YAML, TOML) без указания формата</BaseQuizOption>
<BaseQuizOption value="B">B. Преобразовывать между различными форматами конфигурации</BaseQuizOption>
<BaseQuizOption value="C">C. Проверять синтаксис конфигурационного файла</BaseQuizOption>
<BaseQuizOption value="D">D. Шифровать конфигурационные файлы</BaseQuizOption>
<BaseQuizAnswer>Библиотека anyconfig абстрагирует базовый формат конфигурационного файла, позволяя загружать словари Python из JSON, YAML, TOML и других форматов без необходимости знать, какой формат используется.</BaseQuizAnswer>
</BaseQuiz>

## Relevant links

- <router-link to="/cheatsheet/reading-and-writing-files">Чтение и запись файлов</router-link>
- <router-link to="/cheatsheet/dictionaries">Словари Python</router-link>
- <router-link to="/modules/json-module">Модуль json</router-link>
- <router-link to="/blog/python-pathlib-essentials">10 основных операций с файловой системой, которые должен знать каждый разработчик</router-link>
- <router-link to="/builtin/open">open()</router-link>
- <router-link to="/builtin/dict">dict()</router-link>
