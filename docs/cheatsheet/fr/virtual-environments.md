---
title: 'Environnements Virtuels Python - Aide-mémoire Python'
description: "L'environnement virtuel permet de tester du code Python dans des espaces isolés et d'éviter de surcharger l'installation Python de base avec des bibliothèques spécifiques à un seul projet."
labUrl: 'https://labex.io/fr/labs/python-python-virtual-environments-633669?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Environnement Virtuel
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

L'utilisation d'un Environnement Virtuel sert à tester du code Python dans des environnements encapsulés, et également à éviter de remplir l'installation Python de base avec des bibliothèques que nous pourrions n'utiliser que pour un seul projet.

## venv

`venv` est le module de la bibliothèque standard pour créer des environnements virtuels dans Python 3.3+. Il est intégré à Python, donc aucune installation n'est requise.

1. Créer un environnement virtuel

```bash
python -m venv venv
```

Ou sur certains systèmes :

```bash
python3 -m venv venv
```

Ceci crée un répertoire `venv` dans votre dossier actuel contenant l'environnement virtuel.

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Quelle commande est utilisée pour créer un environnement virtuel avec <code>venv</code> ?
</template>

<base-quiz-option value="A" correct>A. <code>python -m venv venv</code></base-quiz-option>
<base-quiz-option value="B">B. <code>python create venv</code></base-quiz-option>
<base-quiz-option value="C">C. <code>venv create</code></base-quiz-option>
<base-quiz-option value="D">D. <code>python venv new</code></base-quiz-option>
<base-quiz-answer value="A">La commande <code>python -m venv venv</code> crée un environnement virtuel. L'indicateur <code>-m</code> exécute le module venv, et <code>venv</code> à la fin est le nom du répertoire à créer.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

2. Activer l'environnement virtuel

Sur Linux/macOS :

```bash
source venv/bin/activate
```

Sur Windows :

```bash
venv\Scripts\activate
```

Une fois activé, vous verrez `(venv)` au début de votre invite de commande, indiquant que l'environnement virtuel est actif.

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Comment activer un environnement virtuel sur Linux/macOS ?
</template>

<base-quiz-option value="A">A. <code>activate venv</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>source venv/bin/activate</code></base-quiz-option>
<base-quiz-option value="C">C. <code>venv activate</code></base-quiz-option>
<base-quiz-option value="D">D. <code>python venv activate</code></base-quiz-option>
<base-quiz-answer value="B">Sur Linux/macOS, vous activez un environnement virtuel en utilisant <code>source venv/bin/activate</code>. Sur Windows, vous utiliseriez <code>venv\Scripts\activate</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

3. Installer des paquets

Avec l'environnement virtuel activé, installez des paquets en utilisant pip :

```bash
pip install package_name
```

Les paquets installés seront spécifiques à cet environnement virtuel.

4. Désactiver l'environnement virtuel

Pour quitter l'environnement virtuel :

```bash
deactivate
```

Le préfixe `(venv)` disparaîtra de votre invite de commande.

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Quel est l'objectif principal de l'utilisation d'un environnement virtuel ?
</template>

<base-quiz-option value="A" correct>A. Isoler les dépendances du projet et éviter de remplir l'installation Python de base</base-quiz-option>
<base-quiz-option value="B">B. Rendre Python plus rapide</base-quiz-option>
<base-quiz-option value="C">C. Crypter le code Python</base-quiz-option>
<base-quiz-option value="D">D. Compiler Python en code machine</base-quiz-option>
<base-quiz-answer value="A">Les environnements virtuels vous permettent de tester du code Python dans des environnements encapsulés et d'éviter de remplir l'installation Python de base avec des bibliothèques qui pourraient n'être utilisées que pour un seul projet. Cela aide à gérer les dépendances par projet.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## virtualenv

1. Installer virtualenv

```bash
pip install virtualenv
```

1. Installer virtualenvwrapper-win (Windows)

```bash
pip install virtualenvwrapper-win
```

Utilisation :

1. Créer un environnement virtuel nommé `HelloWorld`

```bash
mkvirtualenv HelloWorld
```

Tout ce que nous installons maintenant sera spécifique à ce projet. Et disponible pour les projets que nous connectons à cet environnement.

1. Définir le répertoire du projet

Pour lier notre virtualenv à notre répertoire de travail actuel, nous entrons simplement :

```bash
setprojectdir .
```

1. Désactiver

Pour passer à autre chose dans l'invite de commande, tapez `deactivate` pour désactiver votre environnement.

```bash
deactivate
```

Remarquez comment les parenthèses disparaissent.

1. Travailler sur (Workon)

Ouvrez l'invite de commande et tapez `workon HelloWorld` pour activer l'environnement et vous déplacer vers le dossier racine de votre projet

```bash
workon HelloWorld
```

## Poetry

<base-disclaimer>
  <base-disclaimer-title>
    Du site web de <a href="https://python-poetry.org/">Poetry</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Poetry est un outil de gestion des dépendances et de packaging en Python. Il vous permet de déclarer les bibliothèques dont votre projet dépend et il les gérera (installera/mettra à jour) pour vous.
  </base-disclaimer-content>
</base-disclaimer>

1. Installer Poetry

```bash
pip install --user poetry
```

2. Créer un nouveau projet

```bash
poetry new my-project
```

Ceci créera un répertoire my-project :

```plaintext
my-project
├── pyproject.toml
├── README.rst
├── poetry_demo
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_poetry_demo.py
```

Le fichier pyproject.toml orchestrera votre projet et ses dépendances :

```toml
[tool.poetry]
name = "my-project"
version = "0.1.0"
description = ""
authors = ["your name <your@mail.com>"]

[tool.poetry.dependencies]
python = "*"

[tool.poetry.dev-dependencies]
pytest = "^3.4"
```

3. Paquets

Pour ajouter des dépendances à votre projet, vous pouvez les spécifier dans la section tool.poetry.dependencies :

```toml
[tool.poetry.dependencies]
pendulum = "^1.4"
```

Aussi, au lieu de modifier le fichier pyproject.toml à la main, vous pouvez utiliser la commande add et elle trouvera automatiquement une contrainte de version appropriée.

```bash
poetry add pendulum
```

Pour installer les dépendances listées dans pyproject.toml :

```bash
poetry install
```

Pour supprimer des dépendances :

```bash
poetry remove pendulum
```

Pour plus d'informations, consultez la [documentation](https://poetry.eustace.io/docs/) ou lisez ici :

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Projets Python avec Poetry et VSCode. Partie 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Projets Python avec Poetry et VSCode. Partie 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Projets Python avec Poetry et VSCode. Partie 3</router-link>

## Pipenv

<base-disclaimer>
  <base-disclaimer-title>
    Du site web de <a target="_blank" href="https://pipenv.pypa.io/en/latest/">Pipenv</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Pipenv est un outil qui vise à apporter le meilleur de tous les mondes du packaging (bundler, composer, npm, cargo, yarn, etc.) au monde Python. Windows est un citoyen de première classe, dans notre monde.
  </base-disclaimer-content>
</base-disclaimer>

1. Installer pipenv

```bash
pip install pipenv
```

2. Entrez dans le répertoire de votre projet et installez les paquets pour votre projet

```bash
cd my_project
pipenv install <package>
```

Pipenv installera votre paquet et créera un Pipfile pour vous dans le répertoire de votre projet. Le Pipfile est utilisé pour suivre les dépendances dont votre projet a besoin au cas où vous devriez les réinstaller.

3. Désinstaller des paquets

```bash
pipenv uninstall <package>
```

4. Activer l'environnement virtuel associé à votre projet Python

```bash
pipenv shell
```

5. Quitter l'environnement virtuel

```bash
exit
```

Trouvez plus d'informations et une vidéo sur [docs.pipenv.org](https://docs.pipenv.org/).

## Anaconda

<base-disclaimer>
  <base-disclaimer-title>
    <a target="k" href="https://anaconda.com/">Anaconda</a> est un autre outil populaire pour gérer les paquets Python.
  </base-disclaimer-title>
  <base-disclaimer-content>
    Où les paquets, les notebooks, les projets et les environnements sont partagés. Votre lieu pour l'hébergement public gratuit de paquets conda.
  </base-disclaimer-content>
</base-disclaimer>

Utilisation :

1. Créer un environnement virtuel

```bash
conda create -n HelloWorld
```

2. Pour utiliser l'environnement virtuel, activez-le par :

```bash
conda activate HelloWorld
```

Tout ce qui est installé maintenant sera spécifique au projet HelloWorld

3. Quitter l'environnement virtuel

```bash
conda deactivate
```

## UV

<base-disclaimer>
  <base-disclaimer-title>
    De la <a target="_blank" href="https://docs.astral.sh/uv/">Documentation UV</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    UV est un installateur et résolveur de paquets Python extrêmement rapide, conçu comme un remplacement direct pour les flux de travail pip et pip-tools. UV est 10 à 100 fois plus rapide que pip et fournit une gestion unifiée des paquets, la création d'environnements virtuels et la gestion des versions Python.
  </base-disclaimer-content>
</base-disclaimer>

1. Installer UV

```bash
# Utilisation de curl (Linux/macOS)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Utilisation de pip ou pipx
pip install uv
```

2. Créer un nouveau projet avec environnement virtuel

```bash
uv init my-project
cd my-project
```

3. Ajouter des dépendances

```bash
uv add requests
```

4. Exécuter des commandes dans l'environnement du projet

```bash
uv run python script.py
```

5. Activer l'environnement virtuel manuellement (optionnel)

```bash
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

UV gère automatiquement les environnements virtuels, les versions Python et les dépendances avec une vitesse et une commodité exceptionnelles.

## Liens pertinents

- <router-link to="/cheatsheet/packaging">Packaging</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Projets Python avec Poetry et VSCode. Partie 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Projets Python avec Poetry et VSCode. Partie 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Projets Python avec Poetry et VSCode. Partie 3</router-link>
- <router-link to="/blog/python-uv-package-manager">UV : Le gestionnaire de paquets Python ultra-rapide</router-link>
- <router-link to="/builtin/import">import()</router-link>
