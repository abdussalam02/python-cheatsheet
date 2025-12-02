---
title: 'Python JSON et YAML - Aide-mémoire Python'
description: "JSON (JavaScript Object Notation) est un format léger pour stocker et transporter des données. JSON est souvent utilisé lorsque les données sont envoyées d'un serveur à une page web."
labUrl: 'https://labex.io/fr/labs/python-python-json-and-yaml-633659?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
JSON et YAML
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## JSON

JSON signifie JavaScript Object Notation et est un format léger pour stocker et transporter des données. JSON est souvent utilisé lorsque des données sont envoyées d'un serveur à une page web.

```python
# Read JSON file: json.load() parses JSON from file object
import json
with open("filename.json", "r") as f:  # Open file in read mode
    content = json.load(f)  # Parse JSON and return Python dict/list
```

Écrire un fichier JSON avec :

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
Quelle fonction est utilisée pour écrire un dictionnaire Python dans un fichier JSON ?
</template>

<base-quiz-option value="A">A. <code>json.write()</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>json.dump()</code></base-quiz-option>
<base-quiz-option value="C">C. <code>json.save()</code></base-quiz-option>
<base-quiz-option value="D">D. <code>json.export()</code></base-quiz-option>
<base-quiz-answer value="B">La fonction <code>json.dump()</code> écrit un objet Python (comme un dictionnaire) dans un fichier JSON. <code>json.load()</code> est utilisée pour lire les fichiers JSON.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## YAML

Comparé au JSON, YAML permet une maintenabilité humaine bien meilleure et donne la possibilité d'ajouter des commentaires. C'est un choix pratique pour les fichiers de configuration qu'un humain devra éditer.

Il existe deux bibliothèques principales permettant d'accéder aux fichiers YAML :

- [PyYaml](https://pypi.python.org/pypi/PyYAML)
- [Ruamel.yaml](https://pypi.python.org/pypi/ruamel.yaml)

Installez-les en utilisant `pip install` dans votre environnement virtuel.

La première est plus facile à utiliser, mais la seconde, Ruamel, implémente beaucoup mieux la spécification YAML et permet par exemple de modifier un contenu YAML sans altérer les commentaires.

Ouvrir un fichier YAML avec :

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
Quel est un avantage de YAML par rapport à JSON ?
</template>

<base-quiz-option value="A">A. Les fichiers YAML sont plus petits</base-quiz-option>
<base-quiz-option value="B">B. YAML est plus rapide à analyser</base-quiz-option>
<base-quiz-option value="C" correct>C. YAML permet les commentaires et est plus lisible par l'homme</base-quiz-option>
<base-quiz-option value="D">D. YAML est intégré à Python</base-quiz-option>
<base-quiz-answer value="C">YAML permet les commentaires et est plus lisible par l'homme que JSON, ce qui en fait un choix pratique pour les fichiers de configuration que les humains doivent éditer.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Anyconfig

[Anyconfig](https://pypi.python.org/pypi/anyconfig) est un paquet très pratique, permettant d'abstraire complètement le format de fichier de configuration sous-jacent. Il permet de charger un dictionnaire Python à partir de JSON, YAML, TOML, et autres.

Installez-le avec :

```bash
pip install anyconfig
```

Utilisation :

```python
# anyconfig: load configuration files in various formats (JSON, YAML, TOML, etc.)
import anyconfig
conf1 = anyconfig.load("/path/to/foo/conf.d/a.yml")  # Auto-detects format
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-json-yaml-3">
<template #question>
Que permet la bibliothèque anyconfig ?
</template>

<base-quiz-option value="A" correct>A. Charger des fichiers de configuration dans divers formats (JSON, YAML, TOML) sans spécifier le format</base-quiz-option>
<base-quiz-option value="B">B. Convertir entre différents formats de configuration</base-quiz-option>
<base-quiz-option value="C">C. Valider la syntaxe des fichiers de configuration</base-quiz-option>
<base-quiz-option value="D">D. Crypter les fichiers de configuration</base-quiz-option>
<base-quiz-answer value="A">La bibliothèque anyconfig abstrait le format de fichier de configuration sous-jacent, vous permettant de charger des dictionnaires Python à partir de JSON, YAML, TOML et d'autres formats sans avoir besoin de savoir quel format est utilisé.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Liens pertinents

- <router-link to="/cheatsheet/reading-and-writing-files">Lecture et Écriture de Fichiers</router-link>
- <router-link to="/cheatsheet/dictionaries">Dictionnaires Python</router-link>
- <router-link to="/modules/json-module">Le Module json</router-link>
- <router-link to="/blog/python-pathlib-essentials">10 Opérations Essentielles sur le Système de Fichiers que Tout Développeur Devrait Connaître</router-link>
- <router-link to="/builtin/open">open()</router-link>
- <router-link to="/builtin/dict">dict()</router-link>
