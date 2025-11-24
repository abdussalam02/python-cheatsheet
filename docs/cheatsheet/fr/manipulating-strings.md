---
title: 'Manipulation de Chaînes - Aide-Mémoire Python'
description: "Un caractère d'échappement est créé en tapant une barre oblique inverse \ suivie du caractère à insérer."
labUrl: 'https://labex.io/fr/labs/python-python-string-manipulation-633668?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Manipulation des Chaînes de Caractères
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## Caractères d'échappement

Un caractère d'échappement est créé en tapant une barre oblique inverse `\` suivie du caractère que vous souhaitez insérer.

| Caractère d'échappement | Affiche comme                  |
| ----------------------- | ------------------------------ |
| `\'`                    | Guillemet simple               |
| `\"`                    | Guillemet double               |
| `\t`                    | Tabulation                     |
| `\n`                    | Nouvelle ligne (saut de ligne) |
| `\\`                    | Barre oblique inverse          |
| `\b`                    | Retour arrière                 |
| `\ooo`                  | Valeur octale                  |
| `\r`                    | Retour chariot                 |

```python
# Caractères d'échappement : utiliser la barre oblique inverse pour insérer des caractères spéciaux
# \n = nouvelle ligne, \' = guillemet simple
print("Hello there!\nHow are you?\nI\'m doing fine.")
```

```output
Hello there!
How are you?
I'm doing fine.
```

## Chaînes brutes (Raw strings)

Une chaîne brute ignore entièrement tous les caractères d'échappement et affiche toute barre oblique inverse qui apparaît dans la chaîne.

```python
# Chaîne brute (préfixe r) : traite les barres obliques inverses comme des caractères littéraux
print(r"Hello there!\nHow are you?\nI\'m doing fine.")  # \n affiché littéralement
```

```output
Hello there!\nHow are you?\nI\'m doing fine.
```

Les chaînes brutes sont principalement utilisées pour la définition des <router-link to="/cheatsheet/regular-expressions">expressions régulières</router-link>.

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Que fait une chaîne brute (précédée de <code>r</code>) en Python ?
</template>

<base-quiz-option value="A">A. Convertit tous les caractères en majuscules</base-quiz-option>
<base-quiz-option value="B" correct>B. Traite les barres obliques inverses comme des caractères littéraux, ignorant les séquences d'échappement</base-quiz-option>
<base-quiz-option value="C">C. Supprime tous les espaces</base-quiz-option>
<base-quiz-option value="D">D. Inverse la chaîne</base-quiz-option>
<base-quiz-answer value="B">Les chaînes brutes (précédées de <code>r</code>) traitent les barres obliques inverses comme des caractères littéraux, de sorte que les séquences d'échappement telles que <code>\n</code> ne sont pas interprétées.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Chaînes multilignes

```python
print(
"""Dear Alice,

Eve's cat has been arrested for catnapping,
cat burglary, and extortion.

Sincerely,
Bob"""
)
```

```output
Dear Alice,

Eve's cat has been arrested for catnapping,
cat burglary, and extortion.

Sincerely,
Bob
```

## Indexation et découpage (Slicing) des chaînes

    H   e   l   l   o       w   o   r   l   d    !
    0   1   2   3   4   5   6   7   8   9   10   11

### Indexation

```python
# Indexation de chaîne : accéder aux caractères par position (base 0)
spam = 'Hello world!'

spam[0]  # Retourne le premier caractère : 'H'
```

```output
'H'
```

```python
spam[4]
```

```output
'o'
```

```python
spam[-1]
```

```output
'!'
```

### Découpage (Slicing)

```python
# Découpage de chaîne : extraire une sous-chaîne en utilisant la syntaxe [début:fin]
spam = 'Hello world!'

spam[0:5]  # Retourne les caractères de l'index 0 à 4 : 'Hello'
```

```output
'Hello'
```

```python
spam[:5]
```

```output
'Hello'
```

```python
spam[6:]
```

```output
'world!'
```

```python
spam[6:-1]
```

```output
'world'
```

```python
spam[:-1]
```

```output
'Hello world'
```

```python
spam[::-1]
```

```output
'!dlrow olleH'
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
Que fait <code>spam[::-1]</code> sur une chaîne ?
</template>

<base-quiz-option value="A">A. Retourne le premier caractère</base-quiz-option>
<base-quiz-option value="B">B. Retourne le dernier caractère</base-quiz-option>
<base-quiz-option value="C" correct>C. Inverse la chaîne</base-quiz-option>
<base-quiz-option value="D">D. Supprime tous les caractères</base-quiz-option>
<base-quiz-answer value="C">La tranche <code>[::-1]</code> inverse une chaîne en parcourant tous les caractères à rebours. La valeur de pas <code>-1</code> signifie "revenir en arrière".</base-quiz-answer>
</base-quiz-question>
</base-quiz>

```python
fizz = spam[0:5]
fizz
```

```output
'Hello'
```

## Les opérateurs in et not in

```python
'Hello' in 'Hello World'
```

```output
True
```

```python
'Hello' in 'Hello'
```

```output
True
```

```python
'HELLO' in 'Hello World'
```

```output
False
```

```python
'' in 'spam'
```

```output
True
```

```python
'cats' not in 'cats and dogs'
```

```output
False
```

## upper(), lower() et title()

Transforme une chaîne en majuscules, minuscules et en casse de titre :

```python
greet = 'Hello world!'
greet.upper()
```

```output
'HELLO WORLD!'
```

```python
greet.lower()
```

```output
'hello world!'
```

```python
greet.title()
```

```output
'Hello World!'
```

## Méthodes isupper() et islower()

Retourne `True` ou `False` après avoir évalué si une chaîne est en majuscules ou en minuscules :

```python
spam = 'Hello world!'
spam.islower()
```

```output
False
```

```python
spam.isupper()
```

```output
False
```

```python
'HELLO'.isupper()
```

```output
True
```

```python
'abc12345'.islower()
```

```output
True
```

```python
'12345'.islower()
```

```output
False
```

```python
'12345'.isupper()
```

```output
False
```

## Les méthodes isX des chaînes

| Méthode     | Description                                                                                                                    |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------ |
| isalpha()   | retourne `True` si la chaîne ne contient que des lettres.                                                                      |
| isalnum()   | retourne `True` si la chaîne ne contient que des lettres et des chiffres.                                                      |
| isdecimal() | retourne `True` si la chaîne ne contient que des nombres.                                                                      |
| isspace()   | retourne `True` si la chaîne ne contient que des espaces, des tabulations et des sauts de ligne.                               |
| istitle()   | retourne `True` si la chaîne ne contient que des mots commençant par une majuscule suivie uniquement de caractères minuscules. |

## startswith() et endswith()

```python
'Hello world!'.startswith('Hello')
```

```output
True
```

```python
'Hello world!'.endswith('world!')
```

```output
True
```

```python
'abc123'.startswith('abcdef')
```

```output
False
```

```python
'abc123'.endswith('12')
```

```output
False
```

```python
'Hello world!'.startswith('Hello world!')
```

```output
True
```

```python
'Hello world!'.endswith('Hello world!')
```

```output
True
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Que retourne <code>startswith()</code> ?
</template>

<base-quiz-option value="A" correct>A. <code>True</code> si la chaîne commence par la sous-chaîne spécifiée, <code>False</code> sinon</base-quiz-option>
<base-quiz-option value="B">B. La sous-chaîne qui correspond au début</base-quiz-option>
<base-quiz-option value="C">C. L'index où la sous-chaîne commence</base-quiz-option>
<base-quiz-option value="D">D. Une nouvelle chaîne sans le préfixe</base-quiz-option>
<base-quiz-answer value="A">La méthode <code>startswith()</code> retourne une valeur booléenne : <code>True</code> si la chaîne commence par la sous-chaîne spécifiée, <code>False</code> sinon.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## join() et split()

### join()

La méthode `join()` prend tous les éléments d'un itérable, comme une <router-link to="/cheatsheet/lists-and-tuples">liste</router-link>, un <router-link to="/cheatsheet/dictionaries">dictionnaire</router-link>, un <router-link to="/cheatsheet/lists-and-tuples#the-tuple-data-type">tuple</router-link> ou un <router-link to="/cheatsheet/sets">ensemble</router-link>, et les joint en une seule chaîne. Vous pouvez également spécifier un séparateur.

```python
''.join(['My', 'name', 'is', 'Simon'])
```

```output
'MynameisSimon'
```

```python
', '.join(['cats', 'rats', 'bats'])
```

```output
'cats, rats, bats'
```

```python
' '.join(['My', 'name', 'is', 'Simon'])
```

```output
'My name is Simon'
```

```python
'ABC'.join(['My', 'name', 'is', 'Simon'])
```

```output
'MyABCnameABCisABCSimon'
```

### split()

La méthode `split()` divise une `chaîne` en une `liste`. Par défaut, elle utilise les espaces pour séparer les éléments, mais vous pouvez également définir un autre caractère de votre choix :

```python
'My name is Simon'.split()
```

```output
['My', 'name', 'is', 'Simon']
```

```python
'MyABCnameABCisABCSimon'.split('ABC')
```

```output
['My', 'name', 'is', 'Simon']
```

```python
'My name is Simon'.split('m')
```

```output
['My na', 'e is Si', 'on']
```

```python
' My  name is  Simon'.split()
```

```output
['My', 'name', 'is', 'Simon']
```

```python
' My  name is  Simon'.split(' ')
```

```output
['', 'My', '', 'name', 'is', '', 'Simon']
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Que retourne <code>split()</code> lorsqu'il est appelé sur une chaîne ?
</template>

<base-quiz-option value="A">A. Une chaîne</base-quiz-option>
<base-quiz-option value="B" correct>B. Une liste de chaînes</base-quiz-option>
<base-quiz-option value="C">C. Un tuple de chaînes</base-quiz-option>
<base-quiz-option value="D">D. Un dictionnaire</base-quiz-option>
<base-quiz-answer value="B">La méthode <code>split()</code> divise une chaîne en une liste de sous-chaînes. Par défaut, elle divise sur les espaces, mais vous pouvez spécifier un séparateur différent.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Justification du texte avec rjust(), ljust() et center()

```python
'Hello'.rjust(10)
```

```output
'     Hello'
```

```python
'Hello'.rjust(20)
```

```output
'               Hello'
```

```python
'Hello World'.rjust(20)
```

```output
'         Hello World'
```

```python
'Hello'.ljust(10)
```

```output
'Hello     '
```

```python
'Hello'.center(20)
```

```output
'       Hello       '
```

Un deuxième argument optionnel pour `rjust()` et `ljust()` spécifiera un caractère de remplissage autre que l'espace :

```python
'Hello'.rjust(20, '*')
```

```output
'***************Hello'
```

```python
'Hello'.ljust(20, '-')
```

```output
'Hello---------------'
```

```python
'Hello'.center(20, '=')
```

```output
'=======Hello========'
```

## Suppression des espaces avec strip(), rstrip(), et lstrip()

```python
spam = '    Hello World     '
spam.strip()
```

```output
'Hello World'
```

```python
spam.lstrip()
```

```output
'Hello World     '
```

```python
spam.rstrip()
```

```output
'    Hello World'
```

```python
spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')
```

```output
'BaconSpamEggs'
```

## La méthode Count

Compte le nombre d'occurrences d'un caractère ou d'une sous-chaîne donnée dans la chaîne sur laquelle elle est appliquée. Peut recevoir optionnellement un index de début et de fin.

```python
sentence = 'one sheep two sheep three sheep four'
sentence.count('sheep')
```

```output
3
```

```python
sentence.count('e')
```

```output
9
```

```python
# retourne le compte de 'e' après 'one sh' i.e 6 caractères depuis le début de la chaîne
sentence.count('e', 6)
```

```output
8
```

```python
sentence.count('e', 7)
```

```output
7
```

## Méthode Replace

Remplace toutes les occurrences d'une sous-chaîne donnée par une autre sous-chaîne. Peut recevoir optionnellement un troisième argument pour limiter le nombre de remplacements. Retourne une nouvelle chaîne.

```python
text = "Hello, world!"
text.replace("world", "planet")
```

```output
'Hello, planet!'
```

```python
fruits = "apple, banana, cherry, apple"
fruits.replace("apple", "orange", 1)
```

```output
'orange, banana, cherry, apple'
```

```python
sentence = "I like apples, Apples are my favorite fruit"
sentence.replace("apples", "oranges")
```

```output
'I like oranges, Apples are my favorite fruit'
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
Que retourne la méthode <code>replace()</code> ?
</template>

<base-quiz-option value="A">A. Modifie la chaîne d'origine</base-quiz-option>
<base-quiz-option value="B">B. Retourne <code>None</code></base-quiz-option>
<base-quiz-option value="C" correct>C. Retourne une nouvelle chaîne avec les remplacements effectués</base-quiz-option>
<base-quiz-option value="D">D. Retourne une liste des chaînes remplacées</base-quiz-option>
<base-quiz-answer value="C">La méthode <code>replace()</code> retourne une nouvelle chaîne avec toutes les occurrences de l'ancienne sous-chaîne remplacées par la nouvelle sous-chaîne. La chaîne d'origine n'est pas modifiée.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Liens pertinents

- <router-link to="/builtin/format">format()</router-link>
- <router-link to="/builtin/len">len()</router-link>
- <router-link to="/builtin/str">str()</router-link>
- <router-link to="/builtin/repr">repr()</router-link>
- <router-link to="/builtin/input">input()</router-link>
- <router-link to="/cheatsheet/string-formatting">Formatage de Chaînes</router-link>
- <router-link to="/cheatsheet/regular-expressions">Expressions Régulières</router-link>
