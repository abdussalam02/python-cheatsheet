---
title: 'Python 内包表記 - Python チートシート'
description: 'リスト内包表記はリストを簡潔に作成する方法を提供します'
labUrl: 'https://labex.io/ja/labs/python-python-comprehensions-633649?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python 内包表記
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

リスト内包表記は、他のリストからリストを作成できる特殊な構文であり、数値や 1 つまたは 2 つのネストされた for ループを扱う場合に非常に役立ちます。

<base-disclaimer>
  <base-disclaimer-title>
    Python 3 の<a target="_blank" href="https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions">チュートリアル</a>より
  </base-disclaimer-title>
  <base-disclaimer-content>
    リスト内包表記は、リストを作成するための簡潔な方法を提供します。[...] または、特定の条件を満たすそれらの要素のサブシーケンスを作成します。
  </base-disclaimer-content>
</base-disclaimer>

より詳細な入門については、<router-link to="/blog/python-comprehensions-step-by-step">Python 内包表記：ステップバイステップ入門</router-link>をお読みください。

## リスト内包表記

既存のコレクションから新しいリストを作成する方法を For ループで示します。

```python
# 従来の方式：for ループを使用してリストを作成
names = ['Charles', 'Susan', 'Patrick', 'George']

new_list = []
for n in names:
    new_list.append(n)

new_list
```

```output
['Charles', 'Susan', 'Patrick', 'George']
```

そして、リスト内包表記で同じことを行う方法は次のとおりです。

```python
# リスト内包表記：新しいリストを作成するための簡潔な方法
# 構文：[expression for item in iterable]
names = ['Charles', 'Susan', 'Patrick', 'George']

new_list = [n for n in names]  # すべての名前でリストを作成
new_list
```

```output
['Charles', 'Susan', 'Patrick', 'George']
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-comprehensions-1">
<template #question>
リスト内包表記の基本的な構文は何ですか？
</template>

<base-quiz-option value="A" correct>A. <code>[expression for item in iterable]</code></base-quiz-option>
<base-quiz-option value="B">B. <code>(expression for item in iterable)</code></base-quiz-option>
<base-quiz-option value="C">C. <code>{expression for item in iterable}</code></base-quiz-option>
<base-quiz-option value="D">D. <code>expression for item in iterable</code></base-quiz-option>
<base-quiz-answer value="A">リスト内包表記は角括弧 <code>[]</code> を使用し、構文は <code>[expression for item in iterable]</code> です。これにより、各アイテムに式を適用して新しいリストが作成されます。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

数値でも同じことができます。

```python
# ネストされたリスト内包表記：2 つの範囲からタプルを作成
# ネストされた for ループと同等
n = [(a, b) for a in range(1, 3) for b in range(1, 3)]
n
```

```output
[(1, 1), (1, 2), (2, 1), (2, 2)]
```

## 条件の追加

`new_list` に 'C' で始まる名前のみを含めたい場合、for ループでは次のように行います。

```python
# 従来の方式：if 条件でフィルタリング
names = ['Charles', 'Susan', 'Patrick', 'George', 'Carol']

new_list = []
for n in names:
    if n.startswith('C'):  # 'C'で始まる名前をフィルタリング
        new_list.append(n)

print(new_list)
```

```output
['Charles', 'Carol']
```

リスト内包表記では、`if` ステートメントを最後に追加します。

```python
# 条件付きリスト内包表記：アイテムのフィルタリング
# 構文：[expression for item in iterable if condition]
new_list = [n for n in names if n.startswith('C')]
print(new_list)
```

```output
['Charles', 'Carol']
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-comprehensions-2">
<template #question>
リスト内包表記で<code>if</code>条件はどこに配置されますか？
</template>

<base-quiz-option value="A">A. <code>for</code>キーワードの前</base-quiz-option>
<base-quiz-option value="B" correct>B. <code>for</code>句の後</base-quiz-option>
<base-quiz-option value="C">C. 式の中</base-quiz-option>
<base-quiz-option value="D">D. 角括弧の前</base-quiz-option>
<base-quiz-answer value="B">リスト内包表記では、<code>if</code>条件は<code>for</code>句の後に来ます：<code>[expression for item in iterable if condition]</code>。これにより、条件に基づいてアイテムがフィルタリングされます。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

リスト内包表記で `if-else` ステートメントを使用するには：

```python
# if-else 付きリスト内包表記：条件付き式
# 構文：[expression_if_true if condition else expression_if_false for item in iterable]
nums = [1, 2, 3, 4, 5, 6]
new_list = [num*2 if num % 2 == 0 else num for num in nums]  # 偶数を 2 倍にする
print(new_list)
```

```output
[1, 4, 3, 8, 5, 12]
```

<base-disclaimer>
  <base-disclaimer-title>
    セット内包表記と辞書内包表記
  </base-disclaimer-title>
  <base-disclaimer-content>
    <code>list</code>内包表記の基本は、<b>set</b>（集合）と<b>dictionary</b>（辞書）にも適用されます。
  </base-disclaimer-content>
</base-disclaimer>

## セット内包表記

```python
# セット内包表記：内包表記の構文を使用してセットを作成
# 構文：{expression for item in iterable}
b = {"abc", "def"}
{s.upper() for s in b}  # すべての文字列を大文字に変換
```

```output
{"ABC", "DEF"}
```

## 辞書内包表記

```python
# 辞書内包表記：キーと値を入れ替える
# 構文：{key_expression: value_expression for item in iterable}
c = {'name': 'Pooka', 'age': 5}
{v: k for k, v in c.items()}  # キーと値を逆にする
```

```output
{'Pooka': 'name', 5: 'age'}
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-comprehensions-3">
<template #question>
辞書内包表記に使用される構文は何ですか？
</template>

<base-quiz-option value="A">A. <code>[key: value for item in iterable]</code></base-quiz-option>
<base-quiz-option value="B">B. <code>(key: value for item in iterable)</code></base-quiz-option>
<base-quiz-option value="C" correct>C. <code>{key_expression: value_expression for item in iterable}</code></base-quiz-option>
<base-quiz-option value="D">D. <code>{key, value for item in iterable}</code></base-quiz-option>
<base-quiz-answer value="C">辞書内包表記は波括弧 <code>{}</code> を使用し、構文は <code>{key_expression: value_expression for item in iterable}</code> です。これはリスト内包表記に似ていますが、キーと値のペアを使用します。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

辞書からリスト内包表記を生成できます。

```python
# 辞書からのリスト内包表記：フォーマットされた文字列を作成
c = {'name': 'Pooka', 'age': 5}
["{}:{}".format(k.upper(), v) for k, v in c.items()]  # "KEY:value"としてフォーマット
```

```output
['NAME:Pooka', 'AGE:5']
```

## 関連リンク

- <router-link to="/blog/python-comprehensions-step-by-step">Python 内包表記：ステップバイステップ入門</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Python リストとタプル</router-link>
- <router-link to="/cheatsheet/sets">Python セット</router-link>
- <router-link to="/cheatsheet/dictionaries">Python 辞書</router-link>
- <router-link to="/blog/python-sets-what-why-how">Python セット：何、なぜ、どのように</router-link>
- <router-link to="/blog/python-data-types">Python データ型ブログ記事</router-link>
