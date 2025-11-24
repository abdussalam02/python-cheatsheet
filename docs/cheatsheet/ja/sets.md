---
title: 'Python セット - Python チートシート'
description: 'Python には、データを整理するための組み込みデータ型がいくつか用意されています。これらの構造には、リスト、辞書、タプル、セットが含まれます。'
labUrl: 'https://labex.io/ja/labs/python-python-sets-633665?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python セット
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Python には、データを整理するためのいくつかの組み込みデータ型が用意されています。これらの構造には、リスト、辞書、タプル、そして **セット** が含まれます。

<base-disclaimer>
  <base-disclaimer-title>
    Python 3 の <a target="_blank" href="https://docs.python.org/3/tutorial/datastructures.html#sets">ドキュメント</a> より
  </base-disclaimer-title>
  <base-disclaimer-content>
    セットは、重複する要素のない順序付けられていないコレクションです。基本的な用途には、メンバーシップのテストや重複エントリの削除があります。
  </base-disclaimer-content>
</base-disclaimer>

より詳細な参照については、<router-link to="/blog/python-sets-what-why-how">Python Sets: What, Why and How</router-link> をお読みください。

## セットの初期化

セットを作成するには、波括弧 `{}` を使用する方法と、組み込み関数 `set()` を使用する方法の 2 つがあります。

<base-warning>
  <base-warning-title>
    空のセット
  </base-warning-title>
  <base-warning-content>
    セットを作成する際は、空の波括弧 <code>{}</code> を使用しないように注意してください。そうしないと、代わりに空の辞書になってしまいます。
  </base-warning-content>
</base-warning>

```python
# 波括弧または set() 関数を使用してセットを作成
s = {1, 2, 3}  # 波括弧を使用
s = set([1, 2, 3])  # set() コンストラクタを使用

# 警告：空の {} はセットではなく辞書を作成します
s = {}  # これはセットではなく辞書を作成します
type(s)  # <class 'dict'> を返します
```

```output
<class 'dict'>
```

## 一意な要素の順序付けられていないコレクション

セットは重複する値を自動的に削除します。

```python
# セットは重複を自動的に削除します
s = {1, 2, 3, 2, 3, 4}  # 重複は削除されます
s  # {1, 2, 3, 4} を返します
```

```output
{1, 2, 3, 4}
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
重複する値を持つセットを作成するとどうなりますか？
</template>

<base-quiz-option value="A" correct>A. 重複は自動的に削除されます</base-quiz-option>
<base-quiz-option value="B">B. エラーが発生します</base-quiz-option>
<base-quiz-option value="C">C. セットはすべての重複を保持します</base-quiz-option>
<base-quiz-option value="D">D. 最初の出現のみが保持されます</base-quiz-option>
<base-quiz-answer value="A">セットは重複する値を自動的に削除します。セットは、重複する要素のない順序付けられていないコレクションです。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

そして、順序付けられていないデータ型であるため、インデックス指定はできません。

```python
s = {1, 2, 3}
s[0]
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
```

## set add と update

`add()` メソッドを使用して、セットに単一の要素を追加できます。

```python
# add() メソッド：セットに単一の要素を追加します
s = {1, 2, 3}
s.add(4)  # 要素 4 を追加
s
```

```output
{1, 2, 3, 4}
```

そして `update()` を使用すると、複数の要素を追加できます。

```python
# update() メソッド：イテラブルから複数の要素を追加します
s = {1, 2, 3}
s.update([2, 3, 4, 5, 6])  # 複数の要素を追加します (重複は無視されます)
s
```

```output
{1, 2, 3, 4, 5, 6}
```

## set remove と discard

どちらのメソッドもセットから要素を削除しますが、`remove()` は値が存在しない場合に `key error` を発生させます。

```python
# remove() メソッド：要素を削除します。見つからない場合は KeyError を発生させます
s = {1, 2, 3}
s.remove(3)  # 要素 3 を削除
s
```

```output
{1, 2}
```

```python
s.remove(3)
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 3
```

`discard()` はエラーを発生させません。

```python
# discard() メソッド：要素を削除します。見つからなくてもエラーは発生しません
s = {1, 2, 3}
s.discard(3)  # 要素 3 を削除します (安全、欠落してもエラーなし)
s
```

```output
{1, 2}
```

```python
s.discard(3)
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
セットの <code>remove()</code> メソッドと <code>discard()</code> メソッドの違いは何ですか？
</template>

<base-quiz-option value="A">A. <code>remove()</code> は 1 つの要素を削除し、<code>discard()</code> はすべてを削除します</base-quiz-option>
<base-quiz-option value="B">B. 違いはありません</base-quiz-option>
<base-quiz-option value="C" correct>C. <code>remove()</code> は要素が存在しない場合にエラーを発生させますが、<code>discard()</code> は発生させません</base-quiz-option>
<base-quiz-option value="D">D. <code>remove()</code> の方が高速です</base-quiz-option>
<base-quiz-answer value="C">どちらのメソッドもセットから要素を削除しますが、<code>remove()</code> は要素が存在しない場合に <code>KeyError</code> を発生させるのに対し、<code>discard()</code> は要素が欠落していても何もしません。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## set union

`union()` または `|` は、提供されたセットのすべての要素を含む新しいセットを作成します。

```python
# union(): 複数のセットからすべての要素を結合します (重複なし)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.union(s2)  # または 's1 | s2' - {1, 2, 3, 4, 5} を返します
```

```output
{1, 2, 3, 4, 5}
```

## set intersection

`intersection()` または `&` は、すべてのセットに共通する要素のみを含むセットを返します。

```python
# intersection(): すべてのセットに共通する要素を返します
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
s1.intersection(s2, s3)  # または 's1 & s2 & s3' - {3} を返します
```

```output
{3}
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
セットに対して <code>intersection()</code> は何を返しますか？
</template>

<base-quiz-option value="A">A. すべてのセットからのすべての要素</base-quiz-option>
<base-quiz-option value="B" correct>B. すべてのセットに共通する要素のみ</base-quiz-option>
<base-quiz-option value="C">C. 最初のセットには存在するが、他のセットには存在しない要素</base-quiz-option>
<base-quiz-option value="D">D. いずれかのセットには存在するが、両方には存在しない要素</base-quiz-option>
<base-quiz-answer value="B"><code>intersection()</code> メソッドは、比較されているすべてのセットに存在する要素のみを含むセットを返します。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## set difference

`difference()` または `-` は、最初のセット（呼び出し元のセット）に固有の要素のみを返します。

```python
# difference(): 最初のセットには存在するが、他のセットには存在しない要素を返します
s1 = {1, 2, 3}
s2 = {2, 3, 4}

s1.difference(s2)  # または 's1 - s2' - {1} を返します
```

```output
{1}
```

```python
s2.difference(s1) # または 's2 - s1'
```

```output
{4}
```

## set symmetric_difference

`symmetric_difference()` または `^` は、両者に共通しないすべての要素を返します。

```python
# symmetric_difference(): いずれかのセットには存在するが、両方には存在しない要素を返します
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1.symmetric_difference(s2)  # または 's1 ^ s2' - {1, 4} を返します
```

```output
{1, 4}
```

<base-quiz>
<base-quiz-question correct="D">
<template #question>
2 つのセットに対して <code>symmetric_difference()</code> は何を返しますか？
</template>

<base-quiz-option value="A">A. 両方のセットからのすべての要素</base-quiz-option>
<base-quiz-option value="B">B. 両方のセットに共通する要素のみ</base-quiz-option>
<base-quiz-option value="C">C. 最初のセットには存在するが、2 番目のセットには存在しない要素</base-quiz-option>
<base-quiz-option value="D" correct>D. いずれかのセットには存在するが、両方のセットには存在しない要素</base-quiz-option>
<base-quiz-answer value="D"><code>symmetric_difference()</code> メソッドは、いずれかのセットには存在するが、両方のセットには存在しない要素を含むセットを返します。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 関連リンク

- <router-link to="/blog/python-data-types">Python データ型ブログ投稿</router-link>
- <router-link to="/blog/python-sets-what-why-how">Python Sets: What, Why and How</router-link>
- <router-link to="/cheatsheet/dictionaries">Python Dictionaries</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Python Lists and Tuples</router-link>
