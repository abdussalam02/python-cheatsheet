---
title: 'Python Grundlagen - Python Spickzettel'
description: 'Lernen Sie die Python-Grundlagen mit unserem umfassenden Leitfaden zu Operatoren, Datentypen, Variablen, Funktionen und mehr. Perfekt für Anfänger, die die Grundlagen der Python-Programmierung erlernen.'
labUrl: 'https://labex.io/de/labs/python-python-basics-633647?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Grundlagen
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Wir alle müssen irgendwo anfangen, also wie wäre es hier. Dieser Leitfaden behandelt die grundlegenden Python-Basics, einschließlich Operatoren, Datentypen, Variablen und Kernfunktionen.

<base-disclaimer>
<base-disclaimer-title>
Übersicht der Python-Grundlagen
</base-disclaimer-title>
<base-disclaimer-content>
Die Kern-Python-Grundlagen, die jeder Anfänger kennen sollte:

- Variablen und grundlegende Typen
- Operatoren und Ausdrücke
- Strings und gängige Methoden
- Listen, Tupel und Dictionaries
- Grundlegende Kontrollstrukturen (if, for, while)
- Einfache Funktionen

</base-disclaimer-content>
</base-disclaimer>

## Mathematische Operatoren

Von **höchster** zu **niedrigster** Priorität:

| Operatoren | Operation        | Beispiel        |
| ---------- | ---------------- | --------------- |
| \*\*       | Potenzierung     | `2 ** 3 = 8`    |
| %          | Modulo/Rest      | `22 % 8 = 6`    |
| //         | Ganzzahldivision | `22 // 8 = 2`   |
| /          | Division         | `22 / 8 = 2.75` |
| \*         | Multiplikation   | `3 * 3 = 9`     |
| -          | Subtraktion      | `5 - 2 = 3`     |
| +          | Addition         | `2 + 2 = 4`     |

Beispiele für Ausdrücke:

```python
# Multiplikation hat eine höhere Priorität als Addition
# Dies wird ausgewertet als: 2 + (3 * 6) = 2 + 18 = 20
2 + 3 * 6
```

```output
20
```

```python
# Klammern überschreiben die Operatorrangfolge
# Dies wird ausgewertet als: 5 * 6 = 30
(2 + 3) * 6
```

```output
30
```

```python
2 ** 8
```

```output
256
```

```python
23 // 7
```

```output
3
```

```python
23 % 7
```

```output
2
```

```python
(5 - 1) * ((7 + 1) / (3 - 1))
```

```output
16.0
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Was ist das Ergebnis dieses Python-Ausdrucks?

```python
4 + 2 * 3
```

</template>

<base-quiz-option value="A" correct>A. 10</base-quiz-option>
<base-quiz-option value="B">B. 18</base-quiz-option>
<base-quiz-option value="C">C. 12</base-quiz-option>
<base-quiz-option value="D">D. 20</base-quiz-option>
<base-quiz-answer value="A">Multiplikation hat eine höhere Priorität als Addition, daher wird dies ausgewertet als: 4 + (2 \* 3) = 4 + 6 = 10</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Augmented Assignment Operatoren

| Operator    | Entsprechung     |
| ----------- | ---------------- |
| `var += 1`  | `var = var + 1`  |
| `var -= 1`  | `var = var - 1`  |
| `var *= 1`  | `var = var * 1`  |
| `var /= 1`  | `var = var / 1`  |
| `var //= 1` | `var = var // 1` |
| `var %= 1`  | `var = var % 1`  |
| `var **= 1` | `var = var ** 1` |

Beispiele:

```python
# Augmented Assignment: entspricht greeting = greeting + ' world!'
greeting = 'Hello'
greeting += ' world!'
greeting
```

```output
'Hello world!'
```

```python
# Erhöhe eine Zahl um 1
number = 1
number += 1
number
```

```output
2
```

```python
# Liste replizieren: entspricht my_list = my_list * 3
my_list = ['item']
my_list *= 3
my_list
```

```output
['item', 'item', 'item']
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Was ist der Wert von <code>x</code> nach Ausführung dieses Codes?

```python
x = 5
x += 3
```

</template>

<base-quiz-option value="A">A. 3</base-quiz-option>
<base-quiz-option value="B" correct>B. 8</base-quiz-option>
<base-quiz-option value="C">C. 5</base-quiz-option>
<base-quiz-option value="D">D. 15</base-quiz-option>
<base-quiz-answer value="B">Der Augmented Assignment Operator <code>+=</code> entspricht <code>x = x + 3</code>. Also beginnt <code>x</code> bei 5 und wird dann zu 5 + 3 = 8.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Walrus Operator

Der Walrus Operator ermöglicht die Zuweisung von Variablen innerhalb eines Ausdrucks, während gleichzeitig der Wert der Variablen zurückgegeben wird.

Beispiel:

```python
# Walrus Operator weist zu und gibt Wert in einem Ausdruck zurück
# my_var wird "Hello World!" zugewiesen und dann gedruckt
print(my_var:="Hello World!")
```

```output
Hello World!
```

```python
my_var="Yes"
print(my_var)
```

```output
Yes
```

```python
print(my_var:="Hello")
```

```output
Hello
```

Der _Walrus Operator_, oder **Assignment Expression Operator**, wurde erstmals 2018 durch [PEP 572](https://peps.python.org/pep-0572/) eingeführt und dann offiziell mit **Python 3.8** im Oktober 2019 veröffentlicht.

<base-disclaimer>
  <base-disclaimer-title>
    Syntax Semantik & Beispiele
  </base-disclaimer-title>
  <base-disclaimer-content>
  Das <a href="https://peps.python.org/pep-0572/" target="_blank">PEP 572</a> liefert die Syntax, Semantik und Beispiele für den Walrus Operator.
  </base-disclaimer-content>
</base-disclaimer>

## Datentypen

Das Verständnis von Datentypen ist eine der wichtigsten Grundlagen in Python. Python verfügt über neun grundlegende eingebaute Datentypen, die fast alles abdecken, was Sie benötigen:

| Datentyp                                                   | Beispiele                                | Beschreibung                                |
| ---------------------------------------------------------- | ---------------------------------------- | ------------------------------------------- |
| **Zahlen**                                                 |                                          |                                             |
| <router-link to='/builtin/int'>`int`</router-link>         | `-2, -1, 0, 1, 2, 3, 4, 5`               | Ganze Zahlen (Integer)                      |
| <router-link to='/builtin/float'>`float`</router-link>     | `-1.25, -1.0, -0.5, 0.0, 0.5, 1.0, 1.25` | Zahlen mit Dezimalpunkten                   |
| <router-link to='/builtin/complex'>`complex`</router-link> | `2+3j, complex(1, 4)`                    | Zahlen mit Real- und Imaginärteil           |
| **Text**                                                   |                                          |                                             |
| <router-link to='/builtin/str'>`str`</router-link>         | `'a', 'Hello!', "Python"`                | Text und Zeichen                            |
| **Boolesch**                                               |                                          |                                             |
| <router-link to='/builtin/bool'>`bool`</router-link>       | `True, False`                            | Wahr- oder Falschwerte                      |
| **None**                                                   |                                          |                                             |
| `NoneType`                                                 | `None`                                   | Repräsentiert "kein Wert" oder "nichts"     |
| **Sammlungen**                                             |                                          |                                             |
| <router-link to='/builtin/list'>`list`</router-link>       | `[1, 2, 3], ['a', 'b', 'c']`             | Geordnete, veränderbare Sammlungen          |
| <router-link to='/builtin/dict'>`dict`</router-link>       | `{'name': 'Alice', 'age': 30}`           | Schlüssel-Wert-Paare                        |
| <router-link to='/builtin/tuple'>`tuple`</router-link>     | `(1, 2, 3), ('a', 'b')`                  | Geordnete, unveränderbare Sammlungen        |
| <router-link to='/builtin/set'>`set`</router-link>         | `{1, 2, 3}, {'a', 'b', 'c'}`             | Ungeordnete Sammlungen eindeutiger Elemente |

### Kurze Beispiele

```python
# Zahlen
age = 25                    # int
price = 19.99              # float
coordinate = 2 + 3j        # complex

# Text
name = "Alice"             # str

# Boolesch
is_student = True          # bool

# None
result = None              # NoneType

# Sammlungen
scores = [85, 92, 78]      # list
person = {'name': 'Bob', 'age': 30}  # dict
coordinates = (10, 20)     # tuple
unique_ids = {1, 2, 3}     # set
```

Für einen umfassenden Leitfaden mit visuellen Beispielen und detaillierten Erklärungen, wann jeder Typ verwendet werden sollte, siehe: <router-link to="/blog/python-data-types">Python Datentypen: Ein visueller Leitfaden für Anfänger</router-link>.

## Konkatenation und Replikation

String-Konkatenation:

```python
# String-Konkatenation: benachbarte Strings werden automatisch zusammengefügt
'Alice' 'Bob'
```

```output
'AliceBob'
```

String-Replikation:

```python
# String-Replikation: String mehrmals wiederholen
'Alice' * 5
```

```output
'AliceAliceAliceAliceAlice'
```

## Variablen

Variablen sind ein grundlegender Bestandteil der Python-Basics. Sie können einer Variablen einen beliebigen Namen geben, solange sie die folgenden Regeln befolgt:

1. Sie kann nur ein Wort sein.

```python
# schlecht
my variable = 'Hello'

# gut
var = 'Hello'
```

2. Sie darf nur Buchstaben, Zahlen und das Unterstrichzeichen (`_`) enthalten.

```python
# schlecht
%$@variable = 'Hello'

# gut
my_var = 'Hello'

# gut
my_var_2 = 'Hello'
```

3. Sie darf nicht mit einer Zahl beginnen.

```python
# das funktioniert nicht
23_var = 'hello'
```

4. Ein Variablenname, der mit einem Unterstrich (`_`) beginnt, gilt als "unbrauchbar".

```python
# _spam sollte im Code nicht wiederverwendet werden
_spam = 'Hello'
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
Welche der folgenden Bezeichnungen ist in Python-Grundlagen ein gültiger Variablenname?
</template>

<base-quiz-option value="A">A. <code>3value</code></base-quiz-option>
<base-quiz-option value="B">B. <code>user-name</code></base-quiz-option>
<base-quiz-option value="C" correct>C. <code>user_name</code></base-quiz-option>
<base-quiz-option value="D">D. <code>for</code></base-quiz-option>
<base-quiz-answer value="C"><code>user_name</code> ist ein gültiger Variablenname, da er nur Buchstaben, Zahlen und Unterstriche verwendet und nicht mit einer Zahl beginnt.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Kommentare

Inline-Kommentar:

```python
# Dies ist ein Kommentar
```

Mehrzeiliger Kommentar:

```python
# Dies ist ein
# mehrzeiliger Kommentar
```

Code mit einem Kommentar:

```python
a = 1  # Initialisierung
```

Beachten Sie die zwei Leerzeichen vor dem Kommentar.

Funktions-Docstring:

```python
def foo():
    """
    Dies ist ein Funktions-Docstring
    Sie können auch verwenden:
    ''' Funktions-Docstring '''
    """
```

## Die print() Funktion

Die Funktion `print()` ist eine der ersten Python-Grundlagen, die Sie lernen werden. Sie schreibt den Wert des/der ihr übergebenen Argument(e). [...] sie verarbeitet mehrere Argumente, Gleitkommazahlen und Strings. Strings werden ohne Anführungszeichen gedruckt, und zwischen den Elementen wird ein Leerzeichen eingefügt, sodass Sie Dinge schön formatieren können:

```python
print('Hello world!')
```

```output
Hello world!
```

```python
a = 1
print('Hello world!', a)
```

```output
Hello world! 1
```

### Das end Schlüsselwort

Das Schlüsselwortargument `end` kann verwendet werden, um den Zeilenumbruch nach der Ausgabe zu vermeiden oder die Ausgabe mit einem anderen String zu beenden:

```python
# Verwenden Sie den end-Parameter, um zu ändern, was nach jeder print-Anweisung kommt
phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
for word in phrase:
    print(word, end='-')  # Verwenden Sie '-' anstelle eines Zeilenumbruchs
```

```output
printed-with-a-dash-in-between-
```

### Das sep Schlüsselwort

Das Schlüsselwort `sep` gibt an, wie die Objekte getrennt werden sollen, wenn es mehr als eines gibt:

```python
# Verwenden Sie den sep-Parameter, um den Separator zwischen mehreren Argumenten festzulegen
print('cats', 'dogs', 'mice', sep=',')  # Komma-getrennte Ausgabe
```

```output
cats,dogs,mice
```

## Die input() Funktion

Diese Funktion nimmt die Eingabe des Benutzers entgegen und wandelt sie in einen String um:

```python
# input() liest Benutzereingaben und gibt sie als String zurück
print('What is your name?')   # nach dem Namen fragen
my_name = input()  # Warten, bis der Benutzer tippt und Enter drückt
print('Hi, {}'.format(my_name))
```

```output
What is your name?
Martha
Hi, Martha
```

`input()` kann auch eine Standardnachricht festlegen, ohne `print()` zu verwenden:

```python
my_name = input('What is your name? ')  # Standardnachricht
print('Hi, {}'.format(my_name))
```

```output
What is your name? Martha
Hi, Martha
```

Es ist auch möglich, formatierte Strings zu verwenden, um die Verwendung von .format zu vermeiden:

```python
# input() kann eine Eingabeaufforderungsnachricht direkt anzeigen
my_name = input('What is your name? ')  # Eingabeaufforderung und Lesen in einem Aufruf
print(f'Hi, {my_name}')  # f-String für String-Formatierung
```

```output
What is your name? Martha
Hi, Martha
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Welchen Typ gibt `input()` in Python-Grundlagen zurück?
</template>

<base-quiz-option value="A">A. int</base-quiz-option>
<base-quiz-option value="B" correct>B. str</base-quiz-option>
<base-quiz-option value="C">C. float</base-quiz-option>
<base-quiz-option value="D">D. Hängt von der Benutzereingabe ab</base-quiz-option>
<base-quiz-answer value="B">Die Funktion <code>input()</code> gibt immer einen String zurück, unabhängig davon, was der Benutzer eingibt. Sie müssen ihn bei Bedarf in andere Typen umwandeln.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Die len() Funktion

Ergibt den ganzzahligen Wert der Anzahl der Zeichen in einem String, einer Liste, einem Dictionary usw.:

```python
# len() gibt die Anzahl der Zeichen in einem String zurück
len('hello')  # Gibt 5 zurück
```

```output
5
```

```python
# len() gibt die Anzahl der Elemente in einer Liste zurück
len(['cat', 3, 'dog'])  # Gibt 3 zurück (drei Elemente)
```

```output
3
```

<base-warning>
  <base-warning-title>Test auf Leere</base-warning-title>
  <base-warning-content>
    Der Test auf die Leere von Strings, Listen, Dictionaries usw. sollte nicht
    <code>len</code> verwenden, sondern die direkte boolesche Auswertung bevorzugen.
  </base-warning-content>
</base-warning>

Testbeispiel für Leere:

```python
a = [1, 2, 3]

# schlecht: unnötige len()-Prüfung
if len(a) > 0:  # ergibt True
    print("the list is not empty!")
```

```output
the list is not empty!
```

```python
# gut: direkte boolesche Auswertung (Pythonischer Weg)
if a:  # ergibt True, wenn die Liste nicht leer ist
    print("the list is not empty!")
```

```output
the list is not empty!
```

## Die str(), int() und float() Funktionen

Diese Funktionen ermöglichen es Ihnen, den Typ einer Variablen zu ändern. Sie können beispielsweise von einem `Integer` oder `Float` in einen `String` umwandeln:

```python
# Integer in String umwandeln
str(29)  # Gibt '29' zurück
```

```output
'29'
```

```python
str(-3.14)
```

```output
'-3.14'
```

Oder von einem `String` in einen `Integer` oder `Float`:

```python
# String in Integer umwandeln
int('11')  # Gibt 11 zurück
```

```output
11
```

```python
# String in Float umwandeln
float('3.14')  # Gibt 3.14 zurück
```

```output
3.14
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
Was ist das Ergebnis dieses Python-Codes?

```python
result = int('42')
type(result)
```

</template>

<base-quiz-option value="A">A. <code>str</code></base-quiz-option>
<base-quiz-option value="B">B. <code>float</code></base-quiz-option>
<base-quiz-option value="C" correct>C. <code>int</code></base-quiz-option>
<base-quiz-option value="D">D. <code>NoneType</code></base-quiz-option>
<base-quiz-answer value="C">Die Funktion <code>int()</code> konvertiert einen String in einen Integer. Daher gibt <code>int('42')</code> den Integer <code>42</code> zurück, und <code>type(42)</code> gibt <code>int</code> zurück.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Relevante Links

- <router-link to="/blog/python-data-types">Python Datentypen: Ein visueller Leitfaden für Anfänger</router-link>
- <router-link to="/blog/python-comprehensions-step-by-step">Python Comprehensions Schritt für Schritt</router-link>
- <router-link to="/cheatsheet/control-flow">Kontrollfluss</router-link>
- <router-link to="/cheatsheet/functions">Funktionen</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Listen und Tupel</router-link>
- <router-link to="/cheatsheet/dictionaries">Dictionaries</router-link>
- <router-link to="/cheatsheet/sets">Sets</router-link>
- <router-link to="/cheatsheet/string-formatting">String-Formatierung</router-link>
