---
title: 'Fonction Principale Python - Fiche de Référence Python'
description: "Nom du scope où le code de haut niveau s'exécute. Le nom d'un module est défini sur main lors de la lecture depuis l'entrée standard, un script ou une invite interactive."
labUrl: 'https://labex.io/fr/labs/python-python-main-function-633661?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Environnement de script de haut niveau principal
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## Qu'est-ce que c'est

`__main__` est le nom de la portée dans laquelle le code de haut niveau s'exécute.
Le **nom** d'un module est défini égal à `__main__` lorsqu'il est lu depuis l'entrée standard, un script ou une invite interactive.

Un module peut découvrir s'il s'exécute dans la portée principale en vérifiant son propre `__name__`, ce qui permet une idiome courante pour exécuter conditionnellement du code dans un module. Lorsqu'il est exécuté comme un script ou avec `python -m` mais pas lorsqu'il est importé :

```python
# __name__ == "__main__": vérifier si le script est exécuté directement (non importé)
if __name__ == "__main__":  # Vrai lors de l'exécution comme script, Faux lors de l'importation
    # exécuter uniquement si exécuté comme script
    main()
```

Pour un paquet, le même effet peut être obtenu en incluant un module **main**.py, dont le contenu sera exécuté lorsque le module est exécuté avec -m.

Par exemple, si nous développons un script conçu pour être utilisé comme module, nous devrions faire :

```python
# Exemple : la fonction peut être importée, mais le code de test ne s'exécute que lorsqu'il est exécuté directement
def add(a, b):
    return a+b

if __name__ == "__main__":  # Ne s'exécute que lorsque le fichier est exécuté, pas lorsqu'il est importé
    add(3, 5)
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Quelle est la valeur de <code>__name__</code> lorsqu'un fichier Python est exécuté directement comme un script ?
</template>

<base-quiz-option value="A">A. Le nom du fichier</base-quiz-option>
<base-quiz-option value="B" correct>B. <code>"**main**"</code></base-quiz-option>
<base-quiz-option value="C">C. <code>None</code></base-quiz-option>
<base-quiz-option value="D">D. <code>True</code></base-quiz-option>
<base-quiz-answer value="B">Lorsqu'un fichier Python est exécuté directement comme un script, <code>**name**</code> est défini sur <code>"**main**"</code>. Lorsque le fichier est importé comme un module, <code>**name**</code> est défini sur le nom du module.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Avantages

1. Chaque module Python a son `__name__` défini et si celui-ci est `__main__`, cela implique que le module est exécuté de manière autonome par l'utilisateur, et nous pouvons effectuer les actions appropriées correspondantes.
2. Si vous importez ce script comme module dans un autre script, le **nom** est défini sur le nom du script/module.
3. Les fichiers Python peuvent agir soit comme des modules réutilisables, soit comme des programmes autonomes.
4. `if __name__ == "__main__":` est utilisé pour exécuter du code uniquement si le fichier est exécuté directement et n'est pas importé.

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Quel est l'objectif principal de l'utilisation de <code>if __name__ == "__main__":</code> ?
</template>

<base-quiz-option value="A" correct>A. Exécuter du code uniquement lorsque le fichier est exécuté directement, et non lorsqu'il est importé</base-quiz-option>
<base-quiz-option value="B">B. Empêcher l'importation du fichier</base-quiz-option>
<base-quiz-option value="C">C. Rendre l'exécution du fichier plus rapide</base-quiz-option>
<base-quiz-option value="D">D. Cacher du code aux autres modules</base-quiz-option>
<base-quiz-answer value="A">L'idiome <code>if **name** == "**main**":</code> permet à un fichier Python d'agir à la fois comme un module réutilisable et comme un programme autonome. Le code à l'intérieur de ce bloc ne s'exécute que lorsque le fichier est exécuté directement, et non lorsqu'il est importé.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Liens pertinents

- <router-link to="/cheatsheet/functions">Fonctions</router-link>
- <router-link to="/cheatsheet/packaging">Packaging</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Projets Python avec Poetry et VSCode. Partie 1</router-link>
- <router-link to="/builtin/import">import()</router-link>
