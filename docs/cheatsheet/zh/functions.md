---
title: 'Python 函数 - Python 速查表'
description: '在 Python 中，函数是一段组织良好的代码块，用于执行单个任务。'
labUrl: 'https://labex.io/zh/labs/python-python-functions-633658?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python 函数
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikiversity.org/wiki/Programming_Fundamentals/Functions">编程函数</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    函数是一个组织良好的代码块，用于执行单个任务。它们为您的应用程序提供了更好的模块化和可重用性。
  </base-disclaimer-content>
</base-disclaimer>

## 函数参数

函数可以接受 `参数` 和 `返回值`：

在下面的示例中，函数 **say_hello** 接收参数 "name" 并打印问候语：

```python
# 定义一个接受一个参数的函数
def say_hello(name):
   print(f'Hello {name}')

# 使用字符串参数调用函数
say_hello('Carlos')
```

```output
Hello Carlos
```

```python
say_hello('Wanda')
```

```output
Hello Wanda
```

```python
say_hello('Rose')
```

```output
Hello Rose
```

## 关键字参数

为了提高代码的可读性，我们应该尽可能明确。我们可以通过使用 `关键字参数` 在函数中实现这一点：

```python
# 带有多个参数的函数
def say_hi(name, greeting):
   print(f"{greeting} {name}")

# 位置参数：顺序很重要
say_hi('John', 'Hello')
```

```output
Hello John
```

```python
# 关键字参数：顺序不重要，更具可读性
say_hi(name='Anna', greeting='Hi')
```

```output
Hi Anna
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-functions-1">
<template #question>
在 Python 函数中使用关键字参数的主要优点是什么？
</template>

<base-quiz-option value="A">A. 它们执行得更快</base-quiz-option>
<base-quiz-option value="B">B. 它们使用的内存更少</base-quiz-option>
<base-quiz-option value="C" correct>C. 它们提高了代码的可读性，并且顺序不重要</base-quiz-option>
<base-quiz-option value="D">D. 它们可以防止错误</base-quiz-option>
<base-quiz-answer value="C">关键字参数通过使每个参数的含义清晰来提高代码的可读性，并且允许您以任何顺序传递参数。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 返回值

在使用 `def` 语句创建函数时，您可以使用 `return` 语句指定返回值是什么。返回语句包括以下内容：

- `return` 关键字。

- 函数应返回的值或表达式。

```python
# 使用 return 语句返回一个值的函数
def sum_two_numbers(number_1, number_2):
   return number_1 + number_2

# 调用函数并存储返回的值
result = sum_two_numbers(7, 8)
print(result)
```

```output
15
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-functions-2">
<template #question>
在 Python 中，使用哪个关键字从函数中返回一个值？
</template>

<base-quiz-option value="A" correct>A. <code>return</code></base-quiz-option>
<base-quiz-option value="B">B. <code>output</code></base-quiz-option>
<base-quiz-option value="C">C. <code>yield</code></base-quiz-option>
<base-quiz-option value="D">D. <code>exit</code></base-quiz-option>
<base-quiz-answer value="A">使用 <code>return</code> 关键字从函数返回一个值。如果未使用 return 语句，函数将返回 <code>None</code>。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 局部和全局作用域

- 全局作用域中的代码不能使用任何局部变量。

- 但是，局部作用域可以访问全局变量。

- 函数的局部作用域中的代码不能使用任何其他局部作用域中的变量。

- 您可以使用相同的名称定义不同的变量，如果它们位于不同的作用域中。也就是说，可以有一个名为 spam 的局部变量和一个也名为 spam 的全局变量。

```python
# 全局变量：随处可访问
global_variable = 'I am available everywhere'

def some_function():
    print(global_variable)  # 可以访问全局变量
    # 局部变量：仅在此函数内存在
    local_variable = "only available within this function"
    print(local_variable)

# 这将引发 NameError：local_variable 在全局作用域中不存在
print(local_variable)
```

```output
Traceback (most recent call last):
  File "<stdin>", line 10, in <module>
NameError: name 'local_variable' is not defined
```

## global 语句

如果您需要在函数内部修改全局变量，请使用 global 语句：

```python
# 使用 'global' 关键字从函数内部修改全局变量
def spam():
    global eggs  # 声明我们将修改全局变量
    eggs = 'spam'  # 这会更改全局变量

eggs = 'global'
spam()  # 函数修改全局变量
print(eggs)  # 打印 'spam'，而不是 'global'
```

```output
spam
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-functions-3">
<template #question>
在函数内部，您必须使用哪个关键字来修改全局变量？
</template>

<base-quiz-option value="A">A. <code>nonlocal</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>global</code></base-quiz-option>
<base-quiz-option value="C">C. <code>extern</code></base-quiz-option>
<base-quiz-option value="D">D. 不需要关键字</base-quiz-option>
<base-quiz-answer value="B">必须在函数内部使用 <code>global</code> 关键字来修改全局变量。如果没有它，Python 将创建一个局部变量。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

判断变量是在局部作用域还是全局作用域有四个规则：

1. 如果一个变量在全局作用域中使用（即在所有函数之外），那么它总是全局变量。

1. 如果函数中存在该变量的全局语句，则它是全局变量。

1. 否则，如果该变量在函数中的赋值语句中使用，则它是局部变量。

1. 但如果该变量在赋值语句中未使用，则它是全局变量。

## Lambda 函数

在 Python 中，lambda 函数是单行、匿名函数，可以有任意数量的参数，但只能有一个表达式。

<base-disclaimer>
  <base-disclaimer-title>
    来自 <a target="_blank" href="https://docs.python.org/3/library/ast.html?highlight=lambda#function-and-class-definitions">Python 3 教程</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    lambda 是一个最小函数定义，可以在表达式中使用。与 FunctionDef 不同，body 包含单个节点。
  </base-disclaimer-content>
</base-disclaimer>

<base-warning>
  <base-warning-title>
    单行表达式
  </base-warning-title>
  <base-warning-content>
    Lambda 函数只能评估一个表达式，例如单行代码。
  </base-warning-content>
</base-warning>

这个函数：

```python
# 常规函数定义
def add(x, y):
    return x + y

add(5, 3)
```

```output
8
```

等同于 _lambda_ 函数：

```python
# Lambda 函数：在一行中定义的匿名函数
# 语法：lambda arguments: expression
add = lambda x, y: x + y
add(5, 3)
```

```output
8
```

<base-quiz>
<base-quiz-question correct="D" id="cheatsheet-functions-4">
<template #question>
Python 中的 lambda 函数是什么？
</template>

<base-quiz-option value="A">A. 只能调用一次的函数</base-quiz-option>
<base-quiz-option value="B">B. 不接受任何参数的函数</base-quiz-option>
<base-quiz-option value="C">C. 返回多个值的函数</base-quiz-option>
<base-quiz-option value="D" correct>D. 可以有任意数量的参数但只有一个表达式的单行匿名函数</base-quiz-option>
<base-quiz-answer value="D">Lambda 函数是使用 <code>lambda</code> 关键字定义的匿名、单行函数。它可以接受任意数量的参数，但只能包含一个表达式。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

与常规嵌套函数一样，lambda 也可以作为词法闭包：

```python
# Lambda 闭包：从外部作用域捕获变量的 lambda 函数
def make_adder(n):
    return lambda x: x + n  # Lambda 从外部函数捕获 'n'

# 创建添加不同数量的函数
plus_3 = make_adder(3)  # 返回一个加 3 的 lambda
plus_5 = make_adder(5)  # 返回一个加 5 的 lambda

plus_3(4)  # 返回 4 + 3 = 7
```

```output
7
```

```python
plus_5(4)
```

```output
9
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-functions-5">
<template #question>
Lambda 闭包允许您做什么？
</template>

<base-quiz-option value="A" correct>A. 从外部作用域捕获变量</base-quiz-option>
<base-quiz-option value="B">B. 在不使用 global 关键字的情况下修改全局变量</base-quiz-option>
<base-quiz-option value="C">C. 返回多个值</base-quiz-option>
<base-quiz-option value="D">D. 异步执行代码</base-quiz-option>
<base-quiz-answer value="A">Lambda 闭包允许 lambda 函数捕获并使用其封闭作用域中的变量，类似于常规的嵌套函数。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 相关链接

- <router-link to="/blog/python-easy-args-kwargs">\*args 和 \*\*kwargs 解释</router-link>
- <router-link to="/cheatsheet/args-and-kwargs">Args 和 Kwargs</router-link>
- <router-link to="/cheatsheet/decorators">装饰器</router-link>
- <router-link to="/cheatsheet/control-flow">控制流</router-link>
- <router-link to="/cheatsheet/basics">基础知识</router-link>
- <router-link to="/builtin">内置函数</router-link>
