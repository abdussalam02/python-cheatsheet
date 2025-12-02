---
title: 'Manejo de Excepciones en Python - Hoja de Trucos'
description: 'En Python, el manejo de excepciones es el proceso de responder a la ocurrencia de excepciones.'
labUrl: 'https://labex.io/es/labs/python-python-exception-handling-633656?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Manejo de Excepciones en Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikipedia.org/wiki/Exception_handling">Manejo de excepciones</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    En la computación y la programación de computadoras, el manejo de excepciones es el proceso de responder a la ocurrencia de excepciones, condiciones anómalas o excepcionales que requieren un procesamiento especial.
  </base-disclaimer-content>
</base-disclaimer>

Python tiene muchas [excepciones incorporadas](https://docs.python.org/3/library/exceptions.html) que se generan cuando un programa encuentra un error, y la mayoría de las bibliotecas externas, como la popular [Requests](https://requests.readthedocs.io/en/latest), incluyen sus propias [excepciones personalizadas](https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions) con las que tendremos que lidiar.

## Manejo básico de excepciones

No se puede dividir por cero, eso es una verdad matemática, y si intentas hacerlo en Python, el intérprete generará la excepción incorporada [ZeroDivisionError](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError):

```python
def divide(dividend , divisor):
    print(dividend / divisor)

divide(dividend=10, divisor=5)
```

```output
2
```

```python
divide(dividend=10, divisor=0)
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

Supongamos que no queremos que nuestro programa detenga su ejecución o muestre al usuario una salida que no entenderá. Digamos que queremos imprimir un mensaje útil y claro, entonces necesitamos **_manejar_** la excepción con las palabras clave `try` y `except`:

```python
# try-except: manejar excepciones con elegancia
def divide(dividend , divisor):
    try:  # Intenta ejecutar este código
        print(dividend / divisor)
    except ZeroDivisionError:  # Captura el tipo de excepción específico
        print('No se puede dividir por 0')

divide(dividend=10, divisor=5)
```

```output
2
```

```python
divide(dividend=10, divisor=0)
```

```output
No se puede dividir por 0
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-exception-handling-1">
<template #question>
¿Qué palabras clave se utilizan para manejar excepciones en Python?
</template>

<base-quiz-option value="A" correct>A. <code>try</code> y <code>except</code></base-quiz-option>
<base-quiz-option value="B">B. <code>catch</code> y <code>handle</code></base-quiz-option>
<base-quiz-option value="C">C. <code>error</code> y <code>rescue</code></base-quiz-option>
<base-quiz-option value="D">D. <code>if</code> y <code>else</code></base-quiz-option>
<base-quiz-answer value="A">Python usa <code>try</code> para marcar el código que podría generar una excepción, y <code>except</code> para manejar las excepciones específicas que ocurren.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Manejo de Múltiples excepciones usando un bloque de excepción

También puedes manejar múltiples excepciones en una sola línea como la siguiente sin la necesidad de crear múltiples bloques de excepción.

```python
# Manejar múltiples excepciones en un bloque except
def divide(dividend , divisor):
    try:
        if (dividend == 10):
          var = 'str' + 1  # Esto generará TypeError
        else:
          print(dividend / divisor)
    except (ZeroDivisionError, TypeError) as error:  # Capturar múltiples tipos de excepción
        print(error)  # Imprimir el mensaje de error

divide(dividend=20, divisor=5)
```

```output
4
```

```python
divide(dividend=10, divisor=5)
```

```output
can only concatenate str (not "int") to str
```

```python
divide(dividend=10, divisor=0)
```

```output
division by zero
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-exception-handling-2">
<template #question>
¿Se pueden manejar múltiples tipos de excepción en un solo bloque <code>except</code>?
</template>

<base-quiz-option value="A">A. No, debes usar bloques <code>except</code> separados para cada tipo de excepción</base-quiz-option>
<base-quiz-option value="B" correct>B. Sí, poniéndolos en una tupla como <code>except (Exception1, Exception2)</code></base-quiz-option>
<base-quiz-option value="C">C. Sí, pero solo si están relacionados</base-quiz-option>
<base-quiz-option value="D">D. No, Python no soporta esto</base-quiz-option>
<base-quiz-answer value="B">Puedes manejar múltiples tipos de excepción en un solo bloque <code>except</code> poniéndolos en una tupla: <code>except (ZeroDivisionError, TypeError) as error:</code></base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Código Finally en el manejo de excepciones

El código dentro de la sección `finally` siempre se ejecuta, sin importar si se ha generado una excepción o no:

```python
# Bloque finally: siempre se ejecuta independientemente de las excepciones
def divide(dividend , divisor):
    try:
        print(dividend / divisor)
    except ZeroDivisionError:
        print('No se puede dividir por 0')
    finally:  # Siempre se ejecuta, incluso si ocurre una excepción
        print('Ejecución finalizada')

divide(dividend=10, divisor=5)
```

```output
2.0
Ejecución finalizada
```

```python
divide(dividend=10, divisor=0)
```

```output
No se puede dividir por 0
Ejecución finalizada
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-exception-handling-3">
<template #question>
¿Cuándo se ejecuta el bloque <code>finally</code>?
</template>

<base-quiz-option value="A">A. Solo cuando ocurre una excepción</base-quiz-option>
<base-quiz-option value="B">B. Solo cuando no ocurre ninguna excepción</base-quiz-option>
<base-quiz-option value="C" correct>C. Siempre, independientemente de si ocurrió o no una excepción</base-quiz-option>
<base-quiz-option value="D">D. Nunca</base-quiz-option>
<base-quiz-answer value="C">El bloque <code>finally</code> siempre se ejecuta, haya ocurrido o no una excepción. Es útil para código de limpieza que debe ejecutarse independientemente del resultado.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Excepciones Personalizadas

Las excepciones personalizadas se inicializan creando una `class` que hereda de la clase base `Exception` de Python, y se generan usando la palabra clave `raise`:

```python
# Excepción personalizada: se crea heredando de la clase Exception
class MyCustomException(Exception):
    pass

raise MyCustomException  # Generar la excepción personalizada
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyCustomException
```

Para declarar un mensaje de excepción personalizado, puedes pasarlo como parámetro:

```python
class MyCustomException(Exception):
    pass

raise MyCustomException('Un mensaje personalizado para mi excepción personalizada')
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyCustomException: Un mensaje personalizado para mi excepción personalizada
```

Manejar una excepción personalizada es igual que cualquier otra:

```python
try:
    raise MyCustomException('Un mensaje personalizado para mi excepción personalizada')
except MyCustomException:
    print('Se generó mi excepción personalizada')
```

```output
Se generó mi excepción personalizada
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-exception-handling-4">
<template #question>
¿Cómo se crea una excepción personalizada en Python?
</template>

<base-quiz-option value="A" correct>A. Creando una clase que herede de la clase <code>Exception</code></base-quiz-option>
<base-quiz-option value="B">B. Usando el decorador <code>@exception</code></base-quiz-option>
<base-quiz-option value="C">C. Llamando a <code>Exception.create()</code></base-quiz-option>
<base-quiz-option value="D">D. Importándola de un módulo especial</base-quiz-option>
<base-quiz-answer value="A">Las excepciones personalizadas se crean definiendo una clase que hereda de la clase base <code>Exception</code>. Luego puedes generarlas y manejarlas igual que las excepciones incorporadas.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Enlaces relevantes

- <router-link to="/cheatsheet/control-flow">Flujo de Control</router-link>
- <router-link to="/builtin/breakpoint">breakpoint()</router-link>
- <router-link to="/builtin/isinstance">isinstance()</router-link>
- <router-link to="/builtin/issubclass">issubclass()</router-link>
