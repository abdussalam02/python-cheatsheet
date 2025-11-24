---
title: 'Python 仮想環境 - Python チートシート'
description: '仮想環境の使用は、Python コードを分離された環境でテストし、単一プロジェクトでのみ使用するライブラリで基本の Python インストールを埋め尽くすのを避けるためです。'
labUrl: 'https://labex.io/ja/labs/python-python-virtual-environments-633669?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
仮想環境
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

仮想環境を使用する目的は、カプセル化された環境で Python コードをテストすること、および単一のプロジェクトでのみ使用する可能性のあるライブラリでベースの Python インストールを埋め尽くすことを避けることです。

## venv

`venv` は、Python 3.3 以降で仮想環境を作成するための標準ライブラリモジュールです。Python に組み込まれているため、インストールは不要です。

1. 仮想環境の作成

```bash
python -m venv venv
```

または、システムによっては：

```bash
python3 -m venv venv
```

これにより、現在のフォルダー内に仮想環境を含む `venv` ディレクトリが作成されます。

<base-quiz>
<base-quiz-question correct="A">
<template #question>
<code>venv</code> を使用して仮想環境を作成するために使用されるコマンドは何ですか？
</template>

<base-quiz-option value="A" correct>A. <code>python -m venv venv</code></base-quiz-option>
<base-quiz-option value="B">B. <code>python create venv</code></base-quiz-option>
<base-quiz-option value="C">C. <code>venv create</code></base-quiz-option>
<base-quiz-option value="D">D. <code>python venv new</code></base-quiz-option>
<base-quiz-answer value="A">コマンド <code>python -m venv venv</code> は仮想環境を作成します。<code>-m</code> フラグは venv モジュールを実行し、末尾の <code>venv</code> は作成するディレクトリ名です。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

2. 仮想環境のアクティベート

Linux/macOS の場合：

```bash
source venv/bin/activate
```

Windows の場合：

```bash
venv\Scripts\activate
```

アクティベートされると、コマンドプロンプトの先頭に `(venv)` と表示され、仮想環境がアクティブであることを示します。

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Linux/macOS で仮想環境をアクティベートするにはどうすればよいですか？
</template>

<base-quiz-option value="A">A. <code>activate venv</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>source venv/bin/activate</code></base-quiz-option>
<base-quiz-option value="C">C. <code>venv activate</code></base-quiz-option>
<base-quiz-option value="D">D. <code>python venv activate</code></base-quiz-option>
<base-quiz-answer value="B">Linux/macOS では、<code>source venv/bin/activate</code> を使用して仮想環境をアクティベートします。Windows では <code>venv\Scripts\activate</code> を使用します。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

3. パッケージのインストール

仮想環境がアクティブな状態で、pip を使用してパッケージをインストールします。

```bash
pip install package_name
```

インストールされたパッケージはこの仮想環境に固有のものになります。

4. 仮想環境のディアクティベート

仮想環境を終了するには：

```bash
deactivate
```

コマンドプロンプトから `(venv)` プレフィックスが消えます。

<base-quiz>
<base-quiz-question correct="A">
<template #question>
仮想環境を使用する主な目的は何ですか？
</template>

<base-quiz-option value="A" correct>A. プロジェクトの依存関係を分離し、ベースの Python インストールが埋め尽くされるのを避けるため</base-quiz-option>
<base-quiz-option value="B">B. Python の実行速度を向上させるため</base-quiz-option>
<base-quiz-option value="C">C. Python コードを暗号化するため</base-quiz-option>
<base-quiz-option value="D">D. Python を機械語にコンパイルするため</base-quiz-option>
<base-quiz-answer value="A">仮想環境を使用すると、カプセル化された環境で Python コードをテストし、単一のプロジェクトでのみ使用する可能性のあるライブラリでベースの Python インストールを埋め尽くすことを避けることができます。これはプロジェクトごとの依存関係の管理に役立ちます。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## virtualenv

1. virtualenv のインストール

```bash
pip install virtualenv
```

1. virtualenvwrapper-win のインストール (Windows)

```bash
pip install virtualenvwrapper-win
```

使用方法：

1. `HelloWorld` という名前の仮想環境の作成

```bash
mkvirtualenv HelloWorld
```

ここでインストールするものはすべてこのプロジェクト固有のものになります。そして、この環境に接続するプロジェクトでも利用可能になります。

1. プロジェクトディレクトリの設定

仮想環境を現在の作業ディレクトリにバインドするには、単に以下を入力します。

```bash
setprojectdir .
```

1. ディアクティベート

コマンドラインで別の作業に移るには、`deactivate` と入力して環境をディアクティベートします。

```bash
deactivate
```

括弧が消えることに注意してください。

1. Workon

コマンドプロンプトを開き、`workon HelloWorld` と入力して環境をアクティベートし、プロジェクトのルートフォルダーに移動します。

```bash
workon HelloWorld
```

## Poetry

<base-disclaimer>
  <base-disclaimer-title>
    <a href="https://python-poetry.org/">Poetry のウェブサイト</a>より
  </base-disclaimer-title>
  <base-disclaimer-content>
    Poetry は、Python における依存関係管理とパッケージングのためのツールです。プロジェクトが依存するライブラリを宣言でき、Poetry がそれらを管理（インストール/更新）してくれます。
  </base-disclaimer-content>
</base-disclaimer>

1. Poetry のインストール

```bash
pip install --user poetry
```

2. 新しいプロジェクトの作成

```bash
poetry new my-project
```

これにより、my-project ディレクトリが作成されます。

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

pyproject.toml ファイルがプロジェクトとその依存関係を調整します。

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

3. パッケージ

プロジェクトに依存関係を追加するには、tool.poetry.dependencies セクションで指定できます。

```toml
[tool.poetry.dependencies]
pendulum = "^1.4"
```

また、pyproject.toml ファイルを手動で変更する代わりに、add コマンドを使用すると、適切なバージョン制約が自動的に見つかります。

```bash
poetry add pendulum
```

pyproject.toml にリストされている依存関係をインストールするには：

```bash
poetry install
```

依存関係を削除するには：

```bash
poetry remove pendulum
```

詳細については、[ドキュメント](https://poetry.eustace.io/docs/)を確認するか、こちらをお読みください。

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Python projects with Poetry and VSCode. Part 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Python projects with Poetry and VSCode. Part 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Python projects with Poetry and VSCode. Part 3</router-link>

## Pipenv

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://pipenv.pypa.io/en/latest/">Pipenv ウェブサイト</a>より
  </base-disclaimer-title>
  <base-disclaimer-content>
    Pipenv は、すべてのパッケージングの世界（bundler、composer、npm、cargo、yarn など）の最高のものをもたらすことを目指したツールであり、Python の世界にもたらします。Windows は私たちの世界では一流の市民です。
  </base-disclaimer-content>
</base-disclaimer>

1. pipenv のインストール

```bash
pip install pipenv
```

2. プロジェクトディレクトリに入り、プロジェクトのパッケージをインストールします

```bash
cd my_project
pipenv install <package>
```

Pipenv はパッケージをインストールし、プロジェクトのディレクトリに Pipfile を作成します。Pipfile は、依存関係を再インストールする必要がある場合に備えて、プロジェクトが必要とする依存関係を追跡するために使用されます。

3. パッケージのアンインストール

```bash
pipenv uninstall <package>
```

4. Python プロジェクトに関連付けられた仮想環境のアクティベート

```bash
pipenv shell
```

5. 仮想環境の終了

```bash
exit
```

[docs.pipenv.org](https://docs.pipenv.org/) で詳細情報とビデオを見つけてください。

## Anaconda

<base-disclaimer>
  <base-disclaimer-title>
    <a target="k" href="https://anaconda.com/">Anaconda</a> は Python パッケージを管理するためのもう一つの人気のあるツールです。
  </base-disclaimer-title>
  <base-disclaimer-content>
    パッケージ、ノートブック、プロジェクト、環境が共有される場所。無料のパブリック conda パッケージホスティングのためのあなたの場所。
  </base-disclaimer-content>
</base-disclaimer>

使用方法：

1. 仮想環境の作成

```bash
conda create -n HelloWorld
```

2. 仮想環境を使用するには、次のようにアクティベートします。

```bash
conda activate HelloWorld
```

ここでインストールされるものはすべてプロジェクト HelloWorld に固有のものになります。

3. 仮想環境の終了

```bash
conda deactivate
```

## UV

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://docs.astral.sh/uv/">UV ドキュメント</a>より
  </base-disclaimer-title>
  <base-disclaimer-content>
    UV は、極めて高速な Python パッケージインストーラーおよびリゾルバーであり、pip および pip-tools ワークフローのドロップイン代替として設計されています。UV は pip よりも 10〜100 倍高速で、統合されたパッケージ管理、仮想環境作成、Python バージョン管理を提供します。
  </base-disclaimer-content>
</base-disclaimer>

1. UV のインストール

```bash
# curlを使用 (Linux/macOS)
curl -LsSf https://astral.sh/uv/install.sh | sh

# pipまたはpipxを使用
pip install uv
```

2. 仮想環境を持つ新しいプロジェクトの作成

```bash
uv init my-project
cd my-project
```

3. 依存関係の追加

```bash
uv add requests
```

4. プロジェクト環境でのコマンドの実行

```bash
uv run python script.py
```

5. 仮想環境の手動アクティベート (オプション)

```bash
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

UV は、卓越した速度と利便性で、仮想環境、Python バージョン、および依存関係を自動的に管理します。

## 関連リンク

- <router-link to="/cheatsheet/packaging">Packaging</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Python projects with Poetry and VSCode. Part 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Python projects with Poetry and VSCode. Part 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Python projects with Poetry and VSCode. Part 3</router-link>
- <router-link to="/blog/python-uv-package-manager">UV: The Lightning-Fast Python Package Manager</router-link>
- <router-link to="/builtin/import">import()</router-link>
