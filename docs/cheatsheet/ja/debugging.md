---
title: 'Python デバッグ - Python チートシート'
description: 'コンピュータプログラミングおよびソフトウェア開発において、デバッグとは、プログラム、ソフトウェア、またはシステムが正しく動作するのを妨げるバグ（欠陥や問題）を見つけ、解決するプロセスです。'
labUrl: 'https://labex.io/ja/labs/python-python-debugging-633653?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python デバッグ
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikipedia.org/wiki/Debugging">バグの発見と修正</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    コンピュータープログラミングおよびソフトウェア開発において、デバッグとは、コンピュータープログラム、ソフトウェア、またはシステム内のバグ（欠陥または動作を妨げる問題）を見つけ、解決するプロセスです。
  </base-disclaimer-content>
</base-disclaimer>

## 例外を発生させる (Raising Exceptions)

例外は `raise` ステートメントを使用して発生させます。コード内では、`raise` ステートメントは以下の要素で構成されます。

- `raise` キーワード
- `Exception()` 関数の呼び出し
- `Exception()` 関数に渡される、役立つエラーメッセージを含む文字列

```python
# raise ステートメント：カスタムメッセージで例外を手動で発生させる
raise Exception('This is the error message.')
```

```output
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    raise Exception('This is the error message.')
Exception: This is the error message.
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Python で例外を手動で発生させるために使用されるキーワードは何ですか？
</template>

<base-quiz-option value="A">A. <code>throw</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>raise</code></base-quiz-option>
<base-quiz-option value="C">C. <code>error</code></base-quiz-option>
<base-quiz-option value="D">D. <code>exception</code></base-quiz-option>
<base-quiz-answer value="B">Python で例外を手動で発生させるには、<code>raise</code> キーワードが使用されます。組み込みの例外またはカスタム例外を発生させることができます。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

通常、例外を処理する方法を知っているのは、関数を呼び出すコードであり、関数自体ではありません。そのため、関数内で `raise` ステートメントを、関数を呼び出すコード内で `try` および `except` ステートメントをよく見かけることになります。

```python
# 関数内で例外を発生させ、呼び出し元のコードで処理する
def box_print(symbol, width, height):
    if len(symbol) != 1:
      raise Exception('Symbol must be a single character string.')
    if width <= 2:
      raise Exception('Width must be greater than 2.')
    if height <= 2:
      raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

# 関数呼び出し時に例外を処理する
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:  # 例外をキャッチし、エラーメッセージを出力する
        print('An exception happened: ' + str(err))
```

```output
****
*  *
*  *
****
OOOOOOOOOOOOOOOOOOOO
O                  O
O                  O
O                  O
OOOOOOOOOOOOOOOOOOOO
An exception happened: Width must be greater than 2.
An exception happened: Symbol must be a single character string.
```

[例外処理](/cheatsheet/exception-handling)についてさらに読む。

## トレースバックを文字列として取得する

`traceback` は、発生した例外が未処理のままである場合に Python によって表示されます。しかし、`traceback.format_exc()` を呼び出すことによって、トレースバックを文字列として取得することもできます。この関数は、例外のトレースバックからの情報が必要だが、`except` ステートメントで例外を優雅に処理したい場合に役立ちます。この関数を呼び出す前に、Python の `traceback` モジュールをインポートする必要があります。

```python
# traceback.format_exc(): ロギング/デバッグのためにトレースバックを文字列として取得する
import traceback

try:
    raise Exception('This is the error message.')
except:
    with open('errorInfo.txt', 'w') as error_file:
        error_file.write(traceback.format_exc())  # トレースバックをファイルに書き込む
    print('The traceback info was written to errorInfo.txt.')
```

```output
116
The traceback info was written to errorInfo.txt.
```

116 は `write()` メソッドの戻り値であり、ファイルに 116 文字が書き込まれたことを示します。`traceback` テキストは errorInfo.txt に書き込まれました。

    Traceback (most recent call last):
      File "<pyshell#28>", line 2, in <module>
    Exception: This is the error message.

## アサーション (Assertions)

アサーションは、コードが明らかに間違ったことをしていないことを確認するための健全性チェックです。これらの健全性チェックは `assert` ステートメントによって実行されます。健全性チェックが失敗すると、`AssertionError` 例外が発生します。コード内では、`assert` ステートメントは以下の要素で構成されます。

- `assert` キーワード
- 条件（つまり、`True` または `False` に評価される式）
- コンマ
- 条件が `False` の場合に表示する `string`

```python
# assert ステートメント：条件をチェックし、False の場合は AssertionError を発生させる
pod_bay_door_status = 'open'
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'  # パスする

pod_bay_door_status = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'  # AssertionError を発生させる
```

```output
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'
AssertionError: The pod bay doors need to be "open".
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
<code>assert</code> ステートメントが失敗するとどうなりますか？
</template>

<base-quiz-option value="A">A. プログラムの実行が継続される</base-quiz-option>
<base-quiz-option value="B">B. 警告が出力される</base-quiz-option>
<base-quiz-option value="C" correct>C. <code>AssertionError</code> が発生し、プログラムはクラッシュするはずである</base-quiz-option>
<base-quiz-option value="D">D. 条件が自動的に修正される</base-quiz-option>
<base-quiz-answer value="C"><code>assert</code> ステートメントが失敗すると、<code>AssertionError</code> が発生します。例外とは異なり、アサートステートメントは try-except で処理されるべきではありません。アサートが失敗した場合、バグを迅速に見つけるためにプログラムはクラッシュする必要があります。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

平たく言えば、アサートステートメントは「この条件が真であると主張する。そうでなければ、プログラムのどこかにバグがある」という意味です。例外とは異なり、コードはアサートステートメントを try や except で処理すべきではありません。アサートが失敗した場合、プログラムはクラッシュする必要があります。このようにすぐに失敗させることで、バグの元の原因と、最初にバグに気づくまでの時間を短縮できます。これにより、バグの原因となっているコードを見つける前に確認しなければならないコードの量が少なくなります。

### アサーションの無効化

Python を実行する際に `-O` オプションを渡すことで、アサーションを無効にできます。

## ロギング (Logging)

プログラムの実行中にログメッセージを画面に表示できるように `logging` モジュールを有効にするには、プログラムの先頭に以下をコピーします。

```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Python における<code>logging</code>モジュールの目的は何ですか？
</template>

<base-quiz-option value="A" correct>A. デバッグと監視のためにプログラム実行に関する情報を記録すること</base-quiz-option>
<base-quiz-option value="B">B. エラーの発生を防ぐこと</base-quiz-option>
<base-quiz-option value="C">C. プログラムの実行速度を向上させること</base-quiz-option>
<base-quiz-option value="D">D. ログメッセージを暗号化すること</base-quiz-option>
<base-quiz-answer value="A"><code>logging</code>モジュールを使用すると、プログラムの実行に関する情報を異なるレベル（DEBUG、INFO、WARNING、ERROR、CRITICAL）で記録でき、デバッグや監視に役立ちます。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

例えば、数値の階乗を計算する関数を作成したとします。数学では、階乗 4 は 1 × 2 × 3 × 4、つまり 24 です。階乗 7 は 1 × 2 × 3 × 4 × 5 × 6 × 7、つまり 5,040 です。新しいファイルエディタウィンドウを開き、以下のコードを入力してください。これにはバグがありますが、何が問題なのかを把握するのに役立つように、いくつかのログメッセージも入力します。プログラムを factorialLog.py として保存します。

```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(0, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')
```

```output
2015-05-23 16:20:12,664 - DEBUG - Start of program
2015-05-23 16:20:12,664 - DEBUG - Start of factorial(5)
2015-05-23 16:20:12,665 - DEBUG - i is 0, total is 0
2015-05-23 16:20:12,668 - DEBUG - i is 1, total is 0
2015-05-23 16:20:12,670 - DEBUG - i is 2, total is 0
2015-05-23 16:20:12,673 - DEBUG - i is 3, total is 0
2015-05-23 16:20:12,675 - DEBUG - i is 4, total is 0
2015-05-23 16:20:12,678 - DEBUG - i is 5, total is 0
2015-05-23 16:20:12,680 - DEBUG - End of factorial(5)
0
2015-05-23 16:20:12,684 - DEBUG - End of program
```

## ロギングレベル (Logging Levels)

ロギングレベルは、ログメッセージを重要度によって分類する方法を提供します。重要度が最も低いものから高いものまで、5 つのロギングレベルがあり、表 10-1 に説明されています。各レベルでメッセージをログに記録するには、異なるロギング関数を使用できます。

| Level      | Logging Function     | Description                                                                                                        |
| ---------- | -------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `DEBUG`    | `logging.debug()`    | 最低レベル。細かい詳細に使用されます。通常、これらのメッセージは問題の診断時のみに関心があります。                 |
| `INFO`     | `logging.info()`     | プログラム内の一般的なイベントに関する情報や、プログラムのその時点での動作が正しいことの確認に使用されます。       |
| `WARNING`  | `logging.warning()`  | プログラムの動作を妨げないが、将来的に妨げる可能性のある潜在的な問題を示すために使用されます。                     |
| `ERROR`    | `logging.error()`    | プログラムが何らかの処理に失敗したことを記録するために使用されます。                                               |
| `CRITICAL` | `logging.critical()` | 最高レベル。プログラムの実行全体を停止させた、または停止させようとしている致命的なエラーを示すために使用されます。 |

<base-quiz>
<base-quiz-question correct="D">
<template #question>
Python における最も低いロギングレベルは何ですか？
</template>

<base-quiz-option value="A">A. <code>INFO</code></base-quiz-option>
<base-quiz-option value="B">B. <code>WARNING</code></base-quiz-option>
<base-quiz-option value="C">C. <code>ERROR</code></base-quiz-option>
<base-quiz-option value="D" correct>D. <code>DEBUG</code></base-quiz-option>
<base-quiz-answer value="D">ロギングレベルは、低い方から高い方へ、<code>DEBUG</code>、<code>INFO</code>、<code>WARNING</code>、<code>ERROR</code>、<code>CRITICAL</code> の順です。<code>DEBUG</code> が最も低いレベルで、詳細な診断情報に使用されます。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## ロギングの無効化

プログラムのデバッグが完了した後、おそらくすべてのログメッセージが画面を占有するのを望まないでしょう。`logging.disable()` 関数は、プログラムに入ってすべてのロギング呼び出しを手動で削除する必要がないように、これらを無効にします。

```python
import logging

logging.basicConfig(level=logging.INFO, format=' %(asctime)s -%(levelname)s - %(message)s')
logging.critical('Critical error! Critical error!')
```

```output
2015-05-22 11:10:48,054 - CRITICAL - Critical error! Critical error!
```

```python
logging.disable(logging.CRITICAL)
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')
```

## ファイルへのロギング

ログメッセージを画面に表示する代わりに、テキストファイルに書き込むことができます。`logging.basicConfig()` 関数は、以下のように `filename` キーワード引数を取ります。

```python
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
ログメッセージを画面に表示する代わりにファイルに書き込むにはどうすればよいですか？
</template>

<base-quiz-option value="A">A. <code>logging.file()</code> を使用する</base-quiz-option>
<base-quiz-option value="B" correct>B. <code>logging.basicConfig()</code> に <code>filename</code> パラメータを渡す</base-quiz-option>
<base-quiz-option value="C">C. <code>logging.write()</code> を使用する</base-quiz-option>
<base-quiz-option value="D">D. ログは常に自動的にファイルに書き込まれる</base-quiz-option>
<base-quiz-answer value="B">ログメッセージをファイルに書き込むには、<code>logging.basicConfig()</code> に <code>filename</code> パラメータを渡します。これにより、すべてのログメッセージが画面に表示される代わりに、指定されたファイルに書き込まれます。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 関連リンク

- <router-link to="/cheatsheet/exception-handling">例外処理</router-link>
- <router-link to="/builtin/breakpoint">breakpoint()</router-link>
