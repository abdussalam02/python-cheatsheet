---
title: 'Python Ausnahmebehandlung – Python Spickzettel'
description: 'In Python ist die Ausnahmebehandlung der Prozess der Reaktion auf das Auftreten von Ausnahmen.'
labUrl: 'https://labex.io/de/labs/python-python-exception-handling-633656?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Ausnahmebehandlung
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikipedia.org/wiki/Exception_handling">Exception Handling</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    In der Informatik und Computerprogrammierung ist die Ausnahmebehandlung der Prozess der Reaktion auf das Auftreten von Ausnahmen – anomalen oder außergewöhnlichen Bedingungen, die eine spezielle Verarbeitung erfordern.
  </base-disclaimer-content>
</base-disclaimer>

Python verfügt über viele [eingebaute Ausnahmen](https://docs.python.org/3/library/exceptions.html), die ausgelöst werden, wenn ein Programm auf einen Fehler stößt, und die meisten externen Bibliotheken, wie die beliebte [Requests](https://requests.readthedocs.io/en/latest), enthalten eigene [benutzerdefinierte Ausnahmen](https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions), mit denen wir umgehen müssen.

## Grundlegende Ausnahmebehandlung

Man kann nicht durch Null teilen, das ist eine mathematische Wahrheit, und wenn man versucht, dies in Python zu tun, löst der Interpreter die eingebaute Ausnahme [ZeroDivisionError](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError) aus:

```python
def divide(dividend , divisor):
    print(dividend / divisor)

divide(dividend=10, divisor=5)
```

```output
2
```

```python
divide(dividend=10, divisor=0)
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

Angenommen, wir möchten nicht, dass unser Programm seine Ausführung stoppt oder dem Benutzer eine Ausgabe zeigt, die er nicht versteht. Wenn wir eine nützliche und klare Nachricht ausgeben möchten, müssen wir die Ausnahme mit den Schlüsselwörtern `try` und `except` **_behandeln_**:

```python
# try-except: Ausnahmen elegant behandeln
def divide(dividend , divisor):
    try:  # Versuche, diesen Code auszuführen
        print(dividend / divisor)
    except ZeroDivisionError:  # Fange spezifischen Ausnahmetyp ab
        print('You can not divide by 0')

divide(dividend=10, divisor=5)
```

```output
2
```

```python
divide(dividend=10, divisor=0)
```

```output
You can not divide by 0
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-exception-handling-1">
<template #question>
Welche Schlüsselwörter werden in Python zur Ausnahmebehandlung verwendet?
</template>

<base-quiz-option value="A" correct>A. <code>try</code> und <code>except</code></base-quiz-option>
<base-quiz-option value="B">B. <code>catch</code> und <code>handle</code></base-quiz-option>
<base-quiz-option value="C">C. <code>error</code> und <code>rescue</code></base-quiz-option>
<base-quiz-option value="D">D. <code>if</code> und <code>else</code></base-quiz-option>
<base-quiz-answer value="A">Python verwendet <code>try</code>, um Code zu kennzeichnen, der eine Ausnahme auslösen könnte, und <code>except</code>, um aufgetretene spezifische Ausnahmen zu behandeln.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Behandlung mehrerer Ausnahmen mit einem Ausnahmeblock

Sie können auch mehrere Ausnahmen in einer einzigen Zeile wie folgt behandeln, ohne mehrere Ausnahmeblöcke erstellen zu müssen.

```python
# Mehrere Ausnahmen in einem except-Block behandeln
def divide(dividend , divisor):
    try:
        if (dividend == 10):
          var = 'str' + 1  # Dies löst TypeError aus
        else:
          print(dividend / divisor)
    except (ZeroDivisionError, TypeError) as error:  # Mehrere Ausnahmetypen abfangen
        print(error)  # Die Fehlermeldung ausgeben

divide(dividend=20, divisor=5)
```

```output
4
```

```python
divide(dividend=10, divisor=5)
```

```output
can only concatenate str (not "int") to str
```

```python
divide(dividend=10, divisor=0)
```

```output
division by zero
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-exception-handling-2">
<template #question>
Können Sie mehrere Ausnahmetypen in einem einzigen <code>except</code>-Block behandeln?
</template>

<base-quiz-option value="A">A. Nein, Sie müssen für jeden Ausnahmetyp separate <code>except</code>-Blöcke verwenden</base-quiz-option>
<base-quiz-option value="B" correct>B. Ja, indem Sie sie in ein Tupel wie <code>except (Exception1, Exception2)</code> setzen</base-quiz-option>
<base-quiz-option value="C">C. Ja, aber nur, wenn sie verwandt sind</base-quiz-option>
<base-quiz-option value="D">D. Nein, Python unterstützt dies nicht</base-quiz-option>
<base-quiz-answer value="B">Sie können mehrere Ausnahmetypen in einem <code>except</code>-Block behandeln, indem Sie sie in ein Tupel setzen: <code>except (ZeroDivisionError, TypeError) as error:</code></base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Finally-Code in der Ausnahmebehandlung

Der Code im `finally`-Abschnitt wird immer ausgeführt, unabhängig davon, ob eine Ausnahme ausgelöst wurde oder nicht:

```python
# finally-Block: wird immer ausgeführt, unabhängig von Ausnahmen
def divide(dividend , divisor):
    try:
        print(dividend / divisor)
    except ZeroDivisionError:
        print('You can not divide by 0')
    finally:  # Wird immer ausgeführt, auch wenn eine Ausnahme auftritt
        print('Execution finished')

divide(dividend=10, divisor=5)
```

```output
2.0
Execution finished
```

```python
divide(dividend=10, divisor=0)
```

```output
You can not divide by 0
Execution finished
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-exception-handling-3">
<template #question>
Wann wird der <code>finally</code>-Block ausgeführt?
</template>

<base-quiz-option value="A">A. Nur wenn eine Ausnahme auftritt</base-quiz-option>
<base-quiz-option value="B">B. Nur wenn keine Ausnahme auftritt</base-quiz-option>
<base-quiz-option value="C" correct>C. Immer, unabhängig davon, ob eine Ausnahme aufgetreten ist oder nicht</base-quiz-option>
<base-quiz-option value="D">D. Niemals</base-quiz-option>
<base-quiz-answer value="C">Der <code>finally</code>-Block wird immer ausgeführt, unabhängig davon, ob eine Ausnahme aufgetreten ist oder nicht. Er ist nützlich für Aufräumarbeiten, die unabhängig vom Ergebnis ausgeführt werden müssen.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Benutzerdefinierte Ausnahmen

Benutzerdefinierte Ausnahmen werden initialisiert, indem eine `class` erstellt wird, die von der Basisklasse `Exception` von Python erbt, und mit dem Schlüsselwort `raise` ausgelöst werden:

```python
# Benutzerdefinierte Ausnahme: Erstellung durch Vererbung von der Exception-Klasse
class MyCustomException(Exception):
    pass

raise MyCustomException  # Löst die benutzerdefinierte Ausnahme aus
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyCustomException
```

Um eine benutzerdefinierte Ausnahmemeldung zu deklarieren, können Sie diese als Parameter übergeben:

```python
class MyCustomException(Exception):
    pass

raise MyCustomException('A custom message for my custom exception')
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyCustomException: A custom message for my custom exception
```

Das Behandeln einer benutzerdefinierten Ausnahme ist dasselbe wie bei jeder anderen:

```python
try:
    raise MyCustomException('A custom message for my custom exception')
except MyCustomException:
    print('My custom exception was raised')
```

```output
My custom exception was raised
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-exception-handling-4">
<template #question>
Wie erstellt man eine benutzerdefinierte Ausnahme in Python?
</template>

<base-quiz-option value="A" correct>A. Erstellen Sie eine Klasse, die von der <code>Exception</code>-Klasse erbt</base-quiz-option>
<base-quiz-option value="B">B. Verwenden Sie den Decorator <code>@exception</code></base-quiz-option>
<base-quiz-option value="C">C. Rufen Sie <code>Exception.create()</code> auf</base-quiz-option>
<base-quiz-option value="D">D. Importieren Sie sie aus einem speziellen Modul</base-quiz-option>
<base-quiz-answer value="A">Benutzerdefinierte Ausnahmen werden erstellt, indem eine Klasse definiert wird, die von der Basisklasse <code>Exception</code> erbt. Sie können sie dann wie eingebaute Ausnahmen auslösen und behandeln.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Relevante Links

- <router-link to="/cheatsheet/control-flow">Kontrollfluss</router-link>
- <router-link to="/builtin/breakpoint">breakpoint()</router-link>
- <router-link to="/builtin/isinstance">isinstance()</router-link>
- <router-link to="/builtin/issubclass">issubclass()</router-link>
