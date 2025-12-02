---
title: 'Python デコレータ - Python チートシート'
description: 'Python デコレータは、関数やクラスを拡張するための簡潔で再利用可能な構文を提供する記法です。'
labUrl: 'https://labex.io/ja/labs/python-python-decorators-633654?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python デコレータ
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Python のデコレータは、関数やクラスを拡張するための簡潔で再利用可能な方法を提供します。実践的な例とパターンについては、関連記事の<router-link to="/blog/python-decorators-for-beginners">Python デコレータ：コードをレベルアップするためのシンプルなパターン</router-link>をお読みください。

## 基本的なデコレータ

最も単純な形のデコレータは、別の関数を引数として受け取り、ラッパーを返す関数です。次の例は、デコレータの作成とその使用方法を示しています。

```python
# デコレータ：別の関数を受け取り、ラッパーを返す関数
def your_decorator(func):
  def wrapper():
    # func...の前に何かを行う
    print("Before func!")
    func()  # 元の関数を呼び出す
    # func...の後に何かを行う
    print("After func!")
  return wrapper  # ラッパー関数を返す

# @your_decorator は、foo = your_decorator(foo) の糖衣構文です
@your_decorator
def foo():
  print("Hello World!")

foo()  # ラッパーを呼び出し、それが追加の動作を持つ foo を呼び出す
```

```output
Before func!
Hello World!
After func!
```

<BaseQuiz id="cheatsheet-decorators-1" correct="A">
<template #question>
Python におけるデコレータとは何ですか？
</template>

<BaseQuizOption value="A" correct>A. 別の関数を受け取り、ラッパー関数を返す関数</BaseQuizOption>
<BaseQuizOption value="B">B. 特別な種類のクラス</BaseQuizOption>
<BaseQuizOption value="C">C. Python の組み込みキーワード</BaseQuizOption>
<BaseQuizOption value="D">D. 関数を削除する方法</BaseQuizOption>
<BaseQuizAnswer>デコレータは、別の関数を引数として受け取り、ラッパー関数を返す関数です。<code>@</code>構文は、デコレータを関数に適用するための糖衣構文です。</BaseQuizAnswer>
</BaseQuiz>

## パラメータを持つ関数のデコレータ

```python
# パラメータを持つ関数で動作するデコレータ
def your_decorator(func):
  def wrapper(*args,**kwargs):  # あらゆる引数を受け入れる
    # func...の前に何かを行う
    print("Before func!")
    func(*args,**kwargs)  # 引数を元の関数に渡す
    # func...の後に何かを行う
    print("After func!")
  return wrapper

@your_decorator
def foo(bar):
  print("My name is " + bar)

foo("Jack")  # 引数はラッパー経由で渡される
```

```output
Before func!
My name is Jack
After func!
```

## 基本的なデコレータのテンプレート

このテンプレートは、ほとんどのデコレータのユースケースに役立ちます。パラメータの有無、戻り値の有無にかかわらず、関数に対して有効です。

```python
import functools

# ベストプラクティスのデコレータテンプレート：関数のメタデータを保持し、戻り値を保持する
def your_decorator(func):
  @functools.wraps(func)  # 関数名、docstring などを保持する
  def wrapper(*args,**kwargs):
    # func...の前に何かを行う
    result = func(*args,**kwargs)  # 関数を呼び出し、戻り値をキャプチャする
    # func...の後に何かを行う
    return result  # 元の関数の戻り値を返す
  return wrapper
```

<BaseQuiz id="cheatsheet-decorators-2" correct="B">
<template #question>
デコレータ内の<code>@functools.wraps(func)</code>は何をしますか？
</template>

<BaseQuizOption value="A">A. デコレータの実行を高速化する</BaseQuizOption>
<BaseQuizOption value="B" correct>B. 元の関数のメタデータ（名前、docstring など）を保持する</BaseQuizOption>
<BaseQuizOption value="C">C. 関数の呼び出しを防ぐ</BaseQuizOption>
<BaseQuizOption value="D">D. 関数をクラスに変換する</BaseQuizOption>
<BaseQuizAnswer><code>@functools.wraps(func)</code>デコレータは、元の関数のメタデータ（名前や docstring など）をラッパー関数に保持します。これはデコレータを作成する際のベストプラクティスと見なされます。</BaseQuizAnswer>
</BaseQuiz>

## パラメータ付きデコレータ

デコレータにパラメータを定義することもできます。

```python
import functools

# デコレータファクトリ：パラメータに基づいてデコレータを返す
def your_decorator(arg):
  def decorator(func):
    @functools.wraps(func)  # 関数メタデータを保持する
    def wrapper(*args,**kwargs):
      # func...の前に何かを行う（arg を使用する可能性がある）
      result = func(*args,**kwargs)
      # func...の後に何かを行う（arg を使用する可能性がある）
      return result
    return wrapper
  return decorator  # 実際のデコレータ関数を返す
```

このデコレータを使用するには：

```python
# パラメータ付きデコレータの使用法：@your_decorator(arg='x') は your_decorator('x') を呼び出し、
# それが foo に適用されるデコレータを返す
@your_decorator(arg = 'x')
def foo(bar):
  return bar
```

## クラスベースのデコレータ

クラスメソッドをデコレートするには、デコレータをクラス内に定義する必要があります。暗黙的な引数 `self` のみが渡され、明示的な追加引数がないメソッドをデコレートする場合、追加引数なしのメソッド専用のデコレータを別途作成する必要があります。以下に、特定の例外処理を行う例を示します。

```python
# クラスメソッドデコレータ：クラス内に定義される
class DecorateMyMethod:

  # 'self'パラメータのみを持つメソッド用の静的メソッドデコレータ
  def decorator_for_class_method_with_no_args(method):
    def wrapper_for_class_method(self):  # self のみを受け取る
      try:
        return method(self)  # 元のメソッドを呼び出す
      except Exception as e:
        print("\nWARNING: Please make note of the following:\n")
        print(e)
    return wrapper_for_class_method

  def __init__(self,succeed:bool):
    self.succeed = succeed

  @decorator_for_class_method_with_no_args
  def class_action(self):
    if self.succeed:
      print("You succeeded by choice.")
    else:
      raise Exception("Epic fail of your own creation.")

test_succeed = DecorateMyMethod(True)
test_succeed.class_action()
```

```output
You succeeded by choice.
```

```python
test_fail = DecorateMyMethod(False)
test_fail.class_action()
```

```output
Exception: Epic fail of your own creation.
```

デコレータは、メソッドの代わりにクラスとして定義することもできます。これは、以下の例のように、メソッドが呼び出された回数をカウントするなど、状態を維持および更新する場合に役立ちます。

```python
# クラスベースのデコレータ：呼び出し間で状態を維持する
class CountCallNumber:

  def __init__(self, func):
    self.func = func  # デコレートする関数を保存する
    self.call_number = 0  # 呼び出しカウンターを初期化する

  def __call__(self, *args, **kwargs):  # インスタンスを呼び出し可能にする
    self.call_number += 1  # カウンターをインクリメントする
    print("This is execution number " + str(self.call_number))
    return self.func(*args, **kwargs)  # 元の関数を呼び出す

@CountCallNumber  # CountCallNumber のインスタンスを作成する
def say_hi(name):
  print("Hi! My name is " + name)

say_hi("Jack")  # CountCallNumber.__call__() を呼び出す
```

```output
This is execution number 1
Hi! My name is Jack
```

```python
say_hi("James")
```

```output
This is execution number 2
Hi! My name is James
```

<base-disclaimer>
  <base-disclaimer-title>
    カウントの例
  </base-disclaimer-title>
  <base-disclaimer-content>
  このカウントの例は、Patrick Loeber の<a href="https://youtu.be/HGOBQPFzWKo?si=IUvFzeQbzTmeEgKV" target="_blank">YouTube チュートリアル</a>に触発されています。
  </base-disclaimer-content>
</base-disclaimer>

## 関連リンク

- <router-link to="/blog/python-decorators-for-beginners">Python デコレータ：コードをレベルアップするためのシンプルなパターン</router-link>
- <router-link to="/blog/python-easy-args-kwargs">Python \*args と \*\*kwargs の簡単な使い方</router-link>
- <router-link to="/cheatsheet/functions">関数</router-link>
- <router-link to="/cheatsheet/args-and-kwargs">Args と Kwargs</router-link>
- <router-link to="/builtin/classmethod">classmethod()</router-link>
- <router-link to="/builtin/staticmethod">staticmethod()</router-link>
- <router-link to="/builtin/property">property()</router-link>
- <router-link to="/builtin/callable">callable()</router-link>
