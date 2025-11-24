---
title: 'Python 基础 - Python 速查表'
description: '通过我们涵盖运算符、数据类型、变量、函数等的综合指南学习 Python 基础知识。非常适合初学者学习 Python 编程基础。'
labUrl: 'https://labex.io/zh/labs/python-python-basics-633647?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python 基础知识
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

我们都需要从某个地方开始，那么从这里开始怎么样呢。本指南涵盖了基本的 Python 基础知识，包括运算符、数据类型、变量和核心函数。

<base-disclaimer>
<base-disclaimer-title>
Python 基础知识概述
</base-disclaimer-title>
<base-disclaimer-content>
每个初学者都应该知道的核心 Python 基础知识：

- 变量和基本类型
- 运算符和表达式
- 字符串和常用方法
- 列表、元组和字典
- 基本控制流（if、for、while）
- 简单函数

</base-disclaimer-content>
</base-disclaimer>

## 数学运算符

按**最高**到**最低**的优先级排序：

| 运算符 | 操作      | 示例            |
| :----- | :-------- | :-------------- |
| \*\*   | 幂运算    | `2 ** 3 = 8`    |
| %      | 取模/余数 | `22 % 8 = 6`    |
| //     | 整数除法  | `22 // 8 = 2`   |
| /      | 除法      | `22 / 8 = 2.75` |
| \*     | 乘法      | `3 * 3 = 9`     |
| -      | 减法      | `5 - 2 = 3`     |
| +      | 加法      | `2 + 2 = 4`     |

表达式示例：

```python
# 乘法优先级高于加法
# 所以这被评估为：2 + (3 * 6) = 2 + 18 = 20
2 + 3 * 6
```

```output
20
```

```python
# 括号覆盖运算符优先级
# 这被评估为：5 * 6 = 30
(2 + 3) * 6
```

```output
30
```

```python
2 ** 8
```

```output
256
```

```python
23 // 7
```

```output
3
```

```python
23 % 7
```

```output
2
```

```python
(5 - 1) * ((7 + 1) / (3 - 1))
```

```output
16.0
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
这个 Python 表达式的结果是什么？

```python
4 + 2 * 3
```

</template>

<base-quiz-option value="A" correct>A. 10</base-quiz-option>
<base-quiz-option value="B">B. 18</base-quiz-option>
<base-quiz-option value="C">C. 12</base-quiz-option>
<base-quiz-option value="D">D. 20</base-quiz-option>
<base-quiz-answer value="A">乘法优先级高于加法，所以这被评估为：4 + (2 \* 3) = 4 + 6 = 10</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 增强赋值运算符

| 运算符      | 等效于           |
| :---------- | :--------------- |
| `var += 1`  | `var = var + 1`  |
| `var -= 1`  | `var = var - 1`  |
| `var *= 1`  | `var = var * 1`  |
| `var /= 1`  | `var = var / 1`  |
| `var //= 1` | `var = var // 1` |
| `var %= 1`  | `var = var % 1`  |
| `var **= 1` | `var = var ** 1` |

示例：

```python
# 增强赋值：等同于 greeting = greeting + ' world!'
greeting = 'Hello'
greeting += ' world!'
greeting
```

```output
'Hello world!'
```

```python
# 数字增 1
number = 1
number += 1
number
```

```output
2
```

```python
# 列表复制：等同于 my_list = my_list * 3
my_list = ['item']
my_list *= 3
my_list
```

```output
['item', 'item', 'item']
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
执行此代码后 <code>x</code> 的值是多少？

```python
x = 5
x += 3
```

</template>

<base-quiz-option value="A">A. 3</base-quiz-option>
<base-quiz-option value="B" correct>B. 8</base-quiz-option>
<base-quiz-option value="C">C. 5</base-quiz-option>
<base-quiz-option value="D">D. 15</base-quiz-option>
<base-quiz-answer value="B">增强赋值运算符 <code>+=</code> 等同于 <code>x = x + 3</code>。所以 <code>x</code> 开始是 5，然后变为 5 + 3 = 8。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 海象运算符 (Walrus Operator)

海象运算符允许在表达式中为变量赋值，同时返回该变量的值

示例：

```python
# 海象运算符在一个表达式中赋值并返回值
# my_var 被赋值为 "Hello World!" 然后被打印
print(my_var:="Hello World!")
```

```output
Hello World!
```

```python
my_var="Yes"
print(my_var)
```

```output
Yes
```

```python
print(my_var:="Hello")
```

```output
Hello
```

海象运算符，或**赋值表达式运算符**，首次通过 [PEP 572](https://peps.python.org/pep-0572/) 引入于 2018 年，随后于 2019 年 10 月正式发布于 **Python 3.8**。

<base-disclaimer>
  <base-disclaimer-title>
    语法语义和示例
  </base-disclaimer-title>
  <base-disclaimer-content>
  <a href="https://peps.python.org/pep-0572/" target="_blank">PEP 572</a> 提供了海象运算符的语法、语义和示例。
  </base-disclaimer-content>
</base-disclaimer>

## 数据类型

理解数据类型是 Python 基础知识中最重要的部分之一。Python 有九种核心内置数据类型，几乎涵盖了你需要的所有内容：

| 数据类型                                                   | 示例                                     | 描述                 |
| :--------------------------------------------------------- | :--------------------------------------- | :------------------- |
| **数字 (Numbers)**                                         |                                          |                      |
| <router-link to='/builtin/int'>`int`</router-link>         | `-2, -1, 0, 1, 2, 3, 4, 5`               | 整数                 |
| <router-link to='/builtin/float'>`float`</router-link>     | `-1.25, -1.0, -0.5, 0.0, 0.5, 1.0, 1.25` | 带小数点的数字       |
| <router-link to='/builtin/complex'>`complex`</router-link> | `2+3j, complex(1, 4)`                    | 具有实部和虚部的数字 |
| **文本 (Text)**                                            |                                          |                      |
| <router-link to='/builtin/str'>`str`</router-link>         | `'a', 'Hello!', "Python"`                | 文本和字符           |
| **布尔值 (Boolean)**                                       |                                          |                      |
| <router-link to='/builtin/bool'>`bool`</router-link>       | `True, False`                            | True 或 False 值     |
| **None**                                                   |                                          |                      |
| `NoneType`                                                 | `None`                                   | 表示“无值”或“空”     |
| **集合 (Collections)**                                     |                                          |                      |
| <router-link to='/builtin/list'>`list`</router-link>       | `[1, 2, 3], ['a', 'b', 'c']`             | 有序、可更改的集合   |
| <router-link to='/builtin/dict'>`dict`</router-link>       | `{'name': 'Alice', 'age': 30}`           | 键值对               |
| <router-link to='/builtin/tuple'>`tuple`</router-link>     | `(1, 2, 3), ('a', 'b')`                  | 有序、不可更改的集合 |
| <router-link to='/builtin/set'>`set`</router-link>         | `{1, 2, 3}, {'a', 'b', 'c'}`             | 无序的唯一项集合     |

### 快速示例

```python
# 数字
age = 25                    # int
price = 19.99              # float
coordinate = 2 + 3j        # complex

# 文本
name = "Alice"             # str

# 布尔值
is_student = True          # bool

# None
result = None              # NoneType

# 集合
scores = [85, 92, 78]      # list
person = {'name': 'Bob', 'age': 30}  # dict
coordinates = (10, 20)     # tuple
unique_ids = {1, 2, 3}     # set
```

有关包含视觉示例和每种类型使用时机的详细说明的全面指南，请参阅：<router-link to="/blog/python-data-types">Python 数据类型：初学者的视觉指南</router-link>。

## 拼接和复制

字符串拼接：

```python
# 字符串拼接：相邻的字符串会自动连接
'Alice' 'Bob'
```

```output
'AliceBob'
```

字符串复制：

```python
# 字符串复制：将字符串重复多次
'Alice' * 5
```

```output
'AliceAliceAliceAliceAlice'
```

## 变量

变量是 Python 基础知识的一个基本组成部分。只要遵循以下规则，你可以给变量命名为任何名称：

1. 只能是一个单词。

```python
# 错误
my variable = 'Hello'

# 正确
var = 'Hello'
```

2. 只能使用字母、数字和下划线 (`_`) 字符。

```python
# 错误
%$@variable = 'Hello'

# 正确
my_var = 'Hello'

# 正确
my_var_2 = 'Hello'
```

3. 不能以数字开头。

```python
# 这将不起作用
23_var = 'hello'
```

4. 以（单个）下划线 (`_`) 开头的变量被认为是“不常用的”。

```python
# _spam 不应在代码中再次使用
_spam = 'Hello'
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
在 Python 基础知识中，以下哪个是有效的变量名？
</template>

<base-quiz-option value="A">A. <code>3value</code></base-quiz-option>
<base-quiz-option value="B">B. <code>user-name</code></base-quiz-option>
<base-quiz-option value="C" correct>C. <code>user_name</code></base-quiz-option>
<base-quiz-option value="D">D. <code>for</code></base-quiz-option>
<base-quiz-answer value="C"><code>user_name</code> 是一个有效的变量名，因为它只使用字母、数字和下划线，并且不以数字开头。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 注释

行内注释：

```python
# 这是一个注释
```

多行注释：

```python
# 这是一个
# 多行注释
```

带注释的代码：

```python
a = 1  # 初始化
```

请注意注释前面的两个空格。

函数文档字符串 (docstring)：

```python
def foo():
    """
    这是一个函数文档字符串
    你也可以使用：
    ''' 函数文档字符串 '''
    """
```

## print() 函数

`print()` 函数是你将学习的第一个 Python 基础知识之一。它会写入其接收到的参数的值。[...] 它处理多个参数、浮点数和字符串。字符串在打印时没有引号，并且项目之间会插入一个空格，因此你可以很好地格式化内容：

```python
print('Hello world!')
```

```output
Hello world!
```

```python
a = 1
print('Hello world!', a)
```

```output
Hello world! 1
```

### end 关键字

可以使用关键字参数 `end` 来避免输出后的换行符，或者用不同的字符串结束输出：

```python
# 使用 end 参数来更改每个 print 语句之后的内容
phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
for word in phrase:
    print(word, end='-')  # 使用 '-' 代替换行符
```

```output
printed-with-a-dash-in-between-
```

### sep 关键字

如果存在多个对象，关键字 `sep` 指定了对象之间的分隔方式：

```python
# 使用 sep 参数指定多个参数之间的分隔符
print('cats', 'dogs', 'mice', sep=',')  # 逗号分隔的输出
```

```output
cats,dogs,mice
```

## input() 函数

此函数从用户处获取输入并将其转换为字符串：

```python
# input() 读取用户输入并将其作为字符串返回
print('What is your name?')   # 询问他们的名字
my_name = input()  # 等待用户输入并按 Enter
print('Hi, {}'.format(my_name))
```

```output
What is your name?
Martha
Hi, Martha
```

`input()` 也可以在不使用 `print()` 的情况下设置默认消息：

```python
my_name = input('What is your name? ')  # 默认消息
print('Hi, {}'.format(my_name))
```

```output
What is your name? Martha
Hi, Martha
```

也可以使用格式化字符串来避免使用 .format：

```python
# input() 可以直接显示提示信息
my_name = input('What is your name? ')  # 提示和读取在一次调用中完成
print(f'Hi, {my_name}')  # f-string 用于字符串格式化
```

```output
What is your name? Martha
Hi, Martha
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
在 Python 基础知识中，`input()` 返回什么类型？
</template>

<base-quiz-option value="A">A. int</base-quiz-option>
<base-quiz-option value="B" correct>B. str</base-quiz-option>
<base-quiz-option value="C">C. float</base-quiz-option>
<base-quiz-option value="D">D. 取决于用户输入</base-quiz-option>
<base-quiz-answer value="B"><code>input()</code> 函数总是返回一个字符串，无论用户输入什么。如果需要，你需要将其转换为其他类型。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## len() 函数

评估字符串、列表、字典等的字符数或项目数的整数值：

```python
# len() 返回字符串中的字符数
len('hello')  # 返回 5
```

```output
5
```

```python
# len() 返回列表中项目的数量
len(['cat', 3, 'dog'])  # 返回 3 (三个项目)
```

```output
3
```

<base-warning>
  <base-warning-title>空值测试</base-warning-title>
  <base-warning-content>
    对字符串、列表、字典等的空值测试不应使用
    <code>len</code>，而应优先使用直接的布尔值评估。
  </base-warning-content>
</base-warning>

空值测试示例：

```python
a = [1, 2, 3]

# 错误：不必要的 len() 检查
if len(a) > 0:  # 评估为 True
    print("the list is not empty!")
```

```output
the list is not empty!
```

```python
# 正确：直接布尔评估 (Pythonic 方式)
if a:  # 如果列表不为空，则评估为 True
    print("the list is not empty!")
```

```output
the list is not empty!
```

## str()、int() 和 float() 函数

这些函数允许你更改变量的类型。例如，你可以将 `integer` 或 `float` 转换为 `string`：

```python
# 整数转字符串
str(29)  # 返回 '29'
```

```output
'29'
```

```python
str(-3.14)
```

```output
'-3.14'
```

或者从 `string` 转换为 `integer` 或 `float`：

```python
# 字符串转整数
int('11')  # 返回 11
```

```output
11
```

```python
# 字符串转浮点数
float('3.14')  # 返回 3.14
```

```output
3.14
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
这段 Python 代码的结果是什么？

```python
result = int('42')
type(result)
```

</template>

<base-quiz-option value="A">A. <code>str</code></base-quiz-option>
<base-quiz-option value="B">B. <code>float</code></base-quiz-option>
<base-quiz-option value="C" correct>C. <code>int</code></base-quiz-option>
<base-quiz-option value="D">D. <code>NoneType</code></base-quiz-option>
<base-quiz-answer value="C"><code>int()</code> 函数将字符串转换为整数。因此 <code>int('42')</code> 返回整数 <code>42</code>，而 <code>type(42)</code> 返回 <code>int</code>。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 相关链接

- <router-link to="/blog/python-data-types">Python 数据类型：初学者的视觉指南</router-link>
- <router-link to="/blog/python-comprehensions-step-by-step">Python 推导式分步指南</router-link>
- <router-link to="/cheatsheet/control-flow">控制流</router-link>
- <router-link to="/cheatsheet/functions">函数</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">列表和元组</router-link>
- <router-link to="/cheatsheet/dictionaries">字典</router-link>
- <router-link to="/cheatsheet/sets">集合</router-link>
- <router-link to="/cheatsheet/string-formatting">字符串格式化</router-link>
