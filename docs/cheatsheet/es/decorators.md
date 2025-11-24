---
title: 'Decoradores de Python - Hoja de Trucos de Python'
description: 'Un decorador de Python es una sintaxis que proporciona una forma concisa y reutilizable de extender una función o una clase.'
labUrl: 'https://labex.io/es/labs/python-python-decorators-633654?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Decoradores de Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Un Decorador de Python proporciona una forma concisa y reutilizable de extender
una función o una clase. Lea el artículo complementario <router-link to="/blog/python-decorators-for-beginners">Python Decorators: Simple Patterns to Level Up Your Code</router-link> para ver ejemplos prácticos y patrones.

## Decorador básico

Un decorador en su forma más simple es una función que toma otra
función como argumento y devuelve una función envolvente (wrapper). El siguiente ejemplo muestra la creación de un decorador y su uso.

```python
# Decorador: una función que toma otra función y devuelve un envoltorio
def your_decorator(func):
  def wrapper():
    # Hacer cosas antes de func...
    print("Before func!")
    func()  # Llama a la función original
    # Hacer cosas después de func...
    print("After func!")
  return wrapper  # Devuelve la función envolvente

# @your_decorator es azúcar sintáctico para: foo = your_decorator(foo)
@your_decorator
def foo():
  print("Hello World!")

foo()  # Llama a wrapper, que llama a foo con comportamiento extra
```

```output
Before func!
Hello World!
After func!
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
¿Qué es un decorador en Python?
</template>

<base-quiz-option value="A" correct>A. Una función que toma otra función y devuelve una función envolvente</base-quiz-option>
<base-quiz-option value="B">B. Un tipo especial de clase</base-quiz-option>
<base-quiz-option value="C">C. Una palabra clave incorporada de Python</base-quiz-option>
<base-quiz-option value="D">D. Una forma de eliminar funciones</base-quiz-option>
<base-quiz-answer value="A">Un decorador es una función que toma otra función como argumento y devuelve una función envolvente. La sintaxis <code>@</code> es azúcar sintáctico que aplica el decorador a una función.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Decorador para una función con parámetros

```python
# Decorador que funciona con funciones que tienen parámetros
def your_decorator(func):
  def wrapper(*args,**kwargs):  # Acepta cualquier argumento
    # Hacer cosas antes de func...
    print("Before func!")
    func(*args,**kwargs)  # Pasa argumentos a la función original
    # Hacer cosas después de func...
    print("After func!")
  return wrapper

@your_decorator
def foo(bar):
  print("My name is " + bar)

foo("Jack")  # Los argumentos se pasan a través del envoltorio
```

```output
Before func!
My name is Jack
After func!
```

## Plantilla para un decorador básico

Esta plantilla es útil para la mayoría de los casos de uso de decoradores. Es válida para funciones
con o sin parámetros, y con o sin valor de retorno.

```python
import functools

# Plantilla de decorador de mejores prácticas: preserva los metadatos y el valor de retorno de la función
def your_decorator(func):
  @functools.wraps(func)  # Preserva el nombre de la función, la cadena de documentación, etc.
  def wrapper(*args,**kwargs):
    # Hacer cosas antes de func...
    result = func(*args,**kwargs)  # Llama a la función y captura el valor de retorno
    # Hacer cosas después de func..
    return result  # Devuelve el valor de retorno de la función original
  return wrapper
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
¿Qué hace <code>@functools.wraps(func)</code> en un decorador?
</template>

<base-quiz-option value="A">A. Hace que el decorador se ejecute más rápido</base-quiz-option>
<base-quiz-option value="B" correct>B. Preserva los metadatos de la función original (nombre, cadena de documentación, etc.)</base-quiz-option>
<base-quiz-option value="C">C. Evita que se llame a la función</base-quiz-option>
<base-quiz-option value="D">D. Convierte la función en una clase</base-quiz-option>
<base-quiz-answer value="B">El decorador <code>@functools.wraps(func)</code> preserva los metadatos de la función original (como su nombre y cadena de documentación) en la función envolvente. Esto se considera una mejor práctica al escribir decoradores.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Decorador con parámetros

También puedes definir parámetros para que los use el decorador.

```python
import functools

# Fábrica de decoradores: devuelve un decorador basado en parámetros
def your_decorator(arg):
  def decorator(func):
    @functools.wraps(func)  # Preservar metadatos de la función
    def wrapper(*args,**kwargs):
      # Hacer cosas antes de func posiblemente usando arg...
      result = func(*args,**kwargs)
      # Hacer cosas después de func posiblemente usando arg...
      return result
    return wrapper
  return decorator  # Devuelve la función decoradora real
```

Para usar este decorador:

```python
# Uso del decorador con parámetros: @your_decorator(arg='x') llama a your_decorator('x')
# que devuelve un decorador que luego se aplica a foo
@your_decorator(arg = 'x')
def foo(bar):
  return bar
```

## Decoradores basados en clases

Para decorar un método de clase, debes definir el decorador dentro de la clase. Cuando
solo se pasa el argumento implícito `self` al método, sin argumentos adicionales explícitos, debes crear un decorador separado solo para esos métodos sin argumentos adicionales. Un ejemplo de esto, que se muestra a continuación, es cuando deseas capturar e imprimir excepciones de cierta manera.

```python
# Decorador de método de clase: definido dentro de la clase
class DecorateMyMethod:

  # Decorador de método estático para métodos con solo el parámetro 'self'
  def decorator_for_class_method_with_no_args(method):
    def wrapper_for_class_method(self):  # Solo toma self
      try:
        return method(self)  # Llama al método original
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

Un decorador también puede definirse como una clase en lugar de un método. Esto es útil
para mantener y actualizar un estado, como en el siguiente ejemplo, donde contamos el número de veces que se llama a un método:

```python
# Decorador basado en clases: mantiene el estado entre llamadas
class CountCallNumber:

  def __init__(self, func):
    self.func = func  # Almacena la función a decorar
    self.call_number = 0  # Inicializa el contador de llamadas

  def __call__(self, *args, **kwargs):  # Hace que la instancia sea invocable
    self.call_number += 1  # Incrementa el contador
    print("This is execution number " + str(self.call_number))
    return self.func(*args, **kwargs)  # Llama a la función original

@CountCallNumber  # Crea una instancia de CountCallNumber
def say_hi(name):
  print("Hi! My name is " + name)

say_hi("Jack")  # Llama a CountCallNumber.__call__()
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
    Ejemplo de Conteo
  </base-disclaimer-title>
  <base-disclaimer-content>
  Este ejemplo de conteo está inspirado en el <a href="https://youtu.be/HGOBQPFzWKo?si=IUvFzeQbzTmeEgKV" target="_blank">tutorial de YouTube</a> de Patrick Loeber.
  </base-disclaimer-content>
</base-disclaimer>

## Enlaces relevantes

- <router-link to="/blog/python-decorators-for-beginners">Python Decorators: Simple Patterns to Level Up Your Code</router-link>
- <router-link to="/blog/python-easy-args-kwargs">Python \*args and \*\*kwargs Made Easy</router-link>
- <router-link to="/cheatsheet/functions">Funciones</router-link>
- <router-link to="/cheatsheet/args-and-kwargs">Args y Kwargs</router-link>
- <router-link to="/builtin/classmethod">classmethod()</router-link>
- <router-link to="/builtin/staticmethod">staticmethod()</router-link>
- <router-link to="/builtin/property">property()</router-link>
- <router-link to="/builtin/callable">callable()</router-link>
