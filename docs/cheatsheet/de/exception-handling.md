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

<BaseQuiz id="cheatsheet-exception-handling-1" correct="A">
<template #question>
Welche Schlüsselwörter werden in Python zur Ausnahmebehandlung verwendet?
</template>

<BaseQuizOption value="A" correct>A. <code>try</code> und <code>except</code></BaseQuizOption>
<BaseQuizOption value="B">B. <code>catch</code> und <code>handle</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>error</code> und <code>rescue</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>if</code> und <code>else</code></BaseQuizOption>
<BaseQuizAnswer>Python verwendet <code>try</code>, um Code zu kennzeichnen, der eine Ausnahme auslösen könnte, und <code>except</code>, um aufgetretene spezifische Ausnahmen zu behandeln.</BaseQuizAnswer>
</BaseQuiz>

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

<BaseQuiz id="cheatsheet-exception-handling-2" correct="B">
<template #question>
Können Sie mehrere Ausnahmetypen in einem einzigen <code>except</code>-Block behandeln?
</template>

<BaseQuizOption value="A">A. Nein, Sie müssen für jeden Ausnahmetyp separate <code>except</code>-Blöcke verwenden</BaseQuizOption>
<BaseQuizOption value="B" correct>B. Ja, indem Sie sie in ein Tupel wie <code>except (Exception1, Exception2)</code> setzen</BaseQuizOption>
<BaseQuizOption value="C">C. Ja, aber nur, wenn sie verwandt sind</BaseQuizOption>
<BaseQuizOption value="D">D. Nein, Python unterstützt dies nicht</BaseQuizOption>
<BaseQuizAnswer>Sie können mehrere Ausnahmetypen in einem <code>except</code>-Block behandeln, indem Sie sie in ein Tupel setzen: <code>except (ZeroDivisionError, TypeError) as error:</code></BaseQuizAnswer>
</BaseQuiz>

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

<BaseQuiz id="cheatsheet-exception-handling-3" correct="C">
<template #question>
Wann wird der <code>finally</code>-Block ausgeführt?
</template>

<BaseQuizOption value="A">A. Nur wenn eine Ausnahme auftritt</BaseQuizOption>
<BaseQuizOption value="B">B. Nur wenn keine Ausnahme auftritt</BaseQuizOption>
<BaseQuizOption value="C" correct>C. Immer, unabhängig davon, ob eine Ausnahme aufgetreten ist oder nicht</BaseQuizOption>
<BaseQuizOption value="D">D. Niemals</BaseQuizOption>
<BaseQuizAnswer>Der <code>finally</code>-Block wird immer ausgeführt, unabhängig davon, ob eine Ausnahme aufgetreten ist oder nicht. Er ist nützlich für Aufräumarbeiten, die unabhängig vom Ergebnis ausgeführt werden müssen.</BaseQuizAnswer>
</BaseQuiz>

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

<BaseQuiz id="cheatsheet-exception-handling-4" correct="A">
<template #question>
Wie erstellt man eine benutzerdefinierte Ausnahme in Python?
</template>

<BaseQuizOption value="A" correct>A. Erstellen Sie eine Klasse, die von der <code>Exception</code>-Klasse erbt</BaseQuizOption>
<BaseQuizOption value="B">B. Verwenden Sie den Decorator <code>@exception</code></BaseQuizOption>
<BaseQuizOption value="C">C. Rufen Sie <code>Exception.create()</code> auf</BaseQuizOption>
<BaseQuizOption value="D">D. Importieren Sie sie aus einem speziellen Modul</BaseQuizOption>
<BaseQuizAnswer>Benutzerdefinierte Ausnahmen werden erstellt, indem eine Klasse definiert wird, die von der Basisklasse <code>Exception</code> erbt. Sie können sie dann wie eingebaute Ausnahmen auslösen und behandeln.</BaseQuizAnswer>
</BaseQuiz>

## Relevante Links

- <router-link to="/cheatsheet/control-flow">Kontrollfluss</router-link>
- <router-link to="/builtin/breakpoint">breakpoint()</router-link>
- <router-link to="/builtin/isinstance">isinstance()</router-link>
- <router-link to="/builtin/issubclass">issubclass()</router-link>
