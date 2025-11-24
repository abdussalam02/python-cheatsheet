---
title: 'Python Sets - Python Spickzettel'
description: 'Python verfügt über mehrere integrierte Datentypen, die uns bei der Organisation unserer Daten helfen. Diese Strukturen umfassen Listen, Dictionaries, Tupel und Mengen (Sets).'
labUrl: 'https://labex.io/de/labs/python-python-sets-633665?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Mengen
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Python ist mit mehreren integrierten Datentypen ausgestattet, die uns bei der Organisation unserer Daten helfen. Zu diesen Strukturen gehören Listen, Dictionaries, Tupel und **Mengen** (Sets).

<base-disclaimer>
  <base-disclaimer-title>
    Aus der Python 3 <a target="_blank" href="https://docs.python.org/3/tutorial/datastructures.html#sets">Dokumentation</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Eine Menge ist eine ungeordnete Sammlung ohne doppelte Elemente. Zu den grundlegenden Verwendungszwecken gehören die Mitgliedschaftsprüfung und das Eliminieren doppelter Einträge.
  </base-disclaimer-content>
</base-disclaimer>

Lesen Sie <router-link to="/blog/python-sets-what-why-how">Python Sets: What, Why and How</router-link> für eine tiefere Referenz.

## Initialisieren einer Menge

Es gibt zwei Möglichkeiten, Mengen zu erstellen: mit geschweiften Klammern `{}` und der integrierten Funktion `set()`.

<base-warning>
  <base-warning-title>
    Leere Mengen
  </base-warning-title>
  <base-warning-content>
    Stellen Sie beim Erstellen einer Menge sicher, dass Sie nicht leere geschweifte Klammern <code>{}</code> verwenden, da Sie sonst stattdessen ein leeres Dictionary erhalten.
  </base-warning-content>
</base-warning>

```python
# Create set using curly braces or set() function
s = {1, 2, 3}  # Using curly braces
s = set([1, 2, 3])  # Using set() constructor

# Warning: empty {} creates a dictionary, not a set
s = {}  # this will create a dictionary instead of a set
type(s)  # Returns <class 'dict'>
```

```output
<class 'dict'>
```

## Ungeordnete Sammlungen eindeutiger Elemente

Eine Menge entfernt automatisch alle doppelten Werte.

```python
# Sets automatically remove duplicates
s = {1, 2, 3, 2, 3, 4}  # Duplicates are removed
s  # Returns {1, 2, 3, 4}
```

```output
{1, 2, 3, 4}
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
What happens when you create a set with duplicate values?
</template>

<base-quiz-option value="A" correct>A. Duplicates are automatically removed</base-quiz-option>
<base-quiz-option value="B">B. An error is raised</base-quiz-option>
<base-quiz-option value="C">C. The set keeps all duplicates</base-quiz-option>
<base-quiz-option value="D">D. Only the first occurrence is kept</base-quiz-option>
<base-quiz-answer value="A">Sets automatically remove duplicate values. A set is an unordered collection with no duplicate elements.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Und als ungeordnete Datenstruktur können sie nicht indiziert werden.

```python
s = {1, 2, 3}
s[0]
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
```

## set add und update

Mit der Methode `add()` können wir ein einzelnes Element zur Menge hinzufügen.

```python
# add() method: add a single element to the set
s = {1, 2, 3}
s.add(4)  # Add element 4
s
```

```output
{1, 2, 3, 4}
```

Und mit `update()` mehrere:

```python
# update() method: add multiple elements from an iterable
s = {1, 2, 3}
s.update([2, 3, 4, 5, 6])  # Add multiple elements (duplicates ignored)
s
```

```output
{1, 2, 3, 4, 5, 6}
```

## set remove und discard

Beide Methoden entfernen ein Element aus der Menge, aber `remove()` löst einen `key error` aus, wenn der Wert nicht existiert.

```python
# remove() method: remove element, raises KeyError if not found
s = {1, 2, 3}
s.remove(3)  # Remove element 3
s
```

```output
{1, 2}
```

```python
s.remove(3)
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 3
```

`discard()` löst keine Fehler aus.

```python
# discard() method: remove element, no error if not found
s = {1, 2, 3}
s.discard(3)  # Remove element 3 (safe, no error if missing)
s
```

```output
{1, 2}
```

```python
s.discard(3)
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
What is the difference between <code>remove()</code> and <code>discard()</code> methods for sets?
</template>

<base-quiz-option value="A">A. <code>remove()</code> removes one element, <code>discard()</code> removes all</base-quiz-option>
<base-quiz-option value="B">B. There is no difference</base-quiz-option>
<base-quiz-option value="C" correct>C. <code>remove()</code> raises an error if element doesn't exist, <code>discard()</code> does not</base-quiz-option>
<base-quiz-option value="D">D. <code>remove()</code> is faster</base-quiz-option>
<base-quiz-answer value="C">Both methods remove an element from a set, but <code>remove()</code> raises a <code>KeyError</code> if the element doesn't exist, while <code>discard()</code> does nothing if the element is missing.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## set union

`union()` oder `|` erstellen eine neue Menge mit allen Elementen aus den angegebenen Mengen.

```python
# union(): combine all elements from multiple sets (no duplicates)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.union(s2)  # or 's1 | s2' - returns {1, 2, 3, 4, 5}
```

```output
{1, 2, 3, 4, 5}
```

## set intersection

`intersection()` oder `&` geben eine Menge zurück, die nur die Elemente enthält, die allen gemeinsam sind.

```python
# intersection(): return elements common to all sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
s1.intersection(s2, s3)  # or 's1 & s2 & s3' - returns {3}
```

```output
{3}
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
What does <code>intersection()</code> return for sets?
</template>

<base-quiz-option value="A">A. All elements from all sets</base-quiz-option>
<base-quiz-option value="B" correct>B. Only elements that are common to all sets</base-quiz-option>
<base-quiz-option value="C">C. Elements in the first set but not in others</base-quiz-option>
<base-quiz-option value="D">D. Elements in either set but not both</base-quiz-option>
<base-quiz-answer value="B">The <code>intersection()</code> method returns a set containing only elements that are present in all the sets being compared.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## set difference

`difference()` oder `-` geben nur die Elemente zurück, die für die erste Menge (die aufgerufene Menge) eindeutig sind.

```python
# difference(): return elements in first set but not in others
s1 = {1, 2, 3}
s2 = {2, 3, 4}

s1.difference(s2)  # or 's1 - s2' - returns {1}
```

```output
{1}
```

```python
s2.difference(s1) # or 's2 - s1'
```

```output
{4}
```

## set symmetric_difference

`symmetric_difference()` oder `^` geben alle Elemente zurück, die zwischen ihnen nicht gemeinsam sind.

```python
# symmetric_difference(): return elements in either set, but not both
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1.symmetric_difference(s2)  # or 's1 ^ s2' - returns {1, 4}
```

```output
{1, 4}
```

<base-quiz>
<base-quiz-question correct="D">
<template #question>
What does <code>symmetric_difference()</code> return for two sets?
</template>

<base-quiz-option value="A">A. All elements from both sets</base-quiz-option>
<base-quiz-option value="B">B. Only elements common to both sets</base-quiz-option>
<base-quiz-option value="C">C. Elements in the first set but not in the second</base-quiz-option>
<base-quiz-option value="D" correct>D. Elements in either set, but not in both</base-quiz-option>
<base-quiz-answer value="D">The <code>symmetric_difference()</code> method returns a set containing elements that are in either set, but not in both sets.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Relevante Links

- <router-link to="/blog/python-data-types">Python Data Types Blog Post</router-link>
- <router-link to="/blog/python-sets-what-why-how">Python Sets: What, Why and How</router-link>
- <router-link to="/cheatsheet/dictionaries">Python Dictionaries</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Python Lists and Tuples</router-link>
