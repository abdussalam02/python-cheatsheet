---
title: 'Python 列表与元组 - Python 速查表'
description: '在 Python 中，列表是用于存储数据集合的四种数据类型之一。'
labUrl: 'https://labex.io/zh/labs/python-python-lists-and-tuples-633660?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python 列表
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

列表是 Python 中用于存储数据集合的 4 种数据类型之一。

```python
# List: 有序的项目集合，用方括号括起来
['John', 'Peter', 'Debora', 'Charles']
```

## 使用索引获取值

```python
# 使用索引访问列表元素（从 0 开始，第一个元素是索引 0）
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[0]  # 返回第一个元素：'table'
```

```output
'table'
```

```python
furniture[1]
```

```output
'chair'
```

```python
furniture[2]
```

```output
'rack'
```

```python
furniture[3]
```

```output
'shelf'
```

## 负数索引

```python
# 负数索引：从列表末尾访问元素
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[-1]  # 返回最后一个元素：'shelf'
```

```output
'shelf'
```

```python
furniture[-3]
```

```output
'chair'
```

```python
f'The {furniture[-1]} is bigger than the {furniture[-3]}'
```

```output
'The shelf is bigger than the chair'
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-lists-and-tuples-1">
<template #question>
如果 <code>furniture = ['table', 'chair', 'rack', 'shelf']</code>，那么 <code>furniture[-1]</code> 返回什么？
</template>

<base-quiz-option value="A">A. <code>'table'</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>'shelf'</code></base-quiz-option>
<base-quiz-option value="C">C. <code>['shelf']</code></base-quiz-option>
<base-quiz-option value="D">D. <code>IndexError</code></base-quiz-option>
<base-quiz-answer value="B">负数索引从列表末尾访问元素。<code>-1</code> 指向最后一个元素，<code>-2</code> 指向倒数第二个，依此类推。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 使用切片获取子列表

```python
# 切片：使用 [start:end] 语法获取子列表（end 是不包含的）
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[0:4]  # 返回索引 0 到 3 的元素（不包含 4）
```

```output
['table', 'chair', 'rack', 'shelf']
```

```python
furniture[1:3]
```

```output
['chair', 'rack']
```

```python
furniture[0:-1]
```

```output
['table', 'chair', 'rack']
```

```python
# 从开头切片：省略 start 索引（默认为 0）
furniture[:2]  # 返回前两个元素
```

```output
['table', 'chair']
```

```python
# 切片到末尾：省略 end 索引（默认为列表末尾）
furniture[1:]  # 返回从索引 1 到末尾的所有元素
```

```output
['chair', 'rack', 'shelf']
```

```python
furniture[:]
```

```output
['table', 'chair', 'rack', 'shelf']
```

切片整个列表将执行复制：

```python
# 切片创建副本：[:] 创建列表的浅拷贝
spam = ['cat', 'bat', 'rat', 'elephant']
spam2 = spam[:]  # 创建一个副本，而不是引用
spam2
```

```output
['cat', 'bat', 'rat', 'elephant']
```

```python
spam.append('dog')
spam
```

```output
['cat', 'bat', 'rat', 'elephant', 'dog']
```

```python
spam2
```

```output
['cat', 'bat', 'rat', 'elephant']
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-lists-and-tuples-2">
<template #question>
当 <code>spam</code> 是一个列表时，<code>spam[:]</code> 创建什么？
</template>

<base-quiz-option value="A">A. 对同一列表的引用</base-quiz-option>
<base-quiz-option value="B">B. 一个空列表</base-quiz-option>
<base-quiz-option value="C" correct>C. 列表的浅拷贝</base-quiz-option>
<base-quiz-option value="D">D. 一个反转的列表</base-quiz-option>
<base-quiz-answer value="C">使用 <code>[:]</code> 对整个列表进行切片会创建一个浅拷贝。修改副本不会影响原始列表。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 使用 len() 获取列表长度

```python
# len() 返回列表中项目的数量
furniture = ['table', 'chair', 'rack', 'shelf']
len(furniture)  # 返回 4
```

```output
4
```

## 使用索引更改值

```python
# 通过向索引分配新值来修改列表元素
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[0] = 'desk'  # 替换第一个元素
furniture
```

```output
['desk', 'chair', 'rack', 'shelf']
```

```python
furniture[2] = furniture[1]
furniture
```

```output
['desk', 'chair', 'chair', 'shelf']
```

```python
furniture[-1] = 'bed'
furniture
```

```output
['desk', 'chair', 'chair', 'bed']
```

## 拼接和复制

```python
# 列表拼接：使用 + 运算符组合两个列表
[1, 2, 3] + ['A', 'B', 'C']  # 返回 [1, 2, 3, 'A', 'B', 'C']
```

```output
[1, 2, 3, 'A', 'B', 'C']
```

```python
# 列表复制：使用 * 运算符多次重复列表
['X', 'Y', 'Z'] * 3  # 返回 ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
```

```output
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
```

```python
my_list = [1, 2, 3]
my_list = my_list + ['A', 'B', 'C']
my_list
```

```output
[1, 2, 3, 'A', 'B', 'C']
```

## 使用 for 循环处理列表

```python
# 使用 for 循环遍历列表元素
furniture = ['table', 'chair', 'rack', 'shelf']

for item in furniture:  # 遍历每个项目
    print(item)
```

```output
table
chair
rack
shelf
```

## 使用 enumerate() 在循环中获取索引

```python
# enumerate() 在循环中同时返回索引和值
furniture = ['table', 'chair', 'rack', 'shelf']

for index, item in enumerate(furniture):  # 一起获取索引和项目
    print(f'index: {index} - item: {item}')
```

```output
index: 0 - item: table
index: 1 - item: chair
index: 2 - item: rack
index: 3 - item: shelf
```

## 使用 zip() 在多个列表中循环

```python
# zip() 按元素将多个列表组合在一起进行循环
furniture = ['table', 'chair', 'rack', 'shelf']
price = [100, 50, 80, 40]

for item, amount in zip(furniture, price):  # 配对两个列表中的元素
    print(f'The {item} costs ${amount}')
```

```output
The table costs $100
The chair costs $50
The rack costs $80
The shelf costs $40
```

## in 和 not in 运算符

```python
# in 运算符：检查一个项目是否存在于列表中
'rack' in ['table', 'chair', 'rack', 'shelf']  # 返回 True
```

```output
True
```

```python
'bed' in ['table', 'chair', 'rack', 'shelf']
```

```output
False
```

```python
furniture = ['table', 'chair', 'rack', 'shelf']
'bed' not in furniture
```

```output
True
```

```python
'rack' not in furniture
```

```output
False
```

## 多重赋值技巧

多重赋值技巧是一种快捷方式，允许您在一行代码中用列表中的值给多个变量赋值。所以，与其这样做：

```python
furniture = ['table', 'chair', 'rack', 'shelf']
table = furniture[0]
chair = furniture[1]
rack = furniture[2]
shelf = furniture[3]
```

您可以输入这一行代码：

```python
furniture = ['table', 'chair', 'rack', 'shelf']
table, chair, rack, shelf = furniture

table
```

```output
'table'
```

```python
chair
```

```output
'chair'
```

```python
rack
```

```output
'rack'
```

```python
shelf
```

```output
'shelf'
```

多重赋值技巧也可以用来交换两个变量的值：

```python
a, b = 'table', 'chair'
a, b = b, a
print(a)
```

```output
chair
```

```python
print(b)
```

```output
table
```

## index 方法

`index` 方法允许您通过传递其名称来查找值的索引：

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.index('chair')
```

```output
1
```

## 添加值

### append()

`append` 将一个元素添加到 `list` 的末尾：

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.append('bed')
furniture
```

```output
['table', 'chair', 'rack', 'shelf', 'bed']
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-lists-and-tuples-3">
<template #question>
<code>append()</code> 方法对列表做什么？
</template>

<base-quiz-option value="A" correct>A. 将一个元素添加到列表的末尾</base-quiz-option>
<base-quiz-option value="B">B. 将一个元素添加到列表的开头</base-quiz-option>
<base-quiz-option value="C">C. 替换最后一个元素</base-quiz-option>
<base-quiz-option value="D">D. 移除最后一个元素</base-quiz-option>
<base-quiz-answer value="A"><code>append()</code> 方法将单个元素添加到列表的末尾。要将元素添加到特定位置，请使用 <code>insert()</code>。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

### insert()

`insert` 在给定位置向 `list` 添加一个元素：

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.insert(1, 'bed')
furniture
```

```output
['table', 'bed', 'chair', 'rack', 'shelf']
```

## 移除值

### del()

`del` 使用索引移除一个项：

```python
furniture = ['table', 'chair', 'rack', 'shelf']
del furniture[2]
furniture
```

```output
['table', 'chair', 'shelf']
```

```python
del furniture[2]
furniture
```

```output
['table', 'chair']
```

### remove()

`remove` 使用其实际值移除一个项：

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.remove('chair')
furniture
```

```output
['table', 'rack', 'shelf']
```

<base-warning>
  <base-warning-title>
    移除重复项
  </base-warning-title>
  <base-warning-content>
    如果该值在列表中出现多次，则只移除该值的第一个实例。
  </base-warning-content>
</base-warning>

### pop()

默认情况下，`pop` 将移除并返回列表的最后一个项。您也可以将元素的索引作为可选参数传递：

```python
animals = ['cat', 'bat', 'rat', 'elephant']

animals.pop()
```

```output
'elephant'
```

```python
animals
```

```output
['cat', 'bat', 'rat']
```

```python
animals.pop(0)
```

```output
'cat'
```

```python
animals
```

```output
['bat', 'rat']
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-lists-and-tuples-4">
<template #question>
调用列表上的 <code>pop()</code> 会做什么？
</template>

<base-quiz-option value="A">A. 只移除最后一项</base-quiz-option>
<base-quiz-option value="B" correct>B. 移除并返回一项（默认最后一个，或指定的索引）</base-quiz-option>
<base-quiz-option value="C">C. 只返回最后一项而不移除它</base-quiz-option>
<base-quiz-option value="D">D. 移除列表中的所有项</base-quiz-option>
<base-quiz-answer value="B"><code>pop()</code> 方法会移除并返回一项。默认情况下它移除最后一项，但您可以传递一个索引来移除特定项。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 使用 sort() 对值进行排序

```python
numbers = [2, 5, 3.14, 1, -7]
numbers.sort()
numbers
```

```output
[-7, 1, 2, 3.14, 5]
```

```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.sort()
furniture
```

```output
['chair', 'rack', 'shelf', 'table']
```

您也可以为 `reverse` 关键字参数传递 `True`，以便 `sort()` 以相反的顺序对值进行排序：

```python
furniture.sort(reverse=True)
furniture
```

```output
['table', 'shelf', 'rack', 'chair']
```

如果您需要按常规字母顺序对值进行排序，请在 sort() 方法调用中为 key 关键字参数传递 `str.lower`：

```python
letters = ['a', 'z', 'A', 'Z']
letters.sort(key=str.lower)
letters
```

```output
['a', 'A', 'z', 'Z']
```

您可以使用内置函数 `sorted` 来返回一个新列表：

```python
furniture = ['table', 'chair', 'rack', 'shelf']
sorted(furniture)
```

```output
['chair', 'rack', 'shelf', 'table']
```

## Tuple 数据类型

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://stackoverflow.com/questions/1708510/list-vs-tuple-when-to-use-each">元组与列表</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    元组和列表之间的关键区别在于，<code>元组</code>是<i>不可变</i>对象，而<code>列表</code>是<i>可变</i>对象。这意味着元组不能被更改，而列表可以被修改。元组比列表更节省内存。
  </base-disclaimer-content>
</base-disclaimer>

```python
furniture = ('table', 'chair', 'rack', 'shelf')

furniture[0]
```

```output
'table'
```

```python
furniture[1:3]
```

```output
('chair', 'rack')
```

```python
len(furniture)
```

```output
4
```

元组与列表的主要区别在于，元组像字符串一样是不可变的。

## 在 list() 和 tuple() 之间转换

```python
tuple(['cat', 'dog', 5])
```

```output
('cat', 'dog', 5)
```

```python
list(('cat', 'dog', 5))
```

```output
['cat', 'dog', 5]
```

```python
list('hello')
```

```output
['h', 'e', 'l', 'l', 'o']
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-lists-and-tuples-5">
<template #question>
Python 中列表和元组的主要区别是什么？
</template>

<base-quiz-option value="A">A. 列表只能包含数字，元组可以包含任何内容</base-quiz-option>
<base-quiz-option value="B">B. 元组创建速度更快</base-quiz-option>
<base-quiz-option value="C" correct>C. 列表是可变的（可以更改），元组是不可变的（不能更改）</base-quiz-option>
<base-quiz-option value="D">D. 列表使用方括号，元组使用花括号</base-quiz-option>
<base-quiz-answer value="C">列表是可变的，意味着您可以在创建后修改它们。元组是不可变的，意味着一旦创建就不能更改。两者都可以包含任何类型的数据。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 相关链接

- <router-link to="/blog/python-data-types">Python 数据类型：初学者视觉指南</router-link>
- <router-link to="/blog/python-comprehensions-step-by-step">Python 推导式分步指南</router-link>
- <router-link to="/cheatsheet/comprehensions">Python 推导式</router-link>
- <router-link to="/modules/itertools-module">itertools 模块</router-link>
- <router-link to="/builtin/list">list()</router-link>
- <router-link to="/builtin/tuple">tuple()</router-link>
- <router-link to="/builtin/len">len()</router-link>
