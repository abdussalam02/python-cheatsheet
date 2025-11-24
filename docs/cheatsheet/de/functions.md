---
title: 'Python Funktionen - Python Spickzettel'
description: 'In Python ist eine Funktion ein organisierter Codeblock, der zur Ausführung einer einzelnen Aufgabe dient.'
labUrl: 'https://labex.io/de/labs/python-python-functions-633658?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Funktionen
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikiversity.org/wiki/Programming_Fundamentals/Functions">Programming Functions</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Eine Funktion ist ein Block von organisiertem Code, der verwendet wird, um eine einzelne Aufgabe auszuführen. Sie bieten eine bessere Modularität für Ihre Anwendung und Wiederverwendbarkeit.
  </base-disclaimer-content>
</base-disclaimer>

## Funktionsargumente

Eine Funktion kann `Argumente` und `Rückgabewerte` entgegennehmen:

Im folgenden Beispiel empfängt die Funktion **say_hello** das Argument "name" und gibt eine Begrüßung aus:

```python
# Define a function that takes one argument
def say_hello(name):
   print(f'Hello {name}')

# Call the function with a string argument
say_hello('Carlos')
```

```output
Hello Carlos
```

```python
say_hello('Wanda')
```

```output
Hello Wanda
```

```python
say_hello('Rose')
```

```output
Hello Rose
```

## Schlüsselwortargumente

Um die Lesbarkeit des Codes zu verbessern, sollten wir so explizit wie möglich sein. Dies können wir in unseren Funktionen durch die Verwendung von `Keyword Arguments` (Schlüsselwortargumenten) erreichen:

```python
# Function with multiple parameters
def say_hi(name, greeting):
   print(f"{greeting} {name}")

# Positional arguments: order matters
say_hi('John', 'Hello')
```

```output
Hello John
```

```python
# Keyword arguments: order doesn't matter, more readable
say_hi(name='Anna', greeting='Hi')
```

```output
Hi Anna
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
What is the main advantage of using keyword arguments in Python functions?
</template>

<base-quiz-option value="A">A. They execute faster</base-quiz-option>
<base-quiz-option value="B">B. They use less memory</base-quiz-option>
<base-quiz-option value="C" correct>C. They improve code readability and order doesn't matter</base-quiz-option>
<base-quiz-option value="D">D. They prevent errors</base-quiz-option>
<base-quiz-answer value="C">Keyword arguments improve code readability by making it clear what each argument represents, and they allow you to pass arguments in any order.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Rückgabewerte

Wenn Sie eine Funktion mit der `def`-Anweisung erstellen, können Sie mit einer `return`-Anweisung festlegen, was der Rückgabewert sein soll. Eine Rückgabeanweisung besteht aus Folgendem:

- Das Schlüsselwort `return`.

- Der Wert oder Ausdruck, den die Funktion zurückgeben soll.

```python
# Function that returns a value using return statement
def sum_two_numbers(number_1, number_2):
   return number_1 + number_2

# Call function and store the returned value
result = sum_two_numbers(7, 8)
print(result)
```

```output
15
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
What keyword is used to return a value from a function in Python?
</template>

<base-quiz-option value="A" correct>A. <code>return</code></base-quiz-option>
<base-quiz-option value="B">B. <code>output</code></base-quiz-option>
<base-quiz-option value="C">C. <code>yield</code></base-quiz-option>
<base-quiz-option value="D">D. <code>exit</code></base-quiz-option>
<base-quiz-answer value="A">The <code>return</code> keyword is used to return a value from a function. If no return statement is used, the function returns <code>None</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Lokaler und globaler Gültigkeitsbereich (Scope)

- Code im globalen Gültigkeitsbereich kann keine lokalen Variablen verwenden.

- Ein lokaler Gültigkeitsbereich kann jedoch auf globale Variablen zugreifen.

- Code im lokalen Gültigkeitsbereich einer Funktion kann keine Variablen in einem anderen lokalen Gültigkeitsbereich verwenden.

- Sie können denselben Namen für verschiedene Variablen verwenden, wenn diese sich in unterschiedlichen Gültigkeitsbereichen befinden. Das heißt, es kann eine lokale Variable namens `spam` und eine globale Variable, die ebenfalls `spam` heißt, geben.

```python
# Global variable: accessible everywhere
global_variable = 'I am available everywhere'

def some_function():
    print(global_variable)  # Can access global variable
    # Local variable: only exists within this function
    local_variable = "only available within this function"
    print(local_variable)

# This will raise NameError: local_variable doesn't exist in global scope
print(local_variable)
```

```output
Traceback (most recent call last):
  File "<stdin>", line 10, in <module>
NameError: name 'local_variable' is not defined
```

## Die global-Anweisung

Wenn Sie eine globale Variable innerhalb einer Funktion ändern müssen, verwenden Sie die `global`-Anweisung:

```python
# Use 'global' keyword to modify global variable from inside function
def spam():
    global eggs  # Declare that we're modifying the global variable
    eggs = 'spam'  # This changes the global variable

eggs = 'global'
spam()  # Function modifies global variable
print(eggs)  # Prints 'spam', not 'global'
```

```output
spam
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
What keyword must you use inside a function to modify a global variable?
</template>

<base-quiz-option value="A">A. <code>nonlocal</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>global</code></base-quiz-option>
<base-quiz-option value="C">C. <code>extern</code></base-quiz-option>
<base-quiz-option value="D">D. No keyword needed</base-quiz-option>
<base-quiz-answer value="B">The <code>global</code> keyword must be used inside a function to modify a global variable. Without it, Python will create a local variable instead.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Es gibt vier Regeln, um festzustellen, ob sich eine Variable in einem lokalen oder globalen Gültigkeitsbereich befindet:

1. Wenn eine Variable im globalen Gültigkeitsbereich verwendet wird (d. h. außerhalb aller Funktionen), ist sie immer eine globale Variable.

1. Wenn es in einer Funktion eine `global`-Anweisung für diese Variable gibt, ist sie eine globale Variable.

1. Andernfalls, wenn die Variable in einer Zuweisungsanweisung in der Funktion verwendet wird, ist sie eine lokale Variable.

1. Aber wenn die Variable nicht in einer Zuweisungsanweisung verwendet wird, ist sie eine globale Variable.

## Lambda-Funktionen

In Python ist eine Lambda-Funktion eine einzeilige, anonyme Funktion, die eine beliebige Anzahl von Argumenten haben kann, aber nur einen Ausdruck enthalten darf.

<base-disclaimer>
  <base-disclaimer-title>
    From the <a target="_blank" href="https://docs.python.org/3/library/ast.html?highlight=lambda#function-and-class-definitions">Python 3 Tutorial</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    lambda is a minimal function definition that can be used inside an expression. Unlike FunctionDef, body holds a single node.
  </base-disclaimer-content>
</base-disclaimer>

<base-warning>
  <base-warning-title>
    Single line expression
  </base-warning-title>
  <base-warning-content>
    Lambda functions can only evaluate an expression, like a single line of code.
  </base-warning-content>
</base-warning>

Diese Funktion:

```python
# Regular function definition
def add(x, y):
    return x + y

add(5, 3)
```

```output
8
```

Ist äquivalent zur _Lambda_-Funktion:

```python
# Lambda function: anonymous function defined in one line
# Syntax: lambda arguments: expression
add = lambda x, y: x + y
add(5, 3)
```

```output
8
```

<base-quiz>
<base-quiz-question correct="D">
<template #question>
What is a lambda function in Python?
</template>

<base-quiz-option value="A">A. A function that can only be called once</base-quiz-option>
<base-quiz-option value="B">B. A function that takes no arguments</base-quiz-option>
<base-quiz-option value="C">C. A function that returns multiple values</base-quiz-option>
<base-quiz-option value="D" correct>D. A single-line anonymous function that can have any number of arguments but only one expression</base-quiz-option>
<base-quiz-answer value="D">A lambda function is an anonymous, single-line function defined using the <code>lambda</code> keyword. It can take any number of arguments but can only contain a single expression.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Wie reguläre verschachtelte Funktionen funktionieren auch Lambdas als lexikalische Closures:

```python
# Lambda closure: lambda function that captures variable from outer scope
def make_adder(n):
    return lambda x: x + n  # Lambda captures 'n' from outer function

# Create functions that add different amounts
plus_3 = make_adder(3)  # Returns lambda that adds 3
plus_5 = make_adder(5)  # Returns lambda that adds 5

plus_3(4)  # Returns 4 + 3 = 7
```

```output
7
```

```python
plus_5(4)
```

```output
9
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
What does a lambda closure allow you to do?
</template>

<base-quiz-option value="A" correct>A. Capture variables from the outer scope</base-quiz-option>
<base-quiz-option value="B">B. Modify global variables without the global keyword</base-quiz-option>
<base-quiz-option value="C">C. Return multiple values</base-quiz-option>
<base-quiz-option value="D">D. Execute code asynchronously</base-quiz-option>
<base-quiz-answer value="A">Lambda closures allow lambda functions to capture and use variables from their enclosing scope, similar to regular nested functions.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Relevante Links

- <router-link to="/blog/python-easy-args-kwargs">\*args and \*\*kwargs explained</router-link>
- <router-link to="/cheatsheet/args-and-kwargs">Args und Kwargs</router-link>
- <router-link to="/cheatsheet/decorators">Dekoratoren</router-link>
- <router-link to="/cheatsheet/control-flow">Kontrollfluss</router-link>
- <router-link to="/cheatsheet/basics">Grundlagen</router-link>
- <router-link to="/builtin">Eingebaute Funktionen</router-link>
