---
title: 'Datei- und Verzeichnispfade - Python Spickzettel'
description: 'In Python gibt es zwei Hauptmodule zur Pfadmanipulation: das os.path-Modul und das pathlib-Modul.'
labUrl: 'https://labex.io/de/labs/python-python-file-and-directory-path-manipulation-633657?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Umgang mit Datei- und Verzeichnispfaden
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Für eine eingehende Beschäftigung mit praktischen Dateisystemoperationen lesen Sie unseren Blogbeitrag: <router-link to="/blog/python-pathlib-essentials">10 Essential File System Operations Every Developer Should Know</router-link>.

In Python gibt es zwei Hauptmodule, die sich mit der Pfadmanipulation befassen.
Eines ist das Modul <router-link to="/modules/os-module">os.path</router-link> und das andere ist das Modul <router-link to="/modules/pathlib-module">pathlib</router-link>.

<base-disclaimer>
  <base-disclaimer-title>
    Pathlib vs OS Module
  </base-disclaimer-title>
  <base-disclaimer-content>
    <code>pathlib</code> bietet weitaus mehr Funktionalität als die oben genannten, wie z. B. das Abrufen des Dateinamens, das Abrufen der Dateierweiterung, das Lesen/Schreiben einer Datei ohne manuelles Öffnen usw. Sehen Sie sich die <a target="_blank" href="https://docs.python.org/3/library/pathlib.html">offizielle Dokumentation</a> an, wenn Sie mehr erfahren möchten.
  </base-disclaimer-content>
</base-disclaimer>

## Linux- und Windows-Pfade

Unter Windows werden Pfade mit umgekehrten Schrägstrichen (`\`) als Trennzeichen zwischen
Ordnernamen geschrieben. Auf Unix-basierten Betriebssystemen wie macOS, Linux und BSDs wird der Schrägstrich (`/`) als Pfadtrennzeichen verwendet. Das Verknüpfen von Pfaden kann ein Problem darstellen, wenn Ihr Code auf verschiedenen Plattformen funktionieren soll.

Glücklicherweise bietet das `pathlib`-Modul von Python eine einfache Möglichkeit, dies zu handhaben.

Verwendung von `pathlib` unter \*nix:

```python
# pathlib.Path: plattformübergreifende Pfadbehandlung
from pathlib import Path

print(Path('usr').joinpath('bin').joinpath('spam'))  # Pfadkomponenten verknüpfen
```

```output
usr/bin/spam
```

`pathlib` bietet auch eine Abkürzung für `joinpath` mithilfe des `/`-Operators:

```python
# Path operator (/): bequeme Möglichkeit, Pfade zu verknüpfen (plattformübergreifend)
from pathlib import Path

print(Path('usr') / 'bin' / 'spam')  # / Operator anstelle von joinpath() verwenden
```

```output
usr/bin/spam
```

Beachten Sie, dass sich das Pfadtrennzeichen zwischen Windows und Unix-basierten Betriebssystemen unterscheidet. Deshalb sollten Sie `pathlib` verwenden, anstatt Zeichenketten zusammenzufügen, um Pfade zu verknüpfen.

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-file-directory-path-1">
<template #question>
What is the correct way to join paths using pathlib in Python?
</template>

<base-quiz-option value="A">A. <code>Path('usr') + 'bin' + 'spam'</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>Path('usr') / 'bin' / 'spam'</code></base-quiz-option>
<base-quiz-option value="C">C. <code>Path('usr').join('bin').join('spam')</code></base-quiz-option>
<base-quiz-option value="D">D. <code>Path('usr/bin/spam')</code></base-quiz-option>
<base-quiz-answer value="B">Der <code>/</code> Operator ist die empfohlene Methode, um Pfade mit pathlib zu verknüpfen. Er funktioniert plattformübergreifend und ist lesbarer als die Zeichenkettenverkettung.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Das Verknüpfen von Pfaden ist hilfreich, wenn Sie verschiedene Dateipfade unter demselben Verzeichnis erstellen müssen.

Verwendung von `pathlib` unter \*nix:

```python
# Path.home(): Benutzer-Home-Verzeichnis abrufen, mit Dateinamen kombinieren
my_files = ['accounts.txt', 'details.csv', 'invite.docx']
home = Path.home()  # Home-Verzeichnis-Pfad abrufen
for filename in my_files:
    print(home / filename)  # Home-Pfad mit jedem Dateinamen kombinieren
```

```output
/home/labex/project/accounts.txt
/home/labex/project/details.csv
/home/labex/project/invite.docx
```

### Erweitern des Benutzer-Home-Verzeichnisses

Verwendung von `os.path.expanduser()`, um `~` in das Home-Verzeichnis des Benutzers zu erweitern:

```python
import os.path

# ~ in das Home-Verzeichnis des Benutzers erweitern
print(os.path.expanduser('~'))
```

```output
/home/labex/project
```

```python
# ~/Documents in den vollständigen Pfad erweitern
print(os.path.expanduser('~/Documents'))
```

```output
/home/labex/project/Documents
```

```python
# Funktioniert mit Pfaden, die ~ enthalten
print(os.path.expanduser('~/myfile.txt'))
```

```output
/home/labex/project/myfile.txt
```

## Das aktuelle Arbeitsverzeichnis

Sie können das aktuelle Arbeitsverzeichnis mit `pathlib` abrufen:

```python
# Path.cwd(): aktuelles Arbeitsverzeichnis abrufen
from pathlib import Path

print(Path.cwd())  # Gibt das aktuelle Arbeitsverzeichnis als Path-Objekt zurück
```

```output
/home/labex/project
```

## Erstellen neuer Ordner

Verwendung von `pathlib` unter \*nix:

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

Oh nein, wir haben einen hässlichen Fehler bekommen! Der Grund ist, dass das Verzeichnis 'delicious' nicht existiert, sodass wir die Verzeichnisse 'walnut' und 'waffles' nicht darunter erstellen können. Um dies zu beheben, tun Sie Folgendes:

```python
# mkdir(parents=True): Verzeichnis und alle übergeordneten Verzeichnisse erstellen, falls erforderlich
from pathlib import Path
cwd = Path.cwd()
(cwd / 'delicious' / 'walnut' / 'waffles').mkdir(parents=True)  # Verschachtelte Verzeichnisse erstellen
```

Und alles ist gut :)

## Absolute vs. Relative Pfade

Es gibt zwei Möglichkeiten, einen Dateipfad anzugeben.

- Ein **absoluter Pfad**, der immer mit dem Stammverzeichnis beginnt
- Ein **relativer Pfad**, der sich auf das aktuelle Arbeitsverzeichnis des Programms bezieht

Es gibt auch die Ordner Punkt (`.`) und Punkt-Punkt (`..`). Dies sind keine echten Ordner, sondern spezielle Namen, die in einem Pfad verwendet werden können. Ein einzelner Punkt („Punkt“) für einen Ordnernamen ist eine Kurzform für „dieses Verzeichnis“. Zwei Punkte („Punkt-Punkt“) bedeuten „das übergeordnete Verzeichnis“.

### Umgang mit absoluten Pfaden

Um zu sehen, ob ein Pfad ein absoluter Pfad ist, verwenden Sie `pathlib`:

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
What does <code>Path('/').is_absolute()</code> return?
</template>

<base-quiz-option value="A" correct>A. <code>True</code></base-quiz-option>
<base-quiz-option value="B">B. <code>False</code></base-quiz-option>
<base-quiz-option value="C">C. <code>None</code></base-quiz-option>
<base-quiz-option value="D">D. <code>'/'</code></base-quiz-option>
<base-quiz-answer value="A">Die Methode <code>is_absolute()</code> gibt <code>True</code> für absolute Pfade zurück (solche, die unter Unix mit <code>/</code> oder unter Windows mit einem Laufwerksbuchstaben beginnen).</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Sie können einen absoluten Pfad mit `pathlib` extrahieren:

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

### Umgang mit relativen Pfaden

Sie können einen relativen Pfad von einem Startpfad zu einem anderen Pfad mit `pathlib` abrufen:

```python
from pathlib import Path
print(Path('/etc/passwd').relative_to('/'))
```

```output
etc/passwd
```

## Pfad- und Dateigültigkeit

### Überprüfen, ob eine Datei/ein Verzeichnis existiert

Verwendung von `pathlib` unter \*nix:

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

### Überprüfen, ob ein Pfad eine Datei ist

Verwendung von `pathlib` unter \*nix:

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
What will <code>Path('setup.py').is_file()</code> return if setup.py exists?
</template>

<base-quiz-option value="A">A. <code>'setup.py'</code></base-quiz-option>
<base-quiz-option value="B">B. <code>False</code></base-quiz-option>
<base-quiz-option value="C" correct>C. <code>True</code></base-quiz-option>
<base-quiz-option value="D">D. <code>None</code></base-quiz-option>
<base-quiz-answer value="C">Die Methode <code>is_file()</code> gibt <code>True</code> zurück, wenn der Pfad existiert und eine Datei ist, andernfalls <code>False</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

### Überprüfen, ob ein Pfad ein Verzeichnis ist

Verwendung von `pathlib` unter \*nix:

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

## Größe einer Datei in Bytes abrufen

Verwendung von `pathlib` unter \*nix:

```python
from pathlib import Path

stat = Path('/bin/python3.6').stat()
print(stat) # stat enthält auch einige andere Informationen über die Datei
```

```output
os.stat_result(st_mode=33261, st_ino=141087, st_dev=2051, st_nlink=2, st_uid=0,
--snip--
st_gid=0, st_size=10024, st_atime=1517725562, st_mtime=1515119809, st_ctime=1517261276)
```

```python
print(stat.st_size) # Größe in Bytes
```

```output
10024
```

## Verzeichnisse auflisten

Verzeichnisinhalte auflisten mit `pathlib` unter \*nix:

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

## Dateigrößen von Verzeichnissen

<base-warning>
  <base-warning-title>
    WARNUNG
  </base-warning-title>
  <base-warning-content>
    Verzeichnisse selbst haben auch eine Größe! Sie sollten also mit den Methoden aus den oben genannten Abschnitten überprüfen, ob ein Pfad eine Datei oder ein Verzeichnis ist.
  </base-warning-content>
</base-warning>

Verwendung von `pathlib` unter \*nix:

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

## Dateien und Ordner kopieren

Das Modul `shutil` bietet Funktionen zum Kopieren von Dateien sowie ganzer Ordner.

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
Which function should you use to copy an entire directory tree including all subdirectories and files?
</template>

<base-quiz-option value="A">A. <code>shutil.copy()</code></base-quiz-option>
<base-quiz-option value="B">B. <code>Path.copy()</code></base-quiz-option>
<base-quiz-option value="C">C. <code>os.copy()</code></base-quiz-option>
<base-quiz-option value="D" correct>D. <code>shutil.copytree()</code></base-quiz-option>
<base-quiz-answer value="D">Die Funktion <code>shutil.copytree()</code> kopiert einen gesamten Verzeichnisbaum rekursiv, während <code>shutil.copy()</code> nur eine einzelne Datei kopiert.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Während `shutil.copy()` eine einzelne Datei kopiert, kopiert `shutil.copytree()` einen gesamten Ordner und jeden darin enthaltenen Ordner und jede darin enthaltene Datei:

```python
import shutil

shutil.copytree('/tmp/bacon', '/tmp/bacon_backup')
```

```output
/tmp/bacon_backup
```

## Verschieben und Umbenennen

```python
import shutil

shutil.move('/tmp/bacon.txt', '/tmp/eggs')
```

```output
/tmp/eggs/bacon.txt
```

Der Zielpfad kann auch einen Dateinamen angeben. Im folgenden Beispiel wird die Quelldatei verschoben und umbenannt:

```python
shutil.move('/tmp/bacon.txt', '/tmp/eggs/new_bacon.txt')
```

```output
/tmp/eggs/new_bacon.txt
```

Wenn es keinen eggs-Ordner gibt, benennt `move()` bacon.txt in eine Datei namens eggs um:

```python
shutil.move('/tmp/bacon.txt', '/tmp/eggs')
```

```output
/tmp/eggs
```

## Löschen von Dateien und Ordnern

- Der Aufruf von `Path.unlink()` löscht die Datei am Pfad.
- Der Aufruf von `Path.rmdir()` löscht den Ordner am Pfad. Dieser Ordner muss leer von Dateien oder Ordnern sein.
- Der Aufruf von `shutil.rmtree(path)` entfernt den Ordner am Pfad, und alle darin enthaltenen Dateien und Ordner werden ebenfalls gelöscht.

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-file-directory-path-5">
<template #question>
Which method can delete a non-empty directory and all its contents?
</template>

<base-quiz-option value="A">A. <code>Path.rmdir()</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>shutil.rmtree()</code></base-quiz-option>
<base-quiz-option value="C">C. <code>Path.unlink()</code></base-quiz-option>
<base-quiz-option value="D">D. <code>os.remove()</code></base-quiz-option>
<base-quiz-answer value="B">Die Funktion <code>shutil.rmtree()</code> kann ein Verzeichnis und alle seine Inhalte rekursiv löschen. <code>Path.rmdir()</code> funktioniert nur bei leeren Verzeichnissen.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Durchlaufen eines Verzeichnisbaums

Das `Path`-Objekt verfügt über eine `rglob()`-Methode, um rekursiv über Dateien und Verzeichnisse zu iterieren.

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

## Relevante Links

- <router-link to="/cheatsheet/reading-and-writing-files">Lesen und Schreiben von Dateien</router-link>
- <router-link to="/blog/python-pathlib-essentials">10 Essential File System Operations Every Developer Should Know</router-link>
- <router-link to="/builtin/open">open()</router-link>
