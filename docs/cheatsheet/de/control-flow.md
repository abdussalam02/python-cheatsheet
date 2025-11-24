---
title: 'Python Kontrollfluss - Python Spickzettel'
description: 'Der Kontrollfluss bestimmt die Reihenfolge, in der Anweisungen, Befehle oder Funktionsaufrufe ausgeführt oder ausgewertet werden. Der Kontrollfluss eines Python-Programms wird durch bedingte Anweisungen, Schleifen und Funktionsaufrufe gesteuert.'
labUrl: 'https://labex.io/de/labs/python-python-control-flow-633651?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Kontrollfluss
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    Python Kontrollfluss
  </base-disclaimer-title>
  <base-disclaimer-content>
  Der Kontrollfluss ist die Reihenfolge, in der einzelne Anweisungen, Befehle oder Funktionsaufrufe ausgeführt oder ausgewertet werden. Der Kontrollfluss eines Python-Programms wird durch bedingte Anweisungen, Schleifen und Funktionsaufrufe gesteuert.
  </base-disclaimer-content>
</base-disclaimer>

## Vergleichsoperatoren

| Operator | Bedeutung           |
| -------- | ------------------- |
| `==`     | Gleich              |
| `!=`     | Ungleich            |
| `<`      | Kleiner als         |
| `>`      | Größer als          |
| `<=`     | Kleiner oder gleich |
| `>=`     | Größer oder gleich  |

Diese Operatoren ergeben je nach den gegebenen Werten `True` oder `False`.

Beispiele:

```python
42 == 42
```

```output
True
```

```python
40 == 42
```

```output
False
```

```python
'hello' == 'hello'
```

```output
True
```

```python
'hello' == 'Hello'
```

```output
False
```

```python
'dog' != 'cat'
```

```output
True
```

```python
42 == 42.0
```

```output
True
```

```python
42 == '42'
```

```output
False
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Was ergibt <code>'hello' == 'Hello'</code>?
</template>

<base-quiz-option value="A">A. <code>True</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>False</code></base-quiz-option>
<base-quiz-option value="C">C. <code>None</code></base-quiz-option>
<base-quiz-option value="D">D. Löst einen Fehler aus</base-quiz-option>
<base-quiz-answer value="B">Der String-Vergleich in Python ist case-sensitiv. <code>'hello'</code> und <code>'Hello'</code> sind unterschiedliche Strings, daher gibt der Vergleich <code>False</code> zurück.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Boolesche Operatoren

Es gibt drei Boolesche Operatoren: `and`, `or` und `not`.
In der Reihenfolge der Präzedenz, von höchster zu niedrigster, sind dies `not`, `and` und `or`.

Die _Wahrheitstabelle_ des `and`-Operators:

| Ausdruck          | Ergibt  |
| ----------------- | ------- |
| `True and True`   | `True`  |
| `True and False`  | `False` |
| `False and True`  | `False` |
| `False and False` | `False` |

Die _Wahrheitstabelle_ des `or`-Operators:

| Ausdruck         | Ergibt  |
| ---------------- | ------- |
| `True or True`   | `True`  |
| `True or False`  | `True`  |
| `False or True`  | `True`  |
| `False or False` | `False` |

Die _Wahrheitstabelle_ des `not`-Operators:

| Ausdruck    | Ergibt  |
| ----------- | ------- |
| `not True`  | `False` |
| `not False` | `True`  |

## Vermischung von Operatoren

Sie können Boolesche und Vergleichsoperatoren mischen:

```python
(4 < 5) and (5 < 6)
```

```output
True
```

```python
(4 < 5) and (9 < 6)
```

```output
False
```

```python
(1 == 2) or (2 == 2)
```

```output
True
```

Sie können auch mehrere Boolesche Operatoren in einem Ausdruck zusammen mit den Vergleichsoperatoren verwenden:

```python
2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
```

```output
True
```

```python
# Im folgenden Ausdruck wird zuerst 3 < 4 and 5 > 5 ausgewertet, was zu False führt.
# Dann gibt 5 > 4 True zurück, sodass das Ergebnis nach True or False True ist.
5 > 4 or 3 < 4 and 5 > 5
```

```output
True
```

```python
# Nun wird der Ausdruck in Klammern zuerst ausgewertet, sodass True and False zu False führt.
(5 > 4 or 3 < 4) and 5 > 5
```

```output
False
```

## if Anweisungen

Die `if`-Anweisung wertet einen Ausdruck aus, und wenn dieser Ausdruck `True` ist, führt sie den folgenden eingerückten Code aus:

```python
# if Anweisung: Codeblock ausführen, wenn Bedingung True ist
name = 'Debora'

if name == 'Debora':  # Prüfen, ob name gleich 'Debora' ist
   print('Hi, Debora')  # Diese Zeile wird ausgeführt, wenn die Bedingung True ist
```

```output
Hi, Debora
```

```python
if name != 'George':
   print('You are not George')
```

```output
You are not George
```

Die `else`-Anweisung wird nur ausgeführt, wenn die Auswertung des `if` und aller `elif`-Ausdrücke `False` ist:

```python
# if-else: unterschiedlichen Code basierend auf der Bedingung ausführen
name = 'Debora'

if name == 'George':
   print('Hi, George.')
else:  # Wird ausgeführt, wenn die if-Bedingung False ist
   print('You are not George')
```

```output
You are not George
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Wann wird der <code>else</code>-Block in einer if-else-Anweisung ausgeführt?
</template>

<base-quiz-option value="A">A. Immer</base-quiz-option>
<base-quiz-option value="B" correct>B. Nur wenn die <code>if</code>-Bedingung (und alle <code>elif</code>-Bedingungen, falls vorhanden) <code>False</code> sind</base-quiz-option>
<base-quiz-option value="C">C. Nur wenn die <code>if</code>-Bedingung <code>True</code> ist</base-quiz-option>
<base-quiz-option value="D">D. Nie</base-quiz-option>
<base-quiz-answer value="B">Der <code>else</code>-Block wird nur ausgeführt, wenn die <code>if</code>-Bedingung und alle <code>elif</code>-Bedingungen (falls vorhanden) zu <code>False</code> ausgewertet werden.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Erst nachdem der Ausdruck der `if`-Anweisung `False` ist, wird die `elif`-Anweisung ausgewertet und ausgeführt:

```python
# if-elif: mehrere Bedingungen nacheinander prüfen
name = 'George'

if name == 'Debora':
   print('Hi Debora!')
elif name == 'George':  # Nur geprüft, wenn die vorherige Bedingung False ist
   print('Hi George!')
```

```output
Hi George!
```

Die Teile `elif` und `else` sind optional.

```python
name = 'Antony'

if name == 'Debora':
   print('Hi Debora!')
elif name == 'George':
   print('Hi George!')
else:
   print('Who are you?')
```

```output
Who are you?
```

## Ternärer Bedingungsoperator

Viele Programmiersprachen verfügen über einen ternären Operator, der einen bedingten Ausdruck definiert. Die häufigste Verwendung ist die Erstellung einer knappen, einfachen bedingten Zuweisungsanweisung. Mit anderen Worten, er bietet Code in einer Zeile, um den ersten Ausdruck auszuwerten, wenn die Bedingung wahr ist, und andernfalls den zweiten Ausdruck auszuwerten.

```plaintext
<Ausdruck1> if <Bedingung> else <Ausdruck2>
```

Beispiel:

```python
age = 15

# diese if-Anweisung:
if age < 18:
   print('kid')
else:
   print('adult')
```

```output
kid
```

```python
# Ternärer Operator: bedingter Ausdruck in einer Zeile
# Syntax: Wert_wenn_wahr if Bedingung else Wert_wenn_falsch
print('kid' if age < 18 else 'adult')
```

```output
kid
```

Ternäre Operatoren können verkettet werden:

```python
age = 15

# dieser ternäre Operator:
print('kid' if age < 13 else 'teen' if age < 18 else 'adult')
```

```output
teen
```

```python
# entspricht dieser if-Anweisung:
if age < 13:
    print('kid')
else:
    if age < 18:
        print('teen')
    else:
        print('adult')
```

```output
teen
```

## Switch-Case-Anweisung

<base-disclaimer>
  <base-disclaimer-title>
    Switch-Case-Anweisungen
  </base-disclaimer-title>
  <base-disclaimer-content>
  In Programmiersprachen ist eine Switch-Anweisung eine Art von Auswahlsteuerungsmechanismus, der verwendet wird, um den Wert einer Variablen oder eines Ausdrucks durch Suche und Abbildung den Programmablauf zu ändern.
  </base-disclaimer-content>
</base-disclaimer>

Die _Switch-Case-Anweisungen_ oder **Strukturelle Mustererkennung** (Structural Pattern Matching) wurden erstmals 2020 über [PEP 622](https://peps.python.org/pep-0622/) eingeführt und dann offiziell mit **Python 3.10** im September 2022 veröffentlicht.

<base-disclaimer>
  <base-disclaimer-title>
    Offizielles Tutorial
  </base-disclaimer-title>
  <base-disclaimer-content>
  Die <a href="https://peps.python.org/pep-0636/" target="_blank">PEP 636</a> bietet ein offizielles Tutorial für die Python-Mustererkennung oder Switch-Case-Anweisungen.
  </base-disclaimer-content>
</base-disclaimer>

### Abgleich einzelner Werte

```python
response_code = 201
match response_code:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 300:
        print("Multiple Choices")
    case 307:
        print("Temporary Redirect")
    case 404:
        print("404 Not Found")
    case 500:
        print("Internal Server Error")
    case 502:
        print("502 Bad Gateway")
```

```output
Created
```

### Abgleich mit dem or-Muster

In diesem Beispiel erlaubt das Pipe-Zeichen (`|` oder `or`), dass Python dieselbe Antwort für zwei oder mehr Fälle zurückgibt.

```python
response_code = 502
match response_code:
    case 200 | 201:
        print("OK")
    case 300 | 307:
        print("Redirect")
    case 400 | 401:
        print("Bad Request")
    case 500 | 502:
        print("Internal Server Error")
```

```output
Internal Server Error
```

### Abgleich nach der Länge eines Iterierbaren

```python
today_responses = [200, 300, 404, 500]
match today_responses:
    case [a]:
            print(f"One response today: {a}")
    case [a, b]:
            print(f"Two responses today: {a} and {b}")
    case [a, b, *rest]:
            print(f"All responses: {a}, {b}, {rest}")
```

```output
All responses: 200, 300, [404, 500]
```

### Standardwert

Das Unterstrichsymbol (`_`) wird verwendet, um einen Standardfall zu definieren:

```python
response_code = 800
match response_code:
    case 200 | 201:
        print("OK")
    case 300 | 307:
        print("Redirect")
    case 400 | 401:
        print("Bad Request")
    case 500 | 502:
        print("Internal Server Error")
    case _:
        print("Invalid Code")
```

```output
Invalid Code
```

### Abgleich eingebauter Klassen

```python
response_code = "300"
match response_code:
    case int():
            print('Code is a number')
    case str():
            print('Code is a string')
    case _:
            print('Code is neither a string nor a number')
```

```output
Code is a string
```

### Absichern von Match-Case-Anweisungen (Guarding)

```python
response_code = 300
match response_code:
    case int() if response_code > 99 and response_code < 500:
            print('Code is a valid number')
    case _:
            print('Code is an invalid number')
```

```output
Code is a valid number
```

## while Schleifenanweisungen

Die while-Anweisung wird für wiederholte Ausführung verwendet, solange ein Ausdruck `True` ist:

```python
# while Schleife: Code wiederholen, solange Bedingung True ist
spam = 0
while spam < 5:  # Fortfahren, solange spam kleiner als 5 ist
    print('Hello, world.')
    spam = spam + 1  # Zähler erhöhen, um eine Endlosschleife zu vermeiden
```

```output
Hello, world.
Hello, world.
Hello, world.
Hello, world.
Hello, world.
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Was macht eine <code>while</code>-Schleife?
</template>

<base-quiz-option value="A" correct>A. Wiederholt Code, solange die Bedingung <code>True</code> ist</base-quiz-option>
<base-quiz-option value="B">B. Führt Code genau einmal aus</base-quiz-option>
<base-quiz-option value="C">C. Führt Code eine festgelegte Anzahl von Malen aus</base-quiz-option>
<base-quiz-option value="D">D. Überspringt die Codeausführung</base-quiz-option>
<base-quiz-answer value="A">Eine <code>while</code>-Schleife führt einen Codeblock wiederholt aus, solange die Bedingung zu <code>True</code> ausgewertet wird. Wenn die Bedingung zu <code>False</code> wird, stoppt die Schleife.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## break Anweisungen

Wenn die Ausführung auf eine `break`-Anweisung trifft, wird die `while`-Schleifenklausel sofort verlassen:

```python
# break Anweisung: Schleife sofort beenden, wenn sie angetroffen wird
while True:  # Endlosschleife
    name = input('Please type your name: ')
    if name == 'your name':
        break  # Schleife sofort verlassen

print('Thank you!')
```

```output
Please type your name: your name
Thank you!
```

## continue Anweisungen

Wenn die Programmausführung auf eine `continue`-Anweisung trifft, springt die Programmausführung sofort zurück zum Anfang der Schleife.

```python
# continue Anweisung: Rest der Schleifeniteration überspringen und nächste Iteration starten
while True:
    name = input('Who are you? ')
    if name != 'Joe':
        continue  # Zur nächsten Iteration springen, nicht nach dem Passwort fragen
    password = input('Password? (It is a fish.): ')
    if password == 'swordfish':
        break  # Schleife verlassen, wenn das Passwort korrekt ist

print('Access granted.')
```

```output
Who are you? Charles
Who are you? Debora
Who are you? Joe
Password? (It is a fish.): swordfish
Access granted.
```

## For Schleife

Die `for`-Schleife iteriert über eine `list`, `tuple`, `dictionary`, `set` oder `string`:

```python
# for Schleife: über jedes Element in einer Sequenz iterieren
pets = ['Bella', 'Milo', 'Loki']
for pet in pets:  # Durch jedes Haustier in der Liste iterieren
    print(pet)  # Jeden Haustiernamen ausgeben
```

```output
Bella
Milo
Loki
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
Worüber iteriert eine <code>for</code>-Schleife?
</template>

<base-quiz-option value="A">A. Nur Zahlen</base-quiz-option>
<base-quiz-option value="B">B. Nur Strings</base-quiz-option>
<base-quiz-option value="C" correct>C. Jede iterierbare Sequenz (Liste, Tupel, Dictionary, Set, String usw.)</base-quiz-option>
<base-quiz-option value="D">D. Nur Listen</base-quiz-option>
<base-quiz-answer value="C">Eine <code>for</code>-Schleife kann über jede iterierbare Sequenz iterieren, einschließlich Listen, Tupeln, Dictionaries, Sets, Strings und anderen iterierbaren Objekten.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Die range() Funktion

Die `range()`-Funktion gibt eine Zahlenfolge zurück. Sie beginnt bei 0, wird um 1 erhöht und stoppt vor einer angegebenen Zahl:

```python
for i in range(5):
    print(f'Will stop at 5! or 4? ({i})')
```

```output
Will stop at 5! or 4? (0)
Will stop at 5! or 4? (1)
Will stop at 5! or 4? (2)
Will stop at 5! or 4? (3)
Will stop at 5! or 4? (4)
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Was erzeugt <code>range(5)</code>?
</template>

<base-quiz-option value="A">A. Zahlen von 1 bis 5</base-quiz-option>
<base-quiz-option value="B" correct>B. Zahlen von 0 bis 4</base-quiz-option>
<base-quiz-option value="C">C. Zahlen von 0 bis 5</base-quiz-option>
<base-quiz-option value="D">D. Fünf Zufallszahlen</base-quiz-option>
<base-quiz-answer value="B">Die Funktion <code>range(5)</code> erzeugt Zahlen von 0 bis 4 (insgesamt 5 Zahlen). Der Stoppwert ist exklusiv, sodass sie stoppt, bevor sie 5 erreicht.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Die `range()`-Funktion kann auch ihre 3 Standardargumente modifizieren. Die ersten beiden sind die `start`- und `stop`-Werte, und der dritte ist das `step`-Argument. Der Schritt ist die Menge, um die die Variable nach jeder Iteration erhöht wird.

```python
# range(start, stop, step)
for i in range(0, 10, 2):
   print(i)
```

```output
0
2
4
6
8
```

Sie können sogar eine negative Zahl für das `step`-Argument verwenden, damit die for-Schleife rückwärts zählt statt vorwärts.

```python
for i in range(5, -1, -1):
    print(i)
```

```output
5
4
3
2
1
0
```

## For else Anweisung

Dies ermöglicht die Angabe einer Anweisung, die ausgeführt wird, falls die gesamte Schleife durchlaufen wurde. Nur nützlich, wenn eine `break`-Bedingung in der Schleife auftreten kann:

```python
for i in [1, 2, 3, 4, 5]:
   if i == 3:
       break
else:
   print("only executed when no item is equal to 3")
```

## Programm beenden mit sys.exit()

Die `exit()`-Funktion ermöglicht das Beenden von Python.

```python
import sys

while True:
    feedback = input('Type exit to exit: ')
    if feedback == 'exit':
        print(f'You typed {feedback}.')
        sys.exit()
```

```output
Type exit to exit: open
Type exit to exit: close
Type exit to exit: exit
You typed exit.
```

## Relevante Links

- <router-link to="/cheatsheet/basics">Grundlagen</router-link>
- <router-link to="/cheatsheet/functions">Funktionen</router-link>
- <router-link to="/cheatsheet/exception-handling">Fehlerbehandlung</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Listen und Tupel</router-link>
- <router-link to="/cheatsheet/sets">Sets</router-link>
- <router-link to="/cheatsheet/dictionaries">Dictionaries</router-link>
- <router-link to="/cheatsheet/comprehensions">Comprehensions</router-link>
