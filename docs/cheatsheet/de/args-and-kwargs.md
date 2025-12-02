---
title: 'Python Args und Kwargs – Python Spickzettel'
description: 'Args und Kwargs wirken einschüchternd, sind aber leicht zu verstehen und verleihen Ihren Funktionen Flexibilität und Lesbarkeit.'
labUrl: 'https://labex.io/de/labs/python-python-args-and-kwargs-633646?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Args und Kwargs
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a href="https://docs.python.org/3/tutorial/index.html">Python args und kwargs leicht gemacht</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    <code>*args</code> und <code>**kwargs</code> mögen beängstigend erscheinen, aber die Wahrheit ist, dass sie nicht so schwer zu verstehen sind und die Macht haben, Ihren Funktionen viel Flexibilität zu verleihen.
  </base-disclaimer-content>
</base-disclaimer>

Lesen Sie den Artikel <router-link to="/blog/python-easy-args-kwargs">Python \*args und \*\*kwargs leicht gemacht</router-link> für eine tiefere Einführung.

## Args und Kwargs

`*args` und `**kwargs` ermöglichen es Ihnen, eine undefinierte Anzahl von Argumenten und Schlüsselwörtern zu übergeben, wenn Sie eine Funktion aufrufen.

```python
# Define a function that accepts any number of positional and keyword arguments
def some_function(*args, **kwargs):
    pass

# Call with any number of positional arguments
some_function(arg1, arg2, arg3)

# Call with any number of keyword arguments
some_function(key1=arg1, key2=arg2, key3=arg3)

# Call with both positional and keyword arguments
some_function(arg, key1=arg1)

# Or call with no arguments at all
some_function()
```

<base-warning>
  <base-warning-title>
    Python-Konventionen
  </base-warning-title>
  <base-warning-content>
    Die Wörter <code>*args</code> und <code>**kwargs</code> sind Konventionen. Sie werden nicht vom Interpreter erzwungen, gelten aber in der Python-Community als gute Praxis.
  </base-warning-content>
</base-warning>

## args

Sie können auf die _Argumente_ über die Variable `args` zugreifen:

```python
# *args collects positional arguments into a tuple
def some_function(*args):
    print(f'Arguments passed: {args} as {type(args)}')

# Pass multiple arguments - they'll be collected into args tuple
some_function('arg1', 'arg2', 'arg3')
```

```output
Arguments passed: ('arg1', 'arg2', 'arg3') as <class 'tuple'>
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-args-and-kwargs-1">
<template #question>
In welchen Datentyp sammelt <code>*args</code> Argumente?
</template>

<base-quiz-option value="A">A. Eine Liste</base-quiz-option>
<base-quiz-option value="B" correct>B. Ein Tupel</base-quiz-option>
<base-quiz-option value="C">C. Ein Dictionary</base-quiz-option>
<base-quiz-option value="D">D. Eine Menge</base-quiz-option>
<base-quiz-answer value="B">Der Parameter <code>\*args</code> sammelt positionelle Argumente in einem Tupel. Dies ermöglicht es einer Funktion, eine beliebige Anzahl positioneller Argumente anzunehmen.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## kwargs

Schlüsselwörter werden über die Variable `kwargs` aufgerufen:

```python
# **kwargs collects keyword arguments into a dictionary
def some_function(**kwargs):
    print(f'keywords: {kwargs} as {type(kwargs)}')

# Pass keyword arguments - they'll be collected into kwargs dict
some_function(key1='arg1', key2='arg2')
```

```output
keywords: {'key1': 'arg1', 'key2': 'arg2'} as <class 'dict'>
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-args-and-kwargs-2">
<template #question>
In welchen Datentyp sammelt <code>**kwargs</code> Argumente?
</template>

<base-quiz-option value="A">A. Eine Liste</base-quiz-option>
<base-quiz-option value="B">B. Ein Tupel</base-quiz-option>
<base-quiz-option value="C" correct>C. Ein Dictionary</base-quiz-option>
<base-quiz-option value="D">D. Eine Menge</base-quiz-option>
<base-quiz-answer value="C">Der Parameter <code>\*\*kwargs</code> sammelt Schlüsselwortargumente in einem Dictionary. Dies ermöglicht es einer Funktion, eine beliebige Anzahl von Schlüsselwortargumenten anzunehmen.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Relevante Links

- <router-link to="/cheatsheet/functions">Funktionen</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Listen und Tupel</router-link>
- <router-link to="/cheatsheet/dictionaries">Python Dictionaries</router-link>
- <router-link to="/blog/python-easy-args-kwargs">Python \*args und \*\*kwargs leicht gemacht</router-link>
- <router-link to="/builtin/tuple">tuple()</router-link>
- <router-link to="/builtin/dict">dict()</router-link>
