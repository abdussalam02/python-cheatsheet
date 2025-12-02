---
title: 'Python 异常处理 - Python 速查表'
description: '在 Python 中，异常处理是响应程序中发生异常的过程。'
labUrl: 'https://labex.io/zh/labs/python-python-exception-handling-633656?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python 异常处理
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikipedia.org/wiki/Exception_handling">异常处理</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    在计算和计算机编程中，异常处理是响应异常——需要特殊处理的反常或例外情况——的过程。
  </base-disclaimer-content>
</base-disclaimer>

Python 有许多[内置异常](https://docs.python.org/3/library/exceptions.html)，当程序遇到错误时会引发这些异常，并且大多数外部库，如流行的 [Requests](https://requests.readthedocs.io/en/latest)，都包含其[自定义异常](https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions)，我们需要进行处理。

## 基本异常处理

你不能除以零，这是一个数学真理，如果你在 Python 中尝试这样做，解释器将引发内置异常 [ZeroDivisionError](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError)：

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

假设我们不希望程序停止执行或向用户显示他们无法理解的输出。假设我们想打印一条有用且清晰的消息，那么我们需要使用 `try` 和 `except` 关键字来**_处理_**异常：

```python
# try-except: 优雅地处理异常
def divide(dividend , divisor):
    try:  # 尝试执行此代码
        print(dividend / divisor)
    except ZeroDivisionError:  # 捕获特定异常类型
        print('你不能除以 0')

divide(dividend=10, divisor=5)
```

```output
2
```

```python
divide(dividend=10, divisor=0)
```

```output
你不能除以 0
```

<BaseQuiz id="cheatsheet-exception-handling-1" correct="A">
<template #question>
在 Python 中，使用哪些关键字来处理异常？
</template>

<BaseQuizOption value="A" correct>A. <code>try</code> 和 <code>except</code></BaseQuizOption>
<BaseQuizOption value="B">B. <code>catch</code> 和 <code>handle</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>error</code> 和 <code>rescue</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>if</code> 和 <code>else</code></BaseQuizOption>
<BaseQuizAnswer>Python 使用 <code>try</code> 来标记可能引发异常的代码，使用 <code>except</code> 来处理发生的特定异常。</BaseQuizAnswer>
</BaseQuiz>

## 使用一个异常块处理多个异常

你也可以像下面这样在一行中处理多个异常，而无需创建多个异常块。

```python
# 在一个 except 块中处理多个异常
def divide(dividend , divisor):
    try:
        if (dividend == 10):
          var = 'str' + 1  # 这将引发 TypeError
        else:
          print(dividend / divisor)
    except (ZeroDivisionError, TypeError) as error:  # 捕获多种异常类型
        print(error)  # 打印错误消息

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
可以在单个 <code>except</code> 块中处理多种异常类型吗？
</template>

<BaseQuizOption value="A">A. 不行，必须为每种异常类型使用单独的 <code>except</code> 块</BaseQuizOption>
<BaseQuizOption value="B" correct>B. 可以，通过将它们放在一个元组中，如 <code>except (Exception1, Exception2)</code></BaseQuizOption>
<BaseQuizOption value="C">C. 可以，但仅当它们相关时</BaseQuizOption>
<BaseQuizOption value="D">D. 不行，Python 不支持此功能</BaseQuizOption>
<BaseQuizAnswer>你可以通过将多种异常类型放在一个元组中来在一个 <code>except</code> 块中处理它们：<code>except (ZeroDivisionError, TypeError) as error:</code></BaseQuizAnswer>
</BaseQuiz>

## 异常处理中的 Finally 代码

无论是否引发异常，`finally` 部分中的代码始终会被执行：

```python
# finally 块：无论是否发生异常，都会执行
def divide(dividend , divisor):
    try:
        print(dividend / divisor)
    except ZeroDivisionError:
        print('你不能除以 0')
    finally:  # 无论是否发生异常，都始终执行
        print('执行完毕')

divide(dividend=10, divisor=5)
```

```output
2.0
执行完毕
```

```python
divide(dividend=10, divisor=0)
```

```output
你不能除以 0
执行完毕
```

<BaseQuiz id="cheatsheet-exception-handling-3" correct="C">
<template #question>
<code>finally</code> 块何时执行？
</template>

<BaseQuizOption value="A">A. 仅在发生异常时</BaseQuizOption>
<BaseQuizOption value="B">B. 仅在未发生异常时</BaseQuizOption>
<BaseQuizOption value="C" correct>C. 始终执行，无论是否发生异常</BaseQuizOption>
<BaseQuizOption value="D">D. 从不执行</BaseQuizOption>
<BaseQuizAnswer><code>finally</code> 块始终执行，无论是否发生异常。它对于无论结果如何都必须运行的清理代码很有用。</BaseQuizAnswer>
</BaseQuiz>

## 自定义异常

自定义异常通过创建继承自 Python 的基类 `Exception` 的 `class` 来初始化，并使用 `raise` 关键字引发：

```python
# 自定义异常：通过继承 Exception 类创建
class MyCustomException(Exception):
    pass

raise MyCustomException  # 引发自定义异常
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyCustomException
```

要声明自定义异常消息，可以将其作为参数传递：

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

处理自定义异常与处理任何其他异常相同：

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
如何在 Python 中创建自定义异常？
</template>

<BaseQuizOption value="A" correct>A. 创建一个继承自 <code>Exception</code> 类的类</BaseQuizOption>
<BaseQuizOption value="B">B. 使用 <code>@exception</code> 装饰器</BaseQuizOption>
<BaseQuizOption value="C">C. 调用 <code>Exception.create()</code></BaseQuizOption>
<BaseQuizOption value="D">D. 从特殊模块导入它</BaseQuizOption>
<BaseQuizAnswer>自定义异常是通过定义一个继承自基类 <code>Exception</code> 的类来创建的。然后你可以像处理内置异常一样引发和处理它们。</BaseQuizAnswer>
</BaseQuiz>

## 相关链接

- <router-link to="/cheatsheet/control-flow">控制流</router-link>
- <router-link to="/builtin/breakpoint">breakpoint()</router-link>
- <router-link to="/builtin/isinstance">isinstance()</router-link>
- <router-link to="/builtin/issubclass">issubclass()</router-link>
