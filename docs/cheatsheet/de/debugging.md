---
title: 'Python Debugging - Python Spickzettel'
description: 'Beim Debuggen geht es darum, Fehler (Defekte oder Probleme, die den korrekten Betrieb verhindern) in Computerprogrammen, Software oder Systemen zu finden und zu beheben.'
labUrl: 'https://labex.io/de/labs/python-python-debugging-633653?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Debugging
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikipedia.org/wiki/Debugging">Finden und Beheben von Fehlern</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Beim Programmieren und in der Softwareentwicklung ist Debugging der Prozess des Findens und Behebens von Bugs (Fehlern oder Problemen, die eine korrekte Funktion verhindern) in Computerprogrammen, Software oder Systemen.
  </base-disclaimer-content>
</base-disclaimer>

## Auslösen von Ausnahmen (Raising Exceptions)

Ausnahmen werden mit einer `raise`-Anweisung ausgelöst. Im Code besteht eine `raise`-Anweisung aus Folgendem:

- Das Schlüsselwort `raise`
- Ein Aufruf der Funktion `Exception()`
- Ein String mit einer hilfreichen Fehlermeldung, der an die Funktion `Exception()` übergeben wird

```python
# raise statement: manuelles Auslösen einer Ausnahme mit einer benutzerdefinierten Nachricht
raise Exception('This is the error message.')
```

```output
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    raise Exception('This is the error message.')
Exception: This is the error message.
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-debugging-1">
<template #question>
Welches Schlüsselwort wird verwendet, um in Python manuell eine Ausnahme auszulösen?
</template>

<base-quiz-option value="A">A. <code>throw</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>raise</code></base-quiz-option>
<base-quiz-option value="C">C. <code>error</code></base-quiz-option>
<base-quiz-option value="D">D. <code>exception</code></base-quiz-option>
<base-quiz-answer value="B">Das Schlüsselwort <code>raise</code> wird verwendet, um manuell eine Ausnahme in Python auszulösen. Sie können eingebaute Ausnahmen oder benutzerdefinierte Ausnahmen auslösen.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Typischerweise ist es der Code, der die Funktion aufruft, und nicht die Funktion selbst, der weiß, wie eine Ausnahme zu behandeln ist. Daher werden Sie häufig eine `raise`-Anweisung innerhalb einer Funktion und die Anweisungen `try` und `except` im aufrufenden Code sehen.

```python
# Raise exceptions in function, handle them in calling code
def box_print(symbol, width, height):
    if len(symbol) != 1:
      raise Exception('Symbol must be a single character string.')
    if width <= 2:
      raise Exception('Width must be greater than 2.')
    if height <= 2:
      raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

# Handle exceptions when calling the function
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:  # Catch exception and print error message
        print('An exception happened: ' + str(err))
```

```output
****
*  *
*  *
****
OOOOOOOOOOOOOOOOOOOO
O                  O
O                  O
O                  O
OOOOOOOOOOOOOOOOOOOO
An exception happened: Width must be greater than 2.
An exception happened: Symbol must be a single character string.
```

Lesen Sie mehr über [Exception Handling](/cheatsheet/exception-handling).

## Den Traceback als String erhalten

Der `traceback` wird von Python angezeigt, wenn eine ausgelöste Ausnahme unbehandelt bleibt. Sie können ihn aber auch als String erhalten, indem Sie `traceback.format_exc()` aufrufen. Diese Funktion ist nützlich, wenn Sie die Informationen aus dem Traceback einer Ausnahme benötigen, aber trotzdem eine `except`-Anweisung verwenden möchten, um die Ausnahme elegant zu behandeln. Sie müssen das `traceback`-Modul von Python importieren, bevor Sie diese Funktion aufrufen.

```python
# traceback.format_exc(): Traceback als String für Logging/Debugging erhalten
import traceback

try:
    raise Exception('This is the error message.')
except:
    with open('errorInfo.txt', 'w') as error_file:
        error_file.write(traceback.format_exc())  # Traceback in Datei schreiben
    print('The traceback info was written to errorInfo.txt.')
```

```output
116
The traceback info was written to errorInfo.txt.
```

Die 116 ist der Rückgabewert der `write()`-Methode, da 116 Zeichen in die Datei geschrieben wurden. Der `traceback`-Text wurde in errorInfo.txt geschrieben.

    Traceback (most recent call last):
      File "<pyshell#28>", line 2, in <module>
    Exception: This is the error message.

## Assertions (Zusicherungen)

Eine Assertion ist eine Plausibilitätsprüfung, um sicherzustellen, dass Ihr Code nichts offensichtlich Falsches tut. Diese Plausibilitätsprüfungen werden durch `assert`-Anweisungen durchgeführt. Wenn die Plausibilitätsprüfung fehlschlägt, wird eine Ausnahme vom Typ `AssertionError` ausgelöst. Im Code besteht eine `assert`-Anweisung aus Folgendem:

- Das Schlüsselwort `assert`
- Eine Bedingung (d. h. ein Ausdruck, der zu `True` oder `False` ausgewertet wird)
- Ein Komma
- Ein `string`, der angezeigt wird, wenn die Bedingung `False` ist

```python
# assert statement: Bedingung prüfen, AssertionError auslösen, wenn False
pod_bay_door_status = 'open'
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'  # Erfolgreich

pod_bay_door_status = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'  # Löst AssertionError aus
```

```output
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'
AssertionError: The pod bay doors need to be "open".
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-debugging-2">
<template #question>
Was passiert, wenn eine <code>assert</code>-Anweisung fehlschlägt?
</template>

<base-quiz-option value="A">A. Das Programm läuft weiter</base-quiz-option>
<base-quiz-option value="B">B. Eine Warnung wird ausgegeben</base-quiz-option>
<base-quiz-option value="C" correct>C. Ein <code>AssertionError</code> wird ausgelöst und das Programm sollte abstürzen</base-quiz-option>
<base-quiz-option value="D">D. Die Bedingung wird automatisch korrigiert</base-quiz-option>
<base-quiz-answer value="C">Wenn eine <code>assert</code>-Anweisung fehlschlägt, löst sie einen <code>AssertionError</code> aus. Im Gegensatz zu Ausnahmen sollten Assert-Anweisungen nicht mit try-except abgefangen werden; wenn ein Assert fehlschlägt, sollte Ihr Programm abstürzen, um Ihnen zu helfen, Fehler schnell zu finden.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Vereinfacht ausgedrückt besagt eine Assert-Anweisung: „Ich versichere, dass diese Bedingung wahr ist, und wenn nicht, liegt irgendwo im Programm ein Fehler vor.“ Im Gegensatz zu Ausnahmen sollte Ihr Code Assert-Anweisungen nicht mit try und except behandeln; wenn ein Assert fehlschlägt, sollte Ihr Programm abstürzen. Durch dieses schnelle Scheitern verkürzen Sie die Zeit zwischen der ursprünglichen Ursache des Fehlers und dem ersten Auftreten des Fehlers. Dies reduziert die Menge an Code, die Sie überprüfen müssen, bevor Sie den fehlerverursachenden Code finden.

### Deaktivieren von Assertions

Assertions können deaktiviert werden, indem die Option `-O` beim Ausführen von Python übergeben wird.

## Logging (Protokollierung)

Um das `logging`-Modul so zu aktivieren, dass Log-Meldungen während der Programmausführung auf Ihrem Bildschirm angezeigt werden, kopieren Sie Folgendes an den Anfang Ihres Programms:

```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-debugging-3">
<template #question>
Was ist der Zweck des <code>logging</code>-Moduls in Python?
</template>

<base-quiz-option value="A" correct>A. Aufzeichnung von Informationen über die Programmausführung zur Fehlerbehebung und Überwachung</base-quiz-option>
<base-quiz-option value="B">B. Verhindern, dass Fehler auftreten</base-quiz-option>
<base-quiz-option value="C">C. Beschleunigung der Programmausführung</base-quiz-option>
<base-quiz-option value="D">D. Verschlüsseln von Log-Meldungen</base-quiz-option>
<base-quiz-answer value="A">Das <code>logging</code>-Modul ermöglicht es Ihnen, Informationen über die Ausführung Ihres Programms auf verschiedenen Ebenen (DEBUG, INFO, WARNING, ERROR, CRITICAL) aufzuzeichnen, was zur Fehlerbehebung und Überwachung nützlich ist.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Angenommen, Sie haben eine Funktion zur Berechnung der Fakultät einer Zahl geschrieben. In der Mathematik ist die Fakultät von 4 gleich 1 × 2 × 3 × 4, also 24. Die Fakultät von 7 ist 1 × 2 × 3 × 4 × 5 × 6 × 7, also 5.040. Öffnen Sie ein neues Dateieditorfenster und geben Sie den folgenden Code ein. Er enthält einen Fehler, aber Sie werden auch mehrere Log-Meldungen einfügen, um sich bei der Fehlersuche zu helfen. Speichern Sie das Programm als factorialLog.py.

```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(0, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')
```

```output
2015-05-23 16:20:12,664 - DEBUG - Start of program
2015-05-23 16:20:12,664 - DEBUG - Start of factorial(5)
2015-05-23 16:20:12,665 - DEBUG - i is 0, total is 0
2015-05-23 16:20:12,668 - DEBUG - i is 1, total is 0
2015-05-23 16:20:12,670 - DEBUG - i is 2, total is 0
2015-05-23 16:20:12,673 - DEBUG - i is 3, total is 0
2015-05-23 16:20:12,675 - DEBUG - i is 4, total is 0
2015-05-23 16:20:12,678 - DEBUG - i is 5, total is 0
2015-05-23 16:20:12,680 - DEBUG - End of factorial(5)
0
2015-05-23 16:20:12,684 - DEBUG - End of program
```

## Logging Levels (Protokollierungsebenen)

Logging-Level bieten eine Möglichkeit, Ihre Log-Meldungen nach Wichtigkeit zu kategorisieren. Es gibt fünf Logging-Level, die in Tabelle 10-1 von der geringsten zur höchsten Wichtigkeit beschrieben werden. Meldungen können auf jeder Ebene mit einer anderen Logging-Funktion protokolliert werden.

| Level      | Logging Function     | Description                                                                                                                                                           |
| ---------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DEBUG`    | `logging.debug()`    | Die niedrigste Stufe. Wird für kleine Details verwendet. Normalerweise interessieren Sie sich nur für diese Meldungen bei der Diagnose von Problemen.                 |
| `INFO`     | `logging.info()`     | Wird verwendet, um Informationen über allgemeine Ereignisse in Ihrem Programm aufzuzeichnen oder zu bestätigen, dass Dinge an ihrer Stelle im Programm funktionieren. |
| `WARNING`  | `logging.warning()`  | Wird verwendet, um auf ein potenzielles Problem hinzuweisen, das die Funktion des Programms nicht verhindert, aber in Zukunft tun könnte.                             |
| `ERROR`    | `logging.error()`    | Wird verwendet, um einen Fehler aufzuzeichnen, der dazu führte, dass das Programm etwas nicht tun konnte.                                                             |
| `CRITICAL` | `logging.critical()` | Die höchste Stufe. Wird verwendet, um einen fatalen Fehler anzuzeigen, der dazu geführt hat oder kurz davor steht, dass das Programm vollständig beendet wird.        |

<base-quiz>
<base-quiz-question correct="D" id="cheatsheet-debugging-4">
<template #question>
Was ist die niedrigste Logging-Stufe in Python?
</template>

<base-quiz-option value="A">A. <code>INFO</code></base-quiz-option>
<base-quiz-option value="B">B. <code>WARNING</code></base-quiz-option>
<base-quiz-option value="C">C. <code>ERROR</code></base-quiz-option>
<base-quiz-option value="D" correct>D. <code>DEBUG</code></base-quiz-option>
<base-quiz-answer value="D">Die Logging-Level von niedrig nach hoch sind: <code>DEBUG</code>, <code>INFO</code>, <code>WARNING</code>, <code>ERROR</code>, <code>CRITICAL</code>. <code>DEBUG</code> ist die niedrigste Stufe und wird für detaillierte Diagnoseinformationen verwendet.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Deaktivieren des Loggings

Nachdem Sie Ihr Programm debuggt haben, möchten Sie wahrscheinlich nicht, dass all diese Log-Meldungen den Bildschirm überfluten. Die Funktion `logging.disable()` deaktiviert diese, sodass Sie nicht manuell alle Logging-Aufrufe aus Ihrem Programm entfernen müssen.

```python
import logging

logging.basicConfig(level=logging.INFO, format=' %(asctime)s -%(levelname)s - %(message)s')
logging.critical('Critical error! Critical error!')
```

```output
2015-05-22 11:10:48,054 - CRITICAL - Critical error! Critical error!
```

```python
logging.disable(logging.CRITICAL)
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')
```

## Logging in eine Datei

Anstatt die Log-Meldungen auf dem Bildschirm anzuzeigen, können Sie sie in eine Textdatei schreiben. Die Funktion `logging.basicConfig()` akzeptiert ein Schlüsselwortargument `filename`, wie folgt:

```python
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-debugging-5">
<template #question>
Wie schreiben Sie Log-Meldungen in eine Datei, anstatt sie auf dem Bildschirm anzuzeigen?
</template>

<base-quiz-option value="A">A. Verwenden Sie <code>logging.file()</code></base-quiz-option>
<base-quiz-option value="B" correct>B. Übergeben Sie den Parameter <code>filename</code> an <code>logging.basicConfig()</code></base-quiz-option>
<base-quiz-option value="C">C. Verwenden Sie <code>logging.write()</code></base-quiz-option>
<base-quiz-option value="D">D. Logs werden immer automatisch in Dateien geschrieben</base-quiz-option>
<base-quiz-answer value="B">Um Log-Meldungen in eine Datei zu schreiben, übergeben Sie den Parameter <code>filename</code> an <code>logging.basicConfig()</code>. Dadurch werden alle Log-Meldungen in die angegebene Datei geschrieben, anstatt sie auf dem Bildschirm anzuzeigen.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Relevante Links

- <router-link to="/cheatsheet/exception-handling">Exception Handling</router-link>
- <router-link to="/builtin/breakpoint">breakpoint()</router-link>
