---
title: 'Python 字符串操作速查表'
description: "转义字符通过输入反斜杠 \ 后跟要插入的字符来创建。"
labUrl: 'https://labex.io/zh/labs/python-python-string-manipulation-633668?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
操作字符串
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## 转义字符

转义字符是通过键入反斜杠 `\` 后跟要插入的字符来创建的。

| 转义字符 | 打印为         |
| :------- | :------------- |
| `\'`     | 单引号         |
| `\"`     | 双引号         |
| `\t`     | 制表符         |
| `\n`     | 换行符（换行） |
| `\\`     | 反斜杠         |
| `\b`     | 退格键         |
| `\ooo`   | 八进制值       |
| `\r`     | 回车           |

```python
# 转义字符：使用反斜杠插入特殊字符
# \n = 换行，\' = 单引号
print("Hello there!\nHow are you?\nI\'m doing fine.")
```

```output
Hello there!
How are you?
I'm doing fine.
```

## 原始字符串

原始字符串完全忽略所有转义字符，并打印字符串中出现的任何反斜杠。

```python
# 原始字符串（r 前缀）：将反斜杠视为字面字符
print(r"Hello there!\nHow are you?\nI\'m doing fine.")  # \n 按字面意思打印
```

```output
Hello there!\nHow are you?\nI\'m doing fine.
```

原始字符串主要用于 <router-link to="/cheatsheet/regular-expressions">正则表达式</router-link> 定义。

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-manipulating-strings-1">
<template #question>
Python 中以 <code>r</code> 为前缀的原始字符串的作用是什么？
</template>

<base-quiz-option value="A">A. 将所有字符转换为大写</base-quiz-option>
<base-quiz-option value="B" correct>B. 将反斜杠视为字面字符，忽略转义序列</base-quiz-option>
<base-quiz-option value="C">C. 移除所有空格</base-quiz-option>
<base-quiz-option value="D">D. 反转字符串</base-quiz-option>
<base-quiz-answer value="B">以 <code>r</code> 为前缀的原始字符串将反斜杠视为字面字符，因此 <code>\n</code> 等转义序列不会被解释。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 多行字符串

```python
print(
"""Dear Alice,

Eve's cat has been arrested for catnapping,
cat burglary, and extortion.

Sincerely,
Bob"""
)
```

```output
Dear Alice,

Eve's cat has been arrested for catnapping,
cat burglary, and extortion.

Sincerely,
Bob
```

## 字符串的索引和切片

    H   e   l   l   o       w   o   r   l   d    !
    0   1   2   3   4   5   6   7   8   9   10   11

### 索引

```python
# 字符串索引：通过位置（从 0 开始）访问字符
spam = 'Hello world!'

spam[0]  # 返回第一个字符：'H'
```

```output
'H'
```

```python
spam[4]
```

```output
'o'
```

```python
spam[-1]
```

```output
'!'
```

### 切片

```python
# 字符串切片：使用 [start:end] 语法提取子字符串
spam = 'Hello world!'

spam[0:5]  # 返回索引 0 到 4 的字符：'Hello'
```

```output
'Hello'
```

```python
spam[:5]
```

```output
'Hello'
```

```python
spam[6:]
```

```output
'world!'
```

```python
spam[6:-1]
```

```output
'world'
```

```python
spam[:-1]
```

```output
'Hello world'
```

```python
spam[::-1]
```

```output
'!dlrow olleH'
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-manipulating-strings-2">
<template #question>
<code>spam[::-1]</code> 对字符串做什么？
</template>

<base-quiz-option value="A">A. 返回第一个字符</base-quiz-option>
<base-quiz-option value="B">B. 返回最后一个字符</base-quiz-option>
<base-quiz-option value="C" correct>C. 反转字符串</base-quiz-option>
<base-quiz-option value="D">D. 移除所有字符</base-quiz-option>
<base-quiz-answer value="C">切片 <code>[::-1]</code> 通过向后遍历所有字符来反转字符串。<code>-1</code> 的步长值表示“向后移动”。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

```python
fizz = spam[0:5]
fizz
```

```output
'Hello'
```

## in 和 not in 运算符

```python
'Hello' in 'Hello World'
```

```output
True
```

```python
'Hello' in 'Hello'
```

```output
True
```

```python
'HELLO' in 'Hello World'
```

```output
False
```

```python
'' in 'spam'
```

```output
True
```

```python
'cats' not in 'cats and dogs'
```

```output
False
```

## upper(), lower() 和 title()

将字符串转换为大写、小写和标题大小写：

```python
greet = 'Hello world!'
greet.upper()
```

```output
'HELLO WORLD!'
```

```python
greet.lower()
```

```output
'hello world!'
```

```python
greet.title()
```

```output
'Hello World!'
```

## isupper() 和 islower() 方法

评估字符串是大写还是小写后返回 `True` 或 `False`：

```python
spam = 'Hello world!'
spam.islower()
```

```output
False
```

```python
spam.isupper()
```

```output
False
```

```python
'HELLO'.isupper()
```

```output
True
```

```python
'abc12345'.islower()
```

```output
True
```

```python
'12345'.islower()
```

```output
False
```

```python
'12345'.isupper()
```

```output
False
```

## isX 字符串方法

| 方法        | 描述                                                                  |
| :---------- | :-------------------------------------------------------------------- |
| isalpha()   | 如果字符串仅由字母组成，则返回 `True`。                               |
| isalnum()   | 如果字符串仅由字母和数字组成，则返回 `True`。                         |
| isdecimal() | 如果字符串仅由数字组成，则返回 `True`。                               |
| isspace()   | 如果字符串仅由空格、制表符和换行符组成，则返回 `True`。               |
| istitle()   | 如果字符串仅由以大写字母开头后跟仅小写字符的单词组成，则返回 `True`。 |

## startswith() 和 endswith()

```python
'Hello world!'.startswith('Hello')
```

```output
True
```

```python
'Hello world!'.endswith('world!')
```

```output
True
```

```python
'abc123'.startswith('abcdef')
```

```output
False
```

```python
'abc123'.endswith('12')
```

```output
False
```

```python
'Hello world!'.startswith('Hello world!')
```

```output
True
```

```python
'Hello world!'.endswith('Hello world!')
```

```output
True
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-manipulating-strings-3">
<template #question>
<code>startswith()</code> 返回什么？
</template>

<base-quiz-option value="A" correct>A. 如果字符串以指定的子字符串开头，则返回 <code>True</code>，否则返回 <code>False</code></base-quiz-option>
<base-quiz-option value="B">B. 匹配开头的子字符串</base-quiz-option>
<base-quiz-option value="C">C. 子字符串开始的索引</base-quiz-option>
<base-quiz-option value="D">D. 一个不带前缀的新字符串</base-quiz-option>
<base-quiz-answer value="A"><code>startswith()</code> 方法返回一个布尔值：如果字符串以指定的子字符串开头，则返回 <code>True</code>，否则返回 <code>False</code>。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## join() 和 split()

### join()

`join()` 方法接受可迭代对象（如 <router-link to="/cheatsheet/lists-and-tuples">列表</router-link>、<router-link to="/cheatsheet/dictionaries">字典</router-link>、<router-link to="/cheatsheet/lists-and-tuples#the-tuple-data-type">元组</router-link> 或 <router-link to="/cheatsheet/sets">集合</router-link>）中的所有项，并将它们连接成一个字符串。您也可以指定一个分隔符。

```python
''.join(['My', 'name', 'is', 'Simon'])
```

```output
'MynameisSimon'
```

```python
', '.join(['cats', 'rats', 'bats'])
```

```output
'cats, rats, bats'
```

```python
' '.join(['My', 'name', 'is', 'Simon'])
```

```output
'My name is Simon'
```

```python
'ABC'.join(['My', 'name', 'is', 'Simon'])
```

```output
'MyABCnameABCisABCSimon'
```

### split()

`split()` 方法将一个 `string` 分割成一个 `list`。默认情况下，它使用空格来分隔各项，但您也可以设置另一个选择的字符：

```python
'My name is Simon'.split()
```

```output
['My', 'name', 'is', 'Simon']
```

```python
'MyABCnameABCisABCSimon'.split('ABC')
```

```output
['My', 'name', 'is', 'Simon']
```

```python
'My name is Simon'.split('m')
```

```output
['My na', 'e is Si', 'on']
```

```python
' My  name is  Simon'.split()
```

```output
['My', 'name', 'is', 'Simon']
```

```python
' My  name is  Simon'.split(' ')
```

```output
['', 'My', '', 'name', 'is', '', 'Simon']
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-manipulating-strings-4">
<template #question>
对字符串调用 <code>split()</code> 会返回什么？
</template>

<base-quiz-option value="A">A. 一个字符串</base-quiz-option>
<base-quiz-option value="B" correct>B. 一个字符串列表</base-quiz-option>
<base-quiz-option value="C">C. 一个字符串元组</base-quiz-option>
<base-quiz-option value="D">D. 一个字典</base-quiz-option>
<base-quiz-answer value="B"><code>split()</code> 方法将一个字符串分割成一个子字符串列表。默认情况下，它按空格分割，但您可以指定不同的分隔符。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 使用 rjust(), ljust() 和 center() 进行文本对齐

```python
'Hello'.rjust(10)
```

```output
'     Hello'
```

```python
'Hello'.rjust(20)
```

```output
'               Hello'
```

```python
'Hello World'.rjust(20)
```

```output
'         Hello World'
```

```python
'Hello'.ljust(10)
```

```output
'Hello     '
```

```python
'Hello'.center(20)
```

```output
'       Hello       '
```

`rjust()` 和 `ljust()` 的可选第二个参数将指定一个除空格字符外的填充字符：

```python
'Hello'.rjust(20, '*')
```

```output
'***************Hello'
```

```python
'Hello'.ljust(20, '-')
```

```output
'Hello---------------'
```

```python
'Hello'.center(20, '=')
```

```output
'=======Hello========'
```

## 使用 strip(), rstrip() 和 lstrip() 移除空格

```python
spam = '    Hello World     '
spam.strip()
```

```output
'Hello World'
```

```python
spam.lstrip()
```

```output
'Hello World     '
```

```python
spam.rstrip()
```

```output
'    Hello World'
```

```python
spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')
```

```output
'BaconSpamEggs'
```

## Count 方法

计算给定字符或子字符串在应用它的字符串中出现的次数。可以可选地提供起始和结束索引。

```python
sentence = 'one sheep two sheep three sheep four'
sentence.count('sheep')
```

```output
3
```

```python
sentence.count('e')
```

```output
9
```

```python
# 返回 'one sh' 之后 e 的计数，即从字符串开头算起的第 6 个字符之后
sentence.count('e', 6)
```

```output
8
```

```python
sentence.count('e', 7)
```

```output
7
```

## Replace 方法

替换给定子字符串的所有出现，替换为另一个子字符串。可以可选地提供第三个参数来限制替换次数。返回一个新字符串。

```python
text = "Hello, world!"
text.replace("world", "planet")
```

```output
'Hello, planet!'
```

```python
fruits = "apple, banana, cherry, apple"
fruits.replace("apple", "orange", 1)
```

```output
'orange, banana, cherry, apple'
```

```python
sentence = "I like apples, Apples are my favorite fruit"
sentence.replace("apples", "oranges")
```

```output
'I like oranges, Apples are my favorite fruit'
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-manipulating-strings-5">
<template #question>
<code>replace()</code> 方法返回什么？
</template>

<base-quiz-option value="A">A. 修改原始字符串</base-quiz-option>
<base-quiz-option value="B">B. 返回 <code>None</code></base-quiz-option>
<base-quiz-option value="C" correct>C. 返回一个已进行替换的新字符串</base-quiz-option>
<base-quiz-option value="D">D. 返回一个被替换字符串的列表</base-quiz-option>
<base-quiz-answer value="C"><code>replace()</code> 方法返回一个新字符串，其中旧子字符串的所有出现都替换为新子字符串。原始字符串不会被修改。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 相关链接

- <router-link to="/builtin/format">format()</router-link>
- <router-link to="/builtin/len">len()</router-link>
- <router-link to="/builtin/str">str()</router-link>
- <router-link to="/builtin/repr">repr()</router-link>
- <router-link to="/builtin/input">input()</router-link>
- <router-link to="/cheatsheet/string-formatting">字符串格式化</router-link>
- <router-link to="/cheatsheet/regular-expressions">正则表达式</router-link>
