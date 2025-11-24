---
title: 'Lecture et écriture de fichiers - Aide-mémoire Python'
description: "Pour lire ou écrire dans un fichier en Python, utilisez l'instruction 'with', qui fermera le fichier automatiquement, gérant ainsi les ressources pour vous."
labUrl: 'https://labex.io/fr/labs/python-python-reading-and-writing-files-633663?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Lecture et Écriture de Fichiers
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Pour un examen plus approfondi de la manipulation des chemins de fichiers et de répertoires, consultez la page <router-link to="/cheatsheet/file-directory-path">Chemins de Fichiers et de Répertoires</router-link>.

## Le processus de lecture/écriture de fichiers

Pour lire/écrire dans un fichier en Python, vous voudrez utiliser l'instruction `with`, qui fermera le fichier pour vous une fois terminé, gérant les ressources disponibles pour vous.

## Ouverture et lecture de fichiers

La fonction `open` ouvre un fichier et retourne un objet fichier correspondant.

```python
# Lire le fichier en utilisant l'instruction 'with': ferme automatiquement le fichier une fois terminé
with open('/home/labex/project/hi.txt') as hello_file:
    hello_content = hello_file.read()  # Lire tout le contenu du fichier

hello_content
```

```output
'Hello World!'
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Quel est l'avantage principal d'utiliser l'instruction <code>with</code> lors de l'ouverture de fichiers ?
</template>

<base-quiz-option value="A" correct>A. Le fichier est automatiquement fermé une fois terminé, même si une erreur se produit</base-quiz-option>
<base-quiz-option value="B">B. Les fichiers s'ouvrent plus rapidement</base-quiz-option>
<base-quiz-option value="C">C. Les fichiers peuvent être ouverts en mode lecture et écriture simultanément</base-quiz-option>
<base-quiz-option value="D">D. Les fichiers sont automatiquement compressés</base-quiz-option>
<base-quiz-answer value="A">L'instruction <code>with</code> garantit que le fichier est automatiquement fermé lorsque le bloc se termine, même si une exception se produit. Cela aide à gérer correctement les ressources.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Alternativement, vous pouvez utiliser la méthode _readlines()_ pour obtenir une liste de valeurs de chaînes de caractères à partir du fichier, une chaîne pour chaque ligne de texte :

```python
# readlines() méthode: retourne une liste de chaînes, une par ligne
with open('sonnet29.txt') as sonnet_file:
    sonnet_file.readlines()  # Retourne une liste avec chaque ligne comme une chaîne
```

```output
['When, in disgrace with fortune and men's eyes,\n',
 ' I all alone beweep my  outcast state,\n',
 "And trouble deaf heaven with my bootless cries,\n",
 "And look upon myself and curse my fate,']
```

Vous pouvez également itérer sur le fichier ligne par ligne :

```python
# Itérer sur le fichier ligne par ligne (efficace en mémoire pour les grands fichiers)
with open('sonnet29.txt') as sonnet_file:
    for line in sonnet_file:  # L'objet fichier est itérable
        print(line, end='')  # Imprimer sans saut de ligne supplémentaire
```

```output
When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,
```

## Écriture dans des fichiers

```python
# Écrire dans un fichier: le mode 'w' écrase le fichier existant
with open('bacon.txt', 'w') as bacon_file:  # 'w' = mode écriture
    bacon_file.write('Hello world!\n')  # Retourne le nombre de caractères écrits
```

```output
13
```

```python
# Ajouter à un fichier: le mode 'a' ajoute au fichier existant
with open('bacon.txt', 'a') as bacon_file:  # 'a' = mode ajout
    bacon_file.write('Bacon is not a vegetable.')
```

```output
25
```

```python
with open('bacon.txt') as bacon_file:
    content = bacon_file.read()

print(content)
```

```output
Hello world!
Bacon is not a vegetable.
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Quelle est la différence entre ouvrir un fichier avec le mode <code>'w'</code> et le mode <code>'a'</code> ?
</template>

<base-quiz-option value="A">A. <code>'w'</code> est pour la lecture, <code>'a'</code> est pour l'écriture</base-quiz-option>
<base-quiz-option value="B" correct>B. <code>'w'</code> écrase le fichier, <code>'a'</code> ajoute au fichier</base-quiz-option>
<base-quiz-option value="C">C. <code>'w'</code> est pour Windows, <code>'a'</code> est pour Apple</base-quiz-option>
<base-quiz-option value="D">D. Il n'y a pas de différence</base-quiz-option>
<base-quiz-answer value="B">Le mode <code>'w'</code> ouvre le fichier en écriture et écrase tout contenu existant. Le mode <code>'a'</code> ouvre le fichier pour l'ajout, ajoutant du nouveau contenu à la fin du fichier.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Liens pertinents

- <router-link to="/cheatsheet/file-directory-path">Chemins de Fichiers et de Répertoires</router-link>
- <router-link to="/cheatsheet/json-yaml">JSON et YAML</router-link>
- <router-link to="/blog/python-pathlib-essentials">10 Opérations Essentielles du Système de Fichiers que Tout Développeur Devrait Connaître</router-link>
- <router-link to="/builtin/open">open()</router-link>
- <router-link to="/builtin/print">print()</router-link>
