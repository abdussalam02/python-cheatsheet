---
title: 'Python-Paketierung - Python Spickzettel'
description: 'Erfahren Sie, wie Sie Python-Projekte mit setup.py und pyproject.toml paketieren. Verstehen Sie den modernen Ansatz der Python-Paketierung mit den Spezifikationen PEP-517, PEP-518 und PEP-660.'
labUrl: 'https://labex.io/de/labs/python-python-setup-py-633666?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Packaging
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-warning>
  <base-warning-title>
    Eine 'kontroverse' Meinung
  </base-warning-title>
  <base-warning-content>
    Die Verwendung von <code>setup.py</code> zum Packen und Verteilen Ihrer Python-Pakete kann gelegentlich recht herausfordernd sein. Moderne Tools wie <a target="_blank" href="https://python-poetry.org/">Poetry</a> und <a target="_blank" href="https://docs.astral.sh/uv/">UV</a> machen nicht nur das Packaging <b>viel einfacher</b>, sondern helfen Ihnen auch, Ihre Abhängigkeiten auf sehr bequeme Weise zu verwalten. UV ist besonders bemerkenswert, da es 10-100x schneller ist als herkömmliche Tools.
  </base-warning-content>
</base-warning>

Wenn Sie mehr Informationen über Poetry wünschen, können Sie die folgenden Artikel lesen:

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Python-Projekte mit Poetry und VSCode. Teil 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Python-Projekte mit Poetry und VSCode. Teil 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Python-Projekte mit Poetry und VSCode. Teil 3</router-link>

Für eine umfassende Anleitung zu UV, dem blitzschnellen Python-Paketmanager, lesen Sie: <router-link to="/blog/python-uv-package-manager">UV: Der blitzschnelle Python-Paketmanager</router-link>.

## Introduction

Python Packaging ist der Prozess der Vorbereitung Ihres Python-Projekts für die Verteilung und Installation. Es gibt zwei Hauptansätze: die traditionelle <code>setup.py</code>-Methode und den modernen <code>pyproject.toml</code>-Ansatz (definiert in PEP-517, PEP-518 und PEP-660).

Für eine umfassende Anleitung zur Handhabung von Datei- und Verzeichnispfaden, was für die Verwaltung von Projektstrukturen unerlässlich ist, siehe die Seite <router-link to="/cheatsheet/file-directory-path">File and directory Paths</router-link>.

## Traditional Approach: setup.py

Die Datei <code>setup.py</code> steht im Mittelpunkt eines traditionellen Python-Projekts. Sie beschreibt alle Metadaten über Ihr Projekt. Es gibt einige Felder, die Sie einem Projekt hinzufügen können, um ihm einen reichen Satz an Metadaten zu geben, die das Projekt beschreiben. Es gibt jedoch nur drei erforderliche Felder: name, version und packages. Das Feld name muss eindeutig sein, wenn Sie Ihr Paket im Python Package Index (PyPI) veröffentlichen möchten. Das Feld version verfolgt verschiedene Versionen des Projekts. Das Feld packages beschreibt, wo Sie den Python-Quellcode innerhalb Ihres Projekts abgelegt haben.

Dies ermöglicht es Ihnen, Python-Pakete einfach zu installieren. Oft reicht es aus zu schreiben:

```bash
python setup.py install
```

und das Modul installiert sich selbst.

### Example: setup.py

Unser anfängliches setup.py wird auch Informationen über die Lizenz enthalten und die Datei README.txt für das Feld long_description wiederverwenden. Dies sieht dann so aus:

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
What are the three required fields in a <code>setup.py</code> file?
</template>

<BaseQuizOption value="A">A. name, author, license</BaseQuizOption>
<BaseQuizOption value="B">B. name, description, packages</BaseQuizOption>
<BaseQuizOption value="C" correct>C. name, version, packages</BaseQuizOption>
<BaseQuizOption value="D">D. name, version, license</BaseQuizOption>
<BaseQuizAnswer>The three required fields in <code>setup.py</code> are <code>name</code> (package name, must be unique on PyPI), <code>version</code> (tracks releases), and <code>packages</code> (describes where Python source code is located).</BaseQuizAnswer>
</BaseQuiz>

## Modern Approach: pyproject.toml

Die Datei <code>pyproject.toml</code> ist der moderne Standard für die Python-Projektkonfiguration (PEP-517, PEP-518, PEP-660). Sie bietet eine einheitliche Möglichkeit, die Anforderungen des Build-Systems und die Projektmetadaten in einem einzigen, deklarativen Dateiformat anzugeben.

### Benefits of pyproject.toml

- **Declarative**: Alle Projektmetadaten an einem Ort
- **Build system agnostic**: Funktioniert mit setuptools, poetry, flit und anderen Build-Backends
- **No code execution**: Sicherer und vorhersehbarer als setup.py
- **Standardized**: Folgt PEP-Standards für bessere Tool-Unterstützung

### Example: pyproject.toml

Hier ist ein einfaches <code>pyproject.toml</code>-Beispiel mit setuptools:

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

### Installing from pyproject.toml

Mit <code>pyproject.toml</code> können Sie Ihr Paket mit pip installieren:

```bash
pip install .
```

Oder im editierbaren Modus:

```bash
pip install -e .
```

<BaseQuiz id="cheatsheet-packaging-2" correct="B">
<template #question>
What is the main advantage of <code>pyproject.toml</code> over <code>setup.py</code>?
</template>

<BaseQuizOption value="A">A. It's faster to execute</BaseQuizOption>
<BaseQuizOption value="B" correct>B. It's declarative, safer (no code execution), and follows PEP standards</BaseQuizOption>
<BaseQuizOption value="C">C. It requires less configuration</BaseQuizOption>
<BaseQuizOption value="D">D. It only works with Python 3.10+</BaseQuizOption>
<BaseQuizAnswer>The <code>pyproject.toml</code> approach is declarative (all metadata in one place), safer because it doesn't execute code like <code>setup.py</code> does, and follows PEP standards (PEP-517, PEP-518, PEP-660) for better tooling support.</BaseQuizAnswer>
</BaseQuiz>

## Choosing the Right Approach

- **Use `setup.py`**: If you're working with legacy projects or need fine-grained control
- **Use `pyproject.toml`**: For new projects (recommended), as it's the modern standard and provides better tooling support

Find more information visit the [official documentation](http://docs.python.org/3.11/install/index.html).

## Relevant links

- <router-link to="/cheatsheet/virtual-environments">Virtual Environments</router-link>
- <router-link to="/cheatsheet/file-directory-path">File and directory Paths</router-link>
- <router-link to="/blog/python-uv-package-manager">UV: The Lightning-Fast Python Package Manager</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Python projects with Poetry and VSCode. Part 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Python projects with Poetry and VSCode. Part 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Python projects with Poetry and VSCode. Part 3</router-link>
- <router-link to="/builtin/import">import()</router-link>
