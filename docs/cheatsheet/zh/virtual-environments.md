---
title: 'Python 虚拟环境 - Python 速查表'
description: '使用虚拟环境是为了在隔离环境中测试 Python 代码，并避免用仅供单个项目使用的库填充基础 Python 安装。'
labUrl: 'https://labex.io/zh/labs/python-python-virtual-environments-633669?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
虚拟环境
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

使用虚拟环境的目的是在封装的环境中测试 Python 代码，并避免用仅用于一个项目的库填充基础 Python 安装。

## venv

`venv` 是 Python 3.3+ 中用于创建虚拟环境的标准库模块。它内置于 Python 中，因此无需安装。

1. 创建一个虚拟环境

```bash
python -m venv venv
```

或者在某些系统上：

```bash
python3 -m venv venv
```

这将在当前文件夹中创建一个包含虚拟环境的 `venv` 目录。

<base-quiz>
<base-quiz-question correct="A">
<template #question>
使用 <code>venv</code> 创建虚拟环境的命令是什么？
</template>

<base-quiz-option value="A" correct>A. <code>python -m venv venv</code></base-quiz-option>
<base-quiz-option value="B">B. <code>python create venv</code></base-quiz-option>
<base-quiz-option value="C">C. <code>venv create</code></base-quiz-option>
<base-quiz-option value="D">D. <code>python venv new</code></base-quiz-option>
<base-quiz-answer value="A">命令 <code>python -m venv venv</code> 创建一个虚拟环境。<code>-m</code> 标志运行 venv 模块，末尾的 <code>venv</code> 是要创建的目录的名称。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

2. 激活虚拟环境

在 Linux/macOS 上：

```bash
source venv/bin/activate
```

在 Windows 上：

```bash
venv\Scripts\activate
```

激活后，您将在命令提示符的开头看到 `(venv)`，表示虚拟环境已激活。

<base-quiz>
<base-quiz-question correct="B">
<template #question>
如何在 Linux/macOS 上激活虚拟环境？
</template>

<base-quiz-option value="A">A. <code>activate venv</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>source venv/bin/activate</code></base-quiz-option>
<base-quiz-option value="C">C. <code>venv activate</code></base-quiz-option>
<base-quiz-option value="D">D. <code>python venv activate</code></base-quiz-option>
<base-quiz-answer value="B">在 Linux/macOS 上，使用 <code>source venv/bin/activate</code> 激活虚拟环境。在 Windows 上，您将使用 <code>venv\Scripts\activate</code>。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

3. 安装包

激活虚拟环境后，使用 pip 安装包：

```bash
pip install package_name
```

安装的包将特定于此虚拟环境。

4. 停用虚拟环境

要退出虚拟环境：

```bash
deactivate
```

命令提示符中的 `(venv)` 前缀将消失。

<base-quiz>
<base-quiz-question correct="A">
<template #question>
使用虚拟环境的主要目的是什么？
</template>

<base-quiz-option value="A" correct>A. 隔离项目依赖项并避免填充基础 Python 安装</base-quiz-option>
<base-quiz-option value="B">B. 使 Python 运行得更快</base-quiz-option>
<base-quiz-option value="C">C. 加密 Python 代码</base-quiz-option>
<base-quiz-option value="D">D. 将 Python 编译成机器码</base-quiz-option>
<base-quiz-answer value="A">虚拟环境允许您在封装的环境中测试 Python 代码，并避免用可能仅用于一个项目的库填充基础 Python 安装。这有助于按项目管理依赖项。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## virtualenv

1. 安装 virtualenv

```bash
pip install virtualenv
```

1. 安装 virtualenvwrapper-win (Windows)

```bash
pip install virtualenvwrapper-win
```

用法：

1. 创建一个名为 `HelloWorld` 的虚拟环境

```bash
mkvirtualenv HelloWorld
```

现在安装的任何内容都将特定于此项目。并且可供我们连接到此环境的项目使用。

1. 设置项目目录

要将我们的 virtualenv 与当前工作目录绑定，我们只需输入：

```bash
setprojectdir .
```

1. 停用

要在命令行中进行其他操作，请键入 `deactivate` 以停用您的环境。

```bash
deactivate
```

注意括号如何消失。

1. Workon

打开命令提示符并键入 `workon HelloWorld` 以激活环境并进入项目根文件夹

```bash
workon HelloWorld
```

## Poetry

<base-disclaimer>
  <base-disclaimer-title>
    来自 <a href="https://python-poetry.org/">Poetry 网站</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Poetry 是一个用于 Python 中依赖管理和打包的工具。它允许您声明项目所依赖的库，它将为您管理（安装/更新）它们。
  </base-disclaimer-content>
</base-disclaimer>

1. 安装 Poetry

```bash
pip install --user poetry
```

2. 创建一个新项目

```bash
poetry new my-project
```

这将创建一个 my-project 目录：

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

pyproject.toml 文件将协调您的项目及其依赖项：

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

3. 包

要向项目中添加依赖项，您可以在 tool.poetry.dependencies 部分指定它们：

```toml
[tool.poetry.dependencies]
pendulum = "^1.4"
```

此外，您可以不手动修改 pyproject.toml 文件，而是使用 add 命令，它会自动找到合适的版本约束。

```bash
poetry add pendulum
```

要安装 pyproject.toml 中列出的依赖项：

```bash
poetry install
```

要删除依赖项：

```bash
poetry remove pendulum
```

有关更多信息，请查看[文档](https://poetry.eustace.io/docs/)或在此处阅读：

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">使用 Poetry 和 VSCode 的 Python 项目。第 1 部分</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">使用 Poetry 和 VSCode 的 Python 项目。第 2 部分</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">使用 Poetry 和 VSCode 的 Python 项目。第 3 部分</router-link>

## Pipenv

<base-disclaimer>
  <base-disclaimer-title>
    来自 <a target="_blank" href="https://pipenv.pypa.io/en/latest/">Pipenv 网站</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Pipenv 是一个旨在将所有打包世界（bundler、composer、npm、cargo、yarn 等）中最好的部分带到 Python 世界的工具。Windows 在我们的世界中是首等公民。
  </base-disclaimer-content>
</base-disclaimer>

1. 安装 pipenv

```bash
pip install pipenv
```

2. 进入您的项目目录并安装项目的包

```bash
cd my_project
pipenv install <package>
```

Pipenv 将安装您的包并在项目目录中为您创建一个 Pipfile。Pipfile 用于跟踪项目所需的依赖项，以防您需要重新安装它们。

3. 卸载包

```bash
pipenv uninstall <package>
```

4. 激活与您的 Python 项目关联的虚拟环境

```bash
pipenv shell
```

5. 退出虚拟环境

```bash
exit
```

在 [docs.pipenv.org](https://docs.pipenv.org/) 查找更多信息和视频。

## Anaconda

<base-disclaimer>
  <base-disclaimer-title>
    <a target="k" href="https://anaconda.com/">Anaconda</a> 是另一个流行的 Python 包管理工具。
  </base-disclaimer-title>
  <base-disclaimer-content>
    在这里共享包、notebook、项目和环境。您免费公开托管 conda 包的地方。
  </base-disclaimer-content>
</base-disclaimer>

用法：

1. 创建一个虚拟环境

```bash
conda create -n HelloWorld
```

2. 要使用虚拟环境，请通过以下方式激活它：

```bash
conda activate HelloWorld
```

现在安装的任何内容都将特定于 HelloWorld 项目

3. 退出虚拟环境

```bash
conda deactivate
```

## UV

<base-disclaimer>
  <base-disclaimer-title>
    来自 <a target="_blank" href="https://docs.astral.sh/uv/">UV 文档</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    UV 是一个极其快速的 Python 包安装程序和解析器，设计为 pip 和 pip-tools 工作流程的直接替代品。UV 比 pip 快 10-100 倍，并提供统一的包管理、虚拟环境创建和 Python 版本管理。
  </base-disclaimer-content>
</base-disclaimer>

1. 安装 UV

```bash
# 使用 curl (Linux/macOS)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 使用 pip 或 pipx
pip install uv
```

2. 创建一个带有虚拟环境的新项目

```bash
uv init my-project
cd my-project
```

3. 添加依赖项

```bash
uv add requests
```

4. 在项目环境中运行命令

```bash
uv run python script.py
```

5. 手动激活虚拟环境（可选）

```bash
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

UV 以卓越的速度和便利性自动管理虚拟环境、Python 版本和依赖项。

## 相关链接

- <router-link to="/cheatsheet/packaging">打包</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">使用 Poetry 和 VSCode 的 Python 项目。第 1 部分</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">使用 Poetry 和 VSCode 的 Python 项目。第 2 部分</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">使用 Poetry 和 VSCode 的 Python 项目。第 3 部分</router-link>
- <router-link to="/blog/python-uv-package-manager">UV：闪电般快速的 Python 包管理器</router-link>
- <router-link to="/builtin/import">import()</router-link>
