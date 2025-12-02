---
title: 'Python JSON 与 YAML - Python 速查表'
description: 'JSON（JavaScript 对象表示法）是一种轻量级的数据存储和传输格式。当数据从服务器发送到网页时，JSON 经常被使用。'
labUrl: 'https://labex.io/zh/labs/python-python-json-and-yaml-633659?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
JSON 和 YAML
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## JSON

JSON 代表 JavaScript Object Notation，是一种用于存储和传输数据的轻量级格式。当数据从服务器发送到网页时，通常会使用 JSON。

```python
# 读取 JSON 文件：json.load() 从文件对象解析 JSON
import json
with open("filename.json", "r") as f:  # 以读取模式打开文件
    content = json.load(f)  # 解析 JSON 并返回 Python 字典/列表
```

写入包含以下内容的 JSON 文件：

```python
# 写入 JSON 文件：json.dump() 将 Python 对象写入 JSON
import json

content = {"name": "Joe", "age": 20}
with open("filename.json", "w") as f:  # 以写入模式打开文件
    json.dump(content, f, indent=2)  # 写入 JSON，使用 2 个空格缩进
```

<BaseQuiz id="cheatsheet-json-yaml-1" correct="B">
<template #question>
哪个函数用于将 Python 字典写入 JSON 文件？
</template>

<BaseQuizOption value="A">A. <code>json.write()</code></BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>json.dump()</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>json.save()</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>json.export()</code></BaseQuizOption>
<BaseQuizAnswer><code>json.dump()</code> 函数将 Python 对象（如字典）写入 JSON 文件。<code>json.load()</code> 用于读取 JSON 文件。</BaseQuizAnswer>
</BaseQuiz>

## YAML

与 JSON 相比，YAML 具有更好的人类可维护性，并提供了添加注释的能力。对于需要人工编辑的配置文件来说，它是一个方便的选择。

允许访问 YAML 文件的主要库有两个：

- [PyYaml](https://pypi.python.org/pypi/PyYAML)
- [Ruamel.yaml](https://pypi.python.org/pypi/ruamel.yaml)

在您的虚拟环境中，使用 `pip install` 安装它们。

第一个更容易使用，但第二个 Ruamel 更好地实现了 YAML 规范，并允许例如在不更改注释的情况下修改 YAML 内容。

使用以下方法打开 YAML 文件：

```python
# 使用 ruamel.yaml 库读取 YAML 文件
from ruamel.yaml import YAML

with open("filename.yaml") as f:
    yaml=YAML()  # 创建 YAML 解析器实例
    yaml.load(f)  # 解析 YAML 并返回 Python 字典/列表
```

<BaseQuiz id="cheatsheet-json-yaml-2" correct="C">
<template #question>
YAML 相对于 JSON 的一个优点是什么？
</template>

<BaseQuizOption value="A">A. YAML 文件更小</BaseQuizOption>
<BaseQuizOption value="B">B. YAML 解析速度更快</BaseQuizOption>
<BaseQuizOption value="C" correct>C. YAML 允许注释且更易于人类阅读</BaseQuizOption>
<BaseQuizOption value="D">D. YAML 是 Python 内置的</BaseQuizOption>
<BaseQuizAnswer>YAML 允许注释，并且比 JSON 更易于人类阅读，使其成为需要人工编辑的配置文件的方便选择。</BaseQuizAnswer>
</BaseQuiz>

## Anyconfig

[Anyconfig](https://pypi.python.org/pypi/anyconfig) 是一个非常方便的包，它允许完全抽象底层配置文件格式。它可以从 JSON、YAML、TOML 等加载 Python 字典。

使用以下命令安装它：

```bash
pip install anyconfig
```

用法：

```python
# anyconfig: 以各种格式（JSON、YAML、TOML 等）加载配置文件
import anyconfig
conf1 = anyconfig.load("/path/to/foo/conf.d/a.yml")  # 自动检测格式
```

<BaseQuiz id="cheatsheet-json-yaml-3" correct="A">
<template #question>
anyconfig 库允许您做什么？
</template>

<BaseQuizOption value="A" correct>A. 以各种格式（JSON、YAML、TOML）加载配置文件，而无需指定格式</BaseQuizOption>
<BaseQuizOption value="B">B. 在不同配置格式之间转换</BaseQuizOption>
<BaseQuizOption value="C">C. 验证配置文件语法</BaseQuizOption>
<BaseQuizOption value="D">D. 加密配置文件</BaseQuizOption>
<BaseQuizAnswer>anyconfig 库抽象了底层配置文件格式，允许您从 JSON、YAML、TOML 等格式加载 Python 字典，而无需知道正在使用的具体格式。</BaseQuizAnswer>
</BaseQuiz>

## 相关链接

- <router-link to="/cheatsheet/reading-and-writing-files">读取和写入文件</router-link>
- <router-link to="/cheatsheet/dictionaries">Python 字典</router-link>
- <router-link to="/modules/json-module">json 模块</router-link>
- <router-link to="/blog/python-pathlib-essentials">每位开发者都应知道的 10 个基本文件系统操作</router-link>
- <router-link to="/builtin/open">open()</router-link>
- <router-link to="/builtin/dict">dict()</router-link>
