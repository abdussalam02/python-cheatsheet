---
title: 'Entornos Virtuales de Python - Hoja de Trucos de Python'
description: 'El uso de un Entorno Virtual es para probar código Python en entornos encapsulados y también para evitar llenar la instalación base de Python con librerías que podríamos usar para un solo proyecto.'
labUrl: 'https://labex.io/es/labs/python-python-virtual-environments-633669?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Entorno Virtual
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

El uso de un Entorno Virtual es para probar código python en entornos encapsulados, y también para evitar llenar la instalación base de Python con librerías que podríamos usar solo para un proyecto.

## venv

`venv` es el módulo de la librería estándar para crear entornos virtuales en Python 3.3+. Está integrado en Python, por lo que no requiere instalación.

1. Crear un entorno virtual

```bash
python -m venv venv
```

O en algunos sistemas:

```bash
python3 -m venv venv
```

Esto crea un directorio `venv` en tu carpeta actual que contiene el entorno virtual.

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-virtual-environments-1">
<template #question>
¿Qué comando se utiliza para crear un entorno virtual usando <code>venv</code>?
</template>

<base-quiz-option value="A" correct>A. <code>python -m venv venv</code></base-quiz-option>
<base-quiz-option value="B">B. <code>python create venv</code></base-quiz-option>
<base-quiz-option value="C">C. <code>venv create</code></base-quiz-option>
<base-quiz-option value="D">D. <code>python venv new</code></base-quiz-option>
<base-quiz-answer value="A">El comando <code>python -m venv venv</code> crea un entorno virtual. El flag <code>-m</code> ejecuta el módulo venv, y <code>venv</code> al final es el nombre del directorio a crear.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

2. Activar el entorno virtual

En Linux/macOS:

```bash
source venv/bin/activate
```

En Windows:

```bash
venv\Scripts\activate
```

Una vez activado, verás `(venv)` al principio de tu símbolo del sistema, indicando que el entorno virtual está activo.

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-virtual-environments-2">
<template #question>
¿Cómo se activa un entorno virtual en Linux/macOS?
</template>

<base-quiz-option value="A">A. <code>activate venv</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>source venv/bin/activate</code></base-quiz-option>
<base-quiz-option value="C">C. <code>venv activate</code></base-quiz-option>
<base-quiz-option value="D">D. <code>python venv activate</code></base-quiz-option>
<base-quiz-answer value="B">En Linux/macOS, se activa un entorno virtual usando <code>source venv/bin/activate</code>. En Windows, se usaría <code>venv\Scripts\activate</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

3. Instalar paquetes

Con el entorno virtual activado, instala paquetes usando pip:

```bash
pip install package_name
```

Los paquetes instalados serán específicos de este entorno virtual.

4. Desactivar el entorno virtual

Para salir del entorno virtual:

```bash
deactivate
```

El prefijo `(venv)` desaparecerá de tu símbolo del sistema.

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-virtual-environments-3">
<template #question>
¿Cuál es el propósito principal de usar un entorno virtual?
</template>

<base-quiz-option value="A" correct>A. Aislar las dependencias del proyecto y evitar llenar la instalación base de Python</base-quiz-option>
<base-quiz-option value="B">B. Hacer que Python se ejecute más rápido</base-quiz-option>
<base-quiz-option value="C">C. Cifrar código Python</base-quiz-option>
<base-quiz-option value="D">D. Compilar Python a código máquina</base-quiz-option>
<base-quiz-answer value="A">Los entornos virtuales te permiten probar código Python en entornos encapsulados y evitar llenar la instalación base de Python con librerías que podrían usarse solo para un proyecto. Esto ayuda a gestionar dependencias por proyecto.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## virtualenv

1. Instalar virtualenv

```bash
pip install virtualenv
```

1. Instalar virtualenvwrapper-win (Windows)

```bash
pip install virtualenvwrapper-win
```

Uso:

1. Crear un Entorno Virtual llamado `HelloWorld`

```bash
mkvirtualenv HelloWorld
```

Cualquier cosa que instalemos ahora será específica para este proyecto. Y estará disponible para los proyectos que conectemos a este entorno.

1. Establecer Directorio del Proyecto

Para vincular nuestro virtualenv con nuestro directorio de trabajo actual, simplemente ingresamos:

```bash
setprojectdir .
```

1. Desactivar

Para pasar a otra cosa en la línea de comandos, escribe `deactivate` para desactivar tu entorno.

```bash
deactivate
```

Nota cómo desaparecen los paréntesis.

1. Workon

Abre el símbolo del sistema y escribe `workon HelloWorld` para activar el entorno y moverte a la carpeta raíz de tu proyecto

```bash
workon HelloWorld
```

## Poetry

<base-disclaimer>
  <base-disclaimer-title>
    Desde <a href="https://python-poetry.org/">sitio web de Poetry</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Poetry es una herramienta para la gestión de dependencias y el empaquetado en Python. Te permite declarar las librerías de las que depende tu proyecto y las gestionará (instalará/actualizará) por ti.
  </base-disclaimer-content>
</base-disclaimer>

1. Instalar Poetry

```bash
pip install --user poetry
```

2. Crear un nuevo proyecto

```bash
poetry new my-project
```

Esto creará un directorio my-project:

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

El archivo pyproject.toml orquestará tu proyecto y sus dependencias:

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

3. Paquetes

Para añadir dependencias a tu proyecto, puedes especificarlas en la sección tool.poetry.dependencies:

```toml
[tool.poetry.dependencies]
pendulum = "^1.4"
```

Además, en lugar de modificar el archivo pyproject.toml manualmente, puedes usar el comando add y automáticamente encontrará una restricción de versión adecuada.

```bash
poetry add pendulum
```

Para instalar las dependencias listadas en pyproject.toml:

```bash
poetry install
```

Para eliminar dependencias:

```bash
poetry remove pendulum
```

Para más información, consulta la [documentación](https://poetry.eustace.io/docs/) o lee aquí:

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Proyectos Python con Poetry y VSCode. Parte 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Proyectos Python con Poetry y VSCode. Parte 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Proyectos Python con Poetry y VSCode. Parte 3</router-link>

## Pipenv

<base-disclaimer>
  <base-disclaimer-title>
    Desde <a target="_blank" href="https://pipenv.pypa.io/en/latest/">sitio web de Pipenv</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Pipenv es una herramienta que tiene como objetivo traer lo mejor de todos los mundos de empaquetado (bundler, composer, npm, cargo, yarn, etc.) al mundo de Python. Windows es un ciudadano de primera clase, en nuestro mundo.
  </base-disclaimer-content>
</base-disclaimer>

1. Instalar pipenv

```bash
pip install pipenv
```

2. Entra en el directorio de tu Proyecto e instala los Paquetes para tu proyecto

```bash
cd my_project
pipenv install <package>
```

Pipenv instalará tu paquete y creará un Pipfile para ti en el directorio de tu proyecto. El Pipfile se utiliza para rastrear qué dependencias necesita tu proyecto en caso de que necesites reinstalarlas.

3. Desinstalar Paquetes

```bash
pipenv uninstall <package>
```

4. Activar el Entorno Virtual asociado con tu proyecto Python

```bash
pipenv shell
```

5. Salir del Entorno Virtual

```bash
exit
```

Encuentra más información y un video en [docs.pipenv.org](https://docs.pipenv.org/).

## Anaconda

<base-disclaimer>
  <base-disclaimer-title>
    <a target="k" href="https://anaconda.com/">Anaconda</a> es otra herramienta popular para gestionar paquetes de python.
  </base-disclaimer-title>
  <base-disclaimer-content>
    Donde se comparten paquetes, notebooks, proyectos y entornos. Tu lugar para el alojamiento público gratuito de paquetes conda.
  </base-disclaimer-content>
</base-disclaimer>

Uso:

1. Crear un Entorno Virtual

```bash
conda create -n HelloWorld
```

2. Para usar el Entorno Virtual, actívalo mediante:

```bash
conda activate HelloWorld
```

Cualquier cosa instalada ahora será específica para el proyecto HelloWorld

3. Salir del Entorno Virtual

```bash
conda deactivate
```

## UV

<base-disclaimer>
  <base-disclaimer-title>
    Desde <a target="_blank" href="https://docs.astral.sh/uv/">Documentación de UV</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    UV es un instalador y resolvedor de paquetes de Python extremadamente rápido, diseñado como un reemplazo directo para los flujos de trabajo de pip y pip-tools. UV es entre 10 y 100 veces más rápido que pip y proporciona gestión unificada de paquetes, creación de entornos virtuales y gestión de versiones de Python.
  </base-disclaimer-content>
</base-disclaimer>

1. Instalar UV

```bash
# Usando curl (Linux/macOS)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Usando pip o pipx
pip install uv
```

2. Crear un nuevo proyecto con entorno virtual

```bash
uv init my-project
cd my-project
```

3. Añadir dependencias

```bash
uv add requests
```

4. Ejecutar comandos en el entorno del proyecto

```bash
uv run python script.py
```

5. Activar el entorno virtual manualmente (opcional)

```bash
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

UV gestiona automáticamente los entornos virtuales, las versiones de Python y las dependencias con una velocidad y conveniencia excepcionales.

## Enlaces relevantes

- <router-link to="/cheatsheet/packaging">Empaquetado</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Proyectos Python con Poetry y VSCode. Parte 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Proyectos Python con Poetry y VSCode. Parte 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Proyectos Python con Poetry y VSCode. Parte 3</router-link>
- <router-link to="/blog/python-uv-package-manager">UV: El Gestor de Paquetes Python Ultrarrápido</router-link>
- <router-link to="/builtin/import">import()</router-link>
