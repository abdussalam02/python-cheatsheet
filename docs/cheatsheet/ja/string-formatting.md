---
title: 'Python 文字列フォーマット - Python チートシート'
description: 'Python 3.6 以降を使用している場合、文字列のフォーマットには f 文字列が推奨されます。'
labUrl: 'https://labex.io/ja/labs/python-python-string-formatting-633667?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python 文字列フォーマット
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a href="https://docs.python.org/3/library/stdtypes.html?highlight=sprintf#printf-style-string-formatting">Python 3 ドキュメント</a>より
  </base-disclaimer-title>
  <base-disclaimer-content>
    ここで説明されているフォーマット操作 (<b>% 演算子</b>) は、多くの一般的なエラーの原因となるさまざまな特異性を示します [...]. 新しい <a href="#formatted-string-literals-or-f-strings">フォーマット済み文字列リテラル</a> [...] を使用すると、これらのエラーを回避できます。これらの代替手段は、テキストのフォーマットに対して、より強力で、柔軟で、拡張性の高いアプローチも提供します。
  </base-disclaimer-content>
</base-disclaimer>

## % operator

<base-warning>
  <base-warning-title>
    文字列リテラルを優先する
  </base-warning-title>
  <base-warning-content>
    新しいコードでは、<code>%</code> 演算子よりも <a href="#strformat">str.format</a> または <a href="#formatted-string-literals-or-f-strings">フォーマット済み文字列リテラル</a> (Python 3.6+) の使用が強く推奨されます。
  </base-warning-content>
</base-warning>

```python
# % operator: 旧スタイルの文字列フォーマット (新規コードには非推奨)
name = 'Pete'
'Hello %s' % name  # %s = 文字列プレースホルダ
```

```output
"Hello Pete"
```

`%d` フォーマット指定子を使用して int 値を文字列に変換できます。

```python
num = 5
'I have %d apples' % num
```

```output
"I have 5 apples"
```

## str.format

Python 3 では、文字列フォーマットの新しい方法が導入され、後に Python 2.7 にバックポートされました。これにより、文字列フォーマットの構文がより規則的になります。

```python
# str.format() メソッド：モダンな文字列フォーマット (Python 2.7+)
name = 'John'
age = 20

"Hello I'm {}, my age is {}".format(name, age)  # {} = プレースホルダ
```

```output
"Hello I'm John, my age is 20"
```

```python
"Hello I'm {0}, my age is {1}".format(name, age)
```

```output
"Hello I'm John, my age is 20"
```

## Formatted String Literals or f-Strings

Python 3.6+ を使用している場合、文字列の `f-Strings` が文字列をフォーマットするための推奨される方法です。

<base-disclaimer>
  <base-disclaimer-title>
    <a href="https://docs.python.org/3/reference/lexical_analysis.html#f-strings">Python 3 ドキュメント</a>より
  </base-disclaimer-title>
  <base-disclaimer-content>
    フォーマット済み文字列リテラル、または f-string は、<code>f</code> または <code>F</code> で始まる文字列リテラルです。これらの文字列には、波括弧 <code>{}</code> で区切られた式を含む置換フィールドを含めることができます。他の文字列リテラルは常に定数値を持つ一方、フォーマット済み文字列は実行時に評価される式です。
  </base-disclaimer-content>
</base-disclaimer>

```python
# f-string: 文字列をフォーマットするための推奨される方法 (Python 3.6+)
name = 'Elizabeth'
f'Hello {name}!'  # f プレフィックスにより {} 内に式を含めることができる
```

```output
'Hello Elizabeth!'
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-string-formatting-1">
<template #question>
Python の f-string に使用されるプレフィックスは何ですか？
</template>

<base-quiz-option value="A">A. <code>fmt</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>f</code> または <code>F</code></base-quiz-option>
<base-quiz-option value="C">C. <code>format</code></base-quiz-option>
<base-quiz-option value="D">D. <code>str</code></base-quiz-option>
<base-quiz-answer value="B">f-string は、開始引用符の前に <code>f</code> または <code>F</code> でプレフィックスが付けられます。波括弧 <code>{}</code> 内に式を埋め込むことができます。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

インライン計算を行うことも可能です。

```python
# f-strings は式をサポート：{} 内に計算を含めることができる
a = 5
b = 10
f'Five plus ten is {a + b} and not {2 * (a + b)}.'  # 式を評価する
```

```output
'Five plus ten is 15 and not 30.'
```

### 複数行の f-String

```python
name = 'Robert'
messages = 12
(
f'Hi, {name}. '
f'You have {messages} unread messages'
)
```

```output
'Hi, Robert. You have 12 unread messages'
```

### = 指定子

これは式とその値を出力します。

```python
# = 指定子：変数名とその両方を出力 (Python 3.8+)
from datetime import datetime
now = datetime.now().strftime("%b/%d/%Y - %H:%M:%S")
f'date and time: {now=}'  # "now='Nov/14/2022 - 20:50:01'" を出力
```

```output
"date and time: now='Nov/14/2022 - 20:50:01'"
```

### スペースまたは文字の追加

```python
name = 'Robert'
f"{name.upper() = :-^20}"
```

```output
'name.upper() = -------ROBERT-------'
```

```python
f"{name.upper() = :^20}"
```

```output
'name.upper() =        ROBERT       '
```

```python
f"{name.upper() = :20}"
```

```output
'name.upper() = ROBERT              '
```

## 数字のフォーマット

桁区切り (数千区切り) の追加

```python
a = 10000000
f"{a:,}"
```

```output
'10,000,000'
```

丸め処理

```python
a = 3.1415926
f"{a:.2f}"
```

```output
'3.14'
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-string-formatting-2">
<template #question>
<code>f"{a:.2f}"</code> は何を行いますか？
</template>

<base-quiz-option value="A">A. 数値を最も近い整数に丸める</base-quiz-option>
<base-quiz-option value="B">B. パーセンテージとしてフォーマットする</base-quiz-option>
<base-quiz-option value="C" correct>C. 数値を小数点以下 2 桁の浮動小数点数としてフォーマットする</base-quiz-option>
<base-quiz-option value="D">D. 科学的記数法に変換する</base-quiz-option>
<base-quiz-answer value="C">フォーマット指定子 <code>:.2f</code> は、数値を小数点以下 2 桁の浮動小数点数としてフォーマットします。<code>.2</code> は精度を、<code>f</code> は浮動小数点形式を指定します。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

パーセンテージとして表示

```python
a = 0.816562
f"{a:.2%}"
```

```output
'81.66%'
```

### 数値フォーマットの表

| 数値       | フォーマット | 出力      | 説明                                                |
| ---------- | ------------ | --------- | --------------------------------------------------- |
| 3.1415926  | {:.2f}       | 3.14      | 浮動小数点数を小数点以下 2 桁でフォーマット         |
| 3.1415926  | {:+.2f}      | +3.14     | 符号付き浮動小数点数を小数点以下 2 桁でフォーマット |
| -1         | {:+.2f}      | -1.00     | 符号付き浮動小数点数を小数点以下 2 桁でフォーマット |
| 2.71828    | {:.0f}       | 3         | 浮動小数点数を小数点なしでフォーマット              |
| 4          | {:0>2d}      | 04        | ゼロで数値をパディング (左詰め、幅 2)               |
| 4          | {:x<4d}      | 4xxx      | x で数値をパディング (右詰め、幅 4)                 |
| 10         | {:x<4d}      | 10xx      | x で数値をパディング (右詰め、幅 4)                 |
| 1000000    | {:,}         | 1,000,000 | カンマ区切りでの数値フォーマット                    |
| 0.35       | {:.2%}       | 35.00%    | パーセンテージのフォーマット                        |
| 1000000000 | {:.2e}       | 1.00e+09  | 指数表記                                            |
| 11         | {:11d}       | 11        | 右寄せ (デフォルト、幅 10)                          |
| 11         | {:<11d}      | 11        | 左寄せ (幅 10)                                      |
| 11         | {:^11d}      | 11        | 中央寄せ (幅 10)                                    |

## Template Strings

よりシンプルで機能が少ないメカニズムですが、ユーザーによって生成された文字列を扱う場合に推奨されます。複雑さが軽減されるため、テンプレート文字列はより安全な選択肢となります。

```python
from string import Template
name = 'Elizabeth'
t = Template('Hey $name!')
t.substitute(name=name)
```

```output
'Hey Elizabeth!'
```

## 関連リンク

- <router-link to="/cheatsheet/manipulating-strings">文字列の操作</router-link>
- <router-link to="/blog/python-data-types">Python データ型ブログ投稿</router-link>
- <router-link to="/builtin/format">format()</router-link>
- <router-link to="/builtin/print">print()</router-link>
- <router-link to="/builtin/str">str()</router-link>
- <router-link to="/builtin/repr">repr()</router-link>
- <router-link to="/builtin/ascii">ascii()</router-link>
