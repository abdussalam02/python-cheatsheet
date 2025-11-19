---
title: 'Python 打包 - Python 速查表'
description: '学习如何使用 setup.py 和 pyproject.toml 打包 Python 项目。了解符合 PEP-517、PEP-518 和 PEP-660 规范的现代 Python 打包方法。'
labUrl: 'https://labex.io/zh/labs/python-python-setup-py-633666?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python 打包
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-warning>
  <base-warning-title>
    一个"有争议的"观点
  </base-warning-title>
  <base-warning-content>
    使用 `setup.py` 来打包和分发 Python 包有时会非常具有挑战性。像 <a target="_blank" href="https://python-poetry.org/">Poetry</a> 和 <a target="_blank" href="https://docs.astral.sh/uv/">UV</a> 这样的现代工具不仅使打包**容易得多**，而且还能以非常方便的方式帮助您管理依赖项。UV 因其比传统工具快 10-100 倍的速度而尤为值得注意。
  </base-warning-content>
</base-warning>

如果您想了解有关 Poetry 的更多信息，可以阅读以下文章：

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">使用 Poetry 和 VSCode 的 Python 项目。第 1 部分</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">使用 Poetry 和 VSCode 的 Python 项目。第 2 部分</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">使用 Poetry 和 VSCode 的 Python 项目。第 3 部分</router-link>

有关闪电般快速的 Python 包管理器 UV 的全面指南，请阅读：<router-link to="/blog/python-uv-package-manager">UV：闪电般快速的 Python 包管理器</router-link>。

## 简介

Python 打包是为分发和安装准备 Python 项目的过程。主要有两种方法：传统的 `setup.py` 方法和现代的 `pyproject.toml` 方法（在 PEP-517、PEP-518 和 PEP-660 中定义）。

有关处理文件和目录路径（这对于管理项目结构至关重要）的全面指南，请参阅<router-link to="/cheatsheet/file-directory-path">文件和目录路径</router-link>页面。

## 传统方法：setup.py

`setup.py` 文件是传统 Python 项目的核心。它描述了有关您项目的**所有元数据**。您可以向项目添加相当多的字段，以提供有关该项目的丰富元数据。然而，**只有三个必需的字段**：`name`（名称）、`version`（版本）和 `packages`（包）。如果希望将包发布到 Python 包索引 (PyPI)，则 `name` 字段必须是唯一的。`version` 字段用于跟踪项目的不同版本。包字段描述了您在项目中放置 Python 源代码的位置。

这使您可以轻松安装 Python 包。通常，编写以下内容就足够了：

```bash
python setup.py install
```

模块将自行安装。

### 示例：setup.py

我们最初的 setup.py 还将包含有关许可证的信息，并将重用 README.txt 文件作为 `long_description` 字段。它看起来像这样：

```python
# setup.py: 为分发定义包元数据
from distutils.core import setup
setup(
   name='pythonCheatsheet',  # 包名称（在 PyPI 上必须唯一）
   version='0.1',  # 版本号
   packages=['pipenv',],  # 要包含的包列表
   license='MIT',  # 许可证类型
   long_description=open('README.txt').read(),  # 从文件读取描述
)
```

## 现代方法：pyproject.toml

`pyproject.toml` 文件是 Python 项目配置的现代标准（PEP-517、PEP-518、PEP-660）。它提供了一种统一的方式来在单个声明式文件格式中指定构建系统要求和项目元数据。

### pyproject.toml 的优势

- **声明式**：所有项目元数据集中在一处
- **构建系统无关**：可与 setuptools、poetry、flit 和其他构建后端配合使用
- **无需执行代码**：比 setup.py 更安全、更可预测
- **标准化**：遵循 PEP 标准，提供更好的工具支持

### 示例：pyproject.toml

以下是使用 setuptools 的基本 `pyproject.toml` 示例：

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "pythonCheatsheet"
version = "0.1"
description = "一个 Python 速查表包"
readme = "README.txt"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "您的姓名", email = "your.email@example.com"}
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

使用 `pyproject.toml`，您可以使用 pip 安装包：

```bash
pip install .
```

或使用可编辑模式：

```bash
pip install -e .
```

## 选择正确的方法

- **使用 `setup.py`**：如果您正在处理遗留项目或需要细粒度控制
- **使用 `pyproject.toml`**：适用于新项目（推荐），因为它是现代标准并提供更好的工具支持

要了解更多信息，请访问[官方文档](http://docs.python.org/3.11/install/index.html)。

## 相关链接

- <router-link to="/cheatsheet/virtual-environments">虚拟环境</router-link>
- <router-link to="/cheatsheet/file-directory-path">文件和目录路径</router-link>
- <router-link to="/blog/python-uv-package-manager">UV：闪电般快速的 Python 包管理器</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">使用 Poetry 和 VSCode 的 Python 项目。第 1 部分</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">使用 Poetry 和 VSCode 的 Python 项目。第 2 部分</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">使用 Poetry 和 VSCode 的 Python 项目。第 3 部分</router-link>
- <router-link to="/builtin/import">import()</router-link>
