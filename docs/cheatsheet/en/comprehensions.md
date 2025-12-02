---
title: Python Comprehensions - Python Cheatsheet
description: List comprehensions provide a concise way to create lists
labUrl: https://labex.io/labs/python-python-comprehensions-633649?course=python-cheatsheet
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Comprehensions
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

List Comprehensions are a special kind of syntax that let us create lists out of other lists, and are incredibly useful when dealing with numbers and with one or two levels of nested for loops.

<base-disclaimer>
  <base-disclaimer-title>
    From the Python 3 <a target="_blank" href="https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions">tutorial</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    List comprehensions provide a concise way to create lists. [...] or to create a subsequence of those elements that satisfy a certain condition.
  </base-disclaimer-content>
</base-disclaimer>

Read <router-link to="/blog/python-comprehensions-step-by-step">Python Comprehensions: A step by step Introduction</router-link> for a more in-depth introduction.

## List comprehension

This is how we create a new list from an existing collection with a For Loop:

```python
# Traditional approach: create list using a for loop
names = ['Charles', 'Susan', 'Patrick', 'George']

new_list = []
for n in names:
    new_list.append(n)

new_list
```

```output
['Charles', 'Susan', 'Patrick', 'George']
```

And this is how we do the same with a List Comprehension:

```python
# List comprehension: concise way to create a new list
# Syntax: [expression for item in iterable]
names = ['Charles', 'Susan', 'Patrick', 'George']

new_list = [n for n in names]  # Create list with all names
new_list
```

```output
['Charles', 'Susan', 'Patrick', 'George']
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-comprehensions-1">
<template #question>
What is the basic syntax of a list comprehension?
</template>

<base-quiz-option value="A" correct>A. <code>[expression for item in iterable]</code></base-quiz-option>
<base-quiz-option value="B">B. <code>(expression for item in iterable)</code></base-quiz-option>
<base-quiz-option value="C">C. <code>{expression for item in iterable}</code></base-quiz-option>
<base-quiz-option value="D">D. <code>expression for item in iterable</code></base-quiz-option>
<base-quiz-answer value="A">List comprehensions use square brackets <code>[]</code> with the syntax <code>[expression for item in iterable]</code>. This creates a new list by applying the expression to each item.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

We can do the same with numbers:

```python
# Nested list comprehension: create tuples from two ranges
# Equivalent to nested for loops
n = [(a, b) for a in range(1, 3) for b in range(1, 3)]
n
```

```output
[(1, 1), (1, 2), (2, 1), (2, 2)]
```

## Adding conditionals

If we want `new_list` to have only the names that start with C, with a for loop, we would do it like this:

```python
# Traditional approach: filter with if condition
names = ['Charles', 'Susan', 'Patrick', 'George', 'Carol']

new_list = []
for n in names:
    if n.startswith('C'):  # Filter names starting with 'C'
        new_list.append(n)

print(new_list)
```

```output
['Charles', 'Carol']
```

In a List Comprehension, we add the `if` statement at the end:

```python
# List comprehension with condition: filter items
# Syntax: [expression for item in iterable if condition]
new_list = [n for n in names if n.startswith('C')]
print(new_list)
```

```output
['Charles', 'Carol']
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-comprehensions-2">
<template #question>
Where does the <code>if</code> condition go in a list comprehension?
</template>

<base-quiz-option value="A">A. Before the <code>for</code> keyword</base-quiz-option>
<base-quiz-option value="B" correct>B. After the <code>for</code> clause</base-quiz-option>
<base-quiz-option value="C">C. Inside the expression</base-quiz-option>
<base-quiz-option value="D">D. Before the square brackets</base-quiz-option>
<base-quiz-answer value="B">In a list comprehension, the <code>if</code> condition comes after the <code>for</code> clause: <code>[expression for item in iterable if condition]</code>. This filters items based on the condition.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

To use an `if-else` statement in a List Comprehension:

```python
# List comprehension with if-else: conditional expression
# Syntax: [expression_if_true if condition else expression_if_false for item in iterable]
nums = [1, 2, 3, 4, 5, 6]
new_list = [num*2 if num % 2 == 0 else num for num in nums]  # Double even numbers
print(new_list)
```

```output
[1, 4, 3, 8, 5, 12]
```

<base-disclaimer>
  <base-disclaimer-title>
    Set and Dict comprehensions
  </base-disclaimer-title>
  <base-disclaimer-content>
    The basics of `list` comprehensions also apply to <b>sets</b> and <b>dictionaries</b>.
  </base-disclaimer-content>
</base-disclaimer>

## Set comprehension

```python
# Set comprehension: create a set using comprehension syntax
# Syntax: {expression for item in iterable}
b = {"abc", "def"}
{s.upper() for s in b}  # Convert all strings to uppercase
```

```output
{"ABC", "DEF"}
```

## Dict comprehension

```python
# Dict comprehension: swap keys and values
# Syntax: {key_expression: value_expression for item in iterable}
c = {'name': 'Pooka', 'age': 5}
{v: k for k, v in c.items()}  # Reverse key-value pairs
```

```output
{'Pooka': 'name', 5: 'age'}
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-comprehensions-3">
<template #question>
What syntax is used for dictionary comprehensions?
</template>

<base-quiz-option value="A">A. <code>[key: value for item in iterable]</code></base-quiz-option>
<base-quiz-option value="B">B. <code>(key: value for item in iterable)</code></base-quiz-option>
<base-quiz-option value="C" correct>C. <code>{key_expression: value_expression for item in iterable}</code></base-quiz-option>
<base-quiz-option value="D">D. <code>{key, value for item in iterable}</code></base-quiz-option>
<base-quiz-answer value="C">Dictionary comprehensions use curly braces <code>{}</code> with the syntax <code>{key_expression: value_expression for item in iterable}</code>, similar to list comprehensions but with key-value pairs.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

A List comprehension can be generated from a dictionary:

```python
# List comprehension from dictionary: create formatted strings
c = {'name': 'Pooka', 'age': 5}
["{}:{}".format(k.upper(), v) for k, v in c.items()]  # Format as "KEY:value"
```

```output
['NAME:Pooka', 'AGE:5']
```

## Relevant links

- <router-link to="/blog/python-comprehensions-step-by-step">Python Comprehensions: A step by step Introduction</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Python Lists and Tuples</router-link>
- <router-link to="/cheatsheet/sets">Python Sets</router-link>
- <router-link to="/cheatsheet/dictionaries">Python Dictionaries</router-link>
- <router-link to="/blog/python-sets-what-why-how">Python Sets: What, Why and How</router-link>
- <router-link to="/blog/python-data-types">Python Data Types Blog Post</router-link>
