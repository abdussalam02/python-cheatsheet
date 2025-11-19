---
title: 'Python Packaging - Fiche de Référence Python'
description: 'Apprenez à empaqueter des projets Python en utilisant setup.py et pyproject.toml. Comprenez l'approche moderne de l'empaquetage Python avec les spécifications PEP-517, PEP-518 et PEP-660.'
labUrl: 'https://labex.io/fr/labs/python-python-setup-py-633666?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Packaging
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-warning>
  <base-warning-title>
    Une opinion « controversée »
  </base-warning-title>
  <base-warning-content>
    L'utilisation de `setup.py` pour empaqueter et distribuer vos paquets Python peut être assez difficile de temps en temps. Les outils modernes comme <a target="_blank" href="https://python-poetry.org/">Poetry</a> et <a target="_blank" href="https://docs.astral.sh/uv/">UV</a> rendent non seulement l'empaquetage <b>beaucoup plus facile</b>, mais vous aident également à gérer vos dépendances d'une manière très pratique. UV est particulièrement remarquable pour être 10 à 100 fois plus rapide que les outils traditionnels.
  </base-warning-content>
</base-warning>

Si vous souhaitez plus d'informations sur Poetry, vous pouvez lire les articles suivants :

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Projets Python avec Poetry et VSCode. Partie 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Projets Python avec Poetry et VSCode. Partie 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Projets Python avec Poetry et VSCode. Partie 3</router-link>

Pour un guide complet sur UV, le gestionnaire de paquets Python ultra-rapide, lisez : <router-link to="/blog/python-uv-package-manager">UV : Le gestionnaire de paquets Python ultra-rapide</router-link>.

## Introduction

L'empaquetage Python est le processus de préparation de votre projet Python pour la distribution et l'installation. Il existe deux approches principales : la méthode traditionnelle `setup.py` et l'approche moderne `pyproject.toml` (définie dans PEP-517, PEP-518 et PEP-660).

Pour un guide complet sur la gestion des chemins de fichiers et de répertoires, ce qui est essentiel pour gérer les structures de projet, consultez la page <router-link to="/cheatsheet/file-directory-path">Chemins de fichiers et de répertoires</router-link>.

## Approche traditionnelle : setup.py

Le fichier `setup.py` est au cœur d'un projet Python traditionnel. Il décrit toutes les métadonnées de votre projet. Il existe un certain nombre de champs que vous pouvez ajouter à un projet pour lui donner un ensemble riche de métadonnées décrivant le projet. Cependant, il n'y a que trois champs obligatoires : `name`, `version` et `packages`. Le champ `name` doit être unique si vous souhaitez publier votre paquet sur le Python Package Index (PyPI). Le champ `version` assure le suivi des différentes versions du projet. Le champ `packages` décrit où vous avez placé le code source Python au sein de votre projet.

Cela vous permet d'installer facilement des paquets Python. Souvent, il suffit d'écrire :

```bash
python setup.py install
```

et le module s'installera lui-même.

### Exemple : setup.py

Notre `setup.py` initial inclura également des informations sur la licence et réutilisera le fichier README.txt pour le champ `long_description`. Cela ressemblera à ceci :

```python
# setup.py: définir les métadonnées du paquet pour la distribution
from distutils.core import setup
setup(
   name='pythonCheatsheet',  # Nom du paquet (doit être unique sur PyPI)
   version='0.1',  # Numéro de version
   packages=['pipenv',],  # Liste des paquets à inclure
   license='MIT',  # Type de licence
   long_description=open('README.txt').read(),  # Lire la description depuis le fichier
)
```

## Approche moderne : pyproject.toml

Le fichier `pyproject.toml` est la norme moderne pour la configuration de projets Python (PEP-517, PEP-518, PEP-660). Il fournit un moyen unifié de spécifier les exigences du système de build et les métadonnées du projet dans un seul format de fichier déclaratif.

### Avantages de pyproject.toml

- **Déclaratif** : Toutes les métadonnées du projet en un seul endroit
- **Indépendant du système de build** : Fonctionne avec setuptools, poetry, flit et autres backends de build
- **Pas d'exécution de code** : Plus sûr et plus prévisible que setup.py
- **Standardisé** : Suit les normes PEP pour un meilleur support des outils

### Exemple : pyproject.toml

Voici un exemple de base de `pyproject.toml` utilisant setuptools :

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "pythonCheatsheet"
version = "0.1"
description = "Un paquet de fiche de référence Python"
readme = "README.txt"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Votre Nom", email = "your.email@example.com"}
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

### Installation depuis pyproject.toml

Avec `pyproject.toml`, vous pouvez installer votre paquet en utilisant pip :

```bash
pip install .
```

Ou en mode modifiable :

```bash
pip install -e .
```

## Choisir la bonne approche

- **Utilisez `setup.py`** : Si vous travaillez avec des projets hérités ou avez besoin d'un contrôle précis
- **Utilisez `pyproject.toml`** : Pour les nouveaux projets (recommandé), car c'est la norme moderne et offre un meilleur support des outils

Pour plus d'informations, visitez la [documentation officielle](http://docs.python.org/3.11/install/index.html).

## Liens pertinents

- <router-link to="/cheatsheet/virtual-environments">Environnements Virtuels</router-link>
- <router-link to="/cheatsheet/file-directory-path">Chemins de fichiers et de répertoires</router-link>
- <router-link to="/blog/python-uv-package-manager">UV : Le gestionnaire de paquets Python ultra-rapide</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Projets Python avec Poetry et VSCode. Partie 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Projets Python avec Poetry et VSCode. Partie 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Projets Python avec Poetry et VSCode. Partie 3</router-link>
- <router-link to="/builtin/import">import()</router-link>

