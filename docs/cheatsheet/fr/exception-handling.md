---
title: 'Gestion des Exceptions Python - Fiche Récapitulative Python'
description: "En Python, la gestion des exceptions est le processus de réponse à l'occurrence d'exceptions."
labUrl: 'https://labex.io/fr/labs/python-python-exception-handling-633656?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Gestion des Exceptions Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikipedia.org/wiki/Exception_handling">Gestion des exceptions</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    En informatique et en programmation informatique, la gestion des exceptions est le processus de réponse à l'occurrence d'exceptions – des conditions anormales ou exceptionnelles nécessitant un traitement spécial.
  </base-disclaimer-content>
</base-disclaimer>

Python possède de nombreuses [exceptions intégrées](https://docs.python.org/3/library/exceptions.html) qui sont levées lorsqu'un programme rencontre une erreur, et la plupart des bibliothèques externes, comme la populaire [Requests](https://requests.readthedocs.io/en/latest), incluent ses propres [exceptions personnalisées](https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions) que nous devrons gérer.

## Gestion des exceptions de base

Vous ne pouvez pas diviser par zéro, c'est une vérité mathématique, et si vous essayez de le faire en Python, l'interpréteur lèvera l'exception intégrée [ZeroDivisionError](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError) :

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

Supposons que nous ne voulions pas que notre programme arrête son exécution ou n'affiche à l'utilisateur un résultat qu'il ne comprendra pas. Disons que nous voulons imprimer un message utile et clair, alors nous devons **_gérer_** l'exception avec les mots-clés `try` et `except` :

```python
# try-except: gérer les exceptions avec élégance
def divide(dividend , divisor):
    try:  # Essayer d'exécuter ce code
        print(dividend / divisor)
    except ZeroDivisionError:  # Capturer le type d'exception spécifique
        print('Vous ne pouvez pas diviser par 0')

divide(dividend=10, divisor=5)
```

```output
2
```

```python
divide(dividend=10, divisor=0)
```

```output
Vous ne pouvez pas diviser par 0
```

<BaseQuiz id="cheatsheet-exception-handling-1" correct="A">
<template #question>
Quels mots-clés sont utilisés pour gérer les exceptions en Python ?
</template>

<BaseQuizOption value="A" correct>A. <code>try</code> et <code>except</code></BaseQuizOption>
<BaseQuizOption value="B">B. <code>catch</code> et <code>handle</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>error</code> et <code>rescue</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>if</code> et <code>else</code></BaseQuizOption>
<BaseQuizAnswer>Python utilise <code>try</code> pour marquer le code qui pourrait lever une exception, et <code>except</code> pour gérer les exceptions spécifiques qui se produisent.</BaseQuizAnswer>
</BaseQuiz>

## Gestion de multiples exceptions à l'aide d'un seul bloc d'exception

Vous pouvez également gérer plusieurs exceptions sur une seule ligne comme suit sans avoir besoin de créer plusieurs blocs d'exception.

```python
# Gérer plusieurs exceptions dans un seul bloc except
def divide(dividend , divisor):
    try:
        if (dividend == 10):
          var = 'str' + 1  # Ceci lèvera TypeError
        else:
          print(dividend / divisor)
    except (ZeroDivisionError, TypeError) as error:  # Capturer plusieurs types d'exceptions
        print(error)  # Afficher le message d'erreur

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

<BaseQuiz id="cheatsheet-exception-handling-2" correct="B">
<template #question>
Pouvez-vous gérer plusieurs types d'exceptions dans un seul bloc <code>except</code> ?
</template>

<BaseQuizOption value="A">A. Non, vous devez utiliser des blocs <code>except</code> séparés pour chaque type d'exception</BaseQuizOption>
<BaseQuizOption value="B" correct>B. Oui, en les plaçant dans un tuple comme <code>except (Exception1, Exception2)</code></BaseQuizOption>
<BaseQuizOption value="C">C. Oui, mais seulement s'ils sont liés</BaseQuizOption>
<BaseQuizOption value="D">D. Non, Python ne prend pas cela en charge</BaseQuizOption>
<BaseQuizAnswer>Vous pouvez gérer plusieurs types d'exceptions dans un seul bloc <code>except</code> en les plaçant dans un tuple : <code>except (ZeroDivisionError, TypeError) as error:</code></BaseQuizAnswer>
</BaseQuiz>

## Code Finally dans la gestion des exceptions

Le code à l'intérieur de la section `finally` est toujours exécuté, qu'une exception ait été levée ou non :

```python
# Bloc finally : s'exécute toujours, quelles que soient les exceptions
def divide(dividend , divisor):
    try:
        print(dividend / divisor)
    except ZeroDivisionError:
        print('Vous ne pouvez pas diviser par 0')
    finally:  # S'exécute toujours, même si une exception se produit
        print('Exécution terminée')

divide(dividend=10, divisor=5)
```

```output
2.0
Exécution terminée
```

```python
divide(dividend=10, divisor=0)
```

```output
Vous ne pouvez pas diviser par 0
Exécution terminée
```

<BaseQuiz id="cheatsheet-exception-handling-3" correct="C">
<template #question>
Quand le bloc <code>finally</code> s'exécute-t-il ?
</template>

<BaseQuizOption value="A">A. Seulement lorsqu'une exception se produit</BaseQuizOption>
<BaseQuizOption value="B">B. Seulement lorsqu'aucune exception ne se produit</BaseQuizOption>
<BaseQuizOption value="C" correct>C. Toujours, qu'une exception se soit produite ou non</BaseQuizOption>
<BaseQuizOption value="D">D. Jamais</BaseQuizOption>
<BaseQuizAnswer>Le bloc <code>finally</code> s'exécute toujours, qu'une exception se soit produite ou non. Il est utile pour le code de nettoyage qui doit s'exécuter quel que soit le résultat.</BaseQuizAnswer>
</BaseQuiz>

## Exceptions personnalisées

Les exceptions personnalisées s'initialisent en créant une `class` qui hérite de la classe de base `Exception` de Python, et sont levées à l'aide du mot-clé `raise` :

```python
# Exception personnalisée : créée en héritant de la classe Exception
class MyCustomException(Exception):
    pass

raise MyCustomException  # Lever l'exception personnalisée
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyCustomException
```

Pour déclarer un message d'exception personnalisé, vous pouvez le passer comme paramètre :

```python
class MyCustomException(Exception):
    pass

raise MyCustomException('Un message personnalisé pour mon exception personnalisée')
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyCustomException: Un message personnalisé pour mon exception personnalisée
```

La gestion d'une exception personnalisée est la même que pour toute autre :

```python
try:
    raise MyCustomException('Un message personnalisé pour mon exception personnalisée')
except MyCustomException:
    print('Mon exception personnalisée a été levée')
```

```output
Mon exception personnalisée a été levée
```

<BaseQuiz id="cheatsheet-exception-handling-4" correct="A">
<template #question>
Comment créez-vous une exception personnalisée en Python ?
</template>

<BaseQuizOption value="A" correct>A. Créez une classe qui hérite de la classe <code>Exception</code></BaseQuizOption>
<BaseQuizOption value="B">B. Utilisez le décorateur <code>@exception</code></BaseQuizOption>
<BaseQuizOption value="C">C. Appelez <code>Exception.create()</code></BaseQuizOption>
<BaseQuizOption value="D">D. Importez-la à partir d'un module spécial</BaseQuizOption>
<BaseQuizAnswer>Les exceptions personnalisées sont créées en définissant une classe qui hérite de la classe de base <code>Exception</code>. Vous pouvez ensuite les lever et les gérer comme des exceptions intégrées.</BaseQuizAnswer>
</BaseQuiz>

## Liens pertinents

- <router-link to="/cheatsheet/control-flow">Flux de contrôle</router-link>
- <router-link to="/builtin/breakpoint">breakpoint()</router-link>
- <router-link to="/builtin/isinstance">isinstance()</router-link>
- <router-link to="/builtin/issubclass">issubclass()</router-link>
