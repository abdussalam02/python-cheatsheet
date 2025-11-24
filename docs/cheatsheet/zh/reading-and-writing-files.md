---
title: 'Python 文件读写速查表'
description: '在 Python 中读写文件，推荐使用 with 语句，它能自动管理资源并确保文件在使用后被关闭。'
labUrl: 'https://labex.io/zh/labs/python-python-reading-and-writing-files-633663?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
文件读写
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

有关文件和目录路径操作的更深入了解，请参阅 <router-link to="/cheatsheet/file-directory-path">文件和目录路径</router-link> 页面。

## 文件读写过程

要在 Python 中读/写文件，您应该使用 `with` 语句，它会在您完成后自动关闭文件，为您管理可用资源。

## 打开和读取文件

`open` 函数打开一个文件并返回一个相应的文件对象。

```python
# 使用 'with' 语句读取文件：完成后自动关闭文件
with open('/home/labex/project/hi.txt') as hello_file:
    hello_content = hello_file.read()  # 读取整个文件内容

hello_content
```

```output
'Hello World!'
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
使用 <code>with</code> 语句打开文件的主要优点是什么？
</template>

<base-quiz-option value="A" correct>A. 完成后文件会自动关闭，即使发生错误</base-quiz-option>
<base-quiz-option value="B">B. 文件打开速度更快</base-quiz-option>
<base-quiz-option value="C">C. 文件可以同时以读写模式打开</base-quiz-option>
<base-quiz-option value="D">D. 文件会自动压缩</base-quiz-option>
<base-quiz-answer value="A"><code>with</code> 语句确保在退出代码块时文件会自动关闭，即使发生异常也是如此。这有助于正确管理资源。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

或者，您可以使用 _readlines()_ 方法从文件中获取字符串值列表，文件中的每一行对应一个字符串：

```python
# readlines() 方法：返回字符串列表，每行一个字符串
with open('sonnet29.txt') as sonnet_file:
    sonnet_file.readlines()  # 返回一个列表，其中每行都是一个字符串
```

```output
['When, in disgrace with fortune and men's eyes,\n',
 ' I all alone beweep my  outcast state,\n',
 "And trouble deaf heaven with my bootless cries,\n",
 "And look upon myself and curse my fate,']
```

您也可以逐行迭代文件：

```python
# 逐行迭代文件（对大文件更节省内存）
with open('sonnet29.txt') as sonnet_file:
    for line in sonnet_file:  # 文件对象是可迭代的
        print(line, end='')  # 打印时不加额外换行
```

```output
When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,
```

## 写入文件

```python
# 写入文件：'w' 模式会覆盖现有文件
with open('bacon.txt', 'w') as bacon_file:  # 'w' = 写入模式
    bacon_file.write('Hello world!\n')  # 返回写入的字符数
```

```output
13
```

```python
# 追加到文件：'a' 模式会追加到现有文件
with open('bacon.txt', 'a') as bacon_file:  # 'a' = 追加模式
    bacon_file.write('Bacon is not a vegetable.')
```

```output
25
```

```python
with open('bacon.txt') as bacon_file:
    content = bacon_file.read()

print(content)
```

```output
Hello world!
Bacon is not a vegetable.
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
打开文件时，模式 <code>'w'</code> 和模式 <code>'a'</code> 有什么区别？
</template>

<base-quiz-option value="A">A. <code>'w'</code> 用于读取，<code>'a'</code> 用于写入</base-quiz-option>
<base-quiz-option value="B" correct>B. <code>'w'</code> 覆盖文件，<code>'a'</code> 追加到文件</base-quiz-option>
<base-quiz-option value="C">C. <code>'w'</code> 用于 Windows，<code>'a'</code> 用于 Apple</base-quiz-option>
<base-quiz-option value="D">D. 没有区别</base-quiz-option>
<base-quiz-answer value="B">模式 <code>'w'</code> 以写入方式打开文件并覆盖任何现有内容。模式 <code>'a'</code> 以追加方式打开文件，将新内容添加到文件末尾。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 相关链接

- <router-link to="/cheatsheet/file-directory-path">文件和目录路径</router-link>
- <router-link to="/cheatsheet/json-yaml">JSON 和 YAML</router-link>
- <router-link to="/blog/python-pathlib-essentials">每位开发者都应知道的 10 个基本文件系统操作</router-link>
- <router-link to="/builtin/open">open()</router-link>
- <router-link to="/builtin/print">print()</router-link>
