---
title: Python Packaging - Python Cheatsheet
description: Learn how to package Python projects using setup.py and pyproject.toml. Understand the modern approach to Python packaging with PEP-517, PEP-518, and PEP-660 specifications.
labUrl: https://labex.io/labs/python-python-setup-py-633666?course=python-cheatsheet
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Packaging
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-warning>
  <base-warning-title>
    A 'controversial' opinion
  </base-warning-title>
  <base-warning-content>
    Using `setup.py` to pack and distribute your python packages can be quite challenging every so often. Modern tools like <a target="_blank" href="https://python-poetry.org/">Poetry</a> and <a target="_blank" href="https://docs.astral.sh/uv/">UV</a> make not only the packaging a <b>lot easier</b>, but also help you to manage your dependencies in a very convenient way. UV is particularly notable for being 10-100x faster than traditional tools.
  </base-warning-content>
</base-warning>

If you want more information about Poetry you can read the following articles:

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Python projects with Poetry and VSCode. Part 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Python projects with Poetry and VSCode. Part 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Python projects with Poetry and VSCode. Part 3</router-link>

For a comprehensive guide to UV, the lightning-fast Python package manager, read: <router-link to="/blog/python-uv-package-manager">UV: The Lightning-Fast Python Package Manager</router-link>.

## Introduction

Python packaging is the process of preparing your Python project for distribution and installation. There are two main approaches: the traditional `setup.py` method and the modern `pyproject.toml` approach (defined in PEP-517, PEP-518, and PEP-660).

For a comprehensive guide on handling file and directory paths, which is essential for managing project structures, see the <router-link to="/cheatsheet/file-directory-path">File and directory Paths</router-link> page.

## Traditional Approach: setup.py

The `setup.py` file is at the heart of a traditional Python project. It describes all the metadata about your project. There are quite a few fields you can add to a project to give it a rich set of metadata describing the project. However, there are only three required fields: name, version, and packages. The name field must be unique if you wish to publish your package on the Python Package Index (PyPI). The version field keeps track of different releases of the project. The package's field describes where you've put the Python source code within your project.

This allows you to easily install Python packages. Often it's enough to write:

```bash
python setup.py install
```

and module will install itself.

### Example: setup.py

Our initial setup.py will also include information about the license and will re-use the README.txt file for the long_description field. This will look like:

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

## Modern Approach: pyproject.toml

The `pyproject.toml` file is the modern standard for Python project configuration (PEP-517, PEP-518, PEP-660). It provides a unified way to specify build system requirements and project metadata in a single, declarative file format.

### Benefits of pyproject.toml

- **Declarative**: All project metadata in one place
- **Build system agnostic**: Works with setuptools, poetry, flit, and other build backends
- **No code execution**: Safer and more predictable than setup.py
- **Standardized**: Follows PEP standards for better tooling support

### Example: pyproject.toml

Here's a basic `pyproject.toml` example using setuptools:

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

### Installing from pyproject.toml

With `pyproject.toml`, you can install your package using pip:

```bash
pip install .
```

Or in editable mode:

```bash
pip install -e .
```

## Choosing the Right Approach

- **Use `setup.py`**: If you're working with legacy projects or need fine-grained control
- **Use `pyproject.toml`**: For new projects (recommended), as it's the modern standard and provides better tooling support

Find more information visit the [official documentation](http://docs.python.org/3.11/install/index.html).

## Relevant links

- <router-link to="/cheatsheet/virtual-environments">Virtual Environments</router-link>
- <router-link to="/cheatsheet/file-directory-path">File and directory Paths</router-link>
- <router-link to="/blog/python-uv-package-manager">UV: The Lightning-Fast Python Package Manager</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Python projects with Poetry and VSCode. Part 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Python projects with Poetry and VSCode. Part 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Python projects with Poetry and VSCode. Part 3</router-link>
- <router-link to="/builtin/import">import()</router-link>
