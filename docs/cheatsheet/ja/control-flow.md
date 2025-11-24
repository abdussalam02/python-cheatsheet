---
title: 'Python 制御フロー - Python チートシート'
description: '制御フローとは、個々の文、命令、または関数呼び出しが実行または評価される順序です。Python プログラムの制御フローは、条件文、ループ、および関数呼び出しによって制御されます。'
labUrl: 'https://labex.io/ja/labs/python-python-control-flow-633651?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python 制御フロー
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    Python 制御フロー
  </base-disclaimer-title>
  <base-disclaimer-content>
  制御フローとは、個々のステートメント、命令、または関数呼び出しが実行または評価される順序のことです。Python プログラムの制御フローは、条件文、ループ、および関数呼び出しによって制御されます。
  </base-disclaimer-content>
</base-disclaimer>

## 比較演算子

| 演算子 | 意味                            |
| ------ | ------------------------------- |
| `==`   | 等しい (Equal to)               |
| `!=`   | 等しくない (Not equal to)       |
| `<`    | 未満 (Less than)                |
| `>`    | より大きい (Greater Than)       |
| `<=`   | 以下 (Less than or Equal to)    |
| `>=`   | 以上 (Greater than or Equal to) |

これらの演算子は、与えられた値に応じて True または False を評価します。

例：

```python
42 == 42
```

```output
True
```

```python
40 == 42
```

```output
False
```

```python
'hello' == 'hello'
```

```output
True
```

```python
'hello' == 'Hello'
```

```output
False
```

```python
'dog' != 'cat'
```

```output
True
```

```python
42 == 42.0
```

```output
True
```

```python
42 == '42'
```

```output
False
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
<code>'hello' == 'Hello'</code> は何と評価されますか？
</template>

<base-quiz-option value="A">A. <code>True</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>False</code></base-quiz-option>
<base-quiz-option value="C">C. <code>None</code></base-quiz-option>
<base-quiz-option value="D">D. エラーを発生させる</base-quiz-option>
<base-quiz-answer value="B">Python での文字列比較は大文字と小文字を区別します。<code>'hello'</code> と <code>'Hello'</code> は異なる文字列であるため、比較結果は <code>False</code> になります。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## ブール演算子

3 つのブール演算子があります：`and`、`or`、`not`。
優先順位は、高い方から低い方へ `not`、`and`、`or` の順です。

`and` 演算子の**真理値表**:

| 式                | 評価結果 |
| ----------------- | -------- |
| `True and True`   | `True`   |
| `True and False`  | `False`  |
| `False and True`  | `False`  |
| `False and False` | `False`  |

`or` 演算子の**真理値表**:

| 式               | 評価結果 |
| ---------------- | -------- |
| `True or True`   | `True`   |
| `True or False`  | `True`   |
| `False or True`  | `True`   |
| `False or False` | `False`  |

`not` 演算子の**真理値表**:

| 式          | 評価結果 |
| ----------- | -------- |
| `not True`  | `False`  |
| `not False` | `True`   |

## 演算子の組み合わせ

ブール演算子と比較演算子を組み合わせることができます：

```python
(4 < 5) and (5 < 6)
```

```output
True
```

```python
(4 < 5) and (9 < 6)
```

```output
False
```

```python
(1 == 2) or (2 == 2)
```

```output
True
```

また、比較演算子とともに複数のブール演算子を式内で使用することもできます：

```python
2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
```

```output
True
```

```python
# 以下のステートメントでは、最初に 3 < 4 and 5 > 5 が実行され False と評価されます。
# 次に 5 > 4 が True を返すため、True or False の結果は True になります。
5 > 4 or 3 < 4 and 5 > 5
```

```output
True
```

```python
# ここでは、括弧内のステートメントが最初に実行されるため、True and False は False を返します。
(5 > 4 or 3 < 4) and 5 > 5
```

```output
False
```

## if 文

`if` 文は式を評価し、その式が `True` の場合、それに続くインデントされたコードを実行します：

```python
# if 文：条件が True の場合にコードブロックを実行
name = 'Debora'

if name == 'Debora':  # name が'Debora'と等しいかチェック
   print('Hi, Debora')  # 条件が True の場合にこの行が実行される
```

```output
Hi, Debora
```

```python
if name != 'George':
   print('You are not George')
```

```output
You are not George
```

`else` 文は、`if` およびすべての `elif` 式の評価が `False` の場合にのみ実行されます：

```python
# if-else: 条件に基づいて異なるコードを実行
name = 'Debora'

if name == 'George':
   print('Hi, George.')
else:  # if 条件が False の場合に実行
   print('You are not George')
```

```output
You are not George
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
if-else ステートメントで <code>else</code> ブロックはいつ実行されますか？
</template>

<base-quiz-option value="A">A. 常に</base-quiz-option>
<base-quiz-option value="B" correct>B. <code>if</code> 条件（および存在するすべての <code>elif</code> 条件）が <code>False</code> の場合のみ</base-quiz-option>
<base-quiz-option value="C">C. <code>if</code> 条件が <code>True</code> の場合のみ</base-quiz-option>
<base-quiz-option value="D">D. 実行されない</base-quiz-option>
<base-quiz-answer value="B"><code>else</code> ブロックは、<code>if</code> 条件および（存在するならば）すべての <code>elif</code> 条件が <code>False</code> と評価された場合にのみ実行されます。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

`if` 文の式が `False` になった後にのみ、`elif` 文が評価され実行されます：

```python
# if-elif: 複数の条件を順番にチェック
name = 'George'

if name == 'Debora':
   print('Hi Debora!')
elif name == 'George':  # 前の条件が False の場合にのみチェックされる
   print('Hi George!')
```

```output
Hi George!
```

`elif` および `else` 部分はオプションです。

```python
name = 'Antony'

if name == 'Debora':
   print('Hi Debora!')
elif name == 'George':
   print('Hi George!')
else:
   print('Who are you?')
```

```output
Who are you?
```

## 三項条件演算子

多くのプログラミング言語には、条件式を定義する三項演算子があります。最も一般的な使用法は、簡潔な単純な条件付き代入ステートメントを作成することです。言い換えると、条件が真の場合に最初の式を評価し、そうでない場合に 2 番目の式を評価する一行コードを提供します。

```plaintext
<expression1> if <condition> else <expression2>
```

例：

```python
age = 15

# この if 文：
if age < 18:
   print('kid')
else:
   print('adult')
```

```output
kid
```

```python
# 三項演算子：一行の条件式
# 構文：value_if_true if condition else value_if_false
print('kid' if age < 18 else 'adult')
```

```output
kid
```

三項演算子は連鎖させることができます：

```python
age = 15

# この三項演算子：
print('kid' if age < 13 else 'teen' if age < 18 else 'adult')
```

```output
teen
```

```python
# この if 文と同等です：
if age < 13:
    print('kid')
else:
    if age < 18:
        print('teen')
    else:
        print('adult')
```

```output
teen
```

## Switch-Case ステートメント

<base-disclaimer>
  <base-disclaimer-title>
    Switch-Case ステートメント
  </base-disclaimer-title>
  <base-disclaimer-content>
  コンピュータプログラミング言語において、switch ステートメントは、検索とマッピングを通じてプログラム実行の制御フローを変更できるようにするために使用される、選択制御メカニズムの一種です。
  </base-disclaimer-content>
</base-disclaimer>

**構造的パターンマッチング**としての*Switch-Case ステートメント*は、2020 年に[PEP 622](https://peps.python.org/pep-0622/)を通じて初めて導入され、2022 年 9 月に**Python 3.10**で正式にリリースされました。

<base-disclaimer>
  <base-disclaimer-title>
    公式チュートリアル
  </base-disclaimer-title>
  <base-disclaimer-content>
  <a href="https://peps.python.org/pep-0636/" target="_blank">PEP 636</a>は、Python のパターンマッチングまたは Switch-Case ステートメントの公式チュートリアルを提供します。
  </base-disclaimer-content>
</base-disclaimer>

### 単一値のマッチング

```python
response_code = 201
match response_code:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 300:
        print("Multiple Choices")
    case 307:
        print("Temporary Redirect")
    case 404:
        print("404 Not Found")
    case 500:
        print("Internal Server Error")
    case 502:
        print("502 Bad Gateway")
```

```output
Created
```

### or パターンでのマッチング

この例では、パイプ文字 (`|` または `or`) により、Python は 2 つ以上のケースに対して同じ応答を返すことができます。

```python
response_code = 502
match response_code:
    case 200 | 201:
        print("OK")
    case 300 | 307:
        print("Redirect")
    case 400 | 401:
        print("Bad Request")
    case 500 | 502:
        print("Internal Server Error")
```

```output
Internal Server Error
```

### イテラブル（反復可能オブジェクト）の長さによるマッチング

```python
today_responses = [200, 300, 404, 500]
match today_responses:
    case [a]:
            print(f"One response today: {a}")
    case [a, b]:
            print(f"Two responses today: {a} and {b}")
    case [a, b, *rest]:
            print(f"All responses: {a}, {b}, {rest}")
```

```output
All responses: 200, 300, [404, 500]
```

### デフォルト値

アンダースコア記号 (`_`) は、デフォルトのケースを定義するために使用されます：

```python
response_code = 800
match response_code:
    case 200 | 201:
        print("OK")
    case 300 | 307:
        print("Redirect")
    case 400 | 401:
        print("Bad Request")
    case 500 | 502:
        print("Internal Server Error")
    case _:
        print("Invalid Code")
```

```output
Invalid Code
```

### 組み込みクラスによるマッチング

```python
response_code = "300"
match response_code:
    case int():
            print('Code is a number')
    case str():
            print('Code is a string')
    case _:
            print('Code is neither a string nor a number')
```

```output
Code is a string
```

### Match-Case ステートメントのガード

```python
response_code = 300
match response_code:
    case int() if response_code > 99 and response_code < 500:
            print('Code is a valid number')
    case _:
            print('Code is an invalid number')
```

```output
Code is a valid number
```

## while ループ ステートメント

while ステートメントは、式が `True` である限りコードを繰り返し実行するために使用されます：

```python
# while ループ：条件が True である限りコードを繰り返す
spam = 0
while spam < 5:  # spam が 5 未満の間、継続
    print('Hello, world.')
    spam = spam + 1  # 無限ループを避けるためにカウンターをインクリメント
```

```output
Hello, world.
Hello, world.
Hello, world.
Hello, world.
Hello, world.
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
<code>while</code> ループは何をしますか？
</template>

<base-quiz-option value="A" correct>A. 条件が <code>True</code> である限りコードを繰り返す</base-quiz-option>
<base-quiz-option value="B">B. コードを正確に 1 回実行する</base-quiz-option>
<base-quiz-option value="C">C. コードを固定回数実行する</base-quiz-option>
<base-quiz-option value="D">D. コードの実行をスキップする</base-quiz-option>
<base-quiz-answer value="A"><code>while</code> ループは、条件が <code>True</code> と評価されている限り、コードブロックを繰り返し実行します。条件が <code>False</code> になると、ループは停止します。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## break ステートメント

実行が `break` ステートメントに到達すると、`while` ループの句から直ちに抜けます：

```python
# break ステートメント：発見されたらループを直ちに終了
while True:  # 無限ループ
    name = input('Please type your name: ')
    if name == 'your name':
        break  # ループを直ちに終了

print('Thank you!')
```

```output
Please type your name: your name
Thank you!
```

## continue ステートメント

プログラムの実行が `continue` ステートメントに到達すると、プログラムの実行は直ちにループの先頭にジャンプします。

```python
# continue ステートメント：ループイテレーションの残りをスキップし、次のイテレーションを開始
while True:
    name = input('Who are you? ')
    if name != 'Joe':
        continue  # 次のイテレーションにスキップし、パスワードを尋ねない
    password = input('Password? (It is a fish.): ')
    if password == 'swordfish':
        break  # パスワードが正しい場合にループを終了

print('Access granted.')
```

```output
Who are you? Charles
Who are you? Debora
Who are you? Joe
Password? (It is a fish.): swordfish
Access granted.
```

## For ループ

`for` ループは、`list`、`tuple`、`dictionary`、`set`、または `string` を反復処理します：

```python
# for ループ：シーケンス内の各アイテムを反復処理
pets = ['Bella', 'Milo', 'Loki']
for pet in pets:  # リスト内の各ペットをループ
    print(pet)  # 各ペットの名前を出力
```

```output
Bella
Milo
Loki
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
<code>for</code> ループは何を反復処理しますか？
</template>

<base-quiz-option value="A">A. 数値のみ</base-quiz-option>
<base-quiz-option value="B">B. 文字列のみ</base-quiz-option>
<base-quiz-option value="C" correct>C. すべての反復可能なシーケンス（リスト、タプル、辞書、セット、文字列など）</base-quiz-option>
<base-quiz-option value="D">D. リストのみ</base-quiz-option>
<base-quiz-answer value="C"><code>for</code> ループは、リスト、タプル、辞書、セット、文字列、その他の反復可能なオブジェクトを含む、あらゆる反復可能なシーケンスを反復処理できます。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## range() 関数

`range()` 関数は数値のシーケンスを返します。0 から始まり、1 ずつ増加し、指定された数より前で停止します：

```python
for i in range(5):
    print(f'Will stop at 5! or 4? ({i})')
```

```output
Will stop at 5! or 4? (0)
Will stop at 5! or 4? (1)
Will stop at 5! or 4? (2)
Will stop at 5! or 4? (3)
Will stop at 5! or 4? (4)
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
<code>range(5)</code> は何を生成しますか？
</template>

<base-quiz-option value="A">A. 1 から 5 までの数値</base-quiz-option>
<base-quiz-option value="B" correct>B. 0 から 4 までの数値</base-quiz-option>
<base-quiz-option value="C">C. 0 から 5 までの数値</base-quiz-option>
<base-quiz-option value="D">D. 5 つのランダムな数値</base-quiz-option>
<base-quiz-answer value="B"><code>range(5)</code> 関数は、0 から 4 までの数値を生成します（合計 5 個の数値）。停止値は排他的であるため、5 に達する前に停止します。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

`range()` 関数は、3 つのデフォルト引数（`start`、`stop`、`step`）を変更することもできます。最初の 2 つが `start` と `stop` 値になり、3 番目が `step` 引数になります。ステップは、各イテレーション後に変数がどれだけ増加するかを示す量です。

```python
# range(start, stop, step)
for i in range(0, 10, 2):
   print(i)
```

```output
0
2
4
6
8
```

ステップ引数に負の数を使用すると、for ループを上向きではなく下向きにカウントさせることができます。

```python
for i in range(5, -1, -1):
    print(i)
```

```output
5
4
3
2
1
0
```

## For else ステートメント

これにより、ループ全体が実行された場合に実行するステートメントを指定できます。ループ内で `break` 条件が発生する可能性がある場合にのみ便利です：

```python
for i in [1, 2, 3, 4, 5]:
   if i == 3:
       break
else:
   print("only executed when no item is equal to 3")
```

## sys.exit() によるプログラムの終了

`exit()` 関数は Python を終了させることができます。

```python
import sys

while True:
    feedback = input('Type exit to exit: ')
    if feedback == 'exit':
        print(f'You typed {feedback}.')
        sys.exit()
```

```output
Type exit to exit: open
Type exit to exit: close
Type exit to exit: exit
You typed exit.
```

## 関連リンク

- <router-link to="/cheatsheet/basics">基本</router-link>
- <router-link to="/cheatsheet/functions">関数</router-link>
- <router-link to="/cheatsheet/exception-handling">例外処理</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">リストとタプル</router-link>
- <router-link to="/cheatsheet/sets">セット</router-link>
- <router-link to="/cheatsheet/dictionaries">辞書</router-link>
- <router-link to="/cheatsheet/comprehensions">内包表記</router-link>
