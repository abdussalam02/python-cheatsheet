---
title: 'Python JSON と YAML - Python チートシート'
description: 'JSON（JavaScript Object Notation）は、データの保存と転送のための軽量な形式です。JSON は、データがサーバーから Web ページに送信される際によく使用されます。'
labUrl: 'https://labex.io/ja/labs/python-python-json-and-yaml-633659?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
JSON と YAML
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## JSON

JSON は JavaScript Object Notation の略で、データを保存および転送するための軽量なフォーマットです。JSON は、サーバーから Web ページにデータが送信される際によく使用されます。

```python
# JSON ファイルを読み込む：json.load() はファイルオブジェクトから JSON を解析する
import json
with open("filename.json", "r") as f:  # ファイルを読み取りモードで開く
    content = json.load(f)  # JSON を解析し、Python の dict/list を返す
```

次の内容で JSON ファイルを書き込む：

```python
# JSON ファイルを書き込む：json.dump() は Python オブジェクトを JSON として書き出す
import json

content = {"name": "Joe", "age": 20}
with open("filename.json", "w") as f:  # ファイルを書き込みモードで開く
    json.dump(content, f, indent=2)  # 2 スペースのインデントで JSON を書き出す
```

<BaseQuiz id="cheatsheet-json-yaml-1" correct="B">
<template #question>
Python の辞書を JSON ファイルに書き込むために使用される関数はどれですか？
</template>

<BaseQuizOption value="A">A. <code>json.write()</code></BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>json.dump()</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>json.save()</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>json.export()</code></BaseQuizOption>
<BaseQuizAnswer><code>json.dump()</code>関数は、Python オブジェクト（辞書など）を JSON ファイルに書き込みます。<code>json.load()</code>は JSON ファイルを読み取るために使用されます。</BaseQuizAnswer>
</BaseQuiz>

## YAML

JSON と比較して、YAML は人間による保守性がはるかに高く、コメントを追加する機能を提供します。人間が編集する必要がある設定ファイルにとって便利な選択肢です。

YAML ファイルにアクセスするための主要なライブラリは 2 つあります。

- [PyYaml](https://pypi.python.org/pypi/PyYAML)
- [Ruamel.yaml](https://pypi.python.org/pypi/ruamel.yaml)

これらを仮想環境で`pip install`を使用してインストールします。

前者は使いやすいですが、後者の Ruamel は YAML 仕様をはるかにうまく実装しており、例えばコメントを変更せずに YAML の内容を変更することができます。

次の方法で YAML ファイルを開きます：

```python
# ruamel.yaml ライブラリを使用して YAML ファイルを読み込む
from ruamel.yaml import YAML

with open("filename.yaml") as f:
    yaml=YAML()  # YAML パーサーインスタンスを作成
    yaml.load(f)  # YAML を解析し、Python の dict/list を返す
```

<BaseQuiz id="cheatsheet-json-yaml-2" correct="C">
<template #question>
JSON に対する YAML の利点は何ですか？
</template>

<BaseQuizOption value="A">A. YAML ファイルはより小さい</BaseQuizOption>
<BaseQuizOption value="B">B. YAML は解析が速い</BaseQuizOption>
<BaseQuizOption value="C" correct>C. YAML はコメントを許可し、人間にとってより読みやすい</BaseQuizOption>
<BaseQuizOption value="D">D. YAML は Python に組み込まれている</BaseQuizOption>
<BaseQuizAnswer>YAML はコメントを許可し、JSON よりも人間にとって読みやすいため、人間が編集する必要のある設定ファイルにとって便利な選択肢となります。</BaseQuizAnswer>
</BaseQuiz>

## Anyconfig

[Anyconfig](https://pypi.python.org/pypi/anyconfig)は非常に便利なパッケージで、基盤となる設定ファイル形式を完全に抽象化できます。JSON、YAML、TOML などから Python 辞書をロードできます。

次のようにインストールします：

```bash
pip install anyconfig
```

使用法：

```python
# anyconfig: 様々な形式（JSON, YAML, TOML など）の設定ファイルをロードする
import anyconfig
conf1 = anyconfig.load("/path/to/foo/conf.d/a.yml")  # 形式を自動検出
```

<BaseQuiz id="cheatsheet-json-yaml-3" correct="A">
<template #question>
anyconfig ライブラリは何を可能にしますか？
</template>

<BaseQuizOption value="A" correct>A. 形式を指定せずに様々な形式（JSON、YAML、TOML）の設定ファイルをロードすること</BaseQuizOption>
<BaseQuizOption value="B">B. 異なる設定形式間で変換すること</BaseQuizOption>
<BaseQuizOption value="C">C. 設定ファイルの構文を検証すること</BaseQuizOption>
<BaseQuizOption value="D">D. 設定ファイルを暗号化すること</BaseQuizOption>
<BaseQuizAnswer>anyconfig ライブラリは基盤となる設定ファイル形式を抽象化し、どの形式が使用されているかを知る必要なく、JSON、YAML、TOML などから Python 辞書をロードできるようにします。</BaseQuizAnswer>
</BaseQuiz>

## 関連リンク

- <router-link to="/cheatsheet/reading-and-writing-files">ファイルの読み書き</router-link>
- <router-link to="/cheatsheet/dictionaries">Python 辞書</router-link>
- <router-link to="/modules/json-module">json モジュール</router-link>
- <router-link to="/blog/python-pathlib-essentials">すべての開発者が知っておくべき 10 の必須ファイルシステム操作</router-link>
- <router-link to="/builtin/open">open()</router-link>
- <router-link to="/builtin/dict">dict()</router-link>
