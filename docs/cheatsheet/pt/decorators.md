---
title: 'Decoradores Python - Folha de Dicas Python'
description: 'Um Decorador Python é uma sintaxe que fornece uma maneira concisa e reutilizável de estender uma função ou classe.'
labUrl: 'https://labex.io/pt/labs/python-python-decorators-633654?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Decoradores Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Um Decorador Python fornece uma maneira concisa e reutilizável de estender
uma função ou uma classe. Leia o artigo complementar <router-link to="/blog/python-decorators-for-beginners">Python Decorators: Simple Patterns to Level Up Your Code</router-link> para exemplos práticos e padrões.

## Decorador básico

Um decorador em sua forma mais simples é uma função que recebe outra
função como argumento e retorna um _wrapper_ (invólucro). O exemplo a seguir
mostra a criação de um decorador e seu uso.

```python
# Decorator: a function that takes another function and returns a wrapper
def your_decorator(func):
  def wrapper():
    # Do stuff before func...
    print("Before func!")
    func()  # Call the original function
    # Do stuff after func...
    print("After func!")
  return wrapper  # Return the wrapper function

# @your_decorator is syntactic sugar for: foo = your_decorator(foo)
@your_decorator
def foo():
  print("Hello World!")

foo()  # Calls wrapper, which calls foo with extra behavior
```

```output
Before func!
Hello World!
After func!
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
What is a decorator in Python?
</template>

<base-quiz-option value="A" correct>A. A function that takes another function and returns a wrapper function</base-quiz-option>
<base-quiz-option value="B">B. A special type of class</base-quiz-option>
<base-quiz-option value="C">C. A built-in Python keyword</base-quiz-option>
<base-quiz-option value="D">D. A way to delete functions</base-quiz-option>
<base-quiz-answer value="A">A decorator is a function that takes another function as an argument and returns a wrapper function. The <code>@</code> syntax is syntactic sugar that applies the decorator to a function.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Decorador para uma função com parâmetros

```python
# Decorator that works with functions that have parameters
def your_decorator(func):
  def wrapper(*args,**kwargs):  # Accept any arguments
    # Do stuff before func...
    print("Before func!")
    func(*args,**kwargs)  # Pass arguments to original function
    # Do stuff after func...
    print("After func!")
  return wrapper

@your_decorator
def foo(bar):
  print("My name is " + bar)

foo("Jack")  # Arguments are passed through wrapper
```

```output
Before func!
My name is Jack
After func!
```

## Template para um decorador básico

Este template é útil para a maioria dos casos de uso de decoradores. É válido para funções
com ou sem parâmetros, e com ou sem valor de retorno.

```python
import functools

# Best practice decorator template: preserves function metadata and return value
def your_decorator(func):
  @functools.wraps(func)  # Preserves function name, docstring, etc.
  def wrapper(*args,**kwargs):
    # Do stuff before func...
    result = func(*args,**kwargs)  # Call function and capture return value
    # Do stuff after func..
    return result  # Return the original function's return value
  return wrapper
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
What does <code>@functools.wraps(func)</code> do in a decorator?
</template>

<base-quiz-option value="A">A. Makes the decorator execute faster</base-quiz-option>
<base-quiz-option value="B" correct>B. Preserves the original function's metadata (name, docstring, etc.)</base-quiz-option>
<base-quiz-option value="C">C. Prevents the function from being called</base-quiz-option>
<base-quiz-option value="D">D. Converts the function to a class</base-quiz-option>
<base-quiz-answer value="B">The <code>@functools.wraps(func)</code> decorator preserves the original function's metadata (like its name and docstring) in the wrapper function. This is considered a best practice when writing decorators.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Decorador com parâmetros

Você também pode definir parâmetros para o decorador usar.

```python
import functools

# Decorator factory: returns a decorator based on parameters
def your_decorator(arg):
  def decorator(func):
    @functools.wraps(func)  # Preserve function metadata
    def wrapper(*args,**kwargs):
      # Do stuff before func possibly using arg...
      result = func(*args,**kwargs)
      # Do stuff after func possibly using arg...
      return result
    return wrapper
  return decorator  # Return the actual decorator function
```

Para usar este decorador:

```python
# Using decorator with parameters: @your_decorator(arg='x') calls your_decorator('x')
# which returns a decorator that is then applied to foo
@your_decorator(arg = 'x')
def foo(bar):
  return bar
```

## Decoradores baseados em classes

Para decorar um método de classe, você deve definir o decorador dentro da classe. Quando
apenas o argumento implícito `self` é passado para o método, sem quaisquer argumentos
adicionais explícitos, você deve criar um decorador separado apenas para esses métodos
sem quaisquer argumentos adicionais. Um exemplo disso, mostrado abaixo, é quando você
quer capturar e imprimir exceções de uma certa maneira.

```python
# Class method decorator: defined within the class
class DecorateMyMethod:

  # Static method decorator for methods with only 'self' parameter
  def decorator_for_class_method_with_no_args(method):
    def wrapper_for_class_method(self):  # Only takes self
      try:
        return method(self)  # Call original method
      except Exception as e:
        print("\nWARNING: Please make note of the following:\n")
        print(e)
    return wrapper_for_class_method

  def __init__(self,succeed:bool):
    self.succeed = succeed

  @decorator_for_class_method_with_no_args
  def class_action(self):
    if self.succeed:
      print("You succeeded by choice.")
    else:
      raise Exception("Epic fail of your own creation.")

test_succeed = DecorateMyMethod(True)
test_succeed.class_action()
```

```output
You succeeded by choice.
```

```python
test_fail = DecorateMyMethod(False)
test_fail.class_action()
```

```output
Exception: Epic fail of your own creation.
```

Um decorador também pode ser definido como uma classe em vez de um método. Isso é útil
para manter e atualizar um estado, como no exemplo a seguir, onde contamos o número de
chamadas feitas a um método:

```python
# Class-based decorator: maintains state between calls
class CountCallNumber:

  def __init__(self, func):
    self.func = func  # Store the function to decorate
    self.call_number = 0  # Initialize call counter

  def __call__(self, *args, **kwargs):  # Makes instance callable
    self.call_number += 1  # Increment counter
    print("This is execution number " + str(self.call_number))
    return self.func(*args, **kwargs)  # Call original function

@CountCallNumber  # Creates instance of CountCallNumber
def say_hi(name):
  print("Hi! My name is " + name)

say_hi("Jack")  # Calls CountCallNumber.__call__()
```

```output
This is execution number 1
Hi! My name is Jack
```

```python
say_hi("James")
```

```output
This is execution number 2
Hi! My name is James
```

<base-disclaimer>
  <base-disclaimer-title>
    Count Example
  </base-disclaimer-title>
  <base-disclaimer-content>
  This count example is inspired by Patrick Loeber's <a href="https://youtu.be/HGOBQPFzWKo?si=IUvFzeQbzTmeEgKV" target="_blank">YouTube tutorial</a>.
  </base-disclaimer-content>
</base-disclaimer>

## Relevant links

- <router-link to="/blog/python-decorators-for-beginners">Python Decorators: Simple Patterns to Level Up Your Code</router-link>
- <router-link to="/blog/python-easy-args-kwargs">Python \*args and \*\*kwargs Made Easy</router-link>
- <router-link to="/cheatsheet/functions">Functions</router-link>
- <router-link to="/cheatsheet/args-and-kwargs">Args and Kwargs</router-link>
- <router-link to="/builtin/classmethod">classmethod()</router-link>
- <router-link to="/builtin/staticmethod">staticmethod()</router-link>
- <router-link to="/builtin/property">property()</router-link>
- <router-link to="/builtin/callable">callable()</router-link>
