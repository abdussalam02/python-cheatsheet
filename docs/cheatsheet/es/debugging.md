---
title: 'Depuración de Python - Hoja de Trucos de Python'
description: 'En programación informática y desarrollo de software, la depuración es el proceso de encontrar y resolver errores (defectos o problemas que impiden el funcionamiento correcto) dentro de programas informáticos, software o sistemas.'
labUrl: 'https://labex.io/es/labs/python-python-debugging-633653?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Depuración de Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikipedia.org/wiki/Debugging">Encontrar y resolver errores</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    En la programación informática y el desarrollo de software, la depuración es el proceso de encontrar y resolver errores (defectos o problemas que impiden el funcionamiento correcto) dentro de programas informáticos, software o sistemas.
  </base-disclaimer-content>
</base-disclaimer>

## Lanzar Excepciones

Las excepciones se lanzan con una sentencia `raise`. En el código, una sentencia `raise` consta de lo siguiente:

- La palabra clave `raise`
- Una llamada a la función `Exception()`
- Una cadena con un mensaje de error útil pasada a la función `Exception()`

```python
# sentencia raise: lanzar manualmente una excepción con un mensaje personalizado
raise Exception('Este es el mensaje de error.')
```

```output
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    raise Exception('This is the error message.')
Exception: This is the error message.
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-debugging-1">
<template #question>
¿Qué palabra clave se utiliza para lanzar manualmente una excepción en Python?
</template>

<base-quiz-option value="A">A. <code>throw</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>raise</code></base-quiz-option>
<base-quiz-option value="C">C. <code>error</code></base-quiz-option>
<base-quiz-option value="D">D. <code>exception</code></base-quiz-option>
<base-quiz-answer value="B">La palabra clave <code>raise</code> se utiliza para lanzar manualmente una excepción en Python. Puedes lanzar excepciones integradas o excepciones personalizadas.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Normalmente, es el código que llama a la función, no la función en sí, el que sabe cómo manejar una excepción. Por lo tanto, es común ver una sentencia `raise` dentro de una función y las sentencias `try` y `except` en el código que llama a la función.

```python
# Lanzar excepciones en la función, manejarlas en el código que llama
def box_print(symbol, width, height):
    if len(symbol) != 1:
      raise Exception('El símbolo debe ser una cadena de un solo carácter.')
    if width <= 2:
      raise Exception('El ancho debe ser mayor que 2.')
    if height <= 2:
      raise Exception('La altura debe ser mayor que 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

# Manejar excepciones al llamar a la función
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:  # Capturar excepción e imprimir mensaje de error
        print('Ocurrió una excepción: ' + str(err))
```

```output
****
*  *
*  *
****
OOOOOOOOOOOOOOOOOOOO
O                  O
O                  O
O                  O
OOOOOOOOOOOOOOOOOOOO
Ocurrió una excepción: El ancho debe ser mayor que 2.
Ocurrió una excepción: El símbolo debe ser una cadena de un solo carácter.
```

Lee más sobre [Manejo de Excepciones](/cheatsheet/exception-handling).

## Obtener el Traceback como una cadena

El `traceback` (traza de la pila) se muestra en Python siempre que una excepción lanzada no se maneja. Pero también se puede obtener como una cadena llamando a `traceback.format_exc()`. Esta función es útil si deseas la información del traceback de una excepción, pero también quieres que una sentencia `except` maneje la excepción con elegancia. Deberás importar el módulo `traceback` de Python antes de llamar a esta función.

```python
# traceback.format_exc(): obtener el traceback como cadena para registro/depuración
import traceback

try:
    raise Exception('Este es el mensaje de error.')
except:
    with open('errorInfo.txt', 'w') as error_file:
        error_file.write(traceback.format_exc())  # Escribir traceback en el archivo
    print('La información del traceback se escribió en errorInfo.txt.')
```

```output
116
La información del traceback se escribió en errorInfo.txt.
```

El 116 es el valor de retorno del método `write()`, ya que se escribieron 116 caracteres en el archivo. El texto del `traceback` se escribió en errorInfo.txt.

    Traceback (most recent call last):
      File "<pyshell#28>", line 2, in <module>
    Exception: This is the error message.

## Afirmaciones (Assertions)

Una afirmación es una comprobación de cordura para asegurarse de que su código no está haciendo algo obviamente incorrecto. Estas comprobaciones de cordura se realizan mediante sentencias `assert`. Si la comprobación de cordura falla, se lanza una excepción `AssertionError`. En el código, una sentencia `assert` consta de lo siguiente:

- La palabra clave `assert`
- Una condición (es decir, una expresión que se evalúa como `True` o `False`)
- Una coma
- Una `string` para mostrar cuando la condición es `False`

```python
# sentencia assert: verificar condición, lanzar AssertionError si es Falsa
pod_bay_door_status = 'open'
assert pod_bay_door_status == 'open', 'Las puertas de la bahía de cápsulas deben estar "open".'  # Pasa

pod_bay_door_status = "Lo siento, Dave. Me temo que no puedo hacer eso."
assert pod_bay_door_status == 'open', 'Las puertas de la bahía de cápsulas deben estar "open".'  # Lanza AssertionError
```

```output
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'
AssertionError: The pod bay doors need to be "open".
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-debugging-2">
<template #question>
¿Qué sucede cuando falla una sentencia <code>assert</code>?
</template>

<base-quiz-option value="A">A. El programa sigue ejecutándose</base-quiz-option>
<base-quiz-option value="B">B. Se imprime una advertencia</base-quiz-option>
<base-quiz-option value="C" correct>C. Se lanza una <code>AssertionError</code> y el programa debería fallar</base-quiz-option>
<base-quiz-option value="D">D. La condición se corrige automáticamente</base-quiz-option>
<base-quiz-answer value="C">Cuando falla una sentencia <code>assert</code>, lanza una <code>AssertionError</code>. A diferencia de las excepciones, las sentencias assert no deben capturarse con try-except; si una afirmación falla, su programa debería fallar para ayudarle a encontrar errores rápidamente.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

En lenguaje sencillo, una sentencia `assert` dice: "Afirmo que esta condición es verdadera, y si no lo es, hay un error en algún lugar del programa". A diferencia de las excepciones, su código no debe manejar las sentencias `assert` con `try` y `except`; si una afirmación falla, su programa debe fallar. Al fallar rápidamente de esta manera, acorta el tiempo entre la causa original del error y la primera vez que nota el error. Esto reducirá la cantidad de código que tendrá que revisar antes de encontrar el código que está causando el error.

### Deshabilitar Afirmaciones

Las afirmaciones se pueden deshabilitar pasando la opción `-O` al ejecutar Python.

## Registro (Logging)

Para habilitar el módulo `logging` para mostrar mensajes de registro en su pantalla mientras se ejecuta su programa, copie lo siguiente al principio de su programa:

```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-debugging-3">
<template #question>
¿Cuál es el propósito del módulo <code>logging</code> en Python?
</template>

<base-quiz-option value="A" correct>A. Registrar información sobre la ejecución del programa para depuración y monitoreo</base-quiz-option>
<base-quiz-option value="B">B. Prevenir que ocurran errores</base-quiz-option>
<base-quiz-option value="C">C. Acelerar la ejecución del programa</base-quiz-option>
<base-quiz-option value="D">D. Cifrar los mensajes de registro</base-quiz-option>
<base-quiz-answer value="A">El módulo <code>logging</code> le permite registrar información sobre la ejecución de su programa en diferentes niveles (DEBUG, INFO, WARNING, ERROR, CRITICAL), lo cual es útil para la depuración y el monitoreo.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Supongamos que escribió una función para calcular el factorial de un número. En matemáticas, el factorial de 4 es 1 × 2 × 3 × 4, o 24. El factorial de 7 es 1 × 2 × 3 × 4 × 5 × 6 × 7, o 5,040. Abra una nueva ventana del editor de archivos e ingrese el siguiente código. Tiene un error, pero también ingresará varias sentencias de registro para ayudarse a descubrir qué está saliendo mal. Guarde el programa como factorialLog.py.

```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Inicio del programa')

def factorial(n):
    logging.debug('Inicio de factorial(%s)' % (n))
    total = 1
    for i in range(0, n + 1):
        total *= i
        logging.debug('i es ' + str(i) + ', total es ' + str(total))
    logging.debug('Fin de factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('Fin del programa')
```

```output
2015-05-23 16:20:12,664 - DEBUG - Start of program
2015-05-23 16:20:12,664 - DEBUG - Start of factorial(5)
2015-05-23 16:20:12,665 - DEBUG - i is 0, total is 0
2015-05-23 16:20:12,668 - DEBUG - i is 1, total is 0
2015-05-23 16:20:12,670 - DEBUG - i is 2, total is 0
2015-05-23 16:20:12,673 - DEBUG - i is 3, total is 0
2015-05-23 16:20:12,675 - DEBUG - i is 4, total is 0
2015-05-23 16:20:12,678 - DEBUG - i is 5, total is 0
2015-05-23 16:20:12,680 - DEBUG - End of factorial(5)
0
2015-05-23 16:20:12,684 - DEBUG - End of program
```

## Niveles de Registro

Los niveles de registro proporcionan una forma de categorizar sus mensajes de registro por importancia. Hay cinco niveles de registro, descritos en la Tabla 10-1 de menor a mayor importancia. Los mensajes se pueden registrar en cada nivel utilizando una función de registro diferente.

| Nivel      | Función de Registro  | Descripción                                                                                                                                        |
| ---------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DEBUG`    | `logging.debug()`    | El nivel más bajo. Se utiliza para pequeños detalles. Normalmente, solo le interesan estos mensajes al diagnosticar problemas.                     |
| `INFO`     | `logging.info()`     | Se utiliza para registrar información sobre eventos generales en su programa o confirmar que las cosas funcionan en su punto del programa.         |
| `WARNING`  | `logging.warning()`  | Se utiliza para indicar un problema potencial que no impide que el programa funcione, pero podría hacerlo en el futuro.                            |
| `ERROR`    | `logging.error()`    | Se utiliza para registrar un error que hizo que el programa no pudiera hacer algo.                                                                 |
| `CRITICAL` | `logging.critical()` | El nivel más alto. Se utiliza para indicar un error fatal que ha causado o está a punto de causar que el programa deje de ejecutarse por completo. |

<base-quiz>
<base-quiz-question correct="D" id="cheatsheet-debugging-4">
<template #question>
¿Cuál es el nivel de registro más bajo en Python?
</template>

<base-quiz-option value="A">A. <code>INFO</code></base-quiz-option>
<base-quiz-option value="B">B. <code>WARNING</code></base-quiz-option>
<base-quiz-option value="C">C. <code>ERROR</code></base-quiz-option>
<base-quiz-option value="D" correct>D. <code>DEBUG</code></base-quiz-option>
<base-quiz-answer value="D">Los niveles de registro de menor a mayor son: <code>DEBUG</code>, <code>INFO</code>, <code>WARNING</code>, <code>ERROR</code>, <code>CRITICAL</code>. <code>DEBUG</code> es el nivel más bajo, utilizado para información de diagnóstico detallada.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Deshabilitar el Registro

Después de depurar su programa, probablemente no querrá que todos estos mensajes de registro saturen la pantalla. La función `logging.disable()` los deshabilita para que no tenga que entrar en su programa y eliminar todas las llamadas de registro manualmente.

```python
import logging

logging.basicConfig(level=logging.INFO, format=' %(asctime)s -%(levelname)s - %(message)s')
logging.critical('¡Error crítico! ¡Error crítico!')
```

```output
2015-05-22 11:10:48,054 - CRITICAL - Critical error! Critical error!
```

```python
logging.disable(logging.CRITICAL)
logging.critical('¡Error crítico! ¡Error crítico!')
logging.error('¡Error! ¡Error!')
```

## Registro en un Archivo

En lugar de mostrar los mensajes de registro en la pantalla, puede escribirlos en un archivo de texto. La función `logging.basicConfig()` acepta un argumento de palabra clave `filename`, así:

```python
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-debugging-5">
<template #question>
¿Cómo se escriben los mensajes de registro en un archivo en lugar de mostrarlos en pantalla?
</template>

<base-quiz-option value="A">A. Usando <code>logging.file()</code></base-quiz-option>
<base-quiz-option value="B" correct>B. Pasando el parámetro <code>filename</code> a <code>logging.basicConfig()</code></base-quiz-option>
<base-quiz-option value="C">C. Usando <code>logging.write()</code></base-quiz-option>
<base-quiz-option value="D">D. Los registros siempre se escriben en archivos automáticamente</base-quiz-option>
<base-quiz-answer value="B">Para escribir mensajes de registro en un archivo, pase el parámetro <code>filename</code> a <code>logging.basicConfig()</code>. Esto escribirá todos los mensajes de registro en el archivo especificado en lugar de mostrarlos en pantalla.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Enlaces relevantes

- <router-link to="/cheatsheet/exception-handling">Manejo de Excepciones</router-link>
- <router-link to="/builtin/breakpoint">breakpoint()</router-link>
