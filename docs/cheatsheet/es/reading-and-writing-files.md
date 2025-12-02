---
title: 'Lectura y escritura de archivos - Hoja de trucos de Python'
description: "Para leer/escribir en un archivo en Python, querrás usar la declaración 'with', que cerrará el archivo automáticamente, gestionando los recursos disponibles."
labUrl: 'https://labex.io/es/labs/python-python-reading-and-writing-files-633663?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Lectura y Escritura de Archivos
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Para obtener una mirada más profunda a la manipulación de rutas de archivos y directorios, consulte la página <router-link to="/cheatsheet/file-directory-path">Rutas de Archivos y Directorios</router-link>.

## El proceso de lectura/escritura de archivos

Para leer/escribir en un archivo en Python, querrá usar la declaración `with`, que cerrará el archivo por usted cuando haya terminado, administrando los recursos disponibles.

## Abrir y leer archivos

La función `open` abre un archivo y devuelve un objeto de archivo correspondiente.

```python
# Leer archivo usando la declaración 'with': cierra automáticamente el archivo cuando termina
with open('/home/labex/project/hi.txt') as hello_file:
    hello_content = hello_file.read()  # Leer todo el contenido del archivo

hello_content
```

```output
'Hello World!'
```

<BaseQuiz id="cheatsheet-reading-and-writing-files-1" correct="A">
<template #question>
¿Cuál es la principal ventaja de usar la declaración <code>with</code> al abrir archivos?
</template>

<BaseQuizOption value="A" correct>A. El archivo se cierra automáticamente cuando termina, incluso si ocurre un error</BaseQuizOption>
<BaseQuizOption value="B">B. Los archivos se abren más rápido</BaseQuizOption>
<BaseQuizOption value="C">C. Los archivos se pueden abrir en modo lectura y escritura simultáneamente</BaseQuizOption>
<BaseQuizOption value="D">D. Los archivos se comprimen automáticamente</BaseQuizOption>
<BaseQuizAnswer>La declaración <code>with</code> asegura que el archivo se cierre automáticamente cuando el bloque finaliza, incluso si ocurre una excepción. Esto ayuda a administrar los recursos adecuadamente.</BaseQuizAnswer>
</BaseQuiz>

Alternativamente, puede usar el método _readlines()_ para obtener una lista de valores de cadena del archivo, una cadena por cada línea de texto:

```python
# método readlines(): devuelve una lista de cadenas, una por línea
with open('sonnet29.txt') as sonnet_file:
    sonnet_file.readlines()  # Devuelve una lista con cada línea como una cadena
```

```output
['When, in disgrace with fortune and men's eyes,\n',
 ' I all alone beweep my  outcast state,\n',
 "And trouble deaf heaven with my bootless cries,\n",
 "And look upon myself and curse my fate,']
```

También puede iterar a través del archivo línea por línea:

```python
# Iterar a través del archivo línea por línea (eficiente en memoria para archivos grandes)
with open('sonnet29.txt') as sonnet_file:
    for line in sonnet_file:  # El objeto archivo es iterable
        print(line, end='')  # Imprimir sin nueva línea extra
```

```output
When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,
```

## Escribir en archivos

```python
# Escribir en archivo: el modo 'w' sobrescribe el archivo existente
with open('bacon.txt', 'w') as bacon_file:  # 'w' = modo escritura
    bacon_file.write('Hello world!\n')  # Devuelve el número de caracteres escritos
```

```output
13
```

```python
# Añadir al archivo: el modo 'a' añade al archivo existente
with open('bacon.txt', 'a') as bacon_file:  # 'a' = modo añadir
    bacon_file.write('Bacon is not a vegetable.')
```

```output
25
```

```python
with open('bacon.txt') as bacon_file:
    content = bacon_file.read()

print(content)
```

```output
Hello world!
Bacon is not a vegetable.
```

<BaseQuiz id="cheatsheet-reading-and-writing-files-2" correct="B">
<template #question>
¿Cuál es la diferencia entre abrir un archivo con el modo <code>'w'</code> y el modo <code>'a'</code>?
</template>

<BaseQuizOption value="A">A. <code>'w'</code> es para leer, <code>'a'</code> es para escribir</BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>'w'</code> sobrescribe el archivo, <code>'a'</code> añade contenido al archivo</BaseQuizOption>
<BaseQuizOption value="C">C. <code>'w'</code> es para Windows, <code>'a'</code> es para Apple</BaseQuizOption>
<BaseQuizOption value="D">D. No hay diferencia</BaseQuizOption>
<BaseQuizAnswer>El modo <code>'w'</code> abre el archivo para escritura y sobrescribe cualquier contenido existente. El modo <code>'a'</code> abre el archivo para añadir, agregando nuevo contenido al final del archivo.</BaseQuizAnswer>
</BaseQuiz>

## Enlaces relevantes

- <router-link to="/cheatsheet/file-directory-path">Rutas de Archivos y Directorios</router-link>
- <router-link to="/cheatsheet/json-yaml">JSON y YAML</router-link>
- <router-link to="/blog/python-pathlib-essentials">10 Operaciones Esenciales del Sistema de Archivos que Todo Desarrollador Debe Conocer</router-link>
- <router-link to="/builtin/open">open()</router-link>
- <router-link to="/builtin/print">print()</router-link>
