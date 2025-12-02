---
title: 'Python チートシート：ファイルの読み書き'
description: 'Python でファイルを読み書きするには、with ステートメントを使用します。これにより、処理完了後にファイルが自動的に閉じられ、リソース管理が効率的に行われます。'
labUrl: 'https://labex.io/ja/labs/python-python-reading-and-writing-files-633663?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
ファイルの読み書き
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

ファイルとディレクトリパスの操作についてより深く知りたい場合は、<router-link to="/cheatsheet/file-directory-path">ファイルとディレクトリのパス</router-link>のページを参照してください。

## ファイルの読み書きプロセス

Python でファイルへの読み書きを行うには、`with`ステートメントを使用するのが適切です。これにより、処理が完了した後にファイルが自動的に閉じられ、利用可能なリソースが管理されます。

## ファイルのオープンと読み込み

`open`関数はファイルをオープンし、対応するファイルオブジェクトを返します。

```python
# 'with'ステートメントを使用してファイルを読み込む：完了すると自動的にファイルが閉じられる
with open('/home/labex/project/hi.txt') as hello_file:
    hello_content = hello_file.read()  # ファイルの内容全体を読み込む

hello_content
```

```output
'Hello World!'
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-reading-and-writing-files-1">
<template #question>
ファイルをオープンする際に<code>with</code>ステートメントを使用する主な利点は何ですか？
</template>

<base-quiz-option value="A" correct>A. エラーが発生した場合でも、処理が完了するとファイルが自動的に閉じられる</base-quiz-option>
<base-quiz-option value="B">B. ファイルのオープンが速くなる</base-quiz-option>
<base-quiz-option value="C">C. ファイルを読み取りモードと書き込みモードで同時に開くことができる</base-quiz-option>
<base-quiz-option value="D">D. ファイルが自動的に圧縮される</base-quiz-option>
<base-quiz-answer value="A"><code>with</code>ステートメントは、例外が発生した場合でもブロックを抜けるときにファイルが自動的に閉じられることを保証します。これはリソースを適切に管理するのに役立ちます。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

あるいは、_readlines()_ メソッドを使用して、ファイルから文字列のリストを取得することもできます。これは、テキストの各行に対して 1 つの文字列となります。

```python
# readlines() メソッド：各行に対して 1 つの文字列を含むリストを返す
with open('sonnet29.txt') as sonnet_file:
    sonnet_file.readlines()  # 各行を文字列として含むリストを返す
```

```output
['When, in disgrace with fortune and men's eyes,\n',
 ' I all alone beweep my  outcast state,\n',
 "And trouble deaf heaven with my bootless cries,\n",
 "And look upon myself and curse my fate,']
```

ファイルを 1 行ずつイテレートすることもできます。

```python
# ファイルを 1 行ずつイテレートする (大きなファイルに対してメモリ効率が良い)
with open('sonnet29.txt') as sonnet_file:
    for line in sonnet_file:  # ファイルオブジェクトはイテラブルである
        print(line, end='')  # 余分な改行なしで出力
```

```output
When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,
```

## ファイルへの書き込み

```python
# ファイルへの書き込み：'w'モードは既存のファイルを上書きする
with open('bacon.txt', 'w') as bacon_file:  # 'w' = 書き込みモード
    bacon_file.write('Hello world!\n')  # 書き込まれた文字数を返す
```

```output
13
```

```python
# ファイルへの追記：'a'モードは既存のファイルに追記する
with open('bacon.txt', 'a') as bacon_file:  # 'a' = 追記モード
    bacon_file.write('Bacon is not a vegetable.')
```

```output
25
```

```python
with open('bacon.txt') as bacon_file:
    content = bacon_file.read()

print(content)
```

```output
Hello world!
Bacon is not a vegetable.
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-reading-and-writing-files-2">
<template #question>
モード<code>'w'</code>でファイルを開くこととモード<code>'a'</code>でファイルを開くことの違いは何ですか？
</template>

<base-quiz-option value="A">A. <code>'w'</code>は読み取り用、<code>'a'</code>は書き込み用</base-quiz-option>
<base-quiz-option value="B" correct>B. <code>'w'</code>はファイルを上書きし、<code>'a'</code>はファイルに追記する</base-quiz-option>
<base-quiz-option value="C">C. <code>'w'</code>は Windows 用、<code>'a'</code>は Apple 用</base-quiz-option>
<base-quiz-option value="D">D. 違いはない</base-quiz-option>
<base-quiz-answer value="B">モード<code>'w'</code>はファイルを書き込み用に開き、既存の内容をすべて上書きします。モード<code>'a'</code>はファイルを追記用に開き、新しいコンテンツをファイルの末尾に追加します。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 関連リンク

- <router-link to="/cheatsheet/file-directory-path">ファイルとディレクトリのパス</router-link>
- <router-link to="/cheatsheet/json-yaml">JSON と YAML</router-link>
- <router-link to="/blog/python-pathlib-essentials">すべての開発者が知っておくべき 10 の必須ファイルシステム操作</router-link>
- <router-link to="/builtin/open">open()</router-link>
- <router-link to="/builtin/print">print()</router-link>
