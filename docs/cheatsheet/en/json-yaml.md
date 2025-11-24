---
title: Python JSON and YAML - Python Cheatsheet
description: JSON stands for JavaScript Object Notation and is a lightweight format for storing and transporting data. JSON is often used when data is sent from a server to a web page.
labUrl: https://labex.io/labs/python-python-json-and-yaml-633659?course=python-cheatsheet
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
JSON and YAML
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## JSON

JSON stands for JavaScript Object Notation and is a lightweight format for storing and transporting data. JSON is often used when data is sent from a server to a web page.

```python
# Read JSON file: json.load() parses JSON from file object
import json
with open("filename.json", "r") as f:  # Open file in read mode
    content = json.load(f)  # Parse JSON and return Python dict/list
```

Write a JSON file with:

```python
# Write JSON file: json.dump() writes Python object as JSON
import json

content = {"name": "Joe", "age": 20}
with open("filename.json", "w") as f:  # Open file in write mode
    json.dump(content, f, indent=2)  # Write JSON with 2-space indentation
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Which function is used to write a Python dictionary to a JSON file?
</template>

<base-quiz-option value="A">A. <code>json.write()</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>json.dump()</code></base-quiz-option>
<base-quiz-option value="C">C. <code>json.save()</code></base-quiz-option>
<base-quiz-option value="D">D. <code>json.export()</code></base-quiz-option>
<base-quiz-answer value="B">The <code>json.dump()</code> function writes a Python object (like a dictionary) to a JSON file. <code>json.load()</code> is used to read JSON files.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## YAML

Compared to JSON, YAML allows a much better human maintainability and gives ability to add comments. It is a convenient choice for configuration files where a human will have to edit.

There are two main libraries allowing access to YAML files:

- [PyYaml](https://pypi.python.org/pypi/PyYAML)
- [Ruamel.yaml](https://pypi.python.org/pypi/ruamel.yaml)

Install them using `pip install` in your virtual environment.

The first one is easier to use but the second one, Ruamel, implements much better the YAML
specification, and allow for example to modify a YAML content without altering comments.

Open a YAML file with:

```python
# Read YAML file using ruamel.yaml library
from ruamel.yaml import YAML

with open("filename.yaml") as f:
    yaml=YAML()  # Create YAML parser instance
    yaml.load(f)  # Parse YAML and return Python dict/list
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
What is one advantage of YAML over JSON?
</template>

<base-quiz-option value="A">A. YAML files are smaller</base-quiz-option>
<base-quiz-option value="B">B. YAML is faster to parse</base-quiz-option>
<base-quiz-option value="C" correct>C. YAML allows comments and is more human-readable</base-quiz-option>
<base-quiz-option value="D">D. YAML is built into Python</base-quiz-option>
<base-quiz-answer value="C">YAML allows comments and is more human-readable than JSON, making it a convenient choice for configuration files that humans need to edit.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Anyconfig

[Anyconfig](https://pypi.python.org/pypi/anyconfig) is a very handy package, allowing to abstract completely the underlying configuration file format. It allows to load a Python dictionary from JSON, YAML, TOML, and so on.

Install it with:

```bash
pip install anyconfig
```

Usage:

```python
# anyconfig: load configuration files in various formats (JSON, YAML, TOML, etc.)
import anyconfig
conf1 = anyconfig.load("/path/to/foo/conf.d/a.yml")  # Auto-detects format
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
What does the anyconfig library allow you to do?
</template>

<base-quiz-option value="A" correct>A. Load configuration files in various formats (JSON, YAML, TOML) without specifying the format</base-quiz-option>
<base-quiz-option value="B">B. Convert between different configuration formats</base-quiz-option>
<base-quiz-option value="C">C. Validate configuration file syntax</base-quiz-option>
<base-quiz-option value="D">D. Encrypt configuration files</base-quiz-option>
<base-quiz-answer value="A">The anyconfig library abstracts the underlying configuration file format, allowing you to load Python dictionaries from JSON, YAML, TOML, and other formats without needing to know which format is being used.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Relevant links

- <router-link to="/cheatsheet/reading-and-writing-files">Reading and Writing Files</router-link>
- <router-link to="/cheatsheet/dictionaries">Python Dictionaries</router-link>
- <router-link to="/modules/json-module">The json Module</router-link>
- <router-link to="/blog/python-pathlib-essentials">10 Essential File System Operations Every Developer Should Know</router-link>
- <router-link to="/builtin/open">open()</router-link>
- <router-link to="/builtin/dict">dict()</router-link>
