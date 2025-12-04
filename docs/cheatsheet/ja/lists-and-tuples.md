---
title: 'Python リストとタプル - Python チートシート'
description: 'Python のリストは、データを格納するために使用される 4 つのデータ型の一つです。'
labUrl: 'https://labex.io/ja/labs/python-python-lists-and-tuples-633660?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python リスト
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

リストは、Python にあるデータを格納するための 4 つのデータ型のうちの 1 つです。

```python
# List: 角括弧で囲まれた順序付けられたアイテムのコレクション
['John', 'Peter', 'Debora', 'Charles']
```

## インデックスを使用した値の取得

```python
# インデックスを使用してリスト要素にアクセス (0 から始まる、最初の要素はインデックス 0)
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[0]  # 最初の要素を返します：'table'
```

```output
'table'
```

```python
furniture[1]
```

```output
'chair'
```

```python
furniture[2]
```

```output
'rack'
```

```python
furniture[3]
```

```output
'shelf'
```

## 負のインデックス

```python
# 負のインデックス：リストの末尾から要素にアクセス
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[-1]  # 最後の要素を返します：'shelf'
```

```output
'shelf'
```

```python
furniture[-3]
```

```output
'chair'
```

```python
f'The {furniture[-1]} is bigger than the {furniture[-3]}'
```

```output
'The shelf is bigger than the chair'
```

<BaseQuiz id="cheatsheet-lists-and-tuples-1" correct="B">
<template #question>
<code>furniture = ['table', 'chair', 'rack', 'shelf']</code> の場合、<code>furniture[-1]</code> は何を返しますか？
</template>

<BaseQuizOption value="A">A. <code>'table'</code></BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>'shelf'</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>['shelf']</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>IndexError</code></BaseQuizOption>
<BaseQuizAnswer>負のインデックスはリストの末尾から要素にアクセスします。<code>-1</code> は最後の要素を指し、<code>-2</code> は最後から 2 番目の要素を指します。</BaseQuizAnswer>
</BaseQuiz>

## スライスを使用したサブリストの取得

```python
# スライス：[start:end] 構文を使用してサブリストを取得します (end は排他的)
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[0:4]  # インデックス 0 から 3 までの要素を返します (4 は含まない)
```

```output
['table', 'chair', 'rack', 'shelf']
```

```python
furniture[1:3]
```

```output
['chair', 'rack']
```

```python
furniture[0:-1]
```

```output
['table', 'chair', 'rack']
```

```python
# 先頭からのスライス：start インデックスを省略 (デフォルトは 0)
furniture[:2]  # 最初の 2 つの要素を返します
```

```output
['table', 'chair']
```

```python
# 末尾までのスライス：end インデックスを省略 (デフォルトはリストの末尾)
furniture[1:]  # インデックス 1 から末尾まですべての要素を返します
```

```output
['chair', 'rack', 'shelf']
```

```python
furniture[:]
```

```output
['table', 'chair', 'rack', 'shelf']
```

リスト全体をスライスするとコピーが作成されます：

```python
# スライスはコピーを作成します：[:] はリストのシャローコピーを作成します
spam = ['cat', 'bat', 'rat', 'elephant']
spam2 = spam[:]  # 参照ではなくコピーを作成
spam2
```

```output
['cat', 'bat', 'rat', 'elephant']
```

```python
spam.append('dog')
spam
```

```output
['cat', 'bat', 'rat', 'elephant', 'dog']
```

```python
spam2
```

```output
['cat', 'bat', 'rat', 'elephant']
```

<BaseQuiz id="cheatsheet-lists-and-tuples-2" correct="C">
<template #question>
<code>spam</code> がリストである場合、<code>spam[:]</code> は何を作成しますか？
</template>

<BaseQuizOption value="A">A. 同じリストへの参照</BaseQuizOption>
<BaseQuizOption value="B">B. 空のリスト</BaseQuizOption>
<BaseQuizOption value="C" correct>C. リストのシャローコピー</BaseQuizOption>
<BaseQuizOption value="D">D. 逆順のリスト</BaseQuizOption>
<BaseQuizAnswer>リスト全体を <code>[:]</code> でスライスするとシャローコピーが作成されます。コピーを変更しても元のリストには影響しません。</BaseQuizAnswer>
</BaseQuiz>

## len() を使用したリストの長さの取得

```python
# len() はリスト内のアイテムの数を返します
furniture = ['table', 'chair', 'rack', 'shelf']
len(furniture)  # 4 を返します
```

```output
4
```

## インデックスを使用した値の変更

```python
# インデックスに新しい値を代入してリスト要素を変更します
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[0] = 'desk'  # 最初の要素を置き換えます
furniture
```

```output
['desk', 'chair', 'rack', 'shelf']
```

```python
furniture[2] = furniture[1]
furniture
```

```output
['desk', 'chair', 'chair', 'shelf']
```

```python
furniture[-1] = 'bed'
furniture
```

```output
['desk', 'chair', 'chair', 'bed']
```

## 連結と複製

```python
# リストの連結：+ 演算子を使用して 2 つのリストを結合します
[1, 2, 3] + ['A', 'B', 'C']  # [1, 2, 3, 'A', 'B', 'C'] を返します
```

```output
[1, 2, 3, 'A', 'B', 'C']
```

```python
# リストの複製：* 演算子を使用してリストを複数回繰り返します
['X', 'Y', 'Z'] * 3  # ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z'] を返します
```

```output
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
```

```python
my_list = [1, 2, 3]
my_list = my_list + ['A', 'B', 'C']
my_list
```

```output
[1, 2, 3, 'A', 'B', 'C']
```

## for ループとリストの使用

```python
# for ループを使用してリスト要素を反復処理します
furniture = ['table', 'chair', 'rack', 'shelf']

for item in furniture:  # 各アイテムをループします
    print(item)
```

```output
table
chair
rack
shelf
```

## enumerate() を使用したループでのインデックスの取得

```python
# enumerate() はループ内でインデックスと値の両方を返します
furniture = ['table', 'chair', 'rack', 'shelf']

for index, item in enumerate(furniture):  # インデックスとアイテムを同時に取得
    print(f'index: {index} - item: {item}')
```

```output
index: 0 - item: table
index: 1 - item: chair
index: 2 - item: rack
index: 3 - item: shelf
```

## zip() を使用した複数のリストのループ

```python
# zip() は複数のリストを要素ごとに結合してループします
furniture = ['table', 'chair', 'rack', 'shelf']
price = [100, 50, 80, 40]

for item, amount in zip(furniture, price):  # 両方のリストから要素をペアにします
    print(f'The {item} costs ${amount}')
```

```output
The table costs $100
The chair costs $50
The rack costs $80
The shelf costs $40
```

## in および not in 演算子

```python
# in 演算子：アイテムがリスト内に存在するかどうかを確認します
'rack' in ['table', 'chair', 'rack', 'shelf']  # True を返します
```

```output
True
```

```python
'bed' in ['table', 'chair', 'rack', 'shelf']
```

```output
False
```

```python
furniture = ['table', 'chair', 'rack', 'shelf']
'bed' not in furniture
```

```output
True
```

```python
'rack' not in furniture
```

```output
False
```

## 多重代入のトリック

多重代入のトリックは、1 行のコードでリスト内の複数の変数に値を代入するためのショートカットです。次のように行う代わりに：

```python
furniture = ['table', 'chair', 'rack', 'shelf']
table = furniture[0]
chair = furniture[1]
rack = furniture[2]
shelf = furniture[3]
```

次のコードを記述できます：

```python
furniture = ['table', 'chair', 'rack', 'shelf']
table, chair, rack, shelf = furniture

table
```

```output
'table'
```

```python
chair
```

```output
'chair'
```

```python
rack
```

```output
'rack'
```

```python
shelf
```

```output
'shelf'
```

多重代入のトリックは、2 つの変数の値を交換するためにも使用できます：

```python
a, b = 'table', 'chair'
a, b = b, a
print(a)
```

```output
chair
```

```python
print(b)
```

```output
table
```

## index メソッド

`index` メソッドを使用すると、値の名前を渡すことでその値のインデックスを見つけることができます：

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.index('chair')
```

```output
1
```

## 値の追加

### append()

`append` はリストの末尾に要素を追加します：

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.append('bed')
furniture
```

```output
['table', 'chair', 'rack', 'shelf', 'bed']
```

<BaseQuiz id="cheatsheet-lists-and-tuples-3" correct="A">
<template #question>
<code>append()</code> メソッドはリストに対して何を行いますか？
</template>

<BaseQuizOption value="A" correct>A. リストの末尾に要素を追加する</BaseQuizOption>
<BaseQuizOption value="B">B. リストの先頭に要素を追加する</BaseQuizOption>
<BaseQuizOption value="C">C. 最後の要素を置き換える</BaseQuizOption>
<BaseQuizOption value="D">D. 最後の要素を削除する</BaseQuizOption>
<BaseQuizAnswer><code>append()</code> メソッドは単一の要素をリストの末尾に追加します。特定の位置に要素を追加するには、<code>insert()</code> を使用します。</BaseQuizAnswer>
</BaseQuiz>

### insert()

`insert` は指定された位置にリストに要素を追加します：

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.insert(1, 'bed')
furniture
```

```output
['table', 'bed', 'chair', 'rack', 'shelf']
```

## 値の削除

### del

`del` はインデックスを使用してアイテムを削除します：

```python
furniture = ['table', 'chair', 'rack', 'shelf']
del furniture[2]
furniture
```

```output
['table', 'chair', 'shelf']
```

```python
del furniture[2]
furniture
```

```output
['table', 'chair']
```

### remove()

`remove` は実際の値を使用してアイテムを削除します：

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.remove('chair')
furniture
```

```output
['table', 'rack', 'shelf']
```

<base-warning>
  <base-warning-title>
    繰り返し出現するアイテムの削除
  </base-warning-title>
  <base-warning-content>
    値がリスト内に複数回出現する場合、その値の最初の出現箇所のみが削除されます。
  </base-warning-content>
</base-warning>

### pop()

デフォルトでは、`pop` はリストの最後のアイテムを削除して返します。オプションのパラメーターとして要素のインデックスを渡すこともできます：

```python
animals = ['cat', 'bat', 'rat', 'elephant']

animals.pop()
```

```output
'elephant'
```

```python
animals
```

```output
['cat', 'bat', 'rat']
```

```python
animals.pop(0)
```

```output
'cat'
```

```python
animals
```

```output
['bat', 'rat']
```

<BaseQuiz id="cheatsheet-lists-and-tuples-4" correct="B">
<template #question>
リストに対して <code>pop()</code> を呼び出すと、何が起こりますか？
</template>

<BaseQuizOption value="A">A. 最後のアイテムのみを削除する</BaseQuizOption>
<BaseQuizOption value="B" correct>B. アイテムを削除して返す (デフォルトは最後のアイテム、または指定されたインデックス)</BaseQuizOption>
<BaseQuizOption value="C">C. 最後のアイテムのみを返し、削除はしない</BaseQuizOption>
<BaseQuizOption value="D">D. リストからすべてのアイテムを削除する</BaseQuizOption>
<BaseQuizAnswer><code>pop()</code> メソッドはアイテムを削除して返します。デフォルトでは最後のアイテムを削除しますが、インデックスを渡して特定のアイテムを削除することもできます。</BaseQuizAnswer>
</BaseQuiz>

## sort() を使用した値のソート

```python
numbers = [2, 5, 3.14, 1, -7]
numbers.sort()
numbers
```

```output
[-7, 1, 2, 3.14, 5]
```

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.sort()
furniture
```

```output
['chair', 'rack', 'shelf', 'table']
```

`reverse` キーワード引数に `True` を渡すことで、値を逆順にソートすることもできます：

```python
furniture.sort(reverse=True)
furniture
```

```output
['table', 'shelf', 'rack', 'chair']
```

通常のアルファベット順に値をソートする必要がある場合は、sort() メソッド呼び出しで key キーワード引数に <code>str.lower</code> を渡します：

```python
letters = ['a', 'z', 'A', 'Z']
letters.sort(key=str.lower)
letters
```

```output
['a', 'A', 'z', 'Z']
```

組み込み関数 `sorted` を使用すると、新しいリストを返すことができます：

```python
furniture = ['table', 'chair', 'rack', 'shelf']
sorted(furniture)
```

```output
['chair', 'rack', 'shelf', 'table']
```

## タプル (Tuple) データ型

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://stackoverflow.com/questions/1708510/list-vs-tuple-when-to-use-each">タプルとリスト</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    タプルとリストの主な違いは、<code>タプル</code>が<i>イミュータブル</i>（変更不可能）なオブジェクトであるのに対し、<code>リスト</code>は<i>ミュータブル</i>（変更可能）であるという点です。これは、リストは変更できますが、タプルは変更できないことを意味します。タプルはリストよりもメモリ効率が良いです。
  </base-disclaimer-content>
</base-disclaimer>

```python
furniture = ('table', 'chair', 'rack', 'shelf')

furniture[0]
```

```output
'table'
```

```python
furniture[1:3]
```

```output
('chair', 'rack')
```

```python
len(furniture)
```

```output
4
```

タプルがリストと異なる主な点は、文字列と同様にタプルがイミュータブルであることです。

## list() および tuple() 間の変換

```python
tuple(['cat', 'dog', 5])
```

```output
('cat', 'dog', 5)
```

```python
list(('cat', 'dog', 5))
```

```output
['cat', 'dog', 5]
```

```python
list('hello')
```

```output
['h', 'e', 'l', 'l', 'o']
```

<BaseQuiz id="cheatsheet-lists-and-tuples-5" correct="C">
<template #question>
Python のリストとタプルの主な違いは何ですか？
</template>

<BaseQuizOption value="A">A. リストは数値のみを含むことができ、タプルは何でも含むことができる</BaseQuizOption>
<BaseQuizOption value="B">B. タプルの方が作成が速い</BaseQuizOption>
<BaseQuizOption value="C" correct>C. リストはミュータブル（変更可能）であり、タプルはイミュータブル（変更不可能）である</BaseQuizOption>
<BaseQuizOption value="D">D. リストは角括弧を使い、タプルは波括弧を使う</BaseQuizOption>
<BaseQuizAnswer>リストはミュータブルであり、作成後に変更できます。タプルはイミュータブルであり、作成後は変更できません。どちらも任意の型のデータを格納できます。</BaseQuizAnswer>
</BaseQuiz>

## 関連リンク

- <router-link to="/blog/python-data-types">Python Data Types: A Visual Guide for Beginners</router-link>
- <router-link to="/blog/python-comprehensions-step-by-step">Python Comprehensions Step-by-Step</router-link>
- <router-link to="/cheatsheet/comprehensions">Python Comprehensions</router-link>
- <router-link to="/modules/itertools-module">The itertools Module</router-link>
- <router-link to="/builtin/list">list()</router-link>
- <router-link to="/builtin/tuple">tuple()</router-link>
- <router-link to="/builtin/len">len()</router-link>
