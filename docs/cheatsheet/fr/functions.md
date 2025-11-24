---
title: 'Fonctions Python - Aide-mémoire Python'
description: 'En Python, une fonction est un bloc de code organisé utilisé pour effectuer une tâche unique.'
labUrl: 'https://labex.io/fr/labs/python-python-functions-633658?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Fonctions Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikiversity.org/wiki/Programming_Fundamentals/Functions">Programming Functions</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Une fonction est un bloc de code organisé utilisé pour effectuer une seule tâche. Elles offrent une meilleure modularité pour votre application et une réutilisabilité.
  </base-disclaimer-content>
</base-disclaimer>

## Arguments de Fonction

Une fonction peut prendre des `arguments` et `retourner des valeurs` :

Dans l'exemple suivant, la fonction **say_hello** reçoit l'argument "name" et affiche une salutation :

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

## Arguments Nommés (Keyword Arguments)

Pour améliorer la lisibilité du code, nous devons être aussi explicites que possible. Nous pouvons y parvenir dans nos fonctions en utilisant des `Keyword Arguments` :

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

## Valeurs de Retour (Return Values)

Lors de la création d'une fonction à l'aide de l'instruction `def`, vous pouvez spécifier quelle doit être la valeur de retour avec une instruction `return`. Une instruction de retour se compose de ce qui suit :

- Le mot-clé `return`.

- La valeur ou l'expression que la fonction doit retourner.

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

## Portée Locale et Globale (Local and Global Scope)

- Le code dans la portée globale ne peut utiliser aucune variable locale.

- Cependant, une portée locale peut accéder aux variables globales.

- Le code dans la portée locale d'une fonction ne peut pas utiliser de variables dans toute autre portée locale.

- Vous pouvez utiliser le même nom pour différentes variables si elles se trouvent dans des portées différentes. C'est-à-dire qu'il peut y avoir une variable locale nommée spam et une variable globale également nommée spam.

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

## L'instruction global

Si vous devez modifier une variable globale depuis l'intérieur d'une fonction, utilisez l'instruction global :

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

Il y a quatre règles pour déterminer si une variable est dans une portée locale ou globale :

1. Si une variable est utilisée dans la portée globale (c'est-à-dire en dehors de toutes les fonctions), alors c'est toujours une variable globale.

1. S'il existe une instruction global pour cette variable dans une fonction, c'est une variable globale.

1. Sinon, si la variable est utilisée dans une instruction d'affectation dans la fonction, c'est une variable locale.

1. Mais si la variable n'est pas utilisée dans une instruction d'affectation, c'est une variable globale.

## Fonctions Lambda

En Python, une fonction lambda est une fonction anonyme sur une seule ligne, qui peut avoir n'importe quel nombre d'arguments, mais ne peut avoir qu'une seule expression.

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

Cette fonction :

```python
# Regular function definition
def add(x, y):
    return x + y

add(5, 3)
```

```output
8
```

Est équivalente à la fonction _lambda_ :

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

Comme les fonctions imbriquées régulières, les lambdas fonctionnent également comme des fermetures lexicales (lexical closures) :

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

## Liens pertinents

- <router-link to="/blog/python-easy-args-kwargs">\*args and \*\*kwargs explained</router-link>
- <router-link to="/cheatsheet/args-and-kwargs">Args and Kwargs</router-link>
- <router-link to="/cheatsheet/decorators">Decorators</router-link>
- <router-link to="/cheatsheet/control-flow">Control Flow</router-link>
- <router-link to="/cheatsheet/basics">Basics</router-link>
- <router-link to="/builtin">Built-in Functions</router-link>
