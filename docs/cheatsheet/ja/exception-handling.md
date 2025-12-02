---
title: 'Python 例外処理 - Python チートシート'
description: 'Python における例外処理とは、例外の発生に対応するプロセスです。'
labUrl: 'https://labex.io/ja/labs/python-python-exception-handling-633656?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python 例外処理
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikipedia.org/wiki/Exception_handling">例外処理</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    コンピューティングおよびコンピュータプログラミングにおける例外処理とは、特別な処理を必要とする異常な、または例外的な状態である例外の発生に対応するプロセスです。
  </base-disclaimer-content>
</base-disclaimer>

Python には、プログラムがエラーに遭遇したときに発生する多くの[組み込み例外](https://docs.python.org/3/library/exceptions.html)があり、人気の高い[Requests](https://requests.readthedocs.io/en/latest)のようなほとんどの外部ライブラリには、私たちが対処する必要のある独自の[カスタム例外](https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions)が含まれています。

## 基本的な例外処理

ゼロによる除算は数学的に真実であり、Python でそれを試みると、インタープリタは組み込み例外である[ZeroDivisionError](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError)を発生させます。

```python
def divide(dividend , divisor):
    print(dividend / divisor)

divide(dividend=10, divisor=5)
```

```output
2
```

```python
divide(dividend=10, divisor=0)
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

プログラムの実行を停止させたくない、またはユーザーに理解できない出力を表示したくないとします。わかりやすく明確なメッセージを出力したい場合、`try`キーワードと`except`キーワードを使用して例外を**_処理_**する必要があります。

```python
# try-except: 例外を優雅に処理する
def divide(dividend , divisor):
    try:  # このコードを実行してみる
        print(dividend / divisor)
    except ZeroDivisionError:  # 特定の例外型をキャッチする
        print('You can not divide by 0')

divide(dividend=10, divisor=5)
```

```output
2
```

```python
divide(dividend=10, divisor=0)
```

```output
You can not divide by 0
```

<BaseQuiz id="cheatsheet-exception-handling-1" correct="A">
<template #question>
Python で例外を処理するために使用されるキーワードは何ですか？
</template>

<BaseQuizOption value="A" correct>A. <code>try</code> および <code>except</code></BaseQuizOption>
<BaseQuizOption value="B">B. <code>catch</code> および <code>handle</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>error</code> および <code>rescue</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>if</code> および <code>else</code></BaseQuizOption>
<BaseQuizAnswer>Python では、例外を発生させる可能性のあるコードを示すために<code>try</code>を、発生した特定の例外を処理するために<code>except</code>を使用します。</BaseQuizAnswer>
</BaseQuiz>

## 1 つの例外ブロックを使用した複数の例外の処理

複数の例外を 1 行で処理することもでき、複数の例外ブロックを作成する必要はありません。

```python
# 1 つの except ブロックで複数の例外を処理する
def divide(dividend , divisor):
    try:
        if (dividend == 10):
          var = 'str' + 1  # これは TypeError を発生させる
        else:
          print(dividend / divisor)
    except (ZeroDivisionError, TypeError) as error:  # 複数の例外型をキャッチする
        print(error)  # エラーメッセージを出力する

divide(dividend=20, divisor=5)
```

```output
4
```

```python
divide(dividend=10, divisor=5)
```

```output
can only concatenate str (not "int") to str
```

```python
divide(dividend=10, divisor=0)
```

```output
division by zero
```

<BaseQuiz id="cheatsheet-exception-handling-2" correct="B">
<template #question>
単一の<code>except</code>ブロックで複数の例外タイプを処理できますか？
</template>

<BaseQuizOption value="A">A. いいえ、各例外タイプに対して個別の<code>except</code>ブロックを使用する必要があります</BaseQuizOption>
<BaseQuizOption value="B" correct>B. はい、<code>except (Exception1, Exception2)</code>のようにタプルに入れることで可能です</BaseQuizOption>
<BaseQuizOption value="C">C. はい、ただしそれらが関連している場合に限ります</BaseQuizOption>
<BaseQuizOption value="D">D. いいえ、Python はこれをサポートしていません</BaseQuizOption>
<BaseQuizAnswer>複数の例外タイプは、それらをタプルに入れることによって 1 つの<code>except</code>ブロックで処理できます：<code>except (ZeroDivisionError, TypeError) as error:</code></BaseQuizAnswer>
</BaseQuiz>

## 例外処理における Finally コード

`finally`セクション内のコードは、例外が発生したかどうかにかかわらず、常に実行されます。

```python
# finally ブロック：例外の発生に関係なく常に実行される
def divide(dividend , divisor):
    try:
        print(dividend / divisor)
    except ZeroDivisionError:
        print('You can not divide by 0')
    finally:  # 例外が発生しても常に実行される
        print('Execution finished')

divide(dividend=10, divisor=5)
```

```output
2.0
Execution finished
```

```python
divide(dividend=10, divisor=0)
```

```output
You can not divide by 0
Execution finished
```

<BaseQuiz id="cheatsheet-exception-handling-3" correct="C">
<template #question>
<code>finally</code>ブロックはいつ実行されますか？
</template>

<BaseQuizOption value="A">A. 例外が発生した場合のみ</BaseQuizOption>
<BaseQuizOption value="B">B. 例外が発生しなかった場合のみ</BaseQuizOption>
<BaseQuizOption value="C" correct>C. 例外が発生したかどうかにかかわらず、常に</BaseQuizOption>
<BaseQuizOption value="D">D. 決して</BaseQuizOption>
<BaseQuizAnswer><code>finally</code>ブロックは、例外が発生したかどうかにかかわらず、常に実行されます。結果に関係なく実行する必要があるクリーンアップコードに役立ちます。</BaseQuizAnswer>
</BaseQuiz>

## カスタム例外

カスタム例外は、Python の基本の`Exception`クラスを継承する`class`を作成することによって初期化され、`raise`キーワードを使用して発生させます。

```python
# カスタム例外：Exception クラスから継承して作成
class MyCustomException(Exception):
    pass

raise MyCustomException  # カスタム例外を発生させる
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyCustomException
```

カスタム例外メッセージを宣言するには、それをパラメーターとして渡すことができます。

```python
class MyCustomException(Exception):
    pass

raise MyCustomException('A custom message for my custom exception')
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyCustomException: A custom message for my custom exception
```

カスタム例外の処理は、他の例外と同じです。

```python
try:
    raise MyCustomException('A custom message for my custom exception')
except MyCustomException:
    print('My custom exception was raised')
```

```output
My custom exception was raised
```

<BaseQuiz id="cheatsheet-exception-handling-4" correct="A">
<template #question>
Python でカスタム例外を作成するにはどうすればよいですか？
</template>

<BaseQuizOption value="A" correct>A. <code>Exception</code>クラスを継承するクラスを作成する</BaseQuizOption>
<BaseQuizOption value="B">B. <code>@exception</code>デコレータを使用する</BaseQuizOption>
<BaseQuizOption value="C">C. <code>Exception.create()</code>を呼び出す</BaseQuizOption>
<BaseQuizOption value="D">D. 特別なモジュールからインポートする</BaseQuizOption>
<BaseQuizAnswer>カスタム例外は、基本の<code>Exception</code>クラスを継承するクラスを定義することによって作成されます。その後、組み込み例外とまったく同じように発生させたり処理したりできます。</BaseQuizAnswer>
</BaseQuiz>

## 関連リンク

- <router-link to="/cheatsheet/control-flow">制御フロー</router-link>
- <router-link to="/builtin/breakpoint">breakpoint()</router-link>
- <router-link to="/builtin/isinstance">isinstance()</router-link>
- <router-link to="/builtin/issubclass">issubclass()</router-link>
