---
title: 'Python Context Manager - Python Spickzettel'
description: 'Obwohl Python-Kontextmanager weit verbreitet sind, verstehen nur wenige den Zweck hinter ihrer Verwendung. Diese Anweisungen, die häufig beim Lesen und Schreiben von Dateien verwendet werden, helfen der Anwendung, Systemressourcen zu schonen und die Ressourcenverwaltung zu verbessern, indem sichergestellt wird, dass bestimmte Ressourcen nur für bestimmte Prozesse genutzt werden.'
labUrl: 'https://labex.io/de/labs/python-python-context-manager-633650?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Context Manager
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Obwohl Python-Kontextmanager weit verbreitet sind, verstehen nur wenige den Zweck hinter ihrer Verwendung. Diese Anweisungen, die üblicherweise beim Lesen und Schreiben von Dateien verwendet werden, helfen der Anwendung, Systemspeicher zu schonen und die Ressourcenverwaltung zu verbessern, indem sichergestellt wird, dass bestimmte Ressourcen nur für bestimmte Prozesse verwendet werden.

## Die with-Anweisung

Ein Kontextmanager ist ein Objekt, das benachrichtigt wird, wenn ein Kontext (ein Codeblock) beginnt und endet. Man verwendet ihn üblicherweise mit der `with`-Anweisung. Diese kümmert sich um die Benachrichtigung.

Zum Beispiel sind Datei-Objekte Kontextmanager. Wenn ein Kontext endet, wird das Datei-Objekt automatisch geschlossen:

```python
# Kontextmanager: kümmert sich automatisch um die Ressourcenbereinigung
# Die Datei wird automatisch geschlossen, wenn der 'with'-Block verlassen wird
with open(filename) as f:  # 'f' ist das Datei-Objekt
    file_contents = f.read()

# Die Datei ist hier automatisch geschlossen, auch wenn ein Fehler aufgetreten ist
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Was ist der Hauptvorteil der Verwendung eines Kontextmanagers (der <code>with</code>-Anweisung)?
</template>

<base-quiz-option value="A" correct>A. Automatische Bereinigung von Ressourcen, auch wenn ein Fehler auftritt</base-quiz-option>
<base-quiz-option value="B">B. Lässt Code schneller ausführen</base-quiz-option>
<base-quiz-option value="C">C. Ermöglicht das gleichzeitige Öffnen mehrerer Dateien</base-quiz-option>
<base-quiz-option value="D">D. Verhindert alle Fehler</base-quiz-option>
<base-quiz-answer value="A">Kontextmanager stellen sicher, dass Ressourcen (wie Dateien) ordnungsgemäß bereinigt werden, wenn der Block verlassen wird, auch wenn eine Ausnahme auftritt. Dies verhindert Ressourcenlecks und Datenverlust.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Alles, was die Ausführung des Blocks beendet, führt dazu, dass die Exit-Methode des Kontextmanagers aufgerufen wird. Dies schließt Ausnahmen ein und kann nützlich sein, wenn ein Fehler dazu führt, dass Sie vorzeitig eine geöffnete Datei oder Verbindung verlassen. Ein Skript zu beenden, ohne Dateien/Verbindungen ordnungsgemäß zu schließen, ist eine schlechte Idee, die zu Datenverlust oder anderen Problemen führen kann. Durch die Verwendung eines Kontextmanagers können Sie sicherstellen, dass Vorkehrungen immer getroffen werden, um auf diese Weise Schäden oder Verluste zu verhindern.

## Schreiben Ihres eigenen Kontextmanagers

Es ist auch möglich, einen Kontextmanager mithilfe der Generator-Syntax dank des Decorators `contextlib.contextmanager` zu schreiben:

```python
# Funktionsbasierter Kontextmanager unter Verwendung des contextlib-Decorators
import contextlib
@contextlib.contextmanager
def context_manager(num):
    print('Enter')  # Code vor yield wird bei __enter__ ausgeführt
    yield num + 1   # Der übergebene Wert wird zur 'cm'-Variable
    print('Exit')    # Code nach yield wird bei __exit__ ausgeführt

with context_manager(2) as cm:  # cm empfängt den übergebenen Wert (3)
    print('Right in the middle with cm = {}'.format(cm))
```

```output
Enter
Right in the middle with cm = 3
Exit
```

## Klassenbasierter Kontextmanager

Sie können einen klassenbasierten Kontextmanager definieren. Die Schlüsselmethoden sind `__enter__` und `__exit__`

```python
# Klassenbasierter Kontextmanager: Implementieren Sie die Methoden __enter__ und __exit__
class ContextManager:
    def __enter__(self, *args, **kwargs):  # Wird beim Betreten des 'with'-Blocks aufgerufen
        print("--enter--")
        return self  # Kann ein Objekt zurückgeben, das als 'as'-Variable verwendet wird

    def __exit__(self, *args):  # Wird beim Verlassen des 'with'-Blocks aufgerufen
        print("--exit--")

with ContextManager():  # Ruft __enter__ auf, dann __exit__, wenn fertig
    print("test")
```

```output
--enter--
test
--exit--
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Welche Methoden muss eine Klasse implementieren, um als Kontextmanager verwendet werden zu können?
</template>

<base-quiz-option value="A">A. <code>**init**</code> und <code>**del**</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>**enter**</code> und <code>**exit**</code></base-quiz-option>
<base-quiz-option value="C">C. <code>open</code> und <code>close</code></base-quiz-option>
<base-quiz-option value="D">D. <code>start</code> und <code>stop</code></base-quiz-option>
<base-quiz-answer value="B">Ein klassenbasierter Kontextmanager muss <code>**enter**</code> (aufgerufen beim Betreten des <code>with</code>-Blocks) und <code>**exit**</code> (aufgerufen beim Verlassen des Blocks) implementieren.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Relevante Links

- <router-link to="/cheatsheet/reading-and-writing-files">Lesen und Schreiben von Dateien</router-link>
- <router-link to="/cheatsheet/exception-handling">Fehlerbehandlung</router-link>
- <router-link to="/cheatsheet/decorators">Decorators</router-link>
- <router-link to="/blog/python-pathlib-essentials">10 wesentliche Dateisystemoperationen, die jeder Entwickler kennen sollte</router-link>
- <router-link to="/builtin/open">open()</router-link>
