---
title: 'Rutas de Archivos y Directorios - Hoja de Trucos de Python'
description: 'Hay dos módulos principales en Python que se ocupan de la manipulación de rutas: el módulo os.path y el módulo pathlib.'
labUrl: 'https://labex.io/es/labs/python-python-file-and-directory-path-manipulation-633657?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Manejo de Rutas de Archivos y Directorios
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Para una inmersión profunda en las operaciones prácticas del sistema de archivos, consulte nuestra publicación de blog: <router-link to="/blog/python-pathlib-essentials">10 Operaciones Esenciales del Sistema de Archivos que Todo Desarrollador Debe Conocer</router-link>.

Hay dos módulos principales en Python que se ocupan de la manipulación de rutas.
Uno es el módulo <router-link to="/modules/os-module">os.path</router-link> y el otro es el módulo <router-link to="/modules/pathlib-module">pathlib</router-link>.

<base-disclaimer>
  <base-disclaimer-title>
    Pathlib vs Módulo OS
  </base-disclaimer-title>
  <base-disclaimer-content>
    <code>pathlib</code> proporciona mucha más funcionalidad que las enumeradas anteriormente, como obtener el nombre del archivo, obtener la extensión del archivo, leer/escribir un archivo sin abrirlo manualmente, etc. Consulte la <a target="_blank" href="https://docs.python.org/3/library/pathlib.html">documentación oficial</a> si tiene la intención de saber más.
  </base-disclaimer-content>
</base-disclaimer>

## Rutas de Linux y Windows

En Windows, las rutas se escriben usando barras invertidas (`\`) como separador entre
nombres de carpetas. En sistemas operativos basados en Unix como macOS, Linux y BSDs,
se utiliza la barra inclinada hacia adelante (`/`) como separador de ruta. Unir rutas puede ser
un dolor de cabeza si su código necesita funcionar en diferentes plataformas.

Afortunadamente, el módulo `pathlib` de Python proporciona una forma sencilla de manejar esto.

Usando `pathlib` en \*nix:

```python
# pathlib.Path: manejo de rutas multiplataforma
from pathlib import Path

print(Path('usr').joinpath('bin').joinpath('spam'))  # Unir componentes de ruta
```

```output
usr/bin/spam
```

`pathlib` también proporciona un atajo para `joinpath` usando el operador `/`:

```python
# Operador Path (/): forma conveniente de unir rutas (multiplataforma)
from pathlib import Path

print(Path('usr') / 'bin' / 'spam')  # Usar el operador / en lugar de joinpath()
```

```output
usr/bin/spam
```

Observe que el separador de ruta es diferente entre Windows y los sistemas operativos basados en Unix, por eso querrá usar `pathlib` en lugar de
agregar cadenas para unir rutas.

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-file-directory-path-1">
<template #question>
¿Cuál es la forma correcta de unir rutas usando pathlib en Python?
</template>

<base-quiz-option value="A">A. <code>Path('usr') + 'bin' + 'spam'</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>Path('usr') / 'bin' / 'spam'</code></base-quiz-option>
<base-quiz-option value="C">C. <code>Path('usr').join('bin').join('spam')</code></base-quiz-option>
<base-quiz-option value="D">D. <code>Path('usr/bin/spam')</code></base-quiz-option>
<base-quiz-answer value="B">El operador <code>/</code> es la forma recomendada para unir rutas con pathlib. Funciona en múltiples plataformas y es más legible que la concatenación de cadenas.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Unir rutas es útil si necesita crear diferentes rutas de archivo bajo el
mismo directorio.

Usando `pathlib` en \*nix:

```python
# Path.home(): obtener el directorio de inicio del usuario, combinar con nombres de archivo
my_files = ['accounts.txt', 'details.csv', 'invite.docx']
home = Path.home()  # Obtener la ruta del directorio de inicio
for filename in my_files:
    print(home / filename)  # Combinar la ruta de inicio con cada nombre de archivo
```

```output
/home/labex/project/accounts.txt
/home/labex/project/details.csv
/home/labex/project/invite.docx
```

### Expandir el directorio de inicio del usuario

Usando `os.path.expanduser()` para expandir `~` al directorio de inicio del usuario:

```python
import os.path

# Expandir ~ al directorio de inicio del usuario
print(os.path.expanduser('~'))
```

```output
/home/labex/project
```

```python
# Expandir ~/Documents a la ruta completa
print(os.path.expanduser('~/Documents'))
```

```output
/home/labex/project/Documents
```

```python
# Funciona con rutas que contienen ~
print(os.path.expanduser('~/myfile.txt'))
```

```output
/home/labex/project/myfile.txt
```

## El directorio de trabajo actual

Puede obtener el directorio de trabajo actual usando `pathlib`:

```python
# Path.cwd(): obtener el directorio de trabajo actual
from pathlib import Path

print(Path.cwd())  # Devuelve el directorio de trabajo actual como objeto Path
```

```output
/home/labex/project
```

## Creación de nuevas carpetas

Usando `pathlib` en \*nix:

```python
from pathlib import Path
cwd = Path.cwd()
(cwd / 'delicious' / 'walnut' / 'waffles').mkdir()
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.6/pathlib.py", line 1226, in mkdir
    self._accessor.mkdir(self, mode)
  File "/usr/lib/python3.6/pathlib.py", line 387, in wrapped
    return strfunc(str(pathobj), *args)
FileNotFoundError: [Errno 2] No such file or directory: '/home/labex/project/delicious/walnut/waffles'
```

¡Oh no, obtuvimos un error molesto! La razón es que el directorio 'delicious' no
existe, por lo que no podemos crear los directorios 'walnut' y 'waffles' debajo de él. Para solucionar esto, haga lo siguiente:

```python
# mkdir(parents=True): crear directorio y todos los directorios padre si es necesario
from pathlib import Path
cwd = Path.cwd()
(cwd / 'delicious' / 'walnut' / 'waffles').mkdir(parents=True)  # Crear directorios anidados
```

Y todo está bien :)

## Rutas Absolutas vs. Relativas

Hay dos formas de especificar una ruta de archivo.

- Una **ruta absoluta**, que siempre comienza con la carpeta raíz
- Una **ruta relativa**, que es relativa al directorio de trabajo actual del programa

También están las carpetas punto (`.`) y doble punto (`..`). Estas no son carpetas reales, sino nombres especiales que se pueden usar en una ruta. Un solo punto (“punto”) para un nombre de carpeta es una abreviatura de “este directorio”. Dos puntos (“doble punto”) significa “la carpeta padre”.

### Manejo de rutas absolutas

Para ver si una ruta es una ruta absoluta usando `pathlib`:

```python
from pathlib import Path
Path('/').is_absolute()
```

```output
True
```

```python
Path('..').is_absolute()
```

```output
False
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-file-directory-path-2">
<template #question>
¿Qué devuelve <code>Path('/').is_absolute()</code>?
</template>

<base-quiz-option value="A" correct>A. <code>True</code></base-quiz-option>
<base-quiz-option value="B">B. <code>False</code></base-quiz-option>
<base-quiz-option value="C">C. <code>None</code></base-quiz-option>
<base-quiz-option value="D">D. <code>'/'</code></base-quiz-option>
<base-quiz-answer value="A">El método <code>is_absolute()</code> devuelve <code>True</code> para rutas absolutas (aquellas que comienzan con <code>/</code> en Unix o una letra de unidad en Windows).</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Puede extraer una ruta absoluta con `pathlib`:

```python
from pathlib import Path
print(Path.cwd())
```

```output
/home/labex/project
```

```python
print(Path('..').resolve())
```

```output
/home
```

### Manejo de rutas relativas

Puede obtener una ruta relativa desde una ruta de inicio hasta otra ruta usando `pathlib`:

```python
from pathlib import Path
print(Path('/etc/passwd').relative_to('/'))
```

```output
etc/passwd
```

## Validez de la Ruta y el Archivo

### Comprobar si un archivo/directorio existe

Usando `pathlib` en \*nix:

```python
from pathlib import Path

Path('.').exists()
```

```output
True
```

```python
Path('setup.py').exists()
```

```output
True
```

```python
Path('/etc').exists()
```

```output
True
```

```python
Path('nonexistentfile').exists()
```

```output
False
```

### Comprobar si una ruta es un archivo

Usando `pathlib` en \*nix:

```python
from pathlib import Path

Path('setup.py').is_file()
```

```output
True
```

```python
Path('/home').is_file()
```

```output
False
```

```python
Path('nonexistentfile').is_file()
```

```output
False
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-file-directory-path-3">
<template #question>
¿Qué devolverá <code>Path('setup.py').is_file()</code> si existe setup.py?
</template>

<base-quiz-option value="A">A. <code>'setup.py'</code></base-quiz-option>
<base-quiz-option value="B">B. <code>False</code></base-quiz-option>
<base-quiz-option value="C" correct>C. <code>True</code></base-quiz-option>
<base-quiz-option value="D">D. <code>None</code></base-quiz-option>
<base-quiz-answer value="C">El método <code>is_file()</code> devuelve <code>True</code> si la ruta existe y es un archivo, <code>False</code> en caso contrario.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

### Comprobar si una ruta es un directorio

Usando `pathlib` en \*nix:

```python
from pathlib import Path

Path('/').is_dir()
```

```output
True
```

```python
Path('setup.py').is_dir()
```

```output
False
```

```python
Path('/spam').is_dir()
```

```output
False
```

## Obtener el tamaño de un archivo en bytes

Usando `pathlib` en \*nix:

```python
from pathlib import Path

stat = Path('/bin/python3.6').stat()
print(stat) # stat contiene otra información sobre el archivo también
```

```output
os.stat_result(st_mode=33261, st_ino=141087, st_dev=2051, st_nlink=2, st_uid=0,
--snip--
st_gid=0, st_size=10024, st_atime=1517725562, st_mtime=1515119809, st_ctime=1517261276)
```

```python
print(stat.st_size) # tamaño en bytes
```

```output
10024
```

## Listar directorios

Listar el contenido de un directorio usando `pathlib` en \*nix:

```python
from pathlib import Path

for f in Path('/usr/bin').iterdir():
    print(f)
```

```output
...
/usr/bin/tiff2rgba
/usr/bin/iconv
/usr/bin/ldd
/usr/bin/cache_restore
/usr/bin/udiskie
/usr/bin/unix2dos
/usr/bin/t1reencode
/usr/bin/epstopdf
/usr/bin/idle3
...
```

## Tamaños de archivos de directorio

<base-warning>
  <base-warning-title>
    ADVERTENCIA
  </base-warning-title>
  <base-warning-content>
    ¡Los directorios también tienen un tamaño! Por lo tanto, es posible que desee verificar si una ruta es un archivo o un directorio utilizando los métodos discutidos en la sección anterior.
  </base-warning-content>
</base-warning>

Usando `pathlib` en \*nix:

```python
from pathlib import Path

total_size = 0
for sub_path in Path('/usr/bin').iterdir():
    total_size += sub_path.stat().st_size

print(total_size)
```

```output
1903178911
```

## Copiar archivos y carpetas

El módulo `shutil` proporciona funciones para copiar archivos, así como carpetas enteras.

```python
import shutil

shutil.copy('/tmp/spam.txt', '/tmp/delicious')
```

```output
/tmp/delicious/spam.txt
```

```python
shutil.copy('/tmp/eggs.txt', '/tmp/delicious/eggs2.txt')
```

```output
/tmp/delicious/eggs2.txt
```

<base-quiz>
<base-quiz-question correct="D" id="cheatsheet-file-directory-path-4">
<template #question>
¿Qué función debe usar para copiar un árbol de directorios completo, incluidos todos los subdirectorios y archivos?
</template>

<base-quiz-option value="A">A. <code>shutil.copy()</code></base-quiz-option>
<base-quiz-option value="B">B. <code>Path.copy()</code></base-quiz-option>
<base-quiz-option value="C">C. <code>os.copy()</code></base-quiz-option>
<base-quiz-option value="D" correct>D. <code>shutil.copytree()</code></base-quiz-option>
<base-quiz-answer value="D">La función <code>shutil.copytree()</code> copia un árbol de directorios completo recursivamente, mientras que <code>shutil.copy()</code> solo copia un único archivo.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Mientras que `shutil.copy()` copiará un solo archivo, `shutil.copytree()` copiará una carpeta completa y cada carpeta y archivo que contenga:

```python
import shutil

shutil.copytree('/tmp/bacon', '/tmp/bacon_backup')
```

```output
/tmp/bacon_backup
```

## Mover y Renombrar

```python
import shutil

shutil.move('/tmp/bacon.txt', '/tmp/eggs')
```

```output
/tmp/eggs/bacon.txt
```

La ruta de destino también puede especificar un nombre de archivo. En el siguiente ejemplo, el archivo de origen se mueve y se renombra:

```python
shutil.move('/tmp/bacon.txt', '/tmp/eggs/new_bacon.txt')
```

```output
/tmp/eggs/new_bacon.txt
```

Si no existe la carpeta eggs, entonces `move()` renombrará bacon.txt a un archivo llamado eggs:

```python
shutil.move('/tmp/bacon.txt', '/tmp/eggs')
```

```output
/tmp/eggs
```

## Eliminar archivos y carpetas

- Llamar a `Path.unlink()` eliminará el archivo en la ruta.
- Llamar a `Path.rmdir()` eliminará la carpeta en la ruta. Esta carpeta debe estar vacía de cualquier archivo o carpeta.
- Llamar a `shutil.rmtree(path)` eliminará la carpeta en la ruta, y todos los archivos y carpetas que contenga también se eliminarán.

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-file-directory-path-5">
<template #question>
¿Qué método puede eliminar un directorio no vacío y todo su contenido?
</template>

<base-quiz-option value="A">A. <code>Path.rmdir()</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>shutil.rmtree()</code></base-quiz-option>
<base-quiz-option value="C">C. <code>Path.unlink()</code></base-quiz-option>
<base-quiz-option value="D">D. <code>os.remove()</code></base-quiz-option>
<base-quiz-answer value="B">La función <code>shutil.rmtree()</code> puede eliminar un directorio y todo su contenido recursivamente. <code>Path.rmdir()</code> solo funciona en directorios vacíos.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Recorrer un Árbol de Directorios

El objeto `Path` tiene un método `rglob()` para iterar recursivamente sobre archivos y directorios.

```python
from pathlib import Path

p = Path('/tmp/delicious')
for i in p.rglob('*'):
    print(i)
```

```output
/tmp/delicious/cats
/tmp/delicious/walnut
/tmp/delicious/spam.txt
/tmp/delicious/cats/catnames.txt
/tmp/delicious/cats/zophie.jpg
/tmp/delicious/walnut/waffles
/tmp/delicious/walnut/waffles/butter.txt
```

## Enlaces relevantes

- <router-link to="/cheatsheet/reading-and-writing-files">Lectura y Escritura de Archivos</router-link>
- <router-link to="/blog/python-pathlib-essentials">10 Operaciones Esenciales del Sistema de Archivos que Todo Desarrollador Debe Conocer</router-link>
- <router-link to="/builtin/open">open()</router-link>
