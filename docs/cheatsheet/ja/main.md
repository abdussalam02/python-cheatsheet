---
title: 'Python メイン関数 - Python チートシート'
description: 'トップレベルコードが実行されるスコープ名です。モジュールの名称は、標準入力、スクリプト、または対話型プロンプトから読み込まれる際に「main」に設定されます。'
labUrl: 'https://labex.io/ja/labs/python-python-main-function-633661?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
メインのトップレベルスクリプト環境
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## What is it

`__main__` は、トップレベルコードが実行されるスコープの名前です。
モジュールが標準入力、スクリプト、または対話型プロンプトから読み込まれる場合、そのモジュールの**名前**は `__main__` に設定されます。

モジュールは、自身の `__name__` をチェックすることで、メインスコープで実行されているかどうかを検出でき、これによりモジュール内でコードを条件付きで実行するための一般的なイディオムが可能になります。インポートされたときではなく、スクリプトとして、または `python -m` で実行された場合にのみ実行されます。

```python
# __name__ == "__main__": スクリプトが直接実行されているか（インポートされていないか）を確認
if __name__ == "__main__":  # スクリプトとして実行された場合に True、インポートされた場合に False
    # スクリプトとして実行された場合にのみ実行
    main()
```

パッケージの場合、同じ効果は **main**.py モジュールを含めることで実現でき、このモジュールの内容は、モジュールが -m で実行されたときに実行されます。

例えば、モジュールとして使用されることを意図したスクリプトを開発している場合、次のように記述します。

```python
# 例：関数はインポートできるが、テストコードは直接実行された場合にのみ実行される
def add(a, b):
    return a+b

if __name__ == "__main__":  # ファイルが直接実行された場合にのみ実行され、インポートされた場合には実行されない
    add(3, 5)
```

<BaseQuiz id="cheatsheet-main-1" correct="B">
<template #question>
Python ファイルをスクリプトとして直接実行した場合、<code>__name__</code> の値は何になりますか？
</template>

<BaseQuizOption value="A">A. ファイル名</BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>"**main**"</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>None</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>True</code></BaseQuizOption>
<BaseQuizAnswer>Python ファイルをスクリプトとして直接実行すると、<code>**name**</code> は <code>"**main**"</code> に設定されます。ファイルがモジュールとしてインポートされると、<code>**name**</code> はモジュールの名前に設定されます。</BaseQuizAnswer>
</BaseQuiz>

## Advantages

1. すべての Python モジュールには `__name__` が定義されており、これが `__main__` の場合、そのモジュールがユーザーによってスタンドアロンで実行されていることを意味し、それに応じて適切なアクションを実行できます。
2. このスクリプトを別のスクリプトでモジュールとしてインポートすると、**名前**はスクリプト/モジュールの名前に設定されます。
3. Python ファイルは、再利用可能なモジュールとしても、スタンドアロンプログラムとしても機能できます。
4. `if __name__ == "__main__":` は、ファイルが直接実行された場合にのみコードを実行し、インポートされた場合には実行しないようにするために使用されます。

<BaseQuiz id="cheatsheet-main-2" correct="A">
<template #question>
<code>if __name__ == "__main__":</code> を使用する主な目的は何ですか？
</template>

<BaseQuizOption value="A" correct>A. ファイルが直接実行された場合にのみコードを実行し、インポートされた場合には実行しないこと</BaseQuizOption>
<BaseQuizOption value="B">B. ファイルがインポートされるのを防ぐこと</BaseQuizOption>
<BaseQuizOption value="C">C. ファイルの実行速度を速くすること</BaseQuizOption>
<BaseQuizOption value="D">D. 他のモジュールからコードを隠すこと</BaseQuizOption>
<BaseQuizAnswer><code>if **name** == "**main**":</code> のイディオムにより、Python ファイルは再利用可能なモジュールとスタンドアロンプログラムの両方として機能できます。このブロック内のコードは、ファイルが直接実行された場合にのみ実行され、インポートされた場合には実行されません。</BaseQuizAnswer>
</BaseQuiz>

## Relevant links

- <router-link to="/cheatsheet/functions">Functions</router-link>
- <router-link to="/cheatsheet/packaging">Packaging</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Python projects with Poetry and VSCode. Part 1</router-link>
- <router-link to="/builtin/import">import()</router-link>
