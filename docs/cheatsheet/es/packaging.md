---
title: 'Python Packaging - Hoja de Trucos de Python'
description: 'Aprende cómo empaquetar proyectos Python usando setup.py y pyproject.toml. Comprende el enfoque moderno para el empaquetado de Python con las especificaciones PEP-517, PEP-518 y PEP-660.'
labUrl: 'https://labex.io/es/labs/python-python-setup-py-633666?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Packaging
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-warning>
  <base-warning-title>
    Una opinión 'controvertida'
  </base-warning-title>
  <base-warning-content>
    Usar `setup.py` para empaquetar y distribuir tus paquetes de python puede ser bastante desafiante de vez en cuando. Herramientas modernas como <a target="_blank" href="https://python-poetry.org/">Poetry</a> y <a target="_blank" href="https://docs.astral.sh/uv/">UV</a> no solo hacen que el empaquetado sea **mucho más fácil**, sino que también te ayudan a gestionar tus dependencias de una manera muy conveniente. UV es particularmente notable por ser entre 10 y 100 veces más rápido que las herramientas tradicionales.
  </base-warning-content>
</base-warning>

Si deseas más información sobre Poetry, puedes leer los siguientes artículos:

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Proyectos de Python con Poetry y VSCode. Parte 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Proyectos de Python con Poetry y VSCode. Parte 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Proyectos de Python con Poetry y VSCode. Parte 3</router-link>

Para una guía completa sobre UV, el gestor de paquetes de Python ultrarrápido, lee: <router-link to="/blog/python-uv-package-manager">UV: El gestor de paquetes de Python ultrarrápido</router-link>.

## Introducción

El empaquetado de Python es el proceso de preparar tu proyecto Python para distribución e instalación. Hay dos enfoques principales: el método tradicional `setup.py` y el enfoque moderno `pyproject.toml` (definido en PEP-517, PEP-518 y PEP-660).

Para una guía completa sobre el manejo de rutas de archivos y directorios, lo cual es esencial para gestionar estructuras de proyectos, consulta la página de <router-link to="/cheatsheet/file-directory-path">Rutas de Archivos y Directorios</router-link>.

## Enfoque tradicional: setup.py

El archivo `setup.py` está en el corazón de un proyecto de Python tradicional. Describe todos los metadatos sobre tu proyecto. Hay bastantes campos que puedes añadir a un proyecto para darle un rico conjunto de metadatos que describen el proyecto. Sin embargo, solo hay tres campos obligatorios: `name`, `version` y `packages`. El campo `name` debe ser único si deseas publicar tu paquete en el Python Package Index (PyPI). El campo `version` realiza un seguimiento de las diferentes versiones del proyecto. El campo `packages` describe dónde has colocado el código fuente de Python dentro de tu proyecto.

Esto te permite instalar fácilmente paquetes de Python. A menudo es suficiente escribir:

```bash
python setup.py install
```

y el módulo se instalará a sí mismo.

### Ejemplo: setup.py

Nuestro `setup.py` inicial también incluirá información sobre la licencia y reutilizará el archivo `README.txt` para el campo `long_description`. Se verá así:

```python
# setup.py: define metadatos del paquete para distribución
from distutils.core import setup
setup(
   name='pythonCheatsheet',  # Nombre del paquete (debe ser único en PyPI)
   version='0.1',  # Número de versión
   packages=['pipenv',],  # Lista de paquetes a incluir
   license='MIT',  # Tipo de licencia
   long_description=open('README.txt').read(),  # Leer descripción desde el archivo
)
```

## Enfoque moderno: pyproject.toml

El archivo `pyproject.toml` es el estándar moderno para la configuración de proyectos Python (PEP-517, PEP-518, PEP-660). Proporciona una forma unificada de especificar los requisitos del sistema de compilación y los metadatos del proyecto en un único formato de archivo declarativo.

### Beneficios de pyproject.toml

- **Declarativo**: Todos los metadatos del proyecto en un solo lugar
- **Independiente del sistema de compilación**: Funciona con setuptools, poetry, flit y otros backends de compilación
- **Sin ejecución de código**: Más seguro y predecible que setup.py
- **Estandarizado**: Sigue los estándares PEP para mejor soporte de herramientas

### Ejemplo: pyproject.toml

Aquí tienes un ejemplo básico de `pyproject.toml` usando setuptools:

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "pythonCheatsheet"
version = "0.1"
description = "Un paquete de hoja de trucos de Python"
readme = "README.txt"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Tu Nombre", email = "your.email@example.com"}
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

### Instalación desde pyproject.toml

Con `pyproject.toml`, puedes instalar tu paquete usando pip:

```bash
pip install .
```

O en modo editable:

```bash
pip install -e .
```

## Elegir el enfoque correcto

- **Usa `setup.py`**: Si estás trabajando con proyectos heredados o necesitas control detallado
- **Usa `pyproject.toml`**: Para proyectos nuevos (recomendado), ya que es el estándar moderno y proporciona mejor soporte de herramientas

Encuentra más información visitando la [documentación oficial](http://docs.python.org/3.11/install/index.html).

## Enlaces relevantes

- <router-link to="/cheatsheet/virtual-environments">Entornos Virtuales</router-link>
- <router-link to="/cheatsheet/file-directory-path">Rutas de Archivos y Directorios</router-link>
- <router-link to="/blog/python-uv-package-manager">UV: El gestor de paquetes de Python ultrarrápido</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Proyectos de Python con Poetry y VSCode. Parte 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Proyectos de Python con Poetry y VSCode. Parte 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Proyectos de Python con Poetry y VSCode. Parte 3</router-link>
- <router-link to="/builtin/import">import()</router-link>
