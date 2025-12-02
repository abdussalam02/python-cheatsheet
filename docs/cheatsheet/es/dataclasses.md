---
title: 'Clases de Datos de Python - Hoja de Trucos de Python'
description: 'Las clases de datos son clases de Python adecuadas para almacenar objetos de datos. Este módulo proporciona un decorador y funciones para añadir automáticamente métodos especiales generados como __init__() y __repr__() a clases definidas por el usuario.'
labUrl: 'https://labex.io/es/labs/python-python-dataclasses-633652?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Dataclasses de Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Las `Dataclasses` son clases de python, pero son adecuadas para almacenar objetos de datos.
Este módulo proporciona un decorador y funciones para añadir automáticamente métodos especiales generados como `__init__()` y `__repr__()` a las clases definidas por el usuario.

## Características

1. Almacenan datos y representan un cierto tipo de dato. Ej: Un número. Para aquellos familiarizados con los ORM, una instancia de modelo es un objeto de datos. Representa un tipo específico de entidad. Contiene atributos que definen o representan la entidad.

2. Se pueden comparar con otros objetos del mismo tipo. Ej: Un número puede ser mayor que, menor que, o igual a otro número.

Python 3.7 proporciona un decorador `dataclass` que se utiliza para convertir una clase en una dataclass.

```python
class Number:
    def __init__(self, val):
        self.val = val

obj = Number(2)
obj.val
```

```output
2
```

con dataclass

```python
# Dataclass: genera automáticamente los métodos __init__ y __repr__
from dataclasses import dataclass

@dataclass  # El decorador convierte la clase en una dataclass
class Number:
    val: int  # Se requiere anotación de tipo

obj = Number(2)  # __init__ creado automáticamente
obj.val
```

```output
2
```

## Valores por defecto

Es fácil añadir valores por defecto a los campos de tu data class.

```python
# Dataclass con valores por defecto: los campos con valores por defecto deben ir después de los campos requeridos
@dataclass
class Product:
    name: str        # Campo requerido
    count: int = 0   # Campo opcional con valor por defecto
    price: float = 0.0  # Campo opcional con valor por defecto

obj = Product("Python")  # Solo se requiere el nombre, los demás usan los valores por defecto
obj.name
```

```output
Python
```

```python
obj.count
```

```output
0
```

```python
obj.price
```

```output
0.0
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-dataclasses-1">
<template #question>
En una dataclass, ¿dónde deben colocarse los campos con valores por defecto?
</template>

<base-quiz-option value="A">A. Antes de los campos sin valores por defecto</base-quiz-option>
<base-quiz-option value="B" correct>B. Después de los campos sin valores por defecto</base-quiz-option>
<base-quiz-option value="C">C. No importa</base-quiz-option>
<base-quiz-option value="D">D. En una sección separada</base-quiz-option>
<base-quiz-answer value="B">En las dataclasses, los campos con valores por defecto deben ir después de los campos sin valores por defecto. Esto se debe a que Python necesita conocer el orden de los parámetros requeridos frente a los opcionales para el método <code>**init**</code> generado.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Pistas de tipo (Type hints)

Es obligatorio definir el tipo de dato en la dataclass. Sin embargo, si prefieres no especificar el tipo de dato, usa `typing.Any`.

```python
from dataclasses import dataclass
from typing import Any

@dataclass
class WithoutExplicitTypes:
   name: Any
   value: Any = 42
```

## Enlaces relevantes

- <router-link to="/cheatsheet/oop-basics">Conceptos básicos de OOP</router-link>
- <router-link to="/cheatsheet/decorators">Decoradores</router-link>
- <router-link to="/blog/python-data-types">Publicación del Blog sobre Tipos de Datos de Python</router-link>
- <router-link to="/builtin/object">object()</router-link>
- <router-link to="/builtin/repr">repr()</router-link>
- <router-link to="/builtin/type">type()</router-link>
