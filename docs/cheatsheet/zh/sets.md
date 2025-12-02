---
title: 'Python 集合 - Python 速查表'
description: 'Python 内置了多种数据类型来帮助我们组织数据，这些结构包括列表、字典、元组和集合。'
labUrl: 'https://labex.io/zh/labs/python-python-sets-633665?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python 集合 (Sets)
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

Python 配备了几种内置数据类型来帮助我们组织数据。这些结构包括列表 (lists)、字典 (dictionaries)、元组 (tuples) 和**集合 (sets)**。

<base-disclaimer>
  <base-disclaimer-title>
    来自 Python 3 <a target="_blank" href="https://docs.python.org/3/tutorial/datastructures.html#sets">文档</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    集合是无序的、不包含重复元素的集合。基本用途包括成员资格测试和消除重复条目。
  </base-disclaimer-content>
</base-disclaimer>

阅读 <router-link to="/blog/python-sets-what-why-how">Python 集合：是什么、为什么和如何使用</router-link> 以获得更深入的参考。

## 初始化集合

创建集合有两种方法：使用花括号 `{}` 和内置函数 `set()`

<base-warning>
  <base-warning-title>
    空集合
  </base-warning-title>
  <base-warning-content>
    创建集合时，请确保不要使用空花括号 <code>{}</code>，否则您将得到一个空字典。
  </base-warning-content>
</base-warning>

```python
# 使用花括号或 set() 函数创建集合
s = {1, 2, 3}  # 使用花括号
s = set([1, 2, 3])  # 使用 set() 构造函数

# 警告：空 {} 创建一个字典，而不是一个集合
s = {}  # 这将创建一个字典而不是一个集合
type(s)  # 返回 <class 'dict'>
```

```output
<class 'dict'>
```

## 唯一元素的无序集合

集合会自动删除所有重复的值。

```python
# 集合会自动删除重复项
s = {1, 2, 3, 2, 3, 4}  # 重复项被删除
s  # 返回 {1, 2, 3, 4}
```

```output
{1, 2, 3, 4}
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-sets-1">
<template #question>
当你创建一个包含重复值的集合时会发生什么？
</template>

<base-quiz-option value="A" correct>A. 重复项被自动删除</base-quiz-option>
<base-quiz-option value="B">B. 抛出错误</base-quiz-option>
<base-quiz-option value="C">C. 集合保留所有重复项</base-quiz-option>
<base-quiz-option value="D">D. 只保留第一次出现的</base-quiz-option>
<base-quiz-answer value="A">集合会自动删除重复的值。集合是无序的、不包含重复元素的集合。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

并且由于它是一种无序数据类型，因此不能对其进行索引。

```python
s = {1, 2, 3}
s[0]
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
```

## 集合的添加和更新 (add and update)

使用 `add()` 方法我们可以向集合中添加单个元素。

```python
# add() 方法：向集合中添加单个元素
s = {1, 2, 3}
s.add(4)  # 添加元素 4
s
```

```output
{1, 2, 3, 4}
```

使用 `update()`，可以添加多个元素：

```python
# update() 方法：从可迭代对象中添加多个元素
s = {1, 2, 3}
s.update([2, 3, 4, 5, 6])  # 添加多个元素（忽略重复项）
s
```

```output
{1, 2, 3, 4, 5, 6}
```

## 集合的移除和丢弃 (remove and discard)

这两种方法都会从集合中移除一个元素，但如果值不存在，`remove()` 会引发 `key error`。

```python
# remove() 方法：移除元素，如果找不到则引发 KeyError
s = {1, 2, 3}
s.remove(3)  # 移除元素 3
s
```

```output
{1, 2}
```

```python
s.remove(3)
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 3
```

`discard()` 不会引发任何错误。

```python
# discard() 方法：移除元素，如果找不到则不报错
s = {1, 2, 3}
s.discard(3)  # 移除元素 3 (安全，缺失时不报错)
s
```

```output
{1, 2}
```

```python
s.discard(3)
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-sets-2">
<template #question>
<code>remove()</code> 和 <code>discard()</code> 方法在集合上的区别是什么？
</template>

<base-quiz-option value="A">A. <code>remove()</code> 移除一个元素，<code>discard()</code> 移除所有</base-quiz-option>
<base-quiz-option value="B">B. 没有区别</base-quiz-option>
<base-quiz-option value="C" correct>C. 如果元素不存在，<code>remove()</code> 抛出错误，<code>discard()</code> 不会</base-quiz-option>
<base-quiz-option value="D">D. <code>remove()</code> 更快</base-quiz-option>
<base-quiz-answer value="C">这两种方法都从集合中移除一个元素，但如果元素不存在，<code>remove()</code> 会引发 <code>KeyError</code>，而 <code>discard()</code> 如果元素缺失则不做任何操作。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 集合的并集 (union)

`union()` 或 `|` 将创建一个包含所有提供集合中所有元素的新集合。

```python
# union()：组合来自多个集合的所有元素（无重复项）
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.union(s2)  # 或 's1 | s2' - 返回 {1, 2, 3, 4, 5}
```

```output
{1, 2, 3, 4, 5}
```

## 集合的交集 (intersection)

`intersection()` 或 `&` 将返回一个只包含所有集合中共同元素的集合。

```python
# intersection()：返回所有集合共有的元素
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
s1.intersection(s2, s3)  # 或 's1 & s2 & s3' - 返回 {3}
```

```output
{3}
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-sets-3">
<template #question>
<code>intersection()</code> 返回集合的什么？
</template>

<base-quiz-option value="A">A. 所有集合中的所有元素</base-quiz-option>
<base-quiz-option value="B" correct>B. 仅包含所有集合中共同的元素</base-quiz-option>
<base-quiz-option value="C">C. 第一个集合中存在但其他集合中不存在的元素</base-quiz-option>
<base-quiz-option value="D">D. 存在于任一集合中但不同时存在于两者中的元素</base-quiz-option>
<base-quiz-answer value="B"><code>intersection()</code> 方法返回一个集合，其中仅包含存在于所有比较集合中的元素。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 集合的差集 (difference)

`difference()` 或 `-` 将只返回第一个集合（被调用的集合）中独有的元素。

```python
# difference()：返回第一个集合中存在但其他集合中不存在的元素
s1 = {1, 2, 3}
s2 = {2, 3, 4}

s1.difference(s2)  # 或 's1 - s2' - 返回 {1}
```

```output
{1}
```

```python
s2.difference(s1) # 或 's2 - s1'
```

```output
{4}
```

## 集合的对称差集 (symmetric_difference)

`symmetric_difference()` 或 `^` 将返回所有不共同的元素。

```python
# symmetric_difference()：返回存在于任一集合中但不同时存在于两者中的元素
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1.symmetric_difference(s2)  # 或 's1 ^ s2' - 返回 {1, 4}
```

```output
{1, 4}
```

<base-quiz>
<base-quiz-question correct="D" id="cheatsheet-sets-4">
<template #question>
<code>symmetric_difference()</code> 返回两个集合的什么？
</template>

<base-quiz-option value="A">A. 两个集合中的所有元素</base-quiz-option>
<base-quiz-option value="B">B. 仅包含两个集合中共同的元素</base-quiz-option>
<base-quiz-option value="C">C. 第一个集合中存在但第二个集合中不存在的元素</base-quiz-option>
<base-quiz-option value="D" correct>D. 存在于任一集合中但不同时存在于两者中的元素</base-quiz-option>
<base-quiz-answer value="D"><code>symmetric_difference()</code> 方法返回一个集合，其中包含存在于任一集合中，但不同时存在于两个集合中的元素。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 相关链接

- <router-link to="/blog/python-data-types">Python 数据类型博客文章</router-link>
- <router-link to="/blog/python-sets-what-why-how">Python 集合：是什么、为什么和如何使用</router-link>
- <router-link to="/cheatsheet/dictionaries">Python 字典 (Dictionaries)</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Python 列表和元组 (Lists and Tuples)</router-link>
