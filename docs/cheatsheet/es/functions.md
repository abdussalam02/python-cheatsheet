---
title: 'Funciones de Python - Hoja de Trucos de Python'
description: 'En Python, una función es un bloque de código organizado que se utiliza para realizar una única tarea.'
labUrl: 'https://labex.io/es/labs/python-python-functions-633658?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Funciones de Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikiversity.org/wiki/Programming_Fundamentals/Functions">Programación de Funciones</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Una función es un bloque de código organizado que se utiliza para realizar una única tarea. Proporcionan una mejor modularidad para su aplicación y reutilización.
  </base-disclaimer-content>
</base-disclaimer>

## Argumentos de Función

Una función puede recibir `argumentos` y `valores de retorno`:

En el siguiente ejemplo, la función **say_hello** recibe el argumento "name" e imprime un saludo:

```python
# Definir una función que toma un argumento
def say_hello(name):
   print(f'Hello {name}')

# Llamar a la función con un argumento de cadena
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

## Argumentos de Palabra Clave (Keyword Arguments)

Para mejorar la legibilidad del código, debemos ser lo más explícitos posible. Podemos lograr esto en nuestras funciones utilizando `Argumentos de Palabra Clave` (`Keyword Arguments`):

```python
# Función con múltiples parámetros
def say_hi(name, greeting):
   print(f"{greeting} {name}")

# Argumentos posicionales: el orden importa
say_hi('John', 'Hello')
```

```output
Hello John
```

```python
# Argumentos de palabra clave: el orden no importa, más legible
say_hi(name='Anna', greeting='Hi')
```

```output
Hi Anna
```

<BaseQuiz id="cheatsheet-functions-1" correct="C">
<template #question>
What is the main advantage of using keyword arguments in Python functions?
</template>

<BaseQuizOption value="A">A. They execute faster</BaseQuizOption>
<BaseQuizOption value="B">B. They use less memory</BaseQuizOption>
<BaseQuizOption value="C" correct>C. They improve code readability and order doesn't matter</BaseQuizOption>
<BaseQuizOption value="D">D. They prevent errors</BaseQuizOption>
<BaseQuizAnswer>Los argumentos de palabra clave mejoran la legibilidad del código al dejar claro a qué representa cada argumento, y permiten pasar argumentos en cualquier orden.</BaseQuizAnswer>
</BaseQuiz>

## Valores de Retorno

Al crear una función usando la declaración `def`, puede especificar cuál debe ser el valor de retorno con una declaración `return`. Una declaración de retorno consta de lo siguiente:

- La palabra clave `return`.

- El valor o expresión que la función debe devolver.

```python
# Función que devuelve un valor usando la declaración return
def sum_two_numbers(number_1, number_2):
   return number_1 + number_2

# Llamar a la función y almacenar el valor devuelto
result = sum_two_numbers(7, 8)
print(result)
```

```output
15
```

<BaseQuiz id="cheatsheet-functions-2" correct="A">
<template #question>
What keyword is used to return a value from a function in Python?
</template>

<BaseQuizOption value="A" correct>A. <code>return</code></BaseQuizOption>
<BaseQuizOption value="B">B. <code>output</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>yield</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>exit</code></BaseQuizOption>
<BaseQuizAnswer>La palabra clave <code>return</code> se utiliza para devolver un valor desde una función. Si no se utiliza ninguna declaración de retorno, la función devuelve <code>None</code>.</BaseQuizAnswer>
</BaseQuiz>

## Alcance Local y Global (Local and Global Scope)

- El código en el alcance global no puede usar ninguna variable local.

- Sin embargo, un alcance local puede acceder a variables globales.

- El código en el alcance local de una función no puede usar variables en ningún otro alcance local.

- Puede usar el mismo nombre para diferentes variables si están en diferentes alcances. Es decir, puede haber una variable local llamada spam y una variable global también llamada spam.

```python
# Variable global: accesible en todas partes
global_variable = 'I am available everywhere'

def some_function():
    print(global_variable)  # Puede acceder a la variable global
    # Variable local: solo existe dentro de esta función
    local_variable = "only available within this function"
    print(local_variable)

# Esto generará NameError: local_variable no existe en el alcance global
print(local_variable)
```

```output
Traceback (most recent call last):
  File "<stdin>", line 10, in <module>
NameError: name 'local_variable' is not defined
```

## La Declaración global

Si necesita modificar una variable global desde dentro de una función, use la declaración global:

```python
# Usar la palabra clave 'global' para modificar la variable global desde dentro de la función
def spam():
    global eggs  # Declarar que estamos modificando la variable global
    eggs = 'spam'  # Esto cambia la variable global

eggs = 'global'
spam()  # La función modifica la variable global
print(eggs)  # Imprime 'spam', no 'global'
```

```output
spam
```

<BaseQuiz id="cheatsheet-functions-3" correct="B">
<template #question>
What keyword must you use inside a function to modify a global variable?
</template>

<BaseQuizOption value="A">A. <code>nonlocal</code></BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>global</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>extern</code></BaseQuizOption>
<BaseQuizOption value="D">D. No keyword needed</BaseQuizOption>
<BaseQuizAnswer>La palabra clave <code>global</code> debe usarse dentro de una función para modificar una variable global. Sin ella, Python creará una variable local en su lugar.</BaseQuizAnswer>
</BaseQuiz>

Hay cuatro reglas para saber si una variable está en un alcance local o global:

1. Si una variable se utiliza en el alcance global (es decir, fuera de todas las funciones), siempre es una variable global.

1. Si hay una declaración global para esa variable en una función, es una variable global.

1. De lo contrario, si la variable se utiliza en una declaración de asignación en la función, es una variable local.

1. Pero si la variable no se utiliza en una declaración de asignación, es una variable global.

## Funciones Lambda

En Python, una función lambda es una función anónima de una sola línea, que puede tener cualquier número de argumentos, pero solo puede tener una expresión.

<base-disclaimer>
  <base-disclaimer-title>
    Del <a target="_blank" href="https://docs.python.org/3/library/ast.html?highlight=lambda#function-and-class-definitions">Tutorial de Python 3</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    lambda es una definición de función mínima que se puede utilizar dentro de una expresión. A diferencia de FunctionDef, el cuerpo contiene un único nodo.
  </base-disclaimer-content>
</base-disclaimer>

<base-warning>
  <base-warning-title>
    Expresión de una sola línea
  </base-warning-title>
  <base-warning-content>
    Las funciones Lambda solo pueden evaluar una expresión, como una sola línea de código.
  </base-warning-content>
</base-warning>

Esta función:

```python
# Definición de función regular
def add(x, y):
    return x + y

add(5, 3)
```

```output
8
```

Es equivalente a la función _lambda_:

```python
# Función Lambda: función anónima definida en una línea
# Sintaxis: lambda argumentos: expresión
add = lambda x, y: x + y
add(5, 3)
```

```output
8
```

<BaseQuiz id="cheatsheet-functions-4" correct="D">
<template #question>
What is a lambda function in Python?
</template>

<BaseQuizOption value="A">A. A function that can only be called once</BaseQuizOption>
<BaseQuizOption value="B">B. A function that takes no arguments</BaseQuizOption>
<BaseQuizOption value="C">C. A function that returns multiple values</BaseQuizOption>
<BaseQuizOption value="D" correct>D. A single-line anonymous function that can have any number of arguments but only one expression</BaseQuizOption>
<BaseQuizAnswer>Una función lambda es una función anónima de una sola línea definida usando la palabra clave <code>lambda</code>. Puede tomar cualquier número de argumentos pero solo puede contener una única expresión.</BaseQuizAnswer>
</BaseQuiz>

Al igual que las funciones anidadas regulares, las lambdas también funcionan como cierres léxicos:

```python
# Cierre Lambda: función lambda que captura variables del ámbito exterior
def make_adder(n):
    return lambda x: x + n  # Lambda captura 'n' de la función externa

# Crear funciones que suman diferentes cantidades
plus_3 = make_adder(3)  # Devuelve lambda que suma 3
plus_5 = make_adder(5)  # Devuelve lambda que suma 5

plus_3(4)  # Devuelve 4 + 3 = 7
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

<BaseQuiz id="cheatsheet-functions-5" correct="A">
<template #question>
What does a lambda closure allow you to do?
</template>

<BaseQuizOption value="A" correct>A. Capture variables from the outer scope</BaseQuizOption>
<BaseQuizOption value="B">B. Modify global variables without the global keyword</BaseQuizOption>
<BaseQuizOption value="C">C. Return multiple values</BaseQuizOption>
<BaseQuizOption value="D">D. Execute code asynchronously</BaseQuizOption>
<BaseQuizAnswer>Los cierres lambda permiten que las funciones lambda capturen y utilicen variables de su ámbito circundante, de manera similar a las funciones anidadas regulares.</BaseQuizAnswer>
</BaseQuiz>

## Enlaces relevantes

- <router-link to="/blog/python-easy-args-kwargs">\*args y \*\*kwargs explicados</router-link>
- <router-link to="/cheatsheet/args-and-kwargs">Args y Kwargs</router-link>
- <router-link to="/cheatsheet/decorators">Decoradores</router-link>
- <router-link to="/cheatsheet/control-flow">Flujo de Control</router-link>
- <router-link to="/cheatsheet/basics">Conceptos Básicos</router-link>
- <router-link to="/builtin">Funciones Incorporadas</router-link>
