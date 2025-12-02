---
title: 'Python Args 和 Kwargs - Python 速查表'
description: 'args 和 kwargs 看起来可能令人畏惧，但实际上它们并不难理解，并且能赋予函数灵活性和可读性。'
labUrl: 'https://labex.io/zh/labs/python-python-args-and-kwargs-633646?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Args 和 Kwargs
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a href="https://docs.python.org/3/tutorial/index.html">Python args and kwargs Made Easy</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    <code>*args</code> 和 <code>**kwargs</code> 可能看起来令人畏惧，但事实是它们并不难理解，并且有能力为您的函数带来极大的灵活性。
  </base-disclaimer-content>
</base-disclaimer>

阅读文章 <router-link to="/blog/python-easy-args-kwargs">Python \*args 和 \*\*kwargs 变得简单</router-link> 以获得更深入的介绍。

## Args 和 Kwargs

`*args` 和 `**kwargs` 允许您在调用函数时传递不确定数量的位置参数和关键字参数。

```python
# 定义一个接受任意数量的位置参数和关键字参数的函数
def some_function(*args, **kwargs):
    pass

# 使用任意数量的位置参数调用
some_function(arg1, arg2, arg3)

# 使用任意数量的关键字参数调用
some_function(key1=arg1, key2=arg2, key3=arg3)

# 使用位置参数和关键字参数调用
some_function(arg, key1=arg1)

# 或者不带任何参数调用
some_function()
```

<base-warning>
  <base-warning-title>
    Python 惯例
  </base-warning-title>
  <base-warning-content>
    <code>*args</code> 和 <code>**kwargs</code> 是惯例。它们不是解释器强制要求的，但被 Python 社区认为是良好的实践。
  </base-warning-content>
</base-warning>

## args

您可以通过 `args` 变量访问*位置参数*：

```python
# *args 将位置参数收集到一个元组中
def some_function(*args):
    print(f'Arguments passed: {args} as {type(args)}')

# 传递多个参数 - 它们将被收集到 args 元组中
some_function('arg1', 'arg2', 'arg3')
```

```output
Arguments passed: ('arg1', 'arg2', 'arg3') as <class 'tuple'>
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-args-and-kwargs-1">
<template #question>
<code>*args</code> 将参数收集到什么数据类型中？
</template>

<base-quiz-option value="A">A. 列表 (A list)</base-quiz-option>
<base-quiz-option value="B" correct>B. 元组 (A tuple)</base-quiz-option>
<base-quiz-option value="C">C. 字典 (A dictionary)</base-quiz-option>
<base-quiz-option value="D">D. 集合 (A set)</base-quiz-option>
<base-quiz-answer value="B"><code>\*args</code> 参数将位置参数收集到一个元组中。这允许函数接受任意数量的位置参数。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## kwargs

关键字参数通过 `kwargs` 变量访问：

```python
# **kwargs 将关键字参数收集到一个字典中
def some_function(**kwargs):
    print(f'keywords: {kwargs} as {type(kwargs)}')

# 传递关键字参数 - 它们将被收集到 kwargs 字典中
some_function(key1='arg1', key2='arg2')
```

```output
keywords: {'key1': 'arg1', 'key2': 'arg2'} as <class 'dict'>
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-args-and-kwargs-2">
<template #question>
<code>**kwargs</code> 将参数收集到什么数据类型中？
</template>

<base-quiz-option value="A">A. 列表 (A list)</base-quiz-option>
<base-quiz-option value="B">B. 元组 (A tuple)</base-quiz-option>
<base-quiz-option value="C" correct>C. 字典 (A dictionary)</base-quiz-option>
<base-quiz-option value="D">D. 集合 (A set)</base-quiz-option>
<base-quiz-answer value="C"><code>\*\*kwargs</code> 参数将关键字参数收集到一个字典中。这允许函数接受任意数量的关键字参数。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 相关链接

- <router-link to="/cheatsheet/functions">函数 (Functions)</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">列表和元组 (Lists and Tuples)</router-link>
- <router-link to="/cheatsheet/dictionaries">Python 字典 (Python Dictionaries)</router-link>
- <router-link to="/blog/python-easy-args-kwargs">Python \*args 和 \*\*kwargs 变得简单 (Python \*args and \*\*kwargs Made Easy)</router-link>
- <router-link to="/builtin/tuple">tuple()</router-link>
- <router-link to="/builtin/dict">dict()</router-link>
