---
title: 'Python Virtuelle Umgebungen - Python Spickzettel'
description: 'Virtuelle Umgebungen dienen dazu, Python-Code in gekapselten Umgebungen zu testen und die Basis-Python-Installation nicht mit Bibliotheken zu füllen, die nur für ein einziges Projekt benötigt werden.'
labUrl: 'https://labex.io/de/labs/python-python-virtual-environments-633669?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Virtuelle Umgebung
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Die Verwendung einer virtuellen Umgebung dient dazu, Python-Code in gekapselten Umgebungen zu testen und zu vermeiden, dass die Basis-Python-Installation mit Bibliotheken gefüllt wird, die wir möglicherweise nur für ein einziges Projekt verwenden.

## venv

`venv` ist das Standardbibliotheksmodul zur Erstellung virtueller Umgebungen in Python 3.3+. Es ist in Python integriert, sodass keine Installation erforderlich ist.

1. Virtuelle Umgebung erstellen

```bash
python -m venv venv
```

Oder auf einigen Systemen:

```bash
python3 -m venv venv
```

Dadurch wird ein `venv`-Verzeichnis in Ihrem aktuellen Ordner erstellt, das die virtuelle Umgebung enthält.

<BaseQuiz id="cheatsheet-virtual-environments-1" correct="A">
<template #question>
Welcher Befehl wird verwendet, um eine virtuelle Umgebung mit <code>venv</code> zu erstellen?
</template>

<BaseQuizOption value="A" correct>A. <code>python -m venv venv</code></BaseQuizOption>
<BaseQuizOption value="B">B. <code>python create venv</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>venv create</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>python venv new</code></BaseQuizOption>
<BaseQuizAnswer>Der Befehl <code>python -m venv venv</code> erstellt eine virtuelle Umgebung. Das Flag <code>-m</code> führt das venv-Modul aus, und <code>venv</code> am Ende ist der Name des zu erstellenden Verzeichnisses.</BaseQuizAnswer>
</BaseQuiz>

2. Virtuelle Umgebung aktivieren

Unter Linux/macOS:

```bash
source venv/bin/activate
```

Unter Windows:

```bash
venv\Scripts\activate
```

Sobald sie aktiviert ist, sehen Sie `(venv)` am Anfang Ihrer Eingabeaufforderung, was anzeigt, dass die virtuelle Umgebung aktiv ist.

<BaseQuiz id="cheatsheet-virtual-environments-2" correct="B">
<template #question>
Wie aktivieren Sie eine virtuelle Umgebung unter Linux/macOS?
</template>

<BaseQuizOption value="A">A. <code>activate venv</code></BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>source venv/bin/activate</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>venv activate</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>python venv activate</code></BaseQuizOption>
<BaseQuizAnswer>Unter Linux/macOS aktivieren Sie eine virtuelle Umgebung mit <code>source venv/bin/activate</code>. Unter Windows würden Sie <code>venv\Scripts\activate</code> verwenden.</BaseQuizAnswer>
</BaseQuiz>

3. Pakete installieren

Installieren Sie mit aktivierter virtueller Umgebung Pakete mit pip:

```bash
pip install package_name
```

Installierte Pakete sind spezifisch für diese virtuelle Umgebung.

4. Virtuelle Umgebung deaktivieren

Um die virtuelle Umgebung zu verlassen:

```bash
deactivate
```

Das Präfix `(venv)` verschwindet aus Ihrer Eingabeaufforderung.

<BaseQuiz id="cheatsheet-virtual-environments-3" correct="A">
<template #question>
Was ist der Hauptzweck der Verwendung einer virtuellen Umgebung?
</template>

<BaseQuizOption value="A" correct>A. Zur Isolierung von Projektabhängigkeiten und Vermeidung der Füllung der Basis-Python-Installation</BaseQuizOption>
<BaseQuizOption value="B">B. Um Python schneller laufen zu lassen</BaseQuizOption>
<BaseQuizOption value="C">C. Zum Verschlüsseln von Python-Code</BaseQuizOption>
<BaseQuizOption value="D">D. Zum Kompilieren von Python in Maschinencode</BaseQuizOption>
<BaseQuizAnswer>Virtuelle Umgebungen ermöglichen es Ihnen, Python-Code in gekapselten Umgebungen zu testen und zu vermeiden, dass die Basis-Python-Installation mit Bibliotheken gefüllt wird, die möglicherweise nur für ein Projekt verwendet werden. Dies hilft bei der Verwaltung von Abhängigkeiten pro Projekt.</BaseQuizAnswer>
</BaseQuiz>

## virtualenv

1. virtualenv installieren

```bash
pip install virtualenv
```

1. virtualenvwrapper-win (Windows) installieren

```bash
pip install virtualenvwrapper-win
```

Verwendung:

1. Eine virtuelle Umgebung namens `HelloWorld` erstellen

```bash
mkvirtualenv HelloWorld
```

Alles, was wir jetzt installieren, ist spezifisch für dieses Projekt. Und verfügbar für die Projekte, die wir mit dieser Umgebung verbinden.

1. Projektverzeichnis festlegen

Um unsere virtuelle Umgebung an unser aktuelles Arbeitsverzeichnis zu binden, geben wir einfach Folgendes ein:

```bash
setprojectdir .
```

1. Deaktivieren

Um in der Befehlszeile zu etwas anderem überzugehen, geben Sie `deactivate` ein, um Ihre Umgebung zu deaktivieren.

```bash
deactivate
```

Beachten Sie, wie die Klammern verschwinden.

1. Workon

Öffnen Sie die Eingabeaufforderung und geben Sie `workon HelloWorld` ein, um die Umgebung zu aktivieren und in Ihren Stammprojektordner zu wechseln

```bash
workon HelloWorld
```

## Poetry

<base-disclaimer>
  <base-disclaimer-title>
    Von der <a href="https://python-poetry.org/">Poetry Website</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Poetry ist ein Werkzeug für das Abhängigkeitsmanagement und die Paketierung in Python. Es ermöglicht Ihnen, die Bibliotheken zu deklarieren, von denen Ihr Projekt abhängt, und es wird diese für Sie verwalten (installieren/aktualisieren).
  </base-disclaimer-content>
</base-disclaimer>

1. Poetry installieren

```bash
pip install --user poetry
```

2. Neues Projekt erstellen

```bash
poetry new my-project
```

Dies erstellt ein Verzeichnis `my-project`:

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

Die Datei `pyproject.toml` wird Ihr Projekt und seine Abhängigkeiten orchestrieren:

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

3. Pakete

Um Abhängigkeiten zu Ihrem Projekt hinzuzufügen, können Sie diese im Abschnitt `tool.poetry.dependencies` angeben:

```toml
[tool.poetry.dependencies]
pendulum = "^1.4"
```

Anstatt die Datei `pyproject.toml` manuell zu bearbeiten, können Sie auch den Befehl `add` verwenden, und er findet automatisch eine geeignete Versionsbeschränkung.

```bash
poetry add pendulum
```

Um die in `pyproject.toml` aufgeführten Abhängigkeiten zu installieren:

```bash
poetry install
```

Um Abhängigkeiten zu entfernen:

```bash
poetry remove pendulum
```

Weitere Informationen finden Sie in der [Dokumentation](https://poetry.eustace.io/docs/) oder lesen Sie hier:

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Python-Projekte mit Poetry und VSCode. Teil 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Python-Projekte mit Poetry und VSCode. Teil 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Python-Projekte mit Poetry und VSCode. Teil 3</router-link>

## Pipenv

<base-disclaimer>
  <base-disclaimer-title>
    Von der <a target="_blank" href="https://pipenv.pypa.io/en/latest/">Pipenv Website</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Pipenv ist ein Werkzeug, das das Beste aus allen Paketierungswelten (bundler, composer, npm, cargo, yarn, etc.) in die Python-Welt bringen soll. Windows ist in unserer Welt ein erstklassiger Bürger.
  </base-disclaimer-content>
</base-disclaimer>

1. Pipenv installieren

```bash
pip install pipenv
```

2. In Ihr Projektverzeichnis wechseln und die Pakete für Ihr Projekt installieren

```bash
cd my_project
pipenv install <package>
```

Pipenv installiert Ihr Paket und erstellt eine `Pipfile` für Sie im Verzeichnis Ihres Projekts. Die `Pipfile` wird verwendet, um zu verfolgen, welche Abhängigkeiten Ihr Projekt benötigt, falls Sie sie neu installieren müssen.

3. Pakete deinstallieren

```bash
pipenv uninstall <package>
```

4. Die virtuelle Umgebung aktivieren, die mit Ihrem Python-Projekt verknüpft ist

```bash
pipenv shell
```

5. Die virtuelle Umgebung verlassen

```bash
exit
```

Weitere Informationen und ein Video finden Sie unter [docs.pipenv.org](https://docs.pipenv.org/).

## Anaconda

<base-disclaimer>
  <base-disclaimer-title>
    <a target="k" href="https://anaconda.com/">Anaconda</a> ist ein weiteres beliebtes Werkzeug zur Verwaltung von Python-Paketen.
  </base-disclaimer-title>
  <base-disclaimer-content>
    Wo Pakete, Notebooks, Projekte und Umgebungen geteilt werden. Ihr Ort für kostenloses öffentliches Conda-Paket-Hosting.
  </base-disclaimer-content>
</base-disclaimer>

Verwendung:

1. Virtuelle Umgebung erstellen

```bash
conda create -n HelloWorld
```

2. Um die virtuelle Umgebung zu verwenden, aktivieren Sie sie durch:

```bash
conda activate HelloWorld
```

Alles, was jetzt installiert wird, ist spezifisch für das Projekt HelloWorld

3. Virtuelle Umgebung verlassen

```bash
conda deactivate
```

## UV

<base-disclaimer>
  <base-disclaimer-title>
    Aus der <a target="_blank" href="https://docs.astral.sh/uv/">UV Dokumentation</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    UV ist ein extrem schneller Python-Paketinstallations- und Resolver, der als direkter Ersatz für Pip- und Pip-Tools-Workflows konzipiert ist. UV ist 10-100x schneller als pip und bietet einheitliches Paketmanagement, Erstellung virtueller Umgebungen und Verwaltung von Python-Versionen.
  </base-disclaimer-content>
</base-disclaimer>

1. UV installieren

```bash
# Mit curl (Linux/macOS)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Mit pip oder pipx
pip install uv
```

2. Neues Projekt mit virtueller Umgebung erstellen

```bash
uv init my-project
cd my-project
```

3. Abhängigkeiten hinzufügen

```bash
uv add requests
```

4. Befehle in der Projektumgebung ausführen

```bash
uv run python script.py
```

5. Die virtuelle Umgebung manuell aktivieren (optional)

```bash
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

UV verwaltet virtuelle Umgebungen, Python-Versionen und Abhängigkeiten automatisch mit außergewöhnlicher Geschwindigkeit und Komfort.

## Relevante Links

- <router-link to="/cheatsheet/packaging">Packaging</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Python-Projekte mit Poetry und VSCode. Teil 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Python-Projekte mit Poetry und VSCode. Teil 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Python-Projekte mit Poetry und VSCode. Teil 3</router-link>
- <router-link to="/blog/python-uv-package-manager">UV: Der blitzschnelle Python Paketmanager</router-link>
- <router-link to="/builtin/import">import()</router-link>
