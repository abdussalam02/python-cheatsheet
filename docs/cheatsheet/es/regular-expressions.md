---
title: 'Expresiones Regulares en Python - Hoja de Trucos de Python'
description: 'Una expresión regular (abreviada como regex) es una secuencia de caracteres que especifica un patrón de búsqueda en texto y es utilizada por algoritmos de búsqueda de cadenas.'
labUrl: 'https://labex.io/es/labs/python-python-regular-expressions-633664?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Expresiones Regulares
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikipedia.org/wiki/Regular_expression">Expresiones Regulares</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Una expresión regular (abreviada como regex [...]) es una secuencia de caracteres que especifica un patrón de búsqueda en texto. [...] utilizada por algoritmos de búsqueda de cadenas para operaciones de "buscar" o "buscar y reemplazar" en cadenas, o para validación de entrada.
  </base-disclaimer-content>
</base-disclaimer>

1. Importe el módulo regex con `import re`.
2. Cree un objeto Regex con la función `re.compile()`. (Recuerde usar una cadena sin formato/raw string).
3. Pase la cadena que desea buscar al método `search()` del objeto Regex. Esto devuelve un objeto `Match`.
4. Llame al método `group()` del objeto Match para devolver una cadena con el texto coincidente real.

Todas las funciones regex en Python están en el módulo re:

```python
# Importar el módulo re para operaciones de expresiones regulares
import re
```

## Símbolos Regex

| Símbolo                | Coincide                                                              |
| :--------------------- | :-------------------------------------------------------------------- |
| `?`                    | cero o una vez del grupo precedente.                                  |
| `*`                    | cero o más veces del grupo precedente.                                |
| `+`                    | una o más veces del grupo precedente.                                 |
| `{n}`                  | exactamente n veces del grupo precedente.                             |
| `{n,}`                 | n o más veces del grupo precedente.                                   |
| `{,m}`                 | 0 a m veces del grupo precedente.                                     |
| `{n,m}`                | al menos n y como máximo m veces del p precedente.                    |
| `{n,m}?` o `*?` o `+?` | realiza una coincidencia no codiciosa (non-greedy) del p precedente.  |
| `^spam`                | significa que la cadena debe comenzar con spam.                       |
| `spam$`                | significa que la cadena debe terminar con spam.                       |
| `.`                    | cualquier carácter, excepto los caracteres de nueva línea.            |
| `\d`, `\w`, y `\s`     | un dígito, palabra o carácter de espacio, respectivamente.            |
| `\D`, `\W`, y `\S`     | cualquier cosa excepto un dígito, palabra o espacio, respectivamente. |
| `[abc]`                | cualquier carácter entre los corchetes (como a, b, ).                 |
| `[^abc]`               | cualquier carácter que no esté entre los corchetes.                   |

## Objetos Regex Coincidentes

```python
# re.compile(): crear objeto de patrón regex (usar cadena sin formato r'' para evitar el escape)
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # Patrón: 3 dígitos-3 dígitos-4 dígitos

mo = phone_num_regex.search('Mi número es 415-555-4242.')  # Buscar patrón

print(f'Número de teléfono encontrado: {mo.group()}')  # group() devuelve el texto coincidente
```

```output
Phone number found: 415-555-4242
```

## Agrupación con paréntesis

```python
# Los paréntesis crean grupos: group(1) devuelve el primer grupo, group(2) devuelve el segundo
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')  # Dos grupos entre paréntesis
mo = phone_num_regex.search('Mi número es 415-555-4242.')

mo.group(1)  # Devuelve el primer grupo: '415'
```

```output
'415'
```

```python
mo.group(2)
```

```output
'555-4242'
```

```python
mo.group(0)
```

```output
'415-555-4242'
```

```python
mo.group()
```

```output
'415-555-4242'
```

<BaseQuiz id="cheatsheet-regular-expressions-1" correct="A">
<template #question>
¿Qué devuelve <code>group()</code> cuando se llama en un objeto de coincidencia?
</template>

<BaseQuizOption value="A" correct>A. El texto completo coincidente</BaseQuizOption>
<BaseQuizOption value="B">B. Solo el primer grupo</BaseQuizOption>
<BaseQuizOption value="C">C. Todos los grupos como una lista</BaseQuizOption>
<BaseQuizOption value="D">D. El índice de la coincidencia</BaseQuizOption>
<BaseQuizAnswer>El método <code>group()</code> (o <code>group(0)</code>) devuelve el texto completo coincidente. Para obtener grupos específicos, use <code>group(1)</code>, <code>group(2)</code>, etc.</BaseQuizAnswer>
</BaseQuiz>

Para recuperar todos los grupos a la vez, use el método `groups()`:

```python
# groups(): devuelve una tupla de todos los grupos
mo.groups()  # Devuelve ('415', '555-4242')
```

```output
('415', '555-4242')
```

```python
area_code, main_number = mo.groups()

print(area_code)
```

```output
415
```

```python
print(main_number)
```

```output
555-4242
```

## Múltiples grupos con Pipe

Puede usar el carácter `|` donde quiera hacer coincidir una de muchas expresiones.

```python
hero_regex = re.compile (r'Batman|Tina Fey')

mo1 = hero_regex.search('Batman y Tina Fey.')
mo1.group()
```

```output
'Batman'
```

```python
mo2 = hero_regex.search('Tina Fey y Batman.')
mo2.group()
```

```output
'Tina Fey'
```

También puede usar el pipe para hacer coincidir uno de varios patrones como parte de su regex:

```python
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile perdió una rueda')

mo.group()
```

```output
'Batmobile'
```

```python
mo.group(1)
```

```output
'mobile'
```

## Coincidencia opcional con el signo de Interrogación

El carácter `?` marca el grupo que lo precede como una parte opcional del patrón.

```python
bat_regex = re.compile(r'Bat(wo)?man')

mo1 = bat_regex.search('Las Aventuras de Batman')
mo1.group()
```

```output
'Batman'
```

```python
mo2 = bat_regex.search('Las Aventuras de Batwoman')
mo2.group()
```

```output
'Batwoman'
```

## Coincidencia de cero o más con el Asterisco

El `*` (asterisco) significa "coincidir cero o más veces". El grupo que precede al asterisco puede aparecer cualquier número de veces en el texto.

```python
bat_regex = re.compile(r'Bat(wo)*man')
mo1 = bat_regex.search('Las Aventuras de Batman')
mo1.group()
```

```output
'Batman'
```

```python
mo2 = bat_regex.search('Las Aventuras de Batwoman')
mo2.group()
```

```output
'Batwoman'
```

```python
mo3 = bat_regex.search('Las Aventuras de Batwowowowoman')
mo3.group()
```

```output
'Batwowowowoman'
```

## Coincidencia de uno o más con el Plus

El `+` (o plus) _significa coincidir uno o más veces_. El grupo que precede a un plus debe aparecer al menos una vez:

```python
bat_regex = re.compile(r'Bat(wo)+man')

mo1 = bat_regex.search('Las Aventuras de Batwoman')
mo1.group()
```

```output
'Batwoman'
```

```python
mo2 = bat_regex.search('Las Aventuras de Batwowowowoman')
mo2.group()
```

```output
'Batwowowowoman'
```

```python
mo3 = bat_regex.search('Las Aventuras de Batman')
mo3 is None
```

```output
True
```

## Coincidencia de repeticiones específicas con Llaves

Si tiene un grupo que desea repetir un número específico de veces, siga el grupo en su regex con un número entre llaves:

```python
ha_regex = re.compile(r'(Ha){3}')

mo1 = ha_regex.search('HaHaHa')
mo1.group()
```

```output
'HaHaHa'
```

```python
mo2 = ha_regex.search('Ha')
mo2 is None
```

```output
True
```

En lugar de un número, puede especificar un rango con un mínimo y un máximo entre las llaves. Por ejemplo, la expresión regular (Ha){3,5} coincidirá con 'HaHaHa', 'HaHaHaHa' y 'HaHaHaHaHa'.

```python
ha_regex = re.compile(r'(Ha){2,3}')
mo1 = ha_regex.search('HaHaHaHa')
mo1.group()
```

```output
'HaHaHa'
```

## Coincidencia codiciosa (Greedy) y no codiciosa (Non-greedy)

Las expresiones regulares de Python son codiciosas por defecto: en situaciones ambiguas intentarán hacer coincidir la cadena más larga posible. La versión no codiciosa de las llaves, que coincide con la cadena más corta posible, tiene la llave de cierre seguida de un signo de interrogación.

```python
greedy_ha_regex = re.compile(r'(Ha){3,5}')

mo1 = greedy_ha_regex.search('HaHaHaHaHa')
mo1.group()
```

```output
'HaHaHaHaHa'
```

```python
non_greedy_ha_regex = re.compile(r'(Ha){3,5}?')
mo2 = non_greedy_ha_regex.search('HaHaHaHaHa')
mo2.group()
```

```output
'HaHaHa'
```

<BaseQuiz id="cheatsheet-regular-expressions-2" correct="B">
<template #question>
¿Qué hace que un patrón regex no sea codicioso (non-greedy)?
</template>

<BaseQuizOption value="A">A. Usar <code>_</code> en lugar de <code>+</code></BaseQuizOption>
<BaseQuizOption value="B" correct>B. Añadir un <code>?</code> después del cuantificador (ej. <code>_?</code>, <code>+?</code>, <code>{3,5}?</code>)</BaseQuizOption>
<BaseQuizOption value="C">C. Usar paréntesis</BaseQuizOption>
<BaseQuizOption value="D">D. Usar corchetes</BaseQuizOption>
<BaseQuizAnswer>Añadir un <code>?</code> después de cuantificadores como <code>\*</code>, <code>+</code>, o <code>{n,m}</code> los hace no codiciosos, haciendo coincidir la cadena más corta posible en lugar de la más larga.</BaseQuizAnswer>
</BaseQuiz>

## El método findall()

El método `findall()` devolverá las cadenas de cada coincidencia en la cadena buscada.

```python
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # no tiene grupos

phone_num_regex.findall('Celular: 415-555-9999 Trabajo: 212-555-0000')
```

```output
['415-555-9999', '212-555-0000']
```

## Creando sus propias clases de caracteres

Puede definir su propia clase de caracteres usando corchetes. Por ejemplo, la clase de caracteres _[aeiouAEIOU]_ coincidirá con cualquier vocal, tanto minúscula como mayúscula.

```python
vowel_regex = re.compile(r'[aeiouAEIOU]')
vowel_regex.findall('Robocop come comida de bebé. COMIDA DE BEBÉ.')
```

```output
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
```

También puede incluir rangos de letras o números usando un guion. Por ejemplo, la clase de caracteres _[a-zA-Z0-9]_ coincidirá con todas las letras minúsculas, letras mayúsculas y números.

Al colocar un carácter circunflejo (`^`) justo después del corchete de apertura de la clase de caracteres, puede crear una clase de caracteres negativa que coincidirá con todos los caracteres que no están en la clase de caracteres:

```python
consonant_regex = re.compile(r'[^aeiouAEIOU]')
consonant_regex.findall('Robocop come comida de bebé. COMIDA DE BEBÉ.')
```

```output
['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
```

## Los caracteres Caret y Dollar sign

- También puede usar el símbolo de circunflejo `^` al comienzo de una regex para indicar que una coincidencia debe ocurrir al principio del texto buscado.

- De manera similar, puede colocar un signo de dólar `$` al final de la regex para indicar que la cadena debe terminar con este patrón regex.

- Y puede usar el `^` y el `$` juntos para indicar que toda la cadena debe coincidir con la regex.

La cadena de expresión regular `r'^Hello'` coincide con las cadenas que comienzan con 'Hello':

```python
begins_with_hello = re.compile(r'^Hello')
begins_with_hello.search('Hello mundo!')
```

```output
<_sre.SRE_Match object; span=(0, 5), match='Hello'>
```

```python
begins_with_hello.search('Él dijo hola.') is None
```

```output
True
```

La cadena de expresión regular `r'\d\$'` coincide con cadenas que terminan con un carácter numérico del 0 al 9:

```python
whole_string_is_num = re.compile(r'^\d+$')

whole_string_is_num.search('1234567890')
```

```output
<_sre.SRE_Match object; span=(0, 10), match='1234567890'>
```

```python
whole_string_is_num.search('12345xyz67890') is None
```

```output
True
```

```python
whole_string_is_num.search('12 34567890') is None
```

```output
True
```

## El carácter Comodín

El carácter `.` (o punto) en una expresión regular coincidirá con cualquier carácter excepto una nueva línea:

```python
at_regex = re.compile(r'.at')

at_regex.findall('El gato en el sombrero se sentó en la alfombra plana.')
```

```output
['cat', 'hat', 'sat', 'lat', 'mat']
```

## Coincidencia de todo con Dot-Star

```python
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')

mo = name_regex.search('First Name: Al Last Name: Sweigart')
mo.group(1)
```

```output
'Al'
```

```python
mo.group(2)
```

```output
'Sweigart'
```

El `.*` usa el modo codicioso (greedy): Siempre intentará hacer coincidir la mayor cantidad de texto posible. Para hacer coincidir cualquier y todo el texto de manera no codiciosa, use el punto, el asterisco y el signo de interrogación (`.*?`). El signo de interrogación le dice a Python que coincida de manera no codiciosa:

```python
non_greedy_regex = re.compile(r'<.*?>')
mo = non_greedy_regex.search('<Servir al hombre> para la cena.>')
mo.group()
```

```output
'<To serve man>'
```

```python
greedy_regex = re.compile(r'<.*>')
mo = greedy_regex.search('<Servir al hombre> para la cena.>')
mo.group()
```

```output
'<To serve man> for dinner.>'
```

## Coincidencia de nuevas líneas con el carácter Punto

El punto-asterisco coincide con todo excepto una nueva línea. Al pasar `re.DOTALL` como segundo argumento a `re.compile()`, puede hacer que el carácter punto coincida con todos los caracteres, incluido el carácter de nueva línea:

```python
no_newline_regex = re.compile('.*')
no_newline_regex.search('Sirva la confianza pública.\nProteja al inocente.\nMantenga la ley.').group()
```

```output
'Serve the public trust.'
```

```python
newline_regex = re.compile('.*', re.DOTALL)
newline_regex.search('Sirva la confianza pública.\nProteja al inocente.\nMantenga la ley.').group()
```

```output
'Serve the public trust.\nProtect the innocent.\nUphold the law.'
```

## Coincidencia sin distinción entre mayúsculas y minúsculas

Para hacer que su regex no distinga entre mayúsculas y minúsculas, puede pasar `re.IGNORECASE` o `re.I` como segundo argumento a `re.compile()`:

```python
robocop = re.compile(r'robocop', re.I)

robocop.search('Robocop es parte hombre, parte máquina, todo policía.').group()
```

```output
'Robocop'
```

```python
robocop.search('ROBOCOP protege a los inocentes.').group()
```

```output
'ROBOCOP'
```

```python
robocop.search('Al, ¿por qué tu libro de programación habla tanto de robocop?').group()
```

```output
'robocop'
```

## Sustitución de cadenas con el método sub()

El método `sub()` para objetos Regex recibe dos argumentos:

1. El primer argumento es una cadena para reemplazar cualquier coincidencia.
2. El segundo es la cadena para la expresión regular.

El método `sub()` devuelve una cadena con las sustituciones aplicadas:

```python
names_regex = re.compile(r'Agent \w+')

names_regex.sub('CENSURADO', 'El Agente Alice dio los documentos secretos al Agente Bob.')
```

```output
'CENSORED gave the secret documents to CENSORED.'
```

<BaseQuiz id="cheatsheet-regular-expressions-3" correct="B">
<template #question>
¿Qué hace el método <code>sub()</code>?
</template>

<BaseQuizOption value="A">A. Encuentra todas las coincidencias en una cadena</BaseQuizOption>
<BaseQuizOption value="B" correct>B. Reemplaza todas las coincidencias con una cadena de reemplazo</BaseQuizOption>
<BaseQuizOption value="C">C. Divide una cadena en las coincidencias</BaseQuizOption>
<BaseQuizOption value="D">D. Valida el formato de una cadena</BaseQuizOption>
<BaseQuizAnswer>El método <code>sub()</code> sustituye todas las coincidencias del patrón con una cadena de reemplazo. Devuelve una nueva cadena con las sustituciones aplicadas.</BaseQuizAnswer>
</BaseQuiz>

## Gestión de Regexes complejas

Para indicarle a la función `re.compile()` que ignore los espacios en blanco y los comentarios dentro de la cadena de expresión regular, se puede habilitar el "modo detallado" (verbose mode) pasando la variable `re.VERBOSE` como segundo argumento a `re.compile()`.

Ahora, en lugar de una expresión regular difícil de leer como esta:

```python
phone_regex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
```

puede distribuir la expresión regular en varias líneas con comentarios como este:

```python
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # código de área
    (\s|-|\.)?                    # separador
    \d{3}                         # primeros 3 dígitos
    (\s|-|\.)                     # separador
    \d{4}                         # últimos 4 dígitos
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extensión
    )''', re.VERBOSE)
```

<BaseQuiz id="cheatsheet-regular-expressions-4" correct="A">
<template #question>
¿Qué hace <code>re.VERBOSE</code> cuando se pasa a <code>re.compile()</code>?
</template>

<BaseQuizOption value="A" correct>A. Permite espacios en blanco y comentarios en el patrón regex para una mejor legibilidad</BaseQuizOption>
<BaseQuizOption value="B">B. Hace que la regex no distinga entre mayúsculas y minúsculas</BaseQuizOption>
<BaseQuizOption value="C">C. Hace que el punto coincida con los caracteres de nueva línea</BaseQuizOption>
<BaseQuizOption value="D">D. Acelera la coincidencia de regex</BaseQuizOption>
<BaseQuizAnswer>La bandera <code>re.VERBOSE</code> le permite agregar espacios en blanco y comentarios a su patrón regex, haciendo que las regex complejas sean mucho más legibles sin afectar la coincidencia del patrón.</BaseQuizAnswer>
</BaseQuiz>

## Enlaces relevantes

- <router-link to="/cheatsheet/manipulating-strings">Manipulación de Cadenas</router-link>
- <router-link to="/cheatsheet/string-formatting">Formato de Cadenas</router-link>
- <router-link to="/blog/python-data-types">Publicación del Blog sobre Tipos de Datos de Python</router-link>
- <router-link to="/builtin/compile">compile()</router-link>
