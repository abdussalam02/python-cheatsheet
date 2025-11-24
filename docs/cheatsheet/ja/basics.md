---
title: 'Python の基礎 - Python チートシート'
description: '演算子、データ型、変数、関数などを網羅した包括的なガイドで Python の基礎を学びましょう。Python プログラミングの基本を学ぶ初心者の方に最適です。'
labUrl: 'https://labex.io/ja/labs/python-python-basics-633647?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python の基本
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

誰もがどこかから始める必要があります。ここでは、その第一歩を踏み出しましょう。このガイドでは、演算子、データ型、変数、およびコア関数を含む基本的な Python の基礎を網羅します。

<base-disclaimer>
<base-disclaimer-title>
Python の基本概要
</base-disclaimer-title>
<base-disclaimer-content>
初心者が知っておくべき Python のコアな基本：

- 変数と基本型
- 演算子と式
- 文字列と一般的なメソッド
- リスト、タプル、辞書
- 基本的な制御フロー（if、for、while）
- 簡単な関数

</base-disclaimer-content>
</base-disclaimer>

## 数学演算子

**最も高い**ものから**最も低い**優先順位まで：

| 演算子 | 操作          | 例              |
| :----- | :------------ | :-------------- |
| \*\*   | べき乗        | `2 ** 3 = 8`    |
| %      | モジュロ/剰余 | `22 % 8 = 6`    |
| //     | 整数除算      | `22 // 8 = 2`   |
| /      | 除算          | `22 / 8 = 2.75` |
| \*     | 乗算          | `3 * 3 = 9`     |
| -      | 減算          | `5 - 2 = 3`     |
| +      | 加算          | `2 + 2 = 4`     |

式の例：

```python
# 乗算は加算よりも優先順位が高い
# したがって、これは次のように評価されます：2 + (3 * 6) = 2 + 18 = 20
2 + 3 * 6
```

```output
20
```

```python
# 丸括弧は演算子の優先順位を上書きします
# これは次のように評価されます：5 * 6 = 30
(2 + 3) * 6
```

```output
30
```

```python
2 ** 8
```

```output
256
```

```python
23 // 7
```

```output
3
```

```python
23 % 7
```

```output
2
```

```python
(5 - 1) * ((7 + 1) / (3 - 1))
```

```output
16.0
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
この Python 式の結果は何ですか？

```python
4 + 2 * 3
```

</template>

<base-quiz-option value="A" correct>A. 10</base-quiz-option>
<base-quiz-option value="B">B. 18</base-quiz-option>
<base-quiz-option value="C">C. 12</base-quiz-option>
<base-quiz-option value="D">D. 20</base-quiz-option>
<base-quiz-answer value="A">乗算は加算よりも優先順位が高いため、これは次のように評価されます：4 + (2 \* 3) = 4 + 6 = 10</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 複合代入演算子

| 演算子      | 同等な記述       |
| :---------- | :--------------- |
| `var += 1`  | `var = var + 1`  |
| `var -= 1`  | `var = var - 1`  |
| `var *= 1`  | `var = var * 1`  |
| `var /= 1`  | `var = var / 1`  |
| `var //= 1` | `var = var // 1` |
| `var %= 1`  | `var = var % 1`  |
| `var **= 1` | `var = var ** 1` |

例：

```python
# 複合代入：greeting = greeting + ' world!' と同等
greeting = 'Hello'
greeting += ' world!'
greeting
```

```output
'Hello world!'
```

```python
# 数値を 1 増やす
number = 1
number += 1
number
```

```output
2
```

```python
# リスト要素の複製：my_list = my_list * 3 と同等
my_list = ['item']
my_list *= 3
my_list
```

```output
['item', 'item', 'item']
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
このコードを実行した後、<code>x</code>の値は何になりますか？

```python
x = 5
x += 3
```

</template>

<base-quiz-option value="A">A. 3</base-quiz-option>
<base-quiz-option value="B" correct>B. 8</base-quiz-option>
<base-quiz-option value="C">C. 5</base-quiz-option>
<base-quiz-option value="D">D. 15</base-quiz-option>
<base-quiz-answer value="B">複合代入演算子 <code>+=</code> は <code>x = x + 3</code> と同等です。したがって、<code>x</code>は 5 から始まり、5 + 3 = 8 になります。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## ウォルラス演算子 (Walrus Operator)

ウォルラス演算子（:=）は、式内で変数に値を代入しつつ、その変数の値を返すことを可能にします。

例：

```python
# ウォルラス演算子は、1 つの式で代入と値の返却を行います
# my_var に "Hello World!" が代入され、その後に出力されます
print(my_var:="Hello World!")
```

```output
Hello World!
```

```python
my_var="Yes"
print(my_var)
```

```output
Yes
```

```python
print(my_var:="Hello")
```

```output
Hello
```

ウォルラス演算子、または**代入式演算子**は、[PEP 572](https://peps.python.org/pep-0572/)によって 2018 年に初めて導入され、2019 年 10 月に**Python 3.8**で正式にリリースされました。

<base-disclaimer>
  <base-disclaimer-title>
    構文のセマンティクスと例
  </base-disclaimer-title>
  <base-disclaimer-content>
  <a href="https://peps.python.org/pep-0572/" target="_blank">PEP 572</a>には、ウォルラス演算子の構文、セマンティクス、および例が記載されています。
  </base-disclaimer-content>
</base-disclaimer>

## データ型

データ型を理解することは、Python の最も重要な基本事項の 1 つです。Python には、必要なもののほぼすべてをカバーする 9 つのコア組み込みデータ型があります。

| データ型                                                   | 例                                       | 説明                                         |
| :--------------------------------------------------------- | :--------------------------------------- | :------------------------------------------- |
| **数値**                                                   |                                          |                                              |
| <router-link to='/builtin/int'>`int`</router-link>         | `-2, -1, 0, 1, 2, 3, 4, 5`               | 整数                                         |
| <router-link to='/builtin/float'>`float`</router-link>     | `-1.25, -1.0, -0.5, 0.0, 0.5, 1.0, 1.25` | 小数点を持つ数値                             |
| <router-link to='/builtin/complex'>`complex`</router-link> | `2+3j, complex(1, 4)`                    | 実部と虚部を持つ数値                         |
| **テキスト**                                               |                                          |                                              |
| <router-link to='/builtin/str'>`str`</router-link>         | `'a', 'Hello!', "Python"`                | テキストと文字                               |
| **ブール値**                                               |                                          |                                              |
| <router-link to='/builtin/bool'>`bool`</router-link>       | `True, False`                            | True または False の値                       |
| **None**                                                   |                                          |                                              |
| `NoneType`                                                 | `None`                                   | 「値なし」または「何もない」を表す           |
| **コレクション**                                           |                                          |                                              |
| <router-link to='/builtin/list'>`list`</router-link>       | `[1, 2, 3], ['a', 'b', 'c']`             | 順序付けられた変更可能なコレクション         |
| <router-link to='/builtin/dict'>`dict`</router-link>       | `{'name': 'Alice', 'age': 30}`           | キーと値のペア                               |
| <router-link to='/builtin/tuple'>`tuple`</router-link>     | `(1, 2, 3), ('a', 'b')`                  | 順序付けられた変更不可能なコレクション       |
| <router-link to='/builtin/set'>`set`</router-link>         | `{1, 2, 3}, {'a', 'b', 'c'}`             | 一意な要素の順序付けられていないコレクション |

### 簡単な例

```python
# 数値
age = 25                    # int
price = 19.99              # float
coordinate = 2 + 3j        # complex

# テキスト
name = "Alice"             # str

# ブール値
is_student = True          # bool

# None
result = None              # NoneType

# コレクション
scores = [85, 92, 78]      # list
person = {'name': 'Bob', 'age': 30}  # dict
coordinates = (10, 20)     # tuple
unique_ids = {1, 2, 3}     # set
```

視覚的な例と、各型を使用すべき場合の詳細な説明については、以下を参照してください：<router-link to="/blog/python-data-types">Python データ型：初心者向けビジュアルガイド</router-link>。

## 連結と複製

文字列の連結：

```python
# 文字列の連結：隣接する文字列は自動的に結合されます
'Alice' 'Bob'
```

```output
'AliceBob'
```

文字列の複製：

```python
# 文字列の複製：文字列を複数回繰り返します
'Alice' * 5
```

```output
'AliceAliceAliceAliceAlice'
```

## 変数

変数は Python の基本の基礎です。以下のルールに従う限り、変数は任意の名前を付けることができます。

1. 1 語でなければならない。

```python
# bad
my variable = 'Hello'

# good
var = 'Hello'
```

2. 英字、数字、アンダースコア（`_`）文字のみを使用できる。

```python
# bad
%$@variable = 'Hello'

# good
my_var = 'Hello'

# good
my_var_2 = 'Hello'
```

3. 数字で始めることはできない。

```python
# これは機能しません
23_var = 'hello'
```

4. アンダースコア（`_`）で始まる変数名は「未使用」と見なされます。

```python
# _spam はコード内で再利用されるべきではない
_spam = 'Hello'
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
Python の基本において、次のうち有効な変数名はどれですか？
</template>

<base-quiz-option value="A">A. <code>3value</code></base-quiz-option>
<base-quiz-option value="B">B. <code>user-name</code></base-quiz-option>
<base-quiz-option value="C" correct>C. <code>user_name</code></base-quiz-option>
<base-quiz-option value="D">D. <code>for</code></base-quiz-option>
<base-quiz-answer value="C"><code>user_name</code>は、英字、数字、アンダースコアのみを使用し、数字で始まらないため、有効な変数名です。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## コメント

インラインコメント：

```python
# これはコメントです
```

複数行コメント：

```python
# これは
# 複数行コメントです
```

コメント付きのコード：

```python
a = 1  # 初期化
```

コメントの前に 2 つのスペースがあることに注意してください。

関数の docstring：

```python
def foo():
    """
    これは関数の docstring です
    次のように使用することもできます：
    ''' 関数の Docstring '''
    """
```

## print() 関数

`print()` 関数は、学習する最初の Python の基本事項の 1 つです。引数として与えられた値を書き出します。[...] 複数の引数、浮動小数点数、および文字列を処理します。文字列は引用符なしで印刷され、項目間にはスペースが挿入されるため、きれいに整形できます。

```python
print('Hello world!')
```

```output
Hello world!
```

```python
a = 1
print('Hello world!', a)
```

```output
Hello world! 1
```

### end キーワード

キーワード引数 `end` を使用すると、出力後の改行を回避したり、出力を別の文字列で終了させたりできます。

```python
# end パラメータを使用して、各 print ステートメントの後に続くものを変更します
phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
for word in phrase:
    print(word, end='-')  # 改行の代わりに '-' を使用
```

```output
printed-with-a-dash-in-between-
```

### sep キーワード

キーワード `sep` は、複数のオブジェクトがある場合に、それらを区切る方法を指定します。

```python
# sep パラメータを使用して、複数の引数間の区切り文字を指定します
print('cats', 'dogs', 'mice', sep=',')  # カンマ区切りの出力
```

```output
cats,dogs,mice
```

## input() 関数

この関数はユーザーからの入力を受け取り、それを文字列に変換します。

```python
# input() はユーザー入力を読み取り、文字列として返します
print('What is your name?')   # 名前を尋ねる
my_name = input()  # ユーザーが入力して Enter を押すのを待つ
print('Hi, {}'.format(my_name))
```

```output
What is your name?
Martha
Hi, Martha
```

`input()` は `print()` を使用せずにデフォルトのメッセージを設定することもできます。

```python
my_name = input('What is your name? ')  # プロンプトメッセージ
print('Hi, {}'.format(my_name))
```

```output
What is your name? Martha
Hi, Martha
```

.format を使用せずに、フォーマット済み文字列を使用することも可能です。

```python
# input() はプロンプトメッセージを直接表示できます
my_name = input('What is your name? ')  # プロンプトと読み取りを 1 回の呼び出しで
print(f'Hi, {my_name}')  # 文字列フォーマットのための f-string
```

```output
What is your name? Martha
Hi, Martha
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Python の基本において、`input()` は何を返しますか？
</template>

<base-quiz-option value="A">A. int</base-quiz-option>
<base-quiz-option value="B" correct>B. str</base-quiz-option>
<base-quiz-option value="C">C. float</base-quiz-option>
<base-quiz-option value="D">D. ユーザー入力による</base-quiz-option>
<base-quiz-answer value="B"><code>input()</code>関数は、ユーザーが入力した内容に関わらず、常に文字列を返します。必要に応じて他の型に変換する必要があります。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## len() 関数

文字列、リスト、辞書などの文字数または要素数を整数値で評価します。

```python
# len() は文字列内の文字数を返します
len('hello')  # 5 を返します
```

```output
5
```

```python
# len() はリスト内の要素数を返します
len(['cat', 3, 'dog'])  # 3 を返します (3 つの要素)
```

```output
3
```

<base-warning>
  <base-warning-title>空のテスト</base-warning-title>
  <base-warning-content>
    文字列、リスト、辞書などの空のテストには、<code>len</code>を使用するのではなく、直接的なブール評価を優先すべきです。
  </base-warning-content>
</base-warning>

空のテストの例：

```python
a = [1, 2, 3]

# bad: 不要な len() チェック
if len(a) > 0:  # True と評価される
    print("the list is not empty!")
```

```output
the list is not empty!
```

```python
# good: 直接的なブール評価 (Pythonic な方法)
if a:  # リストが空でない場合に True と評価される
    print("the list is not empty!")
```

```output
the list is not empty!
```

## str(), int(), float() 関数

これらの関数を使用すると、変数の型を変更できます。例えば、`integer`や`float`から`string`に変換できます。

```python
# 整数を文字列に変換
str(29)  # '29'を返します
```

```output
'29'
```

```python
str(-3.14)
```

```output
'-3.14'
```

または、`string`から`integer`や`float`に変換します。

```python
# 文字列を整数に変換
int('11')  # 11 を返します
```

```output
11
```

```python
# 文字列を浮動小数点数に変換
float('3.14')  # 3.14 を返します
```

```output
3.14
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
この Python コードの結果は何ですか？

```python
result = int('42')
type(result)
```

</template>

<base-quiz-option value="A">A. <code>str</code></base-quiz-option>
<base-quiz-option value="B">B. <code>float</code></base-quiz-option>
<base-quiz-option value="C" correct>C. <code>int</code></base-quiz-option>
<base-quiz-option value="D">D. <code>NoneType</code></base-quiz-option>
<base-quiz-answer value="C"><code>int()</code>関数は文字列を整数に変換します。したがって、<code>int('42')</code>は整数<code>42</code>を返し、<code>type(42)</code>は<code>int</code>を返します。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 関連リンク

- <router-link to="/blog/python-data-types">Python データ型：初心者向けビジュアルガイド</router-link>
- <router-link to="/blog/python-comprehensions-step-by-step">Python 内包表記 ステップバイステップ</router-link>
- <router-link to="/cheatsheet/control-flow">制御フロー</router-link>
- <router-link to="/cheatsheet/functions">関数</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">リストとタプル</router-link>
- <router-link to="/cheatsheet/dictionaries">辞書</router-link>
- <router-link to="/cheatsheet/sets">セット</router-link>
- <router-link to="/cheatsheet/string-formatting">文字列のフォーマット</router-link>
