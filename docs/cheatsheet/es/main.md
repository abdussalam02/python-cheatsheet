---
title: 'Función Principal de Python - Hoja de Trucos de Python'
description: 'Es el nombre del ámbito en el que se ejecuta el código de nivel superior. El nombre de un módulo se establece como main cuando se lee desde la entrada estándar, un script o un indicador interactivo.'
labUrl: 'https://labex.io/es/labs/python-python-main-function-633661?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Entorno de script de nivel superior principal
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## Qué es

`__main__` es el nombre del ámbito en el que se ejecuta el código de nivel superior.
El **nombre** de un módulo se establece igual a `__main__` cuando se lee desde la entrada estándar, un script o un indicador interactivo.

Un módulo puede descubrir si se está ejecutando en el ámbito principal comprobando su propio `__name__`, lo que permite una idiomática común para ejecutar código condicionalmente en un módulo. Cuando se ejecuta como un script o con `python -m`, pero no cuando se importa:

```python
# __name__ == "__main__": comprobar si el script se ejecuta directamente (no se importa)
if __name__ == "__main__":  # Verdadero cuando se ejecuta como script, Falso cuando se importa
    # ejecutar solo si se ejecuta como script
    main()
```

Para un paquete, se puede lograr el mismo efecto incluyendo un módulo **main**.py, cuyo contenido se ejecutará cuando el módulo se ejecute con -m.

Por ejemplo, si estamos desarrollando un script diseñado para ser utilizado como módulo, deberíamos hacer:

```python
# Ejemplo: la función se puede importar, pero el código de prueba solo se ejecuta cuando se ejecuta directamente
def add(a, b):
    return a+b

if __name__ == "__main__":  # Solo se ejecuta cuando se ejecuta el archivo, no cuando se importa
    add(3, 5)
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
¿Cuál es el valor de <code>__name__</code> cuando un archivo Python se ejecuta directamente como un script?
</template>

<base-quiz-option value="A">A. El nombre del archivo</base-quiz-option>
<base-quiz-option value="B" correct>B. <code>"**main**"</code></base-quiz-option>
<base-quiz-option value="C">C. <code>None</code></base-quiz-option>
<base-quiz-option value="D">D. <code>True</code></base-quiz-option>
<base-quiz-answer value="B">Cuando un archivo Python se ejecuta directamente como un script, <code>**name**</code> se establece en <code>"**main**"</code>. Cuando el archivo se importa como un módulo, <code>**name**</code> se establece en el nombre del módulo.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Ventajas

1. Cada módulo de Python tiene definido su `__name__` y si este es `__main__`, implica que el módulo es ejecutado de forma independiente por el usuario, y podemos realizar las acciones apropiadas correspondientes.
2. Si importa este script como un módulo en otro script, el **nombre** se establece en el nombre del script/módulo.
3. Los archivos de Python pueden actuar como módulos reutilizables o como programas independientes.
4. `if __name__ == "__main__":` se utiliza para ejecutar algo de código solo si el archivo se ejecuta directamente y no se está importando.

<base-quiz>
<base-quiz-question correct="A">
<template #question>
¿Cuál es el propósito principal de usar <code>if __name__ == "__main__":</code>?
</template>

<base-quiz-option value="A" correct>A. Ejecutar código solo cuando el archivo se ejecuta directamente, no cuando se importa</base-quiz-option>
<base-quiz-option value="B">B. Evitar que el archivo sea importado</base-quiz-option>
<base-quiz-option value="C">C. Hacer que el archivo se ejecute más rápido</base-quiz-option>
<base-quiz-option value="D">D. Ocultar código a otros módulos</base-quiz-option>
<base-quiz-answer value="A">El modismo <code>if **name** == "**main**":</code> permite que un archivo de Python actúe tanto como un módulo reutilizable como un programa independiente. El código dentro de este bloque solo se ejecuta cuando el archivo se ejecuta directamente, no cuando se importa.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Enlaces relevantes

- <router-link to="/cheatsheet/functions">Funciones</router-link>
- <router-link to="/cheatsheet/packaging">Empaquetado</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Proyectos de Python con Poetry y VSCode. Parte 1</router-link>
- <router-link to="/builtin/import">import()</router-link>
