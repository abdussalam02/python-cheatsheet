---
title: 'Упаковка Python - Шпаргалка по Python'
description: 'Узнайте, как упаковывать проекты Python с помощью setup.py и pyproject.toml. Поймите современный подход к упаковке Python с использованием спецификаций PEP-517, PEP-518 и PEP-660.'
labUrl: 'https://labex.io/ru/labs/python-python-setup-py-633666?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Упаковка Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-warning>
  <base-warning-title>
    «Спорное» мнение
  </base-warning-title>
  <base-warning-content>
    Использование `setup.py` для упаковки и распространения ваших пакетов Python иногда может быть довольно сложным. Современные инструменты, такие как <a target="_blank" href="https://python-poetry.org/">Poetry</a> и <a target="_blank" href="https://docs.astral.sh/uv/">UV</a>, не только делают упаковку <b>намного проще</b>, но и помогают очень удобно управлять зависимостями. UV особенно примечателен тем, что он в 10-100 раз быстрее традиционных инструментов.
  </base-warning-content>
</base-warning>

Если вы хотите получить больше информации о Poetry, вы можете прочитать следующие статьи:

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Проекты Python с Poetry и VSCode. Часть 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Проекты Python с Poetry и VSCode. Часть 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Проекты Python с Poetry и VSCode. Часть 3</router-link>

Для получения исчерпывающего руководства по UV, молниеносно быстрому менеджеру пакетов Python, прочтите: <router-link to="/blog/python-uv-package-manager">UV: Молниеносно быстрый менеджер пакетов Python</router-link>.

## Введение

Упаковка Python — это процесс подготовки вашего проекта Python к распространению и установке. Существует два основных подхода: традиционный метод с использованием `setup.py` и современный подход с `pyproject.toml` (определенный в PEP-517, PEP-518 и PEP-660).

Для получения исчерпывающего руководства по работе с путями к файлам и каталогам, что важно для управления структурой проекта, см. страницу <router-link to="/cheatsheet/file-directory-path">Пути к файлам и каталогам</router-link>.

## Традиционный подход: setup.py

Файл `setup.py` находится в центре традиционного проекта Python. Он описывает все метаданные о вашем проекте. Вы можете добавить в проект довольно много полей, чтобы придать ему богатый набор метаданных, описывающих проект. Однако есть только три обязательных поля: `name`, `version` и `packages`. Поле `name` должно быть уникальным, если вы хотите опубликовать свой пакет в Python Package Index (PyPI). Поле `version` отслеживает различные выпуски проекта. Поле `packages` описывает, где вы разместили исходный код Python в вашем проекте.

Это позволяет легко устанавливать пакеты Python. Часто достаточно написать:

```bash
python setup.py install
```

и модуль установит себя.

### Пример: setup.py

Наш первоначальный setup.py также будет включать информацию о лицензии и повторно использовать файл README.txt для поля `long_description`. Это будет выглядеть так:

```python
# setup.py: define package metadata for distribution
from distutils.core import setup
setup(
   name='pythonCheatsheet',  # Package name (must be unique on PyPI)
   version='0.1',  # Version number
   packages=['pipenv',],  # List of packages to include
   license='MIT',  # License type
   long_description=open('README.txt').read(),  # Read description from file
)
```

<BaseQuiz id="cheatsheet-packaging-1" correct="C">
<template #question>
Какие три поля являются обязательными в файле <code>setup.py</code>?
</template>

<BaseQuizOption value="A">A. name, author, license</BaseQuizOption>
<BaseQuizOption value="B">B. name, description, packages</BaseQuizOption>
<BaseQuizOption value="C" correct>C. name, version, packages</BaseQuizOption>
<BaseQuizOption value="D">D. name, version, license</BaseQuizOption>
<BaseQuizAnswer>Три обязательных поля в <code>setup.py</code> это <code>name</code> (имя пакета, должно быть уникальным на PyPI), <code>version</code> (отслеживает выпуски) и <code>packages</code> (описывает, где расположен исходный код Python).</BaseQuizAnswer>
</BaseQuiz>

## Современный подход: pyproject.toml

Файл `pyproject.toml` является современным стандартом для конфигурации проектов Python (PEP-517, PEP-518, PEP-660). Он предоставляет унифицированный способ указания требований к системе сборки и метаданных проекта в едином декларативном формате файла.

### Преимущества pyproject.toml

- **Декларативный**: Все метаданные проекта в одном месте
- **Независимый от системы сборки**: Работает с setuptools, poetry, flit и другими бэкендами сборки
- **Без выполнения кода**: Безопаснее и предсказуемее, чем setup.py
- **Стандартизированный**: Соответствует стандартам PEP для лучшей поддержки инструментов

### Пример: pyproject.toml

Вот базовый пример `pyproject.toml` с использованием setuptools:

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "pythonCheatsheet"
version = "0.1"
description = "A Python cheatsheet package"
readme = "README.txt"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=22.0",
]
```

### Установка из pyproject.toml

С `pyproject.toml` вы можете установить свой пакет с помощью pip:

```bash
pip install .
```

Или в редактируемом режиме:

```bash
pip install -e .
```

<BaseQuiz id="cheatsheet-packaging-2" correct="B">
<template #question>
Каково основное преимущество <code>pyproject.toml</code> перед <code>setup.py</code>?
</template>

<BaseQuizOption value="A">A. Он быстрее выполняется</BaseQuizOption>
<BaseQuizOption value="B" correct>B. Он декларативный, безопаснее (без выполнения кода) и соответствует стандартам PEP</BaseQuizOption>
<BaseQuizOption value="C">C. Он требует меньше конфигурации</BaseQuizOption>
<BaseQuizOption value="D">D. Он работает только с Python 3.10+</BaseQuizOption>
<BaseQuizAnswer>Подход <code>pyproject.toml</code> является декларативным (все метаданные в одном месте), более безопасным, поскольку он не выполняет код, как <code>setup.py</code>, и соответствует стандартам PEP (PEP-517, PEP-518, PEP-660) для лучшей поддержки инструментов.</BaseQuizAnswer>
</BaseQuiz>

## Выбор правильного подхода

- **Использовать `setup.py`**: Если вы работаете с устаревшими проектами или вам нужен детальный контроль
- **Использовать `pyproject.toml`**: Для новых проектов (рекомендуется), так как это современный стандарт и он обеспечивает лучшую поддержку инструментов

Больше информации можно найти в [официальной документации](http://docs.python.org/3.11/install/index.html).

## Связанные ссылки

- <router-link to="/cheatsheet/virtual-environments">Виртуальные окружения</router-link>
- <router-link to="/cheatsheet/file-directory-path">Пути к файлам и каталогам</router-link>
- <router-link to="/blog/python-uv-package-manager">UV: Молниеносно быстрый менеджер пакетов Python</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Проекты Python с Poetry и VSCode. Часть 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Проекты Python с Poetry и VSCode. Часть 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Проекты Python с Poetry и VSCode. Часть 3</router-link>
- <router-link to="/builtin/import">import()</router-link>
