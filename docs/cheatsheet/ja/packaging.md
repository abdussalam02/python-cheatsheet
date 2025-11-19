---
title: 'Python Packaging - Python チートシート'
description: 'setup.py と pyproject.toml を使用して Python プロジェクトをパッケージ化する方法を学びます。PEP-517、PEP-518、PEP-660 仕様を使用した Python パッケージングの現代的なアプローチを理解します。'
labUrl: 'https://labex.io/ja/labs/python-python-setup-py-633666?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Packaging
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-warning>
  <base-warning-title>
    物議を醸す意見
  </base-warning-title>
  <base-warning-content>
    `setup.py` を使用して Python パッケージのビルドと配布を行うことは、時として非常に困難になることがあります。<a target="_blank" href="https://python-poetry.org/">Poetry</a> や <a target="_blank" href="https://docs.astral.sh/uv/">UV</a> のような最新のツールは、パッケージングを**ずっと簡単に**するだけでなく、依存関係を非常に便利に管理するのにも役立ちます。特に UV は、従来のツールよりも 10～100 倍高速である点で注目に値します。
  </base-warning-content>
</base-warning>

Poetry に関する詳細情報が必要な場合は、次の記事をお読みください。

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Poetry と VSCode を使用した Python プロジェクト。パート 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Poetry と VSCode を使用した Python プロジェクト。パート 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Poetry と VSCode を使用した Python プロジェクト。パート 3</router-link>

超高速 Python パッケージマネージャーである UV の包括的なガイドについては、<router-link to="/blog/python-uv-package-manager">UV: 超高速 Python パッケージマネージャー</router-link> をお読みください。

## 導入

Python パッケージングは、Python プロジェクトを配布およびインストール用に準備するプロセスです。主に 2 つのアプローチがあります：従来の `setup.py` メソッドと、現代的な `pyproject.toml` アプローチ（PEP-517、PEP-518、PEP-660 で定義）です。

プロジェクト構造の管理に不可欠な、ファイルおよびディレクトリパスの処理に関する包括的なガイドについては、<router-link to="/cheatsheet/file-directory-path">ファイルとディレクトリのパス</router-link> ページを参照してください。

## 従来のアプローチ: setup.py

`setup.py` ファイルは従来の Python プロジェクトの核となります。これはプロジェクトに関するすべてのメタデータを記述します。プロジェクトにリッチなメタデータセットを与えるために追加できるフィールドはかなりありますが、必須のフィールドは name、version、packages の 3 つだけです。name フィールドは、パッケージを Python Package Index (PyPI) で公開したい場合、一意である必要があります。version フィールドは、プロジェクトの異なるリリースを追跡します。package のフィールドは、プロジェクト内のどこに Python ソースコードを配置したかを記述します。

これにより、Python パッケージを簡単にインストールできます。多くの場合、次のように記述するだけで十分です。

```bash
python setup.py install
```

そしてモジュールは自己インストールされます。

### 例: setup.py

最初の setup.py は、ライセンスに関する情報も含め、`long_description` フィールドに README.txt ファイルを再利用します。これは次のようになります。

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

## 現代的なアプローチ: pyproject.toml

`pyproject.toml` ファイルは、Python プロジェクト設定の現代的な標準（PEP-517、PEP-518、PEP-660）です。単一の宣言型ファイル形式で、ビルドシステム要件とプロジェクトメタデータを指定する統一された方法を提供します。

### pyproject.toml の利点

- **宣言型**: すべてのプロジェクトメタデータを 1 か所に配置
- **ビルドシステムに依存しない**: setuptools、poetry、flit およびその他のビルドバックエンドで動作
- **コード実行なし**: setup.py よりも安全で予測可能
- **標準化**: PEP 標準に準拠し、より優れたツールサポートを提供

### 例: pyproject.toml

setuptools を使用した基本的な `pyproject.toml` の例を次に示します：

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "pythonCheatsheet"
version = "0.1"
description = "Python チートシートパッケージ"
readme = "README.txt"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "あなたの名前", email = "your.email@example.com"}
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

`pyproject.toml` を使用すると、pip を使用してパッケージをインストールできます：

```bash
pip install .
```

または編集可能モードで：

```bash
pip install -e .
```

## 適切なアプローチの選択

- **`setup.py` を使用**: レガシープロジェクトを扱っている場合、または細かい制御が必要な場合
- **`pyproject.toml` を使用**: 新しいプロジェクト（推奨）の場合、現代的な標準であり、より優れたツールサポートを提供します

詳細については、[公式ドキュメント](http://docs.python.org/3.11/install/index.html)をご覧ください。

## 関連リンク

- <router-link to="/cheatsheet/virtual-environments">仮想環境</router-link>
- <router-link to="/cheatsheet/file-directory-path">ファイルとディレクトリのパス</router-link>
- <router-link to="/blog/python-uv-package-manager">UV: 超高速 Python パッケージマネージャー</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Poetry と VSCode を使用した Python プロジェクト。パート 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Poetry と VSCode を使用した Python プロジェクト。パート 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Poetry と VSCode を使用した Python プロジェクト。パート 3</router-link>
- <router-link to="/builtin/import">import()</router-link>

