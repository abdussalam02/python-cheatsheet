---
title: 'Bases Python - Aide-mémoire Python'
description: 'Apprenez les bases de Python avec notre guide complet couvrant les opérateurs, types de données, variables, fonctions et plus. Idéal pour les débutants en programmation Python.'
labUrl: 'https://labex.io/fr/labs/python-python-basics-633647?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Bases de Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Nous devons tous commencer quelque part, alors pourquoi ne pas commencer ici. Ce guide couvre les bases fondamentales de Python, y compris les opérateurs, les types de données, les variables et les fonctions de base.

<base-disclaimer>
<base-disclaimer-title>
Aperçu des bases de Python
</base-disclaimer-title>
<base-disclaimer-content>
Les bases fondamentales de Python que tout débutant devrait connaître :

- Variables et types de base
- Opérateurs et expressions
- Chaînes de caractères et méthodes courantes
- Listes, tuples et dictionnaires
- Flux de contrôle de base (if, for, while)
- Fonctions simples

</base-disclaimer-content>
</base-disclaimer>

## Opérateurs Mathématiques

De la précédence la **plus élevée** à la **plus basse** :

| Opérateurs | Opération        | Exemple         |
| ---------- | ---------------- | --------------- |
| \*\*       | Exposant         | `2 ** 3 = 8`    |
| %          | Modulo/Reste     | `22 % 8 = 6`    |
| //         | Division entière | `22 // 8 = 2`   |
| /          | Division         | `22 / 8 = 2.75` |
| \*         | Multiplication   | `3 * 3 = 9`     |
| -          | Soustraction     | `5 - 2 = 3`     |
| +          | Addition         | `2 + 2 = 4`     |

Exemples d'expressions :

```python
# La multiplication a une précédence plus élevée que l'addition
# Donc ceci est évalué comme : 2 + (3 * 6) = 2 + 18 = 20
2 + 3 * 6
```

```output
20
```

```python
# Les parenthèses remplacent la précédence des opérateurs
# Ceci est évalué comme : 5 * 6 = 30
(2 + 3) * 6
```

```output
30
```

```python
2 ** 8
```

```output
256
```

```python
23 // 7
```

```output
3
```

```python
23 % 7
```

```output
2
```

```python
(5 - 1) * ((7 + 1) / (3 - 1))
```

```output
16.0
```

<BaseQuiz id="cheatsheet-basics-1" correct="A">
<template #question>
Quel est le résultat de cette expression Python ?

```python
4 + 2 * 3
```

</template>

<BaseQuizOption value="A" correct>A. 10</BaseQuizOption>
<BaseQuizOption value="B">B. 18</BaseQuizOption>
<BaseQuizOption value="C">C. 12</BaseQuizOption>
<BaseQuizOption value="D">D. 20</BaseQuizOption>
<BaseQuizAnswer>La multiplication a une précédence plus élevée que l'addition, donc ceci est évalué comme : 4 + (2 \* 3) = 4 + 6 = 10</BaseQuizAnswer>
</BaseQuiz>

## Opérateurs d'Affectation Augmentée

| Opérateur   | Équivalent       |
| ----------- | ---------------- |
| `var += 1`  | `var = var + 1`  |
| `var -= 1`  | `var = var - 1`  |
| `var *= 1`  | `var = var * 1`  |
| `var /= 1`  | `var = var / 1`  |
| `var //= 1` | `var = var // 1` |
| `var %= 1`  | `var = var % 1`  |
| `var **= 1` | `var = var ** 1` |

Exemples :

```python
# Affectation augmentée : équivalent à greeting = greeting + ' world!'
greeting = 'Hello'
greeting += ' world!'
greeting
```

```output
'Hello world!'
```

```python
# Incrémenter un nombre de 1
number = 1
number += 1
number
```

```output
2
```

```python
# Répliquer les éléments d'une liste : équivalent à my_list = my_list * 3
my_list = ['item']
my_list *= 3
my_list
```

```output
['item', 'item', 'item']
```

<BaseQuiz id="cheatsheet-basics-2" correct="B">
<template #question>
Quelle est la valeur de <code>x</code> après l'exécution de ce code ?

```python
x = 5
x += 3
```

</template>

<BaseQuizOption value="A">A. 3</BaseQuizOption>
<BaseQuizOption value="B" correct>B. 8</BaseQuizOption>
<BaseQuizOption value="C">C. 5</BaseQuizOption>
<BaseQuizOption value="D">D. 15</BaseQuizOption>
<BaseQuizAnswer>L'opérateur d'affectation augmentée <code>+=</code> est équivalent à <code>x = x + 3</code>. Donc <code>x</code> commence à 5, puis devient 5 + 3 = 8.</BaseQuizAnswer>
</BaseQuiz>

## Opérateur Walrus

L'opérateur Walrus permet l'affectation de variables au sein d'une expression tout en retournant la valeur de la variable

Exemple :

```python
# L'opérateur Walrus affecte et retourne la valeur en une seule expression
# my_var reçoit "Hello World!" puis est affiché
print(my_var:="Hello World!")
```

```output
Hello World!
```

```python
my_var="Yes"
print(my_var)
```

```output
Yes
```

```python
print(my_var:="Hello")
```

```output
Hello
```

L'opérateur _Walrus_, ou **Opérateur d'Expression d'Affectation**, a été introduit pour la première fois en 2018 via la [PEP 572](https://peps.python.org/pep-0572/), puis officiellement publié avec **Python 3.8** en octobre 2019.

<base-disclaimer>
  <base-disclaimer-title>
    Sémantique de la Syntaxe & Exemples
  </base-disclaimer-title>
  <base-disclaimer-content>
  La <a href="https://peps.python.org/pep-0572/" target="_blank">PEP 572</a> fournit la syntaxe, la sémantique et des exemples pour l'opérateur Walrus.
  </base-disclaimer-content>
</base-disclaimer>

## Types de Données

Comprendre les types de données est l'une des bases les plus importantes de Python. Python possède neuf types de données intégrés principaux qui couvrent presque tout ce dont vous aurez besoin :

| Type de Donnée                                             | Exemples                                 | Description                                  |
| ---------------------------------------------------------- | ---------------------------------------- | -------------------------------------------- |
| **Nombres**                                                |                                          |                                              |
| <router-link to='/builtin/int'>`int`</router-link>         | `-2, -1, 0, 1, 2, 3, 4, 5`               | Nombres entiers (entiers)                    |
| <router-link to='/builtin/float'>`float`</router-link>     | `-1.25, -1.0, -0.5, 0.0, 0.5, 1.0, 1.25` | Nombres avec des points décimaux             |
| <router-link to='/builtin/complex'>`complex`</router-link> | `2+3j, complex(1, 4)`                    | Nombres avec parties réelle et imaginaire    |
| **Texte**                                                  |                                          |                                              |
| <router-link to='/builtin/str'>`str`</router-link>         | `'a', 'Hello!', "Python"`                | Texte et caractères                          |
| **Booléen**                                                |                                          |                                              |
| <router-link to='/builtin/bool'>`bool`</router-link>       | `True, False`                            | Valeurs Vrai ou Faux                         |
| **None**                                                   |                                          |                                              |
| `NoneType`                                                 | `None`                                   | Représente "aucune valeur" ou "rien"         |
| **Collections**                                            |                                          |                                              |
| <router-link to='/builtin/list'>`list`</router-link>       | `[1, 2, 3], ['a', 'b', 'c']`             | Collections ordonnées et modifiables         |
| <router-link to='/builtin/dict'>`dict`</router-link>       | `{'name': 'Alice', 'age': 30}`           | Paires clé-valeur                            |
| <router-link to='/builtin/tuple'>`tuple`</router-link>     | `(1, 2, 3), ('a', 'b')`                  | Collections ordonnées et immuables           |
| <router-link to='/builtin/set'>`set`</router-link>         | `{1, 2, 3}, {'a', 'b', 'c'}`             | Collections non ordonnées d'éléments uniques |

### Exemples Rapides

```python
# Nombres
age = 25                    # int
price = 19.99              # float
coordinate = 2 + 3j        # complex

# Texte
name = "Alice"             # str

# Booléen
is_student = True          # bool

# None
result = None              # NoneType

# Collections
scores = [85, 92, 78]      # list
person = {'name': 'Bob', 'age': 30}  # dict
coordinates = (10, 20)     # tuple
unique_ids = {1, 2, 3}     # set
```

Pour un guide complet avec des exemples visuels et des explications détaillées sur quand utiliser chaque type, consultez : <router-link to="/blog/python-data-types">Types de Données Python : Un Guide Visuel pour Débutants</router-link>.

## Concaténation et Réplication

Concaténation de chaînes de caractères :

```python
# Concaténation de chaînes : les chaînes adjacentes sont automatiquement jointes
'Alice' 'Bob'
```

```output
'AliceBob'
```

Réplication de chaînes de caractères :

```python
# Réplication de chaînes : répéter la chaîne plusieurs fois
'Alice' * 5
```

```output
'AliceAliceAliceAliceAlice'
```

## Variables

Les variables sont un élément fondamental des bases de Python. Vous pouvez nommer une variable comme vous le souhaitez tant qu'elle respecte les règles suivantes :

1. Elle ne peut être qu'un seul mot.

```python
# mauvais
my variable = 'Hello'

# bon
var = 'Hello'
```

2. Elle ne peut utiliser que des lettres, des chiffres et le caractère de soulignement (`_`).

```python
# mauvais
%$@variable = 'Hello'

# bon
my_var = 'Hello'

# bon
my_var_2 = 'Hello'
```

3. Elle ne peut pas commencer par un chiffre.

```python
# ceci ne fonctionnera pas
23_var = 'hello'
```

4. Un nom de variable commençant par un trait de soulignement (`_`) est considéré comme "non utile".

```python
# _spam ne doit pas être réutilisé dans le code
_spam = 'Hello'
```

<BaseQuiz id="cheatsheet-basics-3" correct="C">
<template #question>
Dans les bases de Python, lequel des éléments suivants est un nom de variable valide ?
</template>

<BaseQuizOption value="A">A. <code>3value</code></BaseQuizOption>
<BaseQuizOption value="B">B. <code>user-name</code></BaseQuizOption>
<BaseQuizOption value="C" correct>C. <code>user_name</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>for</code></BaseQuizOption>
<BaseQuizAnswer><code>user_name</code> est un nom de variable valide car il n'utilise que des lettres, des chiffres et des traits de soulignement, et ne commence pas par un chiffre.</BaseQuizAnswer>
</BaseQuiz>

## Commentaires

Commentaire en ligne :

```python
# Ceci est un commentaire
```

Commentaire multiligne :

```python
# Ceci est un
# commentaire multiligne
```

Code avec un commentaire :

```python
a = 1  # initialisation
```

Veuillez noter les deux espaces devant le commentaire.

Docstring de fonction :

```python
def foo():
    """
    Ceci est un docstring de fonction
    Vous pouvez aussi utiliser :
    ''' Docstring de fonction '''
    """
```

## La Fonction print()

La fonction `print()` est l'une des premières bases de Python que vous apprendrez. Elle écrit la valeur de l'argument(s) qu'on lui donne. [...] elle gère les arguments multiples, les quantités à virgule flottante et les chaînes de caractères. Les chaînes sont imprimées sans guillemets, et un espace est inséré entre les éléments, vous pouvez donc formater joliment :

```python
print('Hello world!')
```

```output
Hello world!
```

```python
a = 1
print('Hello world!', a)
```

```output
Hello world! 1
```

### Le mot-clé end

L'argument mot-clé `end` peut être utilisé pour éviter le saut de ligne après la sortie, ou pour terminer la sortie avec une chaîne différente :

```python
# Utiliser le paramètre end pour changer ce qui suit chaque instruction print
phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
for word in phrase:
    print(word, end='-')  # Utiliser '-' au lieu d'un saut de ligne
```

```output
printed-with-a-dash-in-between-
```

### Le mot-clé sep

Le mot-clé `sep` spécifie comment séparer les objets, s'il y en a plus d'un :

```python
# Utiliser le paramètre sep pour spécifier le séparateur entre plusieurs arguments
print('cats', 'dogs', 'mice', sep=',')  # Sortie séparée par des virgules
```

```output
cats,dogs,mice
```

## La Fonction input()

Cette fonction prend l'entrée de l'utilisateur et la convertit en une chaîne de caractères :

```python
# input() lit l'entrée utilisateur et la retourne comme une chaîne
print('What is your name?')   # demander leur nom
my_name = input()  # Attendre que l'utilisateur tape et appuie sur Entrée
print('Hi, {}'.format(my_name))
```

```output
What is your name?
Martha
Hi, Martha
```

`input()` peut également définir un message par défaut sans utiliser `print()` :

```python
my_name = input('What is your name? ')  # message par défaut
print('Hi, {}'.format(my_name))
```

```output
What is your name? Martha
Hi, Martha
```

Il est également possible d'utiliser des chaînes formatées pour éviter d'utiliser .format :

```python
# input() peut afficher un message d'invite directement
my_name = input('What is your name? ')  # Invite et lecture en un seul appel
print(f'Hi, {my_name}')  # f-string pour le formatage de chaîne
```

```output
What is your name? Martha
Hi, Martha
```

<BaseQuiz id="cheatsheet-basics-4" correct="B">
<template #question>
Dans les bases de Python, quel type retourne `input()` ?
</template>

<BaseQuizOption value="A">A. int</BaseQuizOption>
<BaseQuizOption value="B" correct>B. str</BaseQuizOption>
<BaseQuizOption value="C">C. float</BaseQuizOption>
<BaseQuizOption value="D">D. Dépend de l'entrée de l'utilisateur</BaseQuizOption>
<BaseQuizAnswer>La fonction <code>input()</code> retourne toujours une chaîne de caractères, quel que soit ce que l'utilisateur tape. Vous devez la convertir à d'autres types si nécessaire.</BaseQuizAnswer>
</BaseQuiz>

## La Fonction len()

Évalue au nombre entier de caractères dans une chaîne, une liste, un dictionnaire, etc. :

```python
# len() retourne le nombre de caractères dans une chaîne
len('hello')  # Retourne 5
```

```output
5
```

```python
# len() retourne le nombre d'éléments dans une liste
len(['cat', 3, 'dog'])  # Retourne 3 (trois éléments)
```

```output
3
```

<base-warning>
  <base-warning-title>Test de vacuité</base-warning-title>
  <base-warning-content>
    Le test de vacuité des chaînes, listes, dictionnaires, etc., ne devrait pas utiliser
    <code>len</code>, mais préférer l'évaluation booléenne directe.
  </base-warning-content>
</base-warning>

Exemple de test de vacuité :

```python
a = [1, 2, 3]

# mauvais : vérification len() inutile
if len(a) > 0:  # s'évalue à True
    print("the list is not empty!")
```

```output
the list is not empty!
```

```python
# bon : évaluation booléenne directe (manière Pythonique)
if a:  # s'évalue à True si la liste n'est pas vide
    print("the list is not empty!")
```

```output
the list is not empty!
```

## Les Fonctions str(), int(), et float()

Ces fonctions vous permettent de changer le type d'une variable. Par exemple, vous pouvez transformer un `entier` ou un `float` en une `chaîne de caractères` :

```python
# Convertir un entier en chaîne
str(29)  # Retourne '29'
```

```output
'29'
```

```python
str(-3.14)
```

```output
'-3.14'
```

Ou d'une `chaîne de caractères` à un `entier` ou un `float` :

```python
# Convertir une chaîne en entier
int('11')  # Retourne 11
```

```output
11
```

```python
# Convertir une chaîne en float
float('3.14')  # Retourne 3.14
```

```output
3.14
```

<BaseQuiz id="cheatsheet-basics-5" correct="C">
<template #question>
Quel est le résultat de ce code Python ?

```python
result = int('42')
type(result)
```

</template>

<BaseQuizOption value="A">A. <code>str</code></BaseQuizOption>
<BaseQuizOption value="B">B. <code>float</code></BaseQuizOption>
<BaseQuizOption value="C" correct>C. <code>int</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>NoneType</code></BaseQuizOption>
<BaseQuizAnswer>La fonction <code>int()</code> convertit une chaîne en un entier. Donc <code>int('42')</code> retourne l'entier <code>42</code>, et <code>type(42)</code> retourne <code>int</code>.</BaseQuizAnswer>
</BaseQuiz>

## Liens Pertinents

- <router-link to="/blog/python-data-types">Types de Données Python : Un Guide Visuel pour Débutants</router-link>
- <router-link to="/blog/python-comprehensions-step-by-step">Compréhensions Python Étape par Étape</router-link>
- <router-link to="/cheatsheet/control-flow">Flux de Contrôle</router-link>
- <router-link to="/cheatsheet/functions">Fonctions</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Listes et Tuples</router-link>
- <router-link to="/cheatsheet/dictionaries">Dictionnaires</router-link>
- <router-link to="/cheatsheet/sets">Ensembles (Sets)</router-link>
- <router-link to="/cheatsheet/string-formatting">Formatage de Chaînes de Caractères</router-link>
