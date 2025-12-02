---
title: 'Python パッケージング - Python チートシート'
description: 'setup.py と pyproject.toml を使用した Python プロジェクトのパッケージング方法を学習します。PEP-517、PEP-518、PEP-660 仕様に基づく最新の Python パッケージングアプローチを理解します。'
labUrl: 'https://labex.io/ja/labs/python-python-setup-py-633666?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python パッケージング
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-warning>
  <base-warning-title>
    「物議を醸す」意見
  </base-warning-title>
  <base-warning-content>
    Python パッケージをパッケージ化および配布するために<code>setup.py</code>を使用することは、時々非常に困難になることがあります。 <a target="_blank" href="https://python-poetry.org/">Poetry</a>や<a target="_blank" href="https://docs.astral.sh/uv/">UV</a>のような最新のツールは、パッケージングを<b>ずっと簡単に</b>するだけでなく、依存関係を非常に便利に管理するのにも役立ちます。特に UV は、従来のツールよりも 10〜100 倍高速である点で注目に値します。
  </base-warning-content>
</base-warning>

Poetry に関する詳細情報が必要な場合は、次の記事を読むことができます。

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Poetry と VSCode を使った Python プロジェクト。パート 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Poetry と VSCode を使った Python プロジェクト。パート 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Poetry と VSCode を使った Python プロジェクト。パート 3</router-link>

超高速 Python パッケージマネージャーである UV の包括的なガイドについては、<router-link to="/blog/python-uv-package-manager">UV: 超高速 Python パッケージマネージャー</router-link>をお読みください。

## はじめに

Python パッケージングとは、Python プロジェクトを配布およびインストールできるように準備するプロセスです。主なアプローチは 2 つあります。従来の<code>setup.py</code>メソッドと、PEP-517、PEP-518、および PEP-660 で定義されている最新の<code>pyproject.toml</code>アプローチです。

プロジェクト構造を管理するために不可欠なファイルおよびディレクトリパスの処理に関する包括的なガイドについては、<router-link to="/cheatsheet/file-directory-path">ファイルとディレクトリのパス</router-link>ページを参照してください。

## 従来の アプローチ：setup.py

<code>setup.py</code>ファイルは、従来の Python プロジェクトの中心です。プロジェクトに関するすべてのメタデータを記述します。プロジェクトにリッチなメタデータセットを与えるために追加できるフィールドはかなりありますが、必須フィールドは名前、バージョン、パッケージの 3 つだけです。名前フィールドは、パッケージを Python Package Index (PyPI) で公開したい場合、一意である必要があります。バージョンフィールドは、プロジェクトの異なるリリースを追跡します。パッケージのフィールドは、プロジェクト内のどこに Python ソースコードを配置したかを記述します。

これにより、Python パッケージを簡単にインストールできます。多くの場合、次のように記述するだけで十分です。

```bash
python setup.py install
```

そしてモジュールが自己インストールされます。

### 例：setup.py

最初の setup.py にはライセンスに関する情報も含まれ、<code>long_description</code>フィールドに README.txt ファイルを再利用します。これは次のように表示されます。

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

<BaseQuiz id="cheatsheet-packaging-1" correct="C">
<template #question>
<code>setup.py</code>ファイルにおける 3 つの必須フィールドは何ですか？
</template>

<BaseQuizOption value="A">A. name, author, license</BaseQuizOption>
<BaseQuizOption value="B">B. name, description, packages</BaseQuizOption>
<BaseQuizOption value="C" correct>C. name, version, packages</BaseQuizOption>
<BaseQuizOption value="D">D. name, version, license</BaseQuizOption>
<BaseQuizAnswer><code>setup.py</code>の 3 つの必須フィールドは、<code>name</code>（パッケージ名、PyPI で一意である必要があります）、<code>version</code>（リリースを追跡）、および<code>packages</code>（Python ソースコードの場所を記述）です。</BaseQuizAnswer>
</BaseQuiz>

## 最新の アプローチ：pyproject.toml

<code>pyproject.toml</code>ファイルは、Python プロジェクト構成の最新の標準です（PEP-517、PEP-518、PEP-660）。ビルドシステムの要件とプロジェクトのメタデータを単一の宣言的なファイル形式で指定するための統一された方法を提供します。

### pyproject.toml の利点

- **宣言的**: すべてのプロジェクトメタデータが一箇所に
- **ビルドシステムに依存しない**: setuptools、poetry、flit、その他のビルドバックエンドと連携
- **コード実行なし**: setup.py よりも安全で予測可能
- **標準化**: より良いツールサポートのために PEP 標準に従う

### 例：pyproject.toml

setuptools を使用した基本的な<code>pyproject.toml</code>の例を次に示します。

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

### pyproject.toml からのインストール

<code>pyproject.toml</code>を使用すると、pip を使用してパッケージをインストールできます。

```bash
pip install .
```

または編集可能モードで：

```bash
pip install -e .
```

<BaseQuiz id="cheatsheet-packaging-2" correct="B">
<template #question>
<code>pyproject.toml</code>が<code>setup.py</code>よりも優れている主な利点は何ですか？
</template>

<BaseQuizOption value="A">A. 実行が速いこと</BaseQuizOption>
<BaseQuizOption value="B" correct>B. 宣言的であり、安全（コード実行なし）、PEP 標準に従っていること</BaseQuizOption>
<BaseQuizOption value="C">C. 設定が少なくて済むこと</BaseQuizOption>
<BaseQuizOption value="D">D. Python 3.10+ でのみ動作すること</BaseQuizOption>
<BaseQuizAnswer><code>pyproject.toml</code>アプローチは宣言的（すべてのメタデータが一箇所）、<code>setup.py</code>のようにコードを実行しないため安全であり、より良いツールサポートのために PEP 標準（PEP-517、PEP-518、PEP-660）に従っています。</BaseQuizAnswer>
</BaseQuiz>

## 適切なアプローチの選択

- **<code>setup.py</code>を使用する**: レガシープロジェクトを扱っている場合、または細かい制御が必要な場合
- **<code>pyproject.toml</code>を使用する**: 新しいプロジェクトの場合（推奨）、最新の標準であり、より良いツールサポートを提供するため

詳細については、[公式ドキュメント](http://docs.python.org/3.11/install/index.html)をご覧ください。

## 関連リンク

- <router-link to="/cheatsheet/virtual-environments">仮想環境</router-link>
- <router-link to="/cheatsheet/file-directory-path">ファイルとディレクトリのパス</router-link>
- <router-link to="/blog/python-uv-package-manager">UV: 超高速 Python パッケージマネージャー</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Poetry と VSCode を使った Python プロジェクト。パート 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Poetry と VSCode を使った Python プロジェクト。パート 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Poetry と VSCode を使った Python プロジェクト。パート 3</router-link>
- <router-link to="/builtin/import">import()</router-link>
