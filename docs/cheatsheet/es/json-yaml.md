---
title: 'Python JSON y YAML - Hoja de Trucos de Python'
description: 'JSON (Notación de Objetos JavaScript) es un formato ligero para almacenar y transportar datos. Se usa frecuentemente al enviar datos desde un servidor a una página web.'
labUrl: 'https://labex.io/es/labs/python-python-json-and-yaml-633659?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
JSON y YAML
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## JSON

JSON significa JavaScript Object Notation y es un formato ligero para almacenar y transportar datos. JSON se utiliza a menudo cuando los datos se envían desde un servidor a una página web.

```python
# Read JSON file: json.load() parses JSON from file object
import json
with open("filename.json", "r") as f:  # Abrir archivo en modo lectura
    content = json.load(f)  # Analizar JSON y devolver dict/lista de Python
```

Escribir un archivo JSON con:

```python
# Write JSON file: json.dump() writes Python object as JSON
import json

content = {"name": "Joe", "age": 20}
with open("filename.json", "w") as f:  # Abrir archivo en modo escritura
    json.dump(content, f, indent=2)  # Escribir JSON con sangría de 2 espacios
```

<BaseQuiz id="cheatsheet-json-yaml-1" correct="B">
<template #question>
¿Qué función se utiliza para escribir un diccionario de Python en un archivo JSON?
</template>

<BaseQuizOption value="A">A. <code>json.write()</code></BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>json.dump()</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>json.save()</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>json.export()</code></BaseQuizOption>
<BaseQuizAnswer>La función <code>json.dump()</code> escribe un objeto de Python (como un diccionario) en un archivo JSON. <code>json.load()</code> se utiliza para leer archivos JSON.</BaseQuizAnswer>
</BaseQuiz>

## YAML

En comparación con JSON, YAML permite una mantenibilidad humana mucho mejor y da la capacidad de añadir comentarios. Es una opción conveniente para archivos de configuración que un humano tendrá que editar.

Hay dos bibliotecas principales que permiten el acceso a archivos YAML:

- [PyYaml](https://pypi.python.org/pypi/PyYAML)
- [Ruamel.yaml](https://pypi.python.org/pypi/ruamel.yaml)

Instálalas usando `pip install` en tu entorno virtual.

La primera es más fácil de usar, pero la segunda, Ruamel, implementa mucho mejor la especificación YAML y permite, por ejemplo, modificar un contenido YAML sin alterar los comentarios.

Abrir un archivo YAML con:

```python
# Read YAML file using ruamel.yaml library
from ruamel.yaml import YAML

with open("filename.yaml") as f:
    yaml=YAML()  # Crear instancia de analizador YAML
    yaml.load(f)  # Analizar YAML y devolver dict/lista de Python
```

<BaseQuiz id="cheatsheet-json-yaml-2" correct="C">
<template #question>
¿Cuál es una ventaja de YAML sobre JSON?
</template>

<BaseQuizOption value="A">A. Los archivos YAML son más pequeños</BaseQuizOption>
<BaseQuizOption value="B">B. YAML se analiza más rápido</BaseQuizOption>
<BaseQuizOption value="C" correct>C. YAML permite comentarios y es más legible para humanos</BaseQuizOption>
<BaseQuizOption value="D">D. YAML está integrado en Python</BaseQuizOption>
<BaseQuizAnswer>YAML permite comentarios y es más legible para humanos que JSON, lo que lo convierte en una opción conveniente para archivos de configuración que los humanos necesitan editar.</BaseQuizAnswer>
</BaseQuiz>

## Anyconfig

[Anyconfig](https://pypi.python.org/pypi/anyconfig) es un paquete muy útil que permite abstraer completamente el formato subyacente del archivo de configuración. Permite cargar un diccionario de Python desde JSON, YAML, TOML, y otros.

Instálalo con:

```bash
pip install anyconfig
```

Uso:

```python
# anyconfig: load configuration files in various formats (JSON, YAML, TOML, etc.)
import anyconfig
conf1 = anyconfig.load("/path/to/foo/conf.d/a.yml")  # Auto-detecta el formato
```

<BaseQuiz id="cheatsheet-json-yaml-3" correct="A">
<template #question>
¿Qué permite hacer la librería anyconfig?
</template>

<BaseQuizOption value="A" correct>A. Cargar archivos de configuración en varios formatos (JSON, YAML, TOML) sin especificar el formato</BaseQuizOption>
<BaseQuizOption value="B">B. Convertir entre diferentes formatos de configuración</BaseQuizOption>
<BaseQuizOption value="C">C. Validar la sintaxis de los archivos de configuración</BaseQuizOption>
<BaseQuizOption value="D">D. Cifrar archivos de configuración</BaseQuizOption>
<BaseQuizAnswer>La librería anyconfig abstrae el formato subyacente del archivo de configuración, permitiéndole cargar diccionarios de Python desde JSON, YAML, TOML y otros formatos sin necesidad de saber qué formato se está utilizando.</BaseQuizAnswer>
</BaseQuiz>

## Enlaces relevantes

- <router-link to="/cheatsheet/reading-and-writing-files">Lectura y Escritura de Archivos</router-link>
- <router-link to="/cheatsheet/dictionaries">Diccionarios de Python</router-link>
- <router-link to="/modules/json-module">El Módulo json</router-link>
- <router-link to="/blog/python-pathlib-essentials">10 Operaciones Esenciales del Sistema de Archivos que Todo Desarrollador Debe Conocer</router-link>
- <router-link to="/builtin/open">open()</router-link>
- <router-link to="/builtin/dict">dict()</router-link>
