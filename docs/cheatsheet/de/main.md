---
title: 'Python Hauptfunktion – Python Spickzettel'
description: 'Ist der Name des Gültigkeitsbereichs, in dem Code auf oberster Ebene ausgeführt wird. Der Name eines Moduls wird gleich main gesetzt, wenn es von Standardeingabe, einem Skript oder einer interaktiven Eingabeaufforderung gelesen wird.'
labUrl: 'https://labex.io/de/labs/python-python-main-function-633661?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Haupt-Skriptumgebung auf oberster Ebene
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## Was ist das

`__main__` ist der Name des Gültigkeitsbereichs, in dem Code auf oberster Ebene ausgeführt wird.
Der **Name** eines Moduls wird gleich `__main__` gesetzt, wenn es von Standardeingabe, einem Skript oder einer interaktiven Eingabeaufforderung gelesen wird.

Ein Modul kann feststellen, ob es im Haupt-Gültigkeitsbereich ausgeführt wird, indem es seinen eigenen `__name__` überprüft, was ein gängiges Idiom für die bedingte Ausführung von Code in einem Modul ermöglicht. Wenn es als Skript oder mit `python -m` ausgeführt wird, aber nicht, wenn es importiert wird:

```python
# __name__ == "__main__": prüfen, ob das Skript direkt ausgeführt wird (nicht importiert)
if __name__ == "__main__":  # Wahr, wenn als Skript ausgeführt, Falsch, wenn importiert
    # nur ausführen, wenn als Skript ausgeführt
    main()
```

Für ein Paket kann derselbe Effekt durch die Einbeziehung eines **main**.py-Moduls erreicht werden, dessen Inhalt ausgeführt wird, wenn das Modul mit -m ausgeführt wird.

Wenn wir beispielsweise ein Skript entwickeln, das als Modul verwendet werden soll, sollten wir Folgendes tun:

```python
# Beispiel: Funktion kann importiert werden, aber Testcode wird nur ausgeführt, wenn direkt ausgeführt
def add(a, b):
    return a+b

if __name__ == "__main__":  # Wird nur ausgeführt, wenn die Datei ausgeführt wird, nicht beim Importieren
    add(3, 5)
```

<BaseQuiz id="cheatsheet-main-1" correct="B">
<template #question>
Was ist der Wert von <code>__name__</code>, wenn eine Python-Datei direkt als Skript ausgeführt wird?
</template>

<BaseQuizOption value="A">A. Der Dateiname</BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>"**main**"</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>None</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>True</code></BaseQuizOption>
<BaseQuizAnswer>Wenn eine Python-Datei direkt als Skript ausgeführt wird, wird <code>**name**</code> auf <code>"**main**"</code> gesetzt. Wenn die Datei als Modul importiert wird, wird <code>**name**</code> auf den Namen des Moduls gesetzt.</BaseQuizAnswer>
</BaseQuiz>

## Vorteile

1. Jedes Python-Modul hat sein `__name__` definiert, und wenn dieses `__main__` ist, impliziert dies, dass das Modul vom Benutzer eigenständig ausgeführt wird, und wir können entsprechende geeignete Aktionen durchführen.
2. Wenn Sie dieses Skript als Modul in einem anderen Skript importieren, wird der **Name** auf den Namen des Skripts/Moduls gesetzt.
3. Python-Dateien können entweder als wiederverwendbare Module oder als eigenständige Programme fungieren.
4. `if __name__ == "__main__":` wird verwendet, um Code nur dann auszuführen, wenn die Datei direkt ausgeführt und nicht importiert wird.

<BaseQuiz id="cheatsheet-main-2" correct="A">
<template #question>
Was ist der Hauptzweck der Verwendung von <code>if __name__ == "__main__":</code>?
</template>

<BaseQuizOption value="A" correct>A. Code nur auszuführen, wenn die Datei direkt ausgeführt und nicht importiert wird</BaseQuizOption>
<BaseQuizOption value="B">B. Zu verhindern, dass die Datei importiert wird</BaseQuizOption>
<BaseQuizOption value="C">C. Um die Ausführung der Datei zu beschleunigen</BaseQuizOption>
<BaseQuizOption value="D">D. Um Code vor anderen Modulen zu verbergen</BaseQuizOption>
<BaseQuizAnswer>Das Idiom <code>if **name** == "**main**":</code> ermöglicht es einer Python-Datei, sowohl als wiederverwendbares Modul als auch als eigenständiges Programm zu fungieren. Code innerhalb dieses Blocks wird nur ausgeführt, wenn die Datei direkt ausgeführt wird, nicht wenn sie importiert wird.</BaseQuizAnswer>
</BaseQuiz>

## Relevante Links

- <router-link to="/cheatsheet/functions">Funktionen</router-link>
- <router-link to="/cheatsheet/packaging">Paketierung</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Python-Projekte mit Poetry und VSCode. Teil 1</router-link>
- <router-link to="/builtin/import">import()</router-link>
