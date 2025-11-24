---
title: 'Виртуальные среды Python - Справочник по Python'
description: 'Виртуальная среда используется для тестирования кода Python в изолированных окружениях и для предотвращения заполнения базовой установки Python библиотеками, которые могут понадобиться только для одного проекта.'
labUrl: 'https://labex.io/ru/labs/python-python-virtual-environments-633669?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Виртуальное окружение
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Использование Виртуального Окружения заключается в тестировании кода Python в инкапсулированных средах, а также в избежании заполнения базовой установки Python библиотеками, которые мы можем использовать только для одного проекта.

## venv

`venv` — это стандартный библиотечный модуль для создания виртуальных окружений в Python 3.3+. Он встроен в Python, поэтому установка не требуется.

1. Создание виртуального окружения

```bash
python -m venv venv
```

Или в некоторых системах:

```bash
python3 -m venv venv
```

Это создает каталог `venv` в вашей текущей папке, содержащий виртуальное окружение.

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Какая команда используется для создания виртуального окружения с помощью <code>venv</code>?
</template>

<base-quiz-option value="A" correct>A. <code>python -m venv venv</code></base-quiz-option>
<base-quiz-option value="B">B. <code>python create venv</code></base-quiz-option>
<base-quiz-option value="C">C. <code>venv create</code></base-quiz-option>
<base-quiz-option value="D">D. <code>python venv new</code></base-quiz-option>
<base-quiz-answer value="A">Команда <code>python -m venv venv</code> создает виртуальное окружение. Флаг <code>-m</code> запускает модуль venv, а <code>venv</code> в конце — это имя каталога для создания.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

2. Активация виртуального окружения

В Linux/macOS:

```bash
source venv/bin/activate
```

В Windows:

```bash
venv\Scripts\activate
```

После активации в начале вашей командной строки появится `(venv)`, указывающее на то, что виртуальное окружение активно.

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Как активировать виртуальное окружение в Linux/macOS?
</template>

<base-quiz-option value="A">A. <code>activate venv</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>source venv/bin/activate</code></base-quiz-option>
<base-quiz-option value="C">C. <code>venv activate</code></base-quiz-option>
<base-quiz-option value="D">D. <code>python venv activate</code></base-quiz-option>
<base-quiz-answer value="B">В Linux/macOS вы активируете виртуальное окружение с помощью <code>source venv/bin/activate</code>. В Windows вы бы использовали <code>venv\Scripts\activate</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

3. Установка пакетов

При активированном виртуальном окружении устанавливайте пакеты с помощью pip:

```bash
pip install package_name
```

Установленные пакеты будут специфичны для этого виртуального окружения.

4. Деактивация виртуального окружения

Чтобы выйти из виртуального окружения:

```bash
deactivate
```

Префикс `(venv)` исчезнет из вашей командной строки.

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Какова основная цель использования виртуального окружения?
</template>

<base-quiz-option value="A" correct>A. Изолировать зависимости проекта и избежать заполнения базовой установки Python</base-quiz-option>
<base-quiz-option value="B">B. Заставить Python работать быстрее</base-quiz-option>
<base-quiz-option value="C">C. Шифровать код Python</base-quiz-option>
<base-quiz-option value="D">D. Компилировать Python в машинный код</base-quiz-option>
<base-quiz-answer value="A">Виртуальные окружения позволяют тестировать код Python в инкапсулированных средах и избегать заполнения базовой установки Python библиотеками, которые могут использоваться только для одного проекта. Это помогает управлять зависимостями для каждого проекта.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## virtualenv

1. Установка virtualenv

```bash
pip install virtualenv
```

1. Установка virtualenvwrapper-win (Windows)

```bash
pip install virtualenvwrapper-win
```

Использование:

1. Создание виртуального окружения с именем `HelloWorld`

```bash
mkvirtualenv HelloWorld
```

Все, что мы установим сейчас, будет специфично для этого проекта. И доступно для проектов, которые мы подключаем к этому окружению.

1. Установка каталога проекта

Чтобы связать наше виртуальное окружение с текущим рабочим каталогом, мы просто вводим:

```bash
setprojectdir .
```

1. Деактивация

Чтобы перейти к чему-то другому в командной строке, введите `deactivate` для деактивации вашего окружения.

```bash
deactivate
```

Обратите внимание, как исчезают скобки.

1. Workon

Откройте командную строку и введите `workon HelloWorld`, чтобы активировать окружение и перейти в корневую папку вашего проекта

```bash
workon HelloWorld
```

## Poetry

<base-disclaimer>
  <base-disclaimer-title>
    С <a href="https://python-poetry.org/">веб-сайта Poetry</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Poetry — это инструмент для управления зависимостями и упаковки в Python. Он позволяет объявить библиотеки, от которых зависит ваш проект, и будет управлять ими (устанавливать/обновлять) за вас.
  </base-disclaimer-content>
</base-disclaimer>

1. Установка Poetry

```bash
pip install --user poetry
```

2. Создание нового проекта

```bash
poetry new my-project
```

Это создаст каталог my-project:

```plaintext
my-project
├── pyproject.toml
├── README.rst
├── poetry_demo
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_poetry_demo.py
```

Файл pyproject.toml будет оркестровать ваш проект и его зависимости:

```toml
[tool.poetry]
name = "my-project"
version = "0.1.0"
description = ""
authors = ["your name <your@mail.com>"]

[tool.poetry.dependencies]
python = "*"

[tool.poetry.dev-dependencies]
pytest = "^3.4"
```

3. Пакеты

Чтобы добавить зависимости в ваш проект, вы можете указать их в разделе tool.poetry.dependencies:

```toml
[tool.poetry.dependencies]
pendulum = "^1.4"
```

Кроме того, вместо ручного изменения файла pyproject.toml вы можете использовать команду add, и она автоматически найдет подходящее ограничение версии.

```bash
poetry add pendulum
```

Чтобы установить зависимости, перечисленные в pyproject.toml:

```bash
poetry install
```

Чтобы удалить зависимости:

```bash
poetry remove pendulum
```

Для получения дополнительной информации ознакомьтесь с [документацией](https://poetry.eustace.io/docs/) или прочтите здесь:

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Python projects with Poetry and VSCode. Part 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Python projects with Poetry and VSCode. Part 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Python projects with Poetry and VSCode. Part 3</router-link>

## Pipenv

<base-disclaimer>
  <base-disclaimer-title>
    С <a target="_blank" href="https://pipenv.pypa.io/en/latest/">веб-сайта Pipenv</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Pipenv — это инструмент, который стремится привнести лучшее из всех миров упаковки (bundler, composer, npm, cargo, yarn и т. д.) в мир Python. Windows является первоклассным гражданином в нашем мире.
  </base-disclaimer-content>
</base-disclaimer>

1. Установка pipenv

```bash
pip install pipenv
```

2. Перейдите в каталог вашего проекта и установите пакеты для вашего проекта

```bash
cd my_project
pipenv install <package>
```

Pipenv установит ваш пакет и создаст для вас файл Pipfile в каталоге вашего проекта. Pipfile используется для отслеживания зависимостей, необходимых вашему проекту, на случай, если вам потребуется их переустановить.

3. Удаление пакетов

```bash
pipenv uninstall <package>
```

4. Активация виртуального окружения, связанного с вашим проектом Python

```bash
pipenv shell
```

5. Выход из виртуального окружения

```bash
exit
```

Найдите больше информации и видео на [docs.pipenv.org](https://docs.pipenv.org/).

## Anaconda

<base-disclaimer>
  <base-disclaimer-title>
    <a target="k" href="https://anaconda.com/">Anaconda</a> — еще один популярный инструмент для управления пакетами Python.
  </base-disclaimer-title>
  <base-disclaimer-content>
    Где обмениваются пакетами, ноутбуками, проектами и окружениями. Ваше место для бесплатного публичного хостинга пакетов conda.
  </base-disclaimer-content>
</base-disclaimer>

Использование:

1. Создание виртуального окружения

```bash
conda create -n HelloWorld
```

2. Чтобы использовать виртуальное окружение, активируйте его:

```bash
conda activate HelloWorld
```

Все, что будет установлено сейчас, будет специфично для проекта HelloWorld

3. Выход из виртуального окружения

```bash
conda deactivate
```

## UV

<base-disclaimer>
  <base-disclaimer-title>
    Из <a target="_blank" href="https://docs.astral.sh/uv/">документации UV</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    UV — это чрезвычайно быстрый установщик и решатель пакетов Python, разработанный как прямая замена рабочим процессам pip и pip-tools. UV в 10-100 раз быстрее, чем pip, и обеспечивает унифицированное управление пакетами, создание виртуальных окружений и управление версиями Python.
  </base-disclaimer-content>
</base-disclaimer>

1. Установка UV

```bash
# Использование curl (Linux/macOS)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Использование pip или pipx
pip install uv
```

2. Создание нового проекта с виртуальным окружением

```bash
uv init my-project
cd my-project
```

3. Добавление зависимостей

```bash
uv add requests
```

4. Запуск команд в окружении проекта

```bash
uv run python script.py
```

5. Ручная активация виртуального окружения (необязательно)

```bash
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

UV автоматически управляет виртуальными окружениями, версиями Python и зависимостями с исключительной скоростью и удобством.

## Соответствующие ссылки

- <router-link to="/cheatsheet/packaging">Упаковка</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Python projects with Poetry and VSCode. Part 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Python projects with Poetry and VSCode. Part 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Python projects with Poetry and VSCode. Part 3</router-link>
- <router-link to="/blog/python-uv-package-manager">UV: The Lightning-Fast Python Package Manager</router-link>
- <router-link to="/builtin/import">import()</router-link>
