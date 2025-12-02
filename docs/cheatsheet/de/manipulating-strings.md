---
title: 'String-Manipulation - Python Spickzettel'
description: "Ein Escape-Zeichen wird durch Eingabe eines Backslashs \ gefolgt von dem einzufügenden Zeichen erstellt."
labUrl: 'https://labex.io/de/labs/python-python-string-manipulation-633668?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Bearbeiten von Zeichenketten
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## Escape-Zeichen

Ein Escape-Zeichen wird erzeugt, indem man einen Backslash `\` gefolgt von dem Zeichen eingibt, das eingefügt werden soll.

| Escape-Zeichen | Wird ausgegeben als         |
| -------------- | --------------------------- |
| `\'`           | Einfaches Anführungszeichen |
| `\"`           | Doppeltes Anführungszeichen |
| `\t`           | Tabulator                   |
| `\n`           | Neue Zeile (Zeilenumbruch)  |
| `\\`           | Backslash                   |
| `\b`           | Rückschritt                 |
| `\ooo`         | Oktalwert                   |
| `\r`           | Wagenrücklauf               |

```python
# Escape-Zeichen: Backslash verwenden, um Sonderzeichen einzufügen
# \n = neue Zeile, \' = einfaches Anführungszeichen
print("Hello there!\nHow are you?\nI\'m doing fine.")
```

```output
Hello there!
How are you?
I'm doing fine.
```

## Raw Strings (Rohe Zeichenketten)

Ein Raw String ignoriert alle Escape-Zeichen vollständig und gibt jeden Backslash aus, der in der Zeichenkette vorkommt.

```python
# Raw String (r-Präfix): behandelt Backslashes als literale Zeichen
print(r"Hello there!\nHow are you?\nI\'m doing fine.")  # \n wird wörtlich ausgegeben
```

```output
Hello there!\nHow are you?\nI\'m doing fine.
```

Raw Strings werden hauptsächlich für die Definition von <router-link to="/cheatsheet/regular-expressions">Regulären Ausdrücken</router-link> verwendet.

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-manipulating-strings-1">
<template #question>
Was bewirkt ein Raw String (mit <code>r</code> präfixiert) in Python?
</template>

<base-quiz-option value="A">A. Wandelt alle Zeichen in Großbuchstaben um</base-quiz-option>
<base-quiz-option value="B" correct>B. Behandelt Backslashes als literale Zeichen und ignoriert Escape-Sequenzen</base-quiz-option>
<base-quiz-option value="C">C. Entfernt alle Leerzeichen</base-quiz-option>
<base-quiz-option value="D">D. Kehrt die Zeichenkette um</base-quiz-option>
<base-quiz-answer value="B">Raw Strings (mit <code>r</code> präfixiert) behandeln Backslashes als literale Zeichen, sodass Escape-Sequenzen wie <code>\n</code> nicht interpretiert werden.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Mehrzeilige Zeichenketten

```python
print(
"""Dear Alice,

Eve's cat has been arrested for catnapping,
cat burglary, and extortion.

Sincerely,
Bob"""
)
```

```output
Dear Alice,

Eve's cat has been arrested for catnapping,
cat burglary, and extortion.

Sincerely,
Bob
```

## Indizierung und Slicing von Zeichenketten

    H   e   l   l   o       w   o   r   l   d    !
    0   1   2   3   4   5   6   7   8   9   10   11

### Indizierung

```python
# String-Indizierung: Zugriff auf Zeichen über die Position (0-basiert)
spam = 'Hello world!'

spam[0]  # Gibt das erste Zeichen zurück: 'H'
```

```output
'H'
```

```python
spam[4]
```

```output
'o'
```

```python
spam[-1]
```

```output
'!'
```

### Slicing

```python
# String-Slicing: Teilzeichenkette mit der Syntax [start:ende] extrahieren
spam = 'Hello world!'

spam[0:5]  # Gibt Zeichen von Index 0 bis 4 zurück: 'Hello'
```

```output
'Hello'
```

```python
spam[:5]
```

```output
'Hello'
```

```python
spam[6:]
```

```output
'world!'
```

```python
spam[6:-1]
```

```output
'world'
```

```python
spam[:-1]
```

```output
'Hello world'
```

```python
spam[::-1]
```

```output
'!dlrow olleH'
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-manipulating-strings-2">
<template #question>
Was bewirkt <code>spam[::-1]</code> mit einer Zeichenkette?
</template>

<base-quiz-option value="A">A. Gibt das erste Zeichen zurück</base-quiz-option>
<base-quiz-option value="B">B. Gibt das letzte Zeichen zurück</base-quiz-option>
<base-quiz-option value="C" correct>C. Kehrt die Zeichenkette um</base-quiz-option>
<base-quiz-option value="D">D. Entfernt alle Zeichen</base-quiz-option>
<base-quiz-answer value="C">Der Slice <code>[::-1]</code> kehrt eine Zeichenkette um, indem er rückwärts durch alle Zeichen geht. Der Schrittwert <code>-1</code> bedeutet "gehe rückwärts".</base-quiz-answer>
</base-quiz-question>
</base-quiz>

```python
fizz = spam[0:5]
fizz
```

```output
'Hello'
```

## Die Operatoren in und not in

```python
'Hello' in 'Hello World'
```

```output
True
```

```python
'Hello' in 'Hello'
```

```output
True
```

```python
'HELLO' in 'Hello World'
```

```output
False
```

```python
'' in 'spam'
```

```output
True
```

```python
'cats' not in 'cats and dogs'
```

```output
False
```

## upper(), lower() und title()

Wandelt eine Zeichenkette in Groß-, Klein- oder Titel-Schreibweise um:

```python
greet = 'Hello world!'
greet.upper()
```

```output
'HELLO WORLD!'
```

```python
greet.lower()
```

```output
'hello world!'
```

```python
greet.title()
```

```output
'Hello World!'
```

## isupper() und islower() Methoden

Gibt `True` oder `False` zurück, nachdem ausgewertet wurde, ob eine Zeichenkette in Groß- oder Kleinschreibung vorliegt:

```python
spam = 'Hello world!'
spam.islower()
```

```output
False
```

```python
spam.isupper()
```

```output
False
```

```python
'HELLO'.isupper()
```

```output
True
```

```python
'abc12345'.islower()
```

```output
True
```

```python
'12345'.islower()
```

```output
False
```

```python
'12345'.isupper()
```

```output
False
```

## Die isX String-Methoden

| Methode     | Beschreibung                                                                                                                               |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| isalpha()   | gibt `True` zurück, wenn die Zeichenkette nur aus Buchstaben besteht.                                                                      |
| isalnum()   | gibt `True` zurück, wenn die Zeichenkette nur aus Buchstaben und Zahlen besteht.                                                           |
| isdecimal() | gibt `True` zurück, wenn die Zeichenkette nur aus Zahlen besteht.                                                                          |
| isspace()   | gibt `True` zurück, wenn die Zeichenkette nur aus Leerzeichen, Tabs und Zeilenumbrüchen besteht.                                           |
| istitle()   | gibt `True` zurück, wenn die Zeichenkette nur aus Wörtern besteht, die mit einem Großbuchstaben beginnen, gefolgt von nur Kleinbuchstaben. |

## startswith() und endswith()

```python
'Hello world!'.startswith('Hello')
```

```output
True
```

```python
'Hello world!'.endswith('world!')
```

```output
True
```

```python
'abc123'.startswith('abcdef')
```

```output
False
```

```python
'abc123'.endswith('12')
```

```output
False
```

```python
'Hello world!'.startswith('Hello world!')
```

```output
True
```

```python
'Hello world!'.endswith('Hello world!')
```

```output
True
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-manipulating-strings-3">
<template #question>
Was gibt <code>startswith()</code> zurück?
</template>

<base-quiz-option value="A" correct>A. <code>True</code>, wenn die Zeichenkette mit dem angegebenen Teilstring beginnt, andernfalls <code>False</code></base-quiz-option>
<base-quiz-option value="B">B. Den Teilstring, der übereinstimmt</base-quiz-option>
<base-quiz-option value="C">C. Den Index, an dem der Teilstring beginnt</base-quiz-option>
<base-quiz-option value="D">D. Eine neue Zeichenkette ohne das Präfix</base-quiz-option>
<base-quiz-answer value="A">Die Methode <code>startswith()</code> gibt einen booleschen Wert zurück: <code>True</code>, wenn die Zeichenkette mit dem angegebenen Teilstring beginnt, andernfalls <code>False</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## join() und split()

### join()

Die Methode `join()` nimmt alle Elemente eines Iterierbaren, wie einer <router-link to="/cheatsheet/lists-and-tuples">Liste</router-link>, <router-link to="/cheatsheet/dictionaries">Dictionary</router-link>, <router-link to="/cheatsheet/lists-and-tuples#the-tuple-data-type">Tupel</router-link> oder <router-link to="/cheatsheet/sets">Set</router-link>, und fügt sie zu einer Zeichenkette zusammen. Sie können auch einen Trennwert angeben.

```python
''.join(['My', 'name', 'is', 'Simon'])
```

```output
'MynameisSimon'
```

```python
', '.join(['cats', 'rats', 'bats'])
```

```output
'cats, rats, bats'
```

```python
' '.join(['My', 'name', 'is', 'Simon'])
```

```output
'My name is Simon'
```

```python
'ABC'.join(['My', 'name', 'is', 'Simon'])
```

```output
'MyABCnameABCisABCSimon'
```

### split()

Die Methode `split()` teilt eine `string` in eine `list` auf. Standardmäßig verwendet sie Leerzeichen, um die Elemente zu trennen, aber Sie können auch ein anderes Zeichen Ihrer Wahl festlegen:

```python
'My name is Simon'.split()
```

```output
['My', 'name', 'is', 'Simon']
```

```python
'MyABCnameABCisABCSimon'.split('ABC')
```

```output
['My', 'name', 'is', 'Simon']
```

```python
'My name is Simon'.split('m')
```

```output
['My na', 'e is Si', 'on']
```

```python
' My  name is  Simon'.split()
```

```output
['My', 'name', 'is', 'Simon']
```

```python
' My  name is  Simon'.split(' ')
```

```output
['', 'My', '', 'name', 'is', '', 'Simon']
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-manipulating-strings-4">
<template #question>
Was gibt <code>split()</code> zurück, wenn es auf eine Zeichenkette angewendet wird?
</template>

<base-quiz-option value="A">A. Eine Zeichenkette</base-quiz-option>
<base-quiz-option value="B" correct>B. Eine Liste von Zeichenketten</base-quiz-option>
<base-quiz-option value="C">C. Ein Tupel von Zeichenketten</base-quiz-option>
<base-quiz-option value="D">D. Ein Dictionary</base-quiz-option>
<base-quiz-answer value="B">Die Methode <code>split()</code> teilt eine Zeichenkette in eine Liste von Teilzeichenketten auf. Standardmäßig wird nach Leerzeichen geteilt, aber Sie können einen anderen Trennwert angeben.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Textausrichtung mit rjust(), ljust() und center()

```python
'Hello'.rjust(10)
```

```output
'     Hello'
```

```python
'Hello'.rjust(20)
```

```output
'               Hello'
```

```python
'Hello World'.rjust(20)
```

```output
'         Hello World'
```

```python
'Hello'.ljust(10)
```

```output
'Hello     '
```

```python
'Hello'.center(20)
```

```output
'       Hello       '
```

Ein optionales zweites Argument für `rjust()` und `ljust()` legt ein Füllzeichen fest, das vom Leerzeichen abweicht:

```python
'Hello'.rjust(20, '*')
```

```output
'***************Hello'
```

```python
'Hello'.ljust(20, '-')
```

```output
'Hello---------------'
```

```python
'Hello'.center(20, '=')
```

```output
'=======Hello========'
```

## Entfernen von Leerzeichen mit strip(), rstrip() und lstrip()

```python
spam = '    Hello World     '
spam.strip()
```

```output
'Hello World'
```

```python
spam.lstrip()
```

```output
'Hello World     '
```

```python
spam.rstrip()
```

```output
'    Hello World'
```

```python
spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')
```

```output
'BaconSpamEggs'
```

## Die Count-Methode

Zählt die Anzahl der Vorkommen eines gegebenen Zeichens oder Teilstrings in der Zeichenkette, auf die sie angewendet wird. Optional können Start- und Endindex angegeben werden.

```python
sentence = 'one sheep two sheep three sheep four'
sentence.count('sheep')
```

```output
3
```

```python
sentence.count('e')
```

```output
9
```

```python
# zählt die Anzahl von e nach 'one sh' d.h. 6 Zeichen seit Beginn der Zeichenkette
sentence.count('e', 6)
```

```output
8
```

```python
sentence.count('e', 7)
```

```output
7
```

## Replace-Methode

Ersetzt alle Vorkommen eines gegebenen Teilstrings durch einen anderen Teilstring. Optional kann ein drittes Argument angegeben werden, um die Anzahl der Ersetzungen zu begrenzen. Gibt eine neue Zeichenkette zurück.

```python
text = "Hello, world!"
text.replace("world", "planet")
```

```output
'Hello, planet!'
```

```python
fruits = "apple, banana, cherry, apple"
fruits.replace("apple", "orange", 1)
```

```output
'orange, banana, cherry, apple'
```

```python
sentence = "I like apples, Apples are my favorite fruit"
sentence.replace("apples", "oranges")
```

```output
'I like oranges, Apples are my favorite fruit'
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-manipulating-strings-5">
<template #question>
Was gibt die <code>replace()</code> Methode zurück?
</template>

<base-quiz-option value="A">A. Modifiziert die ursprüngliche Zeichenkette</base-quiz-option>
<base-quiz-option value="B">B. Gibt <code>None</code> zurück</base-quiz-option>
<base-quiz-option value="C" correct>C. Gibt eine neue Zeichenkette mit den vorgenommenen Ersetzungen zurück</base-quiz-option>
<base-quiz-option value="D">D. Gibt eine Liste der ersetzten Zeichenketten zurück</base-quiz-option>
<base-quiz-answer value="C">Die Methode <code>replace()</code> gibt eine neue Zeichenkette zurück, in der alle Vorkommen des alten Teilstrings durch den neuen Teilstring ersetzt wurden. Die ursprüngliche Zeichenkette wird nicht geändert.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Relevante Links

- <router-link to="/builtin/format">format()</router-link>
- <router-link to="/builtin/len">len()</router-link>
- <router-link to="/builtin/str">str()</router-link>
- <router-link to="/builtin/repr">repr()</router-link>
- <router-link to="/builtin/input">input()</router-link>
- <router-link to="/cheatsheet/string-formatting">String Formatierung</router-link>
- <router-link to="/cheatsheet/regular-expressions">Reguläre Ausdrücke</router-link>
