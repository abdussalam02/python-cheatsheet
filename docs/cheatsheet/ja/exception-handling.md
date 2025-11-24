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

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Python で例外を処理するために使用されるキーワードは何ですか？
</template>

<base-quiz-option value="A" correct>A. <code>try</code> および <code>except</code></base-quiz-option>
<base-quiz-option value="B">B. <code>catch</code> および <code>handle</code></base-quiz-option>
<base-quiz-option value="C">C. <code>error</code> および <code>rescue</code></base-quiz-option>
<base-quiz-option value="D">D. <code>if</code> および <code>else</code></base-quiz-option>
<base-quiz-answer value="A">Python では、例外を発生させる可能性のあるコードを示すために<code>try</code>を、発生した特定の例外を処理するために<code>except</code>を使用します。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

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

<base-quiz>
<base-quiz-question correct="B">
<template #question>
単一の<code>except</code>ブロックで複数の例外タイプを処理できますか？
</template>

<base-quiz-option value="A">A. いいえ、各例外タイプに対して個別の<code>except</code>ブロックを使用する必要があります</base-quiz-option>
<base-quiz-option value="B" correct>B. はい、<code>except (Exception1, Exception2)</code>のようにタプルに入れることで可能です</base-quiz-option>
<base-quiz-option value="C">C. はい、ただしそれらが関連している場合に限ります</base-quiz-option>
<base-quiz-option value="D">D. いいえ、Python はこれをサポートしていません</base-quiz-option>
<base-quiz-answer value="B">複数の例外タイプは、それらをタプルに入れることによって 1 つの<code>except</code>ブロックで処理できます：<code>except (ZeroDivisionError, TypeError) as error:</code></base-quiz-answer>
</base-quiz-question>
</base-quiz>

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

<base-quiz>
<base-quiz-question correct="C">
<template #question>
<code>finally</code>ブロックはいつ実行されますか？
</template>

<base-quiz-option value="A">A. 例外が発生した場合のみ</base-quiz-option>
<base-quiz-option value="B">B. 例外が発生しなかった場合のみ</base-quiz-option>
<base-quiz-option value="C" correct>C. 例外が発生したかどうかにかかわらず、常に</base-quiz-option>
<base-quiz-option value="D">D. 決して</base-quiz-option>
<base-quiz-answer value="C"><code>finally</code>ブロックは、例外が発生したかどうかにかかわらず、常に実行されます。結果に関係なく実行する必要があるクリーンアップコードに役立ちます。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

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

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Python でカスタム例外を作成するにはどうすればよいですか？
</template>

<base-quiz-option value="A" correct>A. <code>Exception</code>クラスを継承するクラスを作成する</base-quiz-option>
<base-quiz-option value="B">B. <code>@exception</code>デコレータを使用する</base-quiz-option>
<base-quiz-option value="C">C. <code>Exception.create()</code>を呼び出す</base-quiz-option>
<base-quiz-option value="D">D. 特別なモジュールからインポートする</base-quiz-option>
<base-quiz-answer value="A">カスタム例外は、基本の<code>Exception</code>クラスを継承するクラスを定義することによって作成されます。その後、組み込み例外とまったく同じように発生させたり処理したりできます。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 関連リンク

- <router-link to="/cheatsheet/control-flow">制御フロー</router-link>
- <router-link to="/builtin/breakpoint">breakpoint()</router-link>
- <router-link to="/builtin/isinstance">isinstance()</router-link>
- <router-link to="/builtin/issubclass">issubclass()</router-link>
