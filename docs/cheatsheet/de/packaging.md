---
title: 'Python Packaging - Python Spickzettel'
description: 'Lernen Sie, wie Sie Python-Projekte mit setup.py und pyproject.toml verpacken. Verstehen Sie den modernen Ansatz für Python-Packaging mit PEP-517, PEP-518 und PEP-660 Spezifikationen.'
labUrl: 'https://labex.io/de/labs/python-python-setup-py-633666?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Packaging
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-warning>
  <base-warning-title>
    Eine 'umstrittene' Meinung
  </base-warning-title>
  <base-warning-content>
    Die Verwendung von `setup.py` zum Packen und Verteilen Ihrer Python-Pakete kann mitunter sehr herausfordernd sein. Moderne Tools wie <a target="_blank" href="https://python-poetry.org/">Poetry</a> und <a target="_blank" href="https://docs.astral.sh/uv/">UV</a> machen nicht nur das Paketieren **viel einfacher**, sondern helfen Ihnen auch, Ihre Abhängigkeiten sehr bequem zu verwalten. UV ist besonders bemerkenswert, da es 10-100x schneller ist als herkömmliche Tools.
  </base-warning-content>
</base-warning>

Wenn Sie mehr Informationen über Poetry wünschen, können Sie die folgenden Artikel lesen:

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Python-Projekte mit Poetry und VSCode. Teil 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Python-Projekte mit Poetry und VSCode. Teil 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Python-Projekte mit Poetry und VSCode. Teil 3</router-link>

Für eine umfassende Anleitung zu UV, dem blitzschnellen Python-Paketmanager, lesen Sie: <router-link to="/blog/python-uv-package-manager">UV: Der blitzschnelle Python-Paketmanager</router-link>.

## Einführung

Python-Packaging ist der Prozess der Vorbereitung Ihres Python-Projekts für die Verteilung und Installation. Es gibt zwei Hauptansätze: die traditionelle `setup.py`-Methode und den modernen `pyproject.toml`-Ansatz (definiert in PEP-517, PEP-518 und PEP-660).

Für eine umfassende Anleitung zur Handhabung von Datei- und Verzeichnispfaden, was für die Verwaltung von Projektstrukturen unerlässlich ist, siehe die Seite <router-link to="/cheatsheet/file-directory-path">Datei- und Verzeichnispfade</router-link>.

## Traditioneller Ansatz: setup.py

Die Datei `setup.py` steht im Mittelpunkt eines traditionellen Python-Projekts. Sie beschreibt alle Metadaten über Ihr Projekt. Es gibt einige Felder, die Sie einem Projekt hinzufügen können, um ihm einen reichhaltigen Satz von Metadaten zur Beschreibung des Projekts zu geben. Es gibt jedoch nur drei erforderliche Felder: name, version und packages. Das Feld name muss eindeutig sein, wenn Sie Ihr Paket im Python Package Index (PyPI) veröffentlichen möchten. Das Feld version verfolgt verschiedene Versionen des Projekts. Das Feld packages beschreibt, wo Sie den Python-Quellcode innerhalb Ihres Projekts abgelegt haben.

Dies ermöglicht es Ihnen, Python-Pakete einfach zu installieren. Oft genügt es, Folgendes zu schreiben:

```bash
python setup.py install
```

und das Modul installiert sich selbst.

### Beispiel: setup.py

Unser anfängliches setup.py wird auch Informationen über die Lizenz enthalten und die Datei README.txt für das Feld long_description wiederverwenden. Dies sieht dann wie folgt aus:

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

## Moderner Ansatz: pyproject.toml

Die Datei `pyproject.toml` ist der moderne Standard für die Python-Projektkonfiguration (PEP-517, PEP-518, PEP-660). Sie bietet eine einheitliche Möglichkeit, Build-System-Anforderungen und Projektmetadaten in einem einzigen, deklarativen Dateiformat anzugeben.

### Vorteile von pyproject.toml

- **Deklarativ**: Alle Projektmetadaten an einem Ort
- **Build-System-unabhängig**: Funktioniert mit setuptools, poetry, flit und anderen Build-Backends
- **Keine Code-Ausführung**: Sicherer und vorhersehbarer als setup.py
- **Standardisiert**: Folgt PEP-Standards für bessere Tool-Unterstützung

### Beispiel: pyproject.toml

Hier ist ein grundlegendes `pyproject.toml`-Beispiel mit setuptools:

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "pythonCheatsheet"
version = "0.1"
description = "Ein Python-Spickzettel-Paket"
readme = "README.txt"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Ihr Name", email = "your.email@example.com"}
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

### Installation aus pyproject.toml

Mit `pyproject.toml` können Sie Ihr Paket mit pip installieren:

```bash
pip install .
```

Oder im bearbeitbaren Modus:

```bash
pip install -e .
```

## Den richtigen Ansatz wählen

- **Verwenden Sie `setup.py`**: Wenn Sie mit Legacy-Projekten arbeiten oder eine fein abgestimmte Kontrolle benötigen
- **Verwenden Sie `pyproject.toml`**: Für neue Projekte (empfohlen), da es der moderne Standard ist und bessere Tool-Unterstützung bietet

Weitere Informationen finden Sie in der [offiziellen Dokumentation](http://docs.python.org/3.11/install/index.html).

## Relevante Links

- <router-link to="/cheatsheet/virtual-environments">Virtuelle Umgebungen</router-link>
- <router-link to="/cheatsheet/file-directory-path">Datei- und Verzeichnispfade</router-link>
- <router-link to="/blog/python-uv-package-manager">UV: Der blitzschnelle Python-Paketmanager</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Python-Projekte mit Poetry und VSCode. Teil 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Python-Projekte mit Poetry und VSCode. Teil 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Python-Projekte mit Poetry und VSCode. Teil 3</router-link>
- <router-link to="/builtin/import">import()</router-link>

