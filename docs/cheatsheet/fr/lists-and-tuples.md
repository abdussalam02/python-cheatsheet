---
title: 'Listes et Tuples Python - Aide-mémoire Python'
description: "En Python, les listes sont l'un des 4 types de données utilisés pour stocker des collections d'informations."
labUrl: 'https://labex.io/fr/labs/python-python-lists-and-tuples-633660?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Listes Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Les listes sont l'un des 4 types de données en Python utilisés pour stocker des collections de données.

```python
# List: collection ordonnée d'éléments entre crochets
['John', 'Peter', 'Debora', 'Charles']
```

## Obtenir des valeurs avec des index

```python
# Accéder aux éléments de la liste en utilisant l'index (base 0, le premier élément est à l'index 0)
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[0]  # Retourne le premier élément : 'table'
```

```output
'table'
```

```python
furniture[1]
```

```output
'chair'
```

```python
furniture[2]
```

```output
'rack'
```

```python
furniture[3]
```

```output
'shelf'
```

## Index négatifs

```python
# Index négatif : accéder aux éléments depuis la fin de la liste
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[-1]  # Retourne le dernier élément : 'shelf'
```

```output
'shelf'
```

```python
furniture[-3]
```

```output
'chair'
```

```python
f'The {furniture[-1]} is bigger than the {furniture[-3]}'
```

```output
'The shelf is bigger than the chair'
```

<BaseQuiz id="cheatsheet-lists-and-tuples-1" correct="B">
<template #question>
Que retourne <code>furniture[-1]</code> si <code>furniture = ['table', 'chair', 'rack', 'shelf']</code> ?
</template>

<BaseQuizOption value="A">A. <code>'table'</code></BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>'shelf'</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>['shelf']</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>IndexError</code></BaseQuizOption>
<BaseQuizAnswer>Les index négatifs accèdent aux éléments depuis la fin de la liste. <code>-1</code> fait référence au dernier élément, <code>-2</code> à l'avant-dernier, et ainsi de suite.</BaseQuizAnswer>
</BaseQuiz>

## Obtenir des sous-listes avec des Slices

```python
# Slicing : obtenir une sous-liste en utilisant la syntaxe [début:fin] (fin est exclusive)
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[0:4]  # Retourne les éléments de l'index 0 à 3 (4 exclu)
```

```output
['table', 'chair', 'rack', 'shelf']
```

```python
furniture[1:3]
```

```output
['chair', 'rack']
```

```python
furniture[0:-1]
```

```output
['table', 'chair', 'rack']
```

```python
# Slice depuis le début : omettre l'index de début (par défaut à 0)
furniture[:2]  # Retourne les deux premiers éléments
```

```output
['table', 'chair']
```

```python
# Slice jusqu'à la fin : omettre l'index de fin (par défaut jusqu'à la fin de la liste)
furniture[1:]  # Retourne tous les éléments de l'index 1 jusqu'à la fin
```

```output
['chair', 'rack', 'shelf']
```

```python
furniture[:]
```

```output
['table', 'chair', 'rack', 'shelf']
```

Le slicing de la liste complète effectuera une copie :

```python
# Le slicing crée une copie : [:] crée une copie superficielle (shallow copy) de la liste
spam = ['cat', 'bat', 'rat', 'elephant']
spam2 = spam[:]  # Créer une copie, pas une référence
spam2
```

```output
['cat', 'bat', 'rat', 'elephant']
```

```python
spam.append('dog')
spam
```

```output
['cat', 'bat', 'rat', 'elephant', 'dog']
```

```python
spam2
```

```output
['cat', 'bat', 'rat', 'elephant']
```

<BaseQuiz id="cheatsheet-lists-and-tuples-2" correct="C">
<template #question>
Que crée <code>spam[:]</code> lorsqu'il est appliqué à une liste <code>spam</code> ?
</template>

<BaseQuizOption value="A">A. Une référence à la même liste</BaseQuizOption>
<BaseQuizOption value="B">B. Une liste vide</BaseQuizOption>
<BaseQuizOption value="C" correct>C. Une copie superficielle de la liste</BaseQuizOption>
<BaseQuizOption value="D">D. Une liste inversée</BaseQuizOption>
<BaseQuizAnswer>Le slicing de la liste complète avec <code>[:]</code> crée une copie superficielle. Modifier la copie n'affectera pas la liste originale.</BaseQuizAnswer>
</BaseQuiz>

## Obtenir la longueur d'une liste avec len()

```python
# len() retourne le nombre d'éléments dans une liste
furniture = ['table', 'chair', 'rack', 'shelf']
len(furniture)  # Retourne 4
```

```output
4
```

## Modifier des valeurs avec des index

```python
# Modifier les éléments de la liste en assignant de nouvelles valeurs aux index
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[0] = 'desk'  # Remplacer le premier élément
furniture
```

```output
['desk', 'chair', 'rack', 'shelf']
```

```python
furniture[2] = furniture[1]
furniture
```

```output
['desk', 'chair', 'chair', 'shelf']
```

```python
furniture[-1] = 'bed'
furniture
```

```output
['desk', 'chair', 'chair', 'bed']
```

## Concaténation et Répétition

```python
# Concaténation de listes : combiner deux listes en utilisant l'opérateur +
[1, 2, 3] + ['A', 'B', 'C']  # Retourne [1, 2, 3, 'A', 'B', 'C']
```

```output
[1, 2, 3, 'A', 'B', 'C']
```

```python
# Répétition de liste : répéter la liste plusieurs fois en utilisant l'opérateur *
['X', 'Y', 'Z'] * 3  # Retourne ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
```

```output
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
```

```python
my_list = [1, 2, 3]
my_list = my_list + ['A', 'B', 'C']
my_list
```

```output
[1, 2, 3, 'A', 'B', 'C']
```

## Utilisation de boucles for avec des Listes

```python
# Itérer sur les éléments de la liste en utilisant une boucle for
furniture = ['table', 'chair', 'rack', 'shelf']

for item in furniture:  # Boucler sur chaque élément
    print(item)
```

```output
table
chair
rack
shelf
```

## Obtenir l'index dans une boucle avec enumerate()

```python
# enumerate() retourne à la fois l'index et la valeur dans une boucle
furniture = ['table', 'chair', 'rack', 'shelf']

for index, item in enumerate(furniture):  # Obtenir l'index et l'élément ensemble
    print(f'index: {index} - item: {item}')
```

```output
index: 0 - item: table
index: 1 - item: chair
index: 2 - item: rack
index: 3 - item: shelf
```

## Boucler sur plusieurs listes avec zip()

```python
# zip() combine plusieurs listes élément par élément dans une boucle
furniture = ['table', 'chair', 'rack', 'shelf']
price = [100, 50, 80, 40]

for item, amount in zip(furniture, price):  # Associer les éléments des deux listes
    print(f'The {item} costs ${amount}')
```

```output
The table costs $100
The chair costs $50
The rack costs $80
The shelf costs $40
```

## Les opérateurs in et not in

```python
# Opérateur in : vérifier si un élément existe dans une liste
'rack' in ['table', 'chair', 'rack', 'shelf']  # Retourne True
```

```output
True
```

```python
'bed' in ['table', 'chair', 'rack', 'shelf']
```

```output
False
```

```python
furniture = ['table', 'chair', 'rack', 'shelf']
'bed' not in furniture
```

```output
True
```

```python
'rack' not in furniture
```

```output
False
```

## L'astuce de l'affectation multiple

L'astuce de l'affectation multiple est un raccourci qui vous permet d'assigner plusieurs variables avec les valeurs d'une liste en une seule ligne de code. Donc au lieu de faire ceci :

```python
furniture = ['table', 'chair', 'rack', 'shelf']
table = furniture[0]
chair = furniture[1]
rack = furniture[2]
shelf = furniture[3]
```

Vous pourriez taper cette ligne de code :

```python
furniture = ['table', 'chair', 'rack', 'shelf']
table, chair, rack, shelf = furniture

table
```

```output
'table'
```

```python
chair
```

```output
'chair'
```

```python
rack
```

```output
'rack'
```

```python
shelf
```

```output
'shelf'
```

L'astuce de l'affectation multiple peut également être utilisée pour échanger les valeurs de deux variables :

```python
a, b = 'table', 'chair'
a, b = b, a
print(a)
```

```output
chair
```

```python
print(b)
```

```output
table
```

## La méthode index

La méthode `index` vous permet de trouver l'index d'une valeur en passant son nom :

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.index('chair')
```

```output
1
```

## Ajouter des Valeurs

### append()

`append` ajoute un élément à la fin d'une `list` :

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.append('bed')
furniture
```

```output
['table', 'chair', 'rack', 'shelf', 'bed']
```

<BaseQuiz id="cheatsheet-lists-and-tuples-3" correct="A">
<template #question>
Que fait la méthode <code>append()</code> sur une liste ?
</template>

<BaseQuizOption value="A" correct>A. Ajoute un élément à la fin de la liste</BaseQuizOption>
<BaseQuizOption value="B">B. Ajoute un élément au début de la liste</BaseQuizOption>
<BaseQuizOption value="C">C. Remplace le dernier élément</BaseQuizOption>
<BaseQuizOption value="D">D. Supprime le dernier élément</BaseQuizOption>
<BaseQuizAnswer>La méthode <code>append()</code> ajoute un seul élément à la fin d'une liste. Pour ajouter un élément à une position spécifique, utilisez <code>insert()</code>.</BaseQuizAnswer>
</BaseQuiz>

### insert()

`insert` ajoute un élément à une `list` à une position donnée :

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.insert(1, 'bed')
furniture
```

```output
['table', 'bed', 'chair', 'rack', 'shelf']
```

## Supprimer des Valeurs

### del

`del` supprime un élément en utilisant l'index :

```python
furniture = ['table', 'chair', 'rack', 'shelf']
del furniture[2]
furniture
```

```output
['table', 'chair', 'shelf']
```

```python
del furniture[2]
furniture
```

```output
['table', 'chair']
```

### remove()

`remove` supprime un élément en utilisant sa valeur réelle :

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.remove('chair')
furniture
```

```output
['table', 'rack', 'shelf']
```

<base-warning>
  <base-warning-title>
    Supprimer des éléments répétés
  </base-warning-title>
  <base-warning-content>
    Si la valeur apparaît plusieurs fois dans la liste, seule la première occurrence de la valeur sera supprimée.
  </base-warning-content>
</base-warning>

### pop()

Par défaut, `pop` supprime et retourne le dernier élément de la liste. Vous pouvez également passer l'index de l'élément comme paramètre optionnel :

```python
animals = ['cat', 'bat', 'rat', 'elephant']

animals.pop()
```

```output
'elephant'
```

```python
animals
```

```output
['cat', 'bat', 'rat']
```

```python
animals.pop(0)
```

```output
'cat'
```

```python
animals
```

```output
['bat', 'rat']
```

<BaseQuiz id="cheatsheet-lists-and-tuples-4" correct="B">
<template #question>
Que fait <code>pop()</code> lorsqu'il est appelé sur une liste ?
</template>

<BaseQuizOption value="A">A. Supprime uniquement le dernier élément</BaseQuizOption>
<BaseQuizOption value="B" correct>B. Supprime et retourne un élément (le dernier élément par défaut, ou l'index spécifié)</BaseQuizOption>
<BaseQuizOption value="C">C. Retourne uniquement le dernier élément sans le supprimer</BaseQuizOption>
<BaseQuizOption value="D">D. Supprime tous les éléments de la liste</BaseQuizOption>
<BaseQuizAnswer>La méthode <code>pop()</code> supprime et retourne un élément. Par défaut, elle supprime le dernier élément, mais vous pouvez passer un index pour supprimer un élément spécifique.</BaseQuizAnswer>
</BaseQuiz>

## Trier les valeurs avec sort()

```python
numbers = [2, 5, 3.14, 1, -7]
numbers.sort()
numbers
```

```output
[-7, 1, 2, 3.14, 5]
```

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.sort()
furniture
```

```output
['chair', 'rack', 'shelf', 'table']
```

Vous pouvez également passer `True` pour l'argument mot-clé `reverse` pour que `sort()` trie les valeurs dans l'ordre inverse :

```python
furniture.sort(reverse=True)
furniture
```

```output
['table', 'shelf', 'rack', 'chair']
```

Si vous avez besoin de trier les valeurs dans l'ordre alphabétique normal, passez `str.lower` pour l'argument mot-clé `key` dans l'appel de la méthode sort() :

```python
letters = ['a', 'z', 'A', 'Z']
letters.sort(key=str.lower)
letters
```

```output
['a', 'A', 'z', 'Z']
```

Vous pouvez utiliser la fonction intégrée `sorted` pour retourner une nouvelle liste :

```python
furniture = ['table', 'chair', 'rack', 'shelf']
sorted(furniture)
```

```output
['chair', 'rack', 'shelf', 'base-title']
```

## Le type de données Tuple

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://stackoverflow.com/questions/1708510/list-vs-tuple-when-to-use-each">Tuples vs Listes</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    La différence clé entre les tuples et les listes est que, tandis que les <code>tuples</code> sont des objets <i>immuables</i>, les <code>listes</code> sont <i>mutables</i>. Cela signifie que les tuples ne peuvent pas être modifiés alors que les listes peuvent être modifiées. Les tuples sont plus économes en mémoire que les listes.
  </base-disclaimer-content>
</base-disclaimer>

```python
furniture = ('table', 'chair', 'rack', 'shelf')

furniture[0]
```

```output
'table'
```

```python
furniture[1:3]
```

```output
('chair', 'rack')
```

```python
len(furniture)
```

```output
4
```

La principale façon dont les tuples diffèrent des listes est que les tuples, comme les chaînes de caractères, sont immuables.

## Conversion entre list() et tuple()

```python
tuple(['cat', 'dog', 5])
```

```output
('cat', 'dog', 5)
```

```python
list(('cat', 'dog', 5))
```

```output
['cat', 'dog', 5]
```

```python
list('hello')
```

```output
['h', 'e', 'l', 'l', 'o']
```

<BaseQuiz id="cheatsheet-lists-and-tuples-5" correct="C">
<template #question>
Quelle est la principale différence entre les listes et les tuples en Python ?
</template>

<BaseQuizOption value="A">A. Les listes ne peuvent contenir que des nombres, les tuples peuvent contenir n'importe quoi</BaseQuizOption>
<BaseQuizOption value="B">B. Les tuples sont plus rapides à créer</BaseQuizOption>
<BaseQuizOption value="C" correct>C. Les listes sont mutables (peuvent être modifiées), les tuples sont immuables (ne peuvent pas être modifiés)</BaseQuizOption>
<BaseQuizOption value="D">D. Les listes utilisent des crochets, les tuples utilisent des accolades</BaseQuizOption>
<BaseQuizAnswer>Les listes sont mutables, ce qui signifie que vous pouvez les modifier après leur création. Les tuples sont immuables, ce qui signifie qu'une fois créés, ils ne peuvent pas être modifiés. Les deux peuvent contenir n'importe quel type de données.</BaseQuizAnswer>
</BaseQuiz>

## Liens pertinents

- <router-link to="/blog/python-data-types">Python Data Types: A Visual Guide for Beginners</router-link>
- <router-link to="/blog/python-comprehensions-step-by-step">Python Comprehensions Step-by-Step</router-link>
- <router-link to="/cheatsheet/comprehensions">Python Comprehensions</router-link>
- <router-link to="/modules/itertools-module">The itertools Module</router-link>
- <router-link to="/builtin/list">list()</router-link>
- <router-link to="/builtin/tuple">tuple()</router-link>
- <router-link to="/builtin/len">len()</router-link>
