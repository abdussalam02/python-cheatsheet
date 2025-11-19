---
title: 'Python Packaging - Справочник по Python'
description: 'Узнайте, как упаковывать проекты Python с помощью setup.py и pyproject.toml. Поймите современный подход к упаковке Python со спецификациями PEP-517, PEP-518 и PEP-660.'
labUrl: 'https://labex.io/ru/labs/python-python-setup-py-633666?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Packaging
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-warning>
  <base-warning-title>
    «Спорное» мнение
  </base-warning-title>
  <base-warning-content>
    Использование `setup.py` для упаковки и распространения ваших пакетов Python может быть довольно сложным время от времени. Современные инструменты, такие как <a target="_blank" href="https://python-poetry.org/">Poetry</a> и <a target="_blank" href="https://docs.astral.sh/uv/">UV</a>, не только делают упаковку **намного проще**, но и помогают очень удобно управлять зависимостями. UV особенно примечателен тем, что он в 10-100 раз быстрее традиционных инструментов.
  </base-warning-content>
</base-warning>

Если вы хотите получить больше информации о Poetry, вы можете прочитать следующие статьи:

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Проекты Python с Poetry и VSCode. Часть 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Проекты Python с Poetry и VSCode. Часть 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Проекты Python с Poetry и VSCode. Часть 3</router-link>

Для получения исчерпывающего руководства по UV, молниеносно быстрому менеджеру пакетов Python, прочтите: <router-link to="/blog/python-uv-package-manager">UV: Молниеносно быстрый менеджер пакетов Python</router-link>.

## Введение

Упаковка Python — это процесс подготовки вашего проекта Python к распространению и установке. Существует два основных подхода: традиционный метод `setup.py` и современный подход `pyproject.toml` (определен в PEP-517, PEP-518 и PEP-660).

Для получения исчерпывающего руководства по работе с путями к файлам и каталогам, что важно для управления структурой проекта, см. страницу <router-link to="/cheatsheet/file-directory-path">Пути к файлам и каталогам</router-link>.

## Традиционный подход: setup.py

Файл `setup.py` находится в основе традиционного проекта Python. Он описывает все метаданные о вашем проекте. Вы можете добавить в проект довольно много полей, чтобы придать ему богатый набор метаданных, описывающих проект. Однако есть только три обязательных поля: `name`, `version` и `packages`. Поле `name` должно быть уникальным, если вы хотите опубликовать свой пакет в Python Package Index (PyPI). Поле `version` отслеживает различные выпуски проекта. Поле `packages` описывает, где вы разместили исходный код Python в вашем проекте.

Это позволяет легко устанавливать пакеты Python. Часто достаточно написать:

```bash
python setup.py install
```

и модуль установит себя сам.

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

## Современный подход: pyproject.toml

Файл `pyproject.toml` — это современный стандарт для конфигурации проектов Python (PEP-517, PEP-518, PEP-660). Он предоставляет единый способ указания требований системы сборки и метаданных проекта в едином декларативном формате файла.

### Преимущества pyproject.toml

- **Декларативный**: Все метаданные проекта в одном месте
- **Независимый от системы сборки**: Работает с setuptools, poetry, flit и другими бэкендами сборки
- **Без выполнения кода**: Безопаснее и предсказуемее, чем setup.py
- **Стандартизированный**: Следует стандартам PEP для лучшей поддержки инструментов

### Пример: pyproject.toml

Вот базовый пример `pyproject.toml` с использованием setuptools:

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "pythonCheatsheet"
version = "0.1"
description = "Пакет справочника Python"
readme = "README.txt"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Ваше Имя", email = "your.email@example.com"}
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

Или в режиме редактирования:

```bash
pip install -e .
```

## Выбор правильного подхода

- **Используйте `setup.py`**: Если вы работаете с устаревшими проектами или вам нужен детальный контроль
- **Используйте `pyproject.toml`**: Для новых проектов (рекомендуется), так как это современный стандарт и обеспечивает лучшую поддержку инструментов

Больше информации можно найти в [официальной документации](http://docs.python.org/3.11/install/index.html).

## Соответствующие ссылки

- <router-link to="/cheatsheet/virtual-environments">Виртуальные окружения</router-link>
- <router-link to="/cheatsheet/file-directory-path">Пути к файлам и каталогам</router-link>
- <router-link to="/blog/python-uv-package-manager">UV: Молниеносно быстрый менеджер пакетов Python</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Проекты Python с Poetry и VSCode. Часть 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Проекты Python с Poetry и VSCode. Часть 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Проекты Python с Poetry и VSCode. Часть 3</router-link>
- <router-link to="/builtin/import">import()</router-link>

