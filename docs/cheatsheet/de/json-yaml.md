---
title: 'Python JSON und YAML - Python Spickzettel'
description: 'JSON (JavaScript Object Notation) ist ein leichtgewichtiges Format zur Speicherung und Übertragung von Daten. JSON wird häufig verwendet, wenn Daten von einem Server an eine Webseite gesendet werden.'
labUrl: 'https://labex.io/de/labs/python-python-json-and-yaml-633659?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
JSON und YAML
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## JSON

JSON steht für JavaScript Object Notation und ist ein leichtgewichtiges Format zum Speichern und Übertragen von Daten. JSON wird häufig verwendet, wenn Daten von einem Server an eine Webseite gesendet werden.

```python
# Read JSON file: json.load() parses JSON from file object
import json
with open("filename.json", "r") as f:  # Open file in read mode
    content = json.load(f)  # Parse JSON and return Python dict/list
```

Schreiben Sie eine JSON-Datei mit:

```python
# Write JSON file: json.dump() writes Python object as JSON
import json

content = {"name": "Joe", "age": 20}
with open("filename.json", "w") as f:  # Open file in write mode
    json.dump(content, f, indent=2)  # Write JSON with 2-space indentation
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-json-yaml-1">
<template #question>
Welche Funktion wird verwendet, um ein Python-Wörterbuch in eine JSON-Datei zu schreiben?
</template>

<base-quiz-option value="A">A. <code>json.write()</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>json.dump()</code></base-quiz-option>
<base-quiz-option value="C">C. <code>json.save()</code></base-quiz-option>
<base-quiz-option value="D">D. <code>json.export()</code></base-quiz-option>
<base-quiz-answer value="B">Die Funktion <code>json.dump()</code> schreibt ein Python-Objekt (wie ein Wörterbuch) in eine JSON-Datei. <code>json.load()</code> wird zum Lesen von JSON-Dateien verwendet.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## YAML

Im Vergleich zu JSON ermöglicht YAML eine wesentlich bessere menschliche Wartbarkeit und bietet die Möglichkeit, Kommentare hinzuzufügen. Es ist eine bequeme Wahl für Konfigurationsdateien, die von Menschen bearbeitet werden müssen.

Es gibt zwei Hauptbibliotheken, die den Zugriff auf YAML-Dateien ermöglichen:

- [PyYaml](https://pypi.python.org/pypi/PyYAML)
- [Ruamel.yaml](https://pypi.python.org/pypi/ruamel.yaml)

Installieren Sie diese mit `pip install` in Ihrer virtuellen Umgebung.

Die erste ist einfacher zu verwenden, aber die zweite, Ruamel, implementiert die YAML-Spezifikation wesentlich besser und erlaubt es beispielsweise, einen YAML-Inhalt zu ändern, ohne Kommentare zu verändern.

Öffnen Sie eine YAML-Datei mit:

```python
# Read YAML file using ruamel.yaml library
from ruamel.yaml import YAML

with open("filename.yaml") as f:
    yaml=YAML()  # Create YAML parser instance
    yaml.load(f)  # Parse YAML and return Python dict/list
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-json-yaml-2">
<template #question>
Was ist ein Vorteil von YAML gegenüber JSON?
</template>

<base-quiz-option value="A">A. YAML-Dateien sind kleiner</base-quiz-option>
<base-quiz-option value="B">B. YAML wird schneller geparst</base-quiz-option>
<base-quiz-option value="C" correct>C. YAML erlaubt Kommentare und ist besser lesbar für Menschen</base-quiz-option>
<base-quiz-option value="D">D. YAML ist in Python integriert</base-quiz-option>
<base-quiz-answer value="C">YAML erlaubt Kommentare und ist besser lesbar für Menschen als JSON, was es zu einer bequemen Wahl für Konfigurationsdateien macht, die von Menschen bearbeitet werden müssen.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Anyconfig

[Anyconfig](https://pypi.python.org/pypi/anyconfig) ist ein sehr nützliches Paket, das es ermöglicht, das zugrunde liegende Konfigurationsdateiformat vollständig zu abstrahieren. Es erlaubt das Laden eines Python-Wörterbuchs aus JSON, YAML, TOML und Ähnlichem.

Installieren Sie es mit:

```bash
pip install anyconfig
```

Verwendung:

```python
# anyconfig: load configuration files in various formats (JSON, YAML, TOML, etc.)
import anyconfig
conf1 = anyconfig.load("/path/to/foo/conf.d/a.yml")  # Auto-detects format
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-json-yaml-3">
<template #question>
Was ermöglicht Ihnen die anyconfig-Bibliothek?
</template>

<base-quiz-option value="A" correct>A. Konfigurationsdateien in verschiedenen Formaten (JSON, YAML, TOML) zu laden, ohne das Format angeben zu müssen</base-quiz-option>
<base-quiz-option value="B">B. Zwischen verschiedenen Konfigurationsformaten zu konvertieren</base-quiz-option>
<base-quiz-option value="C">C. Die Syntax von Konfigurationsdateien zu validieren</base-quiz-option>
<base-quiz-option value="D">D. Konfigurationsdateien zu verschlüsseln</base-quiz-option>
<base-quiz-answer value="A">Die anyconfig-Bibliothek abstrahiert das zugrunde liegende Konfigurationsdateiformat und ermöglicht es Ihnen, Python-Wörterbücher aus JSON, YAML, TOML und anderen Formaten zu laden, ohne wissen zu müssen, welches Format verwendet wird.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Relevante Links

- <router-link to="/cheatsheet/reading-and-writing-files">Dateien lesen und schreiben</router-link>
- <router-link to="/cheatsheet/dictionaries">Python-Wörterbücher</router-link>
- <router-link to="/modules/json-module">Das json-Modul</router-link>
- <router-link to="/blog/python-pathlib-essentials">10 wesentliche Dateioperationen, die jeder Entwickler kennen sollte</router-link>
- <router-link to="/builtin/open">open()</router-link>
- <router-link to="/builtin/dict">dict()</router-link>
