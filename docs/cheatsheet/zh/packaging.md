---
title: 'Python 打包 - Python 速查表'
description: '学习如何使用 setup.py 和 pyproject.toml 打包 Python 项目。了解基于 PEP-517、PEP-518 和 PEP-660 规范的现代 Python 打包方法。'
labUrl: 'https://labex.io/zh/labs/python-python-setup-py-633666?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python 打包
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-warning>
  <base-warning-title>
    一个“有争议的”观点
  </base-warning-title>
  <base-warning-content>
    使用 <code>setup.py</code> 来打包和分发你的 Python 包有时会非常具有挑战性。像 <a target="_blank" href="https://python-poetry.org/">Poetry</a> 和 <a target="_blank" href="https://docs.astral.sh/uv/">UV</a> 这样的现代工具不仅使打包**容易得多**，而且还能以非常方便的方式帮助你管理依赖项。UV 特别值得注意，因为它比传统工具快 10-100 倍。
  </base-warning-content>
</base-warning>

如果你想了解更多关于 Poetry 的信息，可以阅读以下文章：

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">使用 Poetry 和 VSCode 的 Python 项目。第 1 部分</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">使用 Poetry 和 VSCode 的 Python 项目。第 2 部分</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">使用 Poetry 和 VSCode 的 Python 项目。第 3 部分</router-link>

有关闪电般快速的 Python 包管理器 UV 的全面指南，请阅读：<router-link to="/blog/python-uv-package-manager">UV：闪电般的 Python 包管理器</router-link>。

## 简介

Python 打包是准备你的 Python 项目以供分发和安装的过程。主要有两种方法：传统的 <code>setup.py</code> 方法和现代的 <code>pyproject.toml</code> 方法（定义在 PEP-517、PEP-518 和 PEP-660 中）。

有关处理文件和目录路径的全面指南（这对管理项目结构至关重要），请参阅 <router-link to="/cheatsheet/file-directory-path">文件和目录路径</router-link> 页面。

## 传统方法：setup.py

<code>setup.py</code> 文件是传统 Python 项目的核心。它描述了关于你项目的所有元数据。你可以向项目添加相当多的字段，以提供描述该项目的丰富元数据。然而，只有三个字段是必需的：<code>name</code>、<code>version</code> 和 <code>packages</code>。如果希望将包发布到 Python 包索引 (PyPI)，<code>name</code> 字段必须是唯一的。<code>version</code> 字段用于跟踪项目的不同版本。<code>packages</code> 字段描述了你在项目中放置 Python 源代码的位置。

这使得你可以轻松安装 Python 包。通常，编写以下内容就足够了：

```bash
python setup.py install
```

然后模块将自行安装。

### 示例：setup.py

我们最初的 setup.py 还会包含有关许可证的信息，并将重用 README.txt 文件作为 long_description 字段。它看起来像这样：

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
<code>setup.py</code> 文件中三个必需的字段是什么？
</template>

<base-quiz-option value="A">A. name, author, license</base-quiz-option>
<base-quiz-option value="B">B. name, description, packages</base-quiz-option>
<base-quiz-option value="C" correct>C. name, version, packages</base-quiz-option>
<base-quiz-option value="D">D. name, version, license</base-quiz-option>
<base-quiz-answer value="C"><code>setup.py</code> 中的三个必需字段是 <code>name</code>（包名，在 PyPI 上必须唯一）、<code>version</code>（跟踪版本）和 <code>packages</code>（描述 Python 源代码所在位置）。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 现代方法：pyproject.toml

<code>pyproject.toml</code> 文件是 Python 项目配置的现代标准（PEP-517、PEP-518、PEP-660）。它提供了一种统一的方式，在一个声明性的单一文件中指定构建系统要求和项目元数据。

### pyproject.toml 的优势

- **声明式 (Declarative)**：所有项目元数据集中在一个地方
- **构建系统无关 (Build system agnostic)**：可与 setuptools、poetry、flit 和其他构建后端配合使用
- **无代码执行 (No code execution)**：比 setup.py 更安全、更可预测
- **标准化 (Standardized)**：遵循 PEP 标准，以获得更好的工具支持

### 示例：pyproject.toml

这是一个使用 setuptools 的基本 <code>pyproject.toml</code> 示例：

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

### 从 pyproject.toml 安装

使用 <code>pyproject.toml</code>，你可以使用 pip 安装你的包：

```bash
pip install .
```

或者以可编辑模式：

```bash
pip install -e .
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
<code>pyproject.toml</code> 相对于 <code>setup.py</code> 的主要优势是什么？
</template>

<base-quiz-option value="A">A. 执行速度更快</base-quiz-option>
<base-quiz-option value="B" correct>B. 它是声明式的、更安全（无代码执行）并遵循 PEP 标准</base-quiz-option>
<base-quiz-option value="C">C. 它需要的配置更少</base-quiz-option>
<base-quiz-option value="D">D. 它只适用于 Python 3.10+</base-quiz-option>
<base-quiz-answer value="B"><code>pyproject.toml</code> 方法是声明式的（所有元数据集中在一个地方），比执行代码的 <code>setup.py</code> 更安全，并且遵循 PEP 标准（PEP-517、PEP-518、PEP-660）以获得更好的工具支持。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 选择正确的方法

- **使用 <code>setup.py</code>**：如果你正在处理遗留项目或需要细粒度的控制
- **使用 <code>pyproject.toml</code>**：用于新项目（推荐），因为它代表现代标准并提供更好的工具支持

访问[官方文档](http://docs.python.org/3.11/install/index.html)了解更多信息。

## 相关链接

- <router-link to="/cheatsheet/virtual-environments">虚拟环境</router-link>
- <router-link to="/cheatsheet/file-directory-path">文件和目录路径</router-link>
- <router-link to="/blog/python-uv-package-manager">UV：闪电般的 Python 包管理器</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">使用 Poetry 和 VSCode 的 Python 项目。第 1 部分</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">使用 Poetry 和 VSCode 的 Python 项目。第 2 部分</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">使用 Poetry 和 VSCode 的 Python 项目。第 3 部分</router-link>
- <router-link to="/builtin/import">import()</router-link>
