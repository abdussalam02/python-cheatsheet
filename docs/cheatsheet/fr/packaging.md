---
title: 'Packaging Python - Fiche Mémo Python'
description: "Apprenez à packager des projets Python avec setup.py et pyproject.toml. Comprenez l'approche moderne du packaging Python avec les spécifications PEP-517, PEP-518 et PEP-660."
labUrl: 'https://labex.io/fr/labs/python-python-setup-py-633666?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Packaging Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-warning>
  <base-warning-title>
    Une opinion « controversée »
  </base-warning-title>
  <base-warning-content>
    L'utilisation de <code>setup.py</code> pour empaqueter et distribuer vos packages Python peut être assez difficile de temps en temps. Les outils modernes comme <a target="_blank" href="https://python-poetry.org/">Poetry</a> et <a target="_blank" href="https://docs.astral.sh/uv/">UV</a> rendent non seulement l'empaquetage <b>beaucoup plus facile</b>, mais vous aident également à gérer vos dépendances de manière très pratique. UV est particulièrement remarquable pour être 10 à 100 fois plus rapide que les outils traditionnels.
  </base-warning-content>
</base-warning>

Si vous souhaitez plus d'informations sur Poetry, vous pouvez lire les articles suivants :

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Projets Python avec Poetry et VSCode. Partie 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Projets Python avec Poetry et VSCode. Partie 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Projets Python avec Poetry et VSCode. Partie 3</router-link>

Pour un guide complet sur UV, le gestionnaire de packages Python ultra-rapide, lisez : <router-link to="/blog/python-uv-package-manager">UV : Le gestionnaire de packages Python ultra-rapide</router-link>.

## Introduction

L'empaquetage Python (Python packaging) est le processus de préparation de votre projet Python pour la distribution et l'installation. Il existe deux approches principales : la méthode traditionnelle <code>setup.py</code> et l'approche moderne <code>pyproject.toml</code> (définie dans PEP-517, PEP-518 et PEP-660).

Pour un guide complet sur la gestion des chemins de fichiers et de répertoires, essentiel pour gérer les structures de projet, consultez la page <router-link to="/cheatsheet/file-directory-path">Chemins de fichiers et de répertoires</router-link>.

## Approche Traditionnelle : setup.py

Le fichier <code>setup.py</code> est au cœur d'un projet Python traditionnel. Il décrit toutes les métadonnées de votre projet. Il existe un certain nombre de champs que vous pouvez ajouter à un projet pour lui donner un ensemble riche de métadonnées décrivant le projet. Cependant, seuls trois champs sont obligatoires : <code>name</code>, <code>version</code> et <code>packages</code>. Le champ <code>name</code> doit être unique si vous souhaitez publier votre package sur l'Index des Packages Python (PyPI). Le champ <code>version</code> suit les différentes versions du projet. Le champ <code>packages</code> décrit où vous avez placé le code source Python au sein de votre projet.

Cela vous permet d'installer facilement des packages Python. Souvent, il suffit d'écrire :

```bash
python setup.py install
```

et le module s'installera lui-même.

### Exemple : setup.py

Notre <code>setup.py</code> initial inclura également des informations sur la licence et réutilisera le fichier README.txt pour le champ <code>long_description</code>. Cela ressemblera à ceci :

```python
# setup.py: define package metadata for distribution
from distutils.core import setup
setup(
   name='pythonCheatsheet',  # Package name (must be unique on PyPI)
   version='0.1',  # Version number
   packages=['pipenv',],  # List of packages to include
   license='MIT',  # License type
   long_description=open('README.txt').read(),  # Read description from file
)
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
Quels sont les trois champs obligatoires dans un fichier <code>setup.py</code> ?
</template>

<base-quiz-option value="A">A. name, author, license</base-quiz-option>
<base-quiz-option value="B">B. name, description, packages</base-quiz-option>
<base-quiz-option value="C" correct>C. name, version, packages</base-quiz-option>
<base-quiz-option value="D">D. name, version, license</base-quiz-option>
<base-quiz-answer value="C">Les trois champs obligatoires dans <code>setup.py</code> sont <code>name</code> (nom du package, doit être unique sur PyPI), <code>version</code> (suit les versions) et <code>packages</code> (décrit où se trouve le code source Python).</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Approche Moderne : pyproject.toml

Le fichier <code>pyproject.toml</code> est la norme moderne pour la configuration des projets Python (PEP-517, PEP-518, PEP-660). Il fournit une manière unifiée de spécifier les exigences du système de construction (build system) et les métadonnées du projet dans un format de fichier unique et déclaratif.

### Avantages de pyproject.toml

- **Déclaratif** : Toutes les métadonnées du projet en un seul endroit
- **Agnostique du système de construction** : Fonctionne avec setuptools, poetry, flit et d'autres backends de construction
- **Pas d'exécution de code** : Plus sûr et plus prévisible que setup.py
- **Standardisé** : Suit les normes PEP pour un meilleur support des outils

### Exemple : pyproject.toml

Voici un exemple de base de <code>pyproject.toml</code> utilisant setuptools :

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "pythonCheatsheet"
version = "0.1"
description = "A Python cheatsheet package"
readme = "README.txt"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=22.0",
]
```

### Installation à partir de pyproject.toml

Avec <code>pyproject.toml</code>, vous pouvez installer votre package en utilisant pip :

```bash
pip install .
```

Ou en mode éditable :

```bash
pip install -e .
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Quel est l'avantage principal de <code>pyproject.toml</code> par rapport à <code>setup.py</code> ?
</template>

<base-quiz-option value="A">A. Il est plus rapide à exécuter</base-quiz-option>
<base-quiz-option value="B" correct>B. Il est déclaratif, plus sûr (pas d'exécution de code) et suit les normes PEP</base-quiz-option>
<base-quiz-option value="C">C. Il nécessite moins de configuration</base-quiz-option>
<base-quiz-option value="D">D. Il ne fonctionne qu'avec Python 3.10+</base-quiz-option>
<base-quiz-answer value="B">L'approche <code>pyproject.toml</code> est déclarative (toutes les métadonnées en un seul endroit), plus sûre car elle n'exécute pas de code comme le fait <code>setup.py</code>, et suit les normes PEP (PEP-517, PEP-518, PEP-660) pour un meilleur support des outils.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Choisir la bonne approche

- **Utiliser <code>setup.py</code>** : Si vous travaillez avec des projets hérités (legacy) ou si vous avez besoin d'un contrôle granulaire
- **Utiliser <code>pyproject.toml</code>** : Pour les nouveaux projets (recommandé), car c'est la norme moderne et offre un meilleur support des outils

Trouvez plus d'informations en visitant la [documentation officielle](http://docs.python.org/3.11/install/index.html).

## Liens pertinents

- <router-link to="/cheatsheet/virtual-environments">Environnements Virtuels</router-link>
- <router-link to="/cheatsheet/file-directory-path">Chemins de fichiers et de répertoires</router-link>
- <router-link to="/blog/python-uv-package-manager">UV : Le gestionnaire de packages Python ultra-rapide</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Projets Python avec Poetry et VSCode. Partie 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Projets Python avec Poetry et VSCode. Partie 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Projets Python avec Poetry et VSCode. Partie 3</router-link>
- <router-link to="/builtin/import">import()</router-link>
