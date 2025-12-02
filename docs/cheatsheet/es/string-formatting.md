---
title: 'Formato de Cadenas en Python - Hoja de Trucos de Python'
description: 'Si usas Python 3.6+, las f-strings son el método recomendado para formatear cadenas.'
labUrl: 'https://labex.io/es/labs/python-python-string-formatting-633667?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Formato de Cadenas en Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    De la <a href="https://docs.python.org/3/library/stdtypes.html?highlight=sprintf#printf-style-string-formatting">documentación de Python 3</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Las operaciones de formato descritas aquí (<b>operador %</b>) exhiben una variedad de peculiaridades que conducen a varios errores comunes [...]. Usar los literales de cadena formateados más nuevos <a href="#formatted-string-literals-or-f-strings">o f-strings</a> [...] ayuda a evitar estos errores. Estas alternativas también proporcionan enfoques más potentes, flexibles y extensibles para formatear texto.
  </base-disclaimer-content>
</base-disclaimer>

## % operator

<base-warning>
  <base-warning-title>
    Prefiera los Literales de Cadena
  </base-warning-title>
  <base-warning-content>
    Para código nuevo, se recomienda encarecidamente usar <a href="#strformat">str.format</a>, o <a href="#formatted-string-literals-or-f-strings">literales de cadena formateados</a> (Python 3.6+) sobre el operador <code>%</code>.
  </base-warning-content>
</base-warning>

```python
# % operator: formato de cadena de estilo antiguo (no recomendado para código nuevo)
name = 'Pete'
'Hello %s' % name  # %s = marcador de posición de cadena
```

```output
"Hello Pete"
```

Podemos usar el especificador de formato `%d` para convertir un valor int a una cadena:

```python
num = 5
'I have %d apples' % num
```

```output
"I have 5 apples"
```

## str.format

Python 3 introdujo una nueva forma de formatear cadenas que luego fue retroportada a Python 2.7. Esto hace que la sintaxis para el formato de cadenas sea más regular.

```python
# str.format() method: formato de cadena moderno (Python 2.7+)
name = 'John'
age = 20

"Hello I'm {}, my age is {}".format(name, age)  # {} = marcador de posición
```

```output
"Hello I'm John, my age is 20"
```

```python
"Hello I'm {0}, my age is {1}".format(name, age)
```

```output
"Hello I'm John, my age is 20"
```

## Formatted String Literals or f-Strings

Si está utilizando Python 3.6+, las `f-Strings` de cadenas son la forma recomendada de formatear cadenas.

<base-disclaimer>
  <base-disclaimer-title>
    De la <a href="https://docs.python.org/3/reference/lexical_analysis.html#f-strings">documentación de Python 3</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Un literal de cadena formateado o f-string es un literal de cadena que está prefijado con <code>f</code> o <code>F</code>. Estas cadenas pueden contener campos de reemplazo, que son expresiones delimitadas por llaves {}. Si bien otros literales de cadena siempre tienen un valor constante, las cadenas formateadas son realmente expresiones evaluadas en tiempo de ejecución.
  </base-disclaimer-content>
</base-disclaimer>

```python
# f-string: forma recomendada de formatear cadenas (Python 3.6+)
name = 'Elizabeth'
f'Hello {name}!'  # El prefijo f permite expresiones en {}
```

```output
'Hello Elizabeth!'
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-string-formatting-1">
<template #question>
¿Qué prefijo se utiliza para las f-strings en Python?
</template>

<base-quiz-option value="A">A. <code>fmt</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>f</code> o <code>F</code></base-quiz-option>
<base-quiz-option value="C">C. <code>format</code></base-quiz-option>
<base-quiz-option value="D">D. <code>str</code></base-quiz-option>
<base-quiz-answer value="B">Las f-strings van precedidas por <code>f</code> o <code>F</code> antes de la comilla de apertura. Permiten incrustar expresiones dentro de llaves <code>{}</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Incluso es posible hacer aritmética en línea con ellas:

```python
# Las f-strings soportan expresiones: pueden incluir cálculos dentro de {}
a = 5
b = 10
f'Five plus ten is {a + b} and not {2 * (a + b)}.'  # Evalúa expresiones
```

```output
'Five plus ten is 15 and not 30.'
```

### F-Strings Multilínea

```python
name = 'Robert'
messages = 12
(
f'Hi, {name}. '
f'You have {messages} unread messages'
)
```

```output
'Hi, Robert. You have 12 unread messages'
```

### El especificador =

Esto imprimirá la expresión y su valor:

```python
# Especificador =: imprime tanto el nombre de la variable como el valor (Python 3.8+)
from datetime import datetime
now = datetime.now().strftime("%b/%d/%Y - %H:%M:%S")
f'date and time: {now=}'  # Imprime "now='Nov/14/2022 - 20:50:01'"
```

```output
"date and time: now='Nov/14/2022 - 20:50:01'"
```

### Añadir espacios o caracteres

```python
name = 'Robert'
f"{name.upper() = :-^20}"
```

```output
'name.upper() = -------ROBERT-------'
```

```python
f"{name.upper() = :^20}"
```

```output
'name.upper() =        ROBERT       '
```

```python
f"{name.upper() = :20}"
```

```output
'name.upper() = ROBERT              '
```

## Formato de Dígitos

Añadir separador de miles

```python
a = 10000000
f"{a:,}"
```

```output
'10,000,000'
```

Redondeo

```python
a = 3.1415926
f"{a:.2f}"
```

```output
'3.14'
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-string-formatting-2">
<template #question>
¿Qué hace <code>f"{a:.2f}"</code>?
</template>

<base-quiz-option value="A">A. Redondea el número al entero más cercano</base-quiz-option>
<base-quiz-option value="B">B. Formatea como porcentaje</base-quiz-option>
<base-quiz-option value="C" correct>C. Formatea el número como un flotante con 2 decimales</base-quiz-option>
<base-quiz-option value="D">D. Convierte a notación científica</base-quiz-option>
<base-quiz-answer value="C">El especificador de formato <code>:.2f</code> formatea un número como un flotante con exactamente 2 decimales. El <code>.2</code> especifica la precisión y <code>f</code> significa formato flotante.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Mostrar como Porcentaje

```python
a = 0.816562
f"{a:.2%}"
```

```output
'81.66%'
```

### Tabla de formato de números

| Número     | Formato | Salida    | Descripción                                         |
| ---------- | ------- | --------- | --------------------------------------------------- |
| 3.1415926  | {:.2f}  | 3.14      | Formato flotante 2 decimales                        |
| 3.1415926  | {:+.2f} | +3.14     | Formato flotante 2 decimales con signo              |
| -1         | {:+.2f} | -1.00     | Formato flotante 2 decimales con signo              |
| 2.71828    | {:.0f}  | 3         | Formato flotante sin decimales                      |
| 4          | {:0>2d} | 04        | Rellena el número con ceros (relleno izq., ancho 2) |
| 4          | {:x<4d} | 4xxx      | Rellena el número con x's (relleno der., ancho 4)   |
| 10         | {:x<4d} | 10xx      | Rellena el número con x's (relleno der., ancho 4)   |
| 1000000    | {:,}    | 1,000,000 | Formato de número con separador de coma             |
| 0.35       | {:.2%}  | 35.00%    | Formato de porcentaje                               |
| 1000000000 | {:.2e}  | 1.00e+09  | Notación exponencial                                |
| 11         | {:11d}  | 11        | Alineado a la derecha (predeterminado, ancho 10)    |
| 11         | {:<11d} | 11        | Alineado a la izquierda (ancho 10)                  |
| 11         | {:^11d} | 11        | Alineado al centro (ancho 10)                       |

## Template Strings

Un mecanismo más simple y menos potente, pero se recomienda cuando se manejan cadenas generadas por usuarios. Debido a su menor complejidad, las cadenas de plantilla son una opción más segura.

```python
from string import Template
name = 'Elizabeth'
t = Template('Hey $name!')
t.substitute(name=name)
```

```output
'Hey Elizabeth!'
```

## Enlaces relevantes

- <router-link to="/cheatsheet/manipulating-strings">Manipulación de Cadenas</router-link>
- <router-link to="/blog/python-data-types">Publicación del Blog sobre Tipos de Datos de Python</router-link>
- <router-link to="/builtin/format">format()</router-link>
- <router-link to="/builtin/print">print()</router-link>
- <router-link to="/builtin/str">str()</router-link>
- <router-link to="/builtin/repr">repr()</router-link>
- <router-link to="/builtin/ascii">ascii()</router-link>
