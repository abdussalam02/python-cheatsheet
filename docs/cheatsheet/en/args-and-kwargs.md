---
title: Python Args and Kwargs - Python Cheatsheet
description: args and kwargs may seem scary, but the truth is that they are not that difficult to grasp and have the power to grant your functions with flexibility and readability
labUrl: https://labex.io/labs/python-python-args-and-kwargs-633646?course=python-cheatsheet
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Args and Kwargs
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a href="https://docs.python.org/3/tutorial/index.html">Python args and kwargs Made Easy</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    <code>*args</code> and <code>**kwargs</code> may seem scary, but the truth is that they are not that difficult to grasp and have the power to grant your functions with lots of flexibility.
  </base-disclaimer-content>
</base-disclaimer>

Read the article <router-link to="/blog/python-easy-args-kwargs">Python \*args and \*\*kwargs Made Easy</router-link> for a more in deep introduction.

## Args and Kwargs

`*args` and `**kwargs` allow you to pass an undefined number of arguments and keywords when calling a function.

```python
# Define a function that accepts any number of positional and keyword arguments
def some_function(*args, **kwargs):
    pass

# Call with any number of positional arguments
some_function(arg1, arg2, arg3)

# Call with any number of keyword arguments
some_function(key1=arg1, key2=arg2, key3=arg3)

# Call with both positional and keyword arguments
some_function(arg, key1=arg1)

# Or call with no arguments at all
some_function()
```

<base-warning>
  <base-warning-title>
    Python conventions
  </base-warning-title>
  <base-warning-content>
    The words <code>*args</code> and <code>**kwargs</code> are conventions. They are not imposed by the interpreter, but considered good practice by the Python community.
  </base-warning-content>
</base-warning>

## args

You can access the _arguments_ through the `args` variable:

```python
# *args collects positional arguments into a tuple
def some_function(*args):
    print(f'Arguments passed: {args} as {type(args)}')

# Pass multiple arguments - they'll be collected into args tuple
some_function('arg1', 'arg2', 'arg3')
```

```output
Arguments passed: ('arg1', 'arg2', 'arg3') as <class 'tuple'>
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
What data type does <code>*args</code> collect arguments into?
</template>

<base-quiz-option value="A">A. A list</base-quiz-option>
<base-quiz-option value="B" correct>B. A tuple</base-quiz-option>
<base-quiz-option value="C">C. A dictionary</base-quiz-option>
<base-quiz-option value="D">D. A set</base-quiz-option>
<base-quiz-answer value="B">The <code>\*args</code> parameter collects positional arguments into a tuple. This allows a function to accept any number of positional arguments.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## kwargs

Keywords are accessed through the `kwargs` variable:

```python
# **kwargs collects keyword arguments into a dictionary
def some_function(**kwargs):
    print(f'keywords: {kwargs} as {type(kwargs)}')

# Pass keyword arguments - they'll be collected into kwargs dict
some_function(key1='arg1', key2='arg2')
```

```output
keywords: {'key1': 'arg1', 'key2': 'arg2'} as <class 'dict'>
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
What data type does <code>**kwargs</code> collect arguments into?
</template>

<base-quiz-option value="A">A. A list</base-quiz-option>
<base-quiz-option value="B">B. A tuple</base-quiz-option>
<base-quiz-option value="C" correct>C. A dictionary</base-quiz-option>
<base-quiz-option value="D">D. A set</base-quiz-option>
<base-quiz-answer value="C">The <code>\*\*kwargs</code> parameter collects keyword arguments into a dictionary. This allows a function to accept any number of keyword arguments.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Relevant links

- <router-link to="/cheatsheet/functions">Functions</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Lists and Tuples</router-link>
- <router-link to="/cheatsheet/dictionaries">Python Dictionaries</router-link>
- <router-link to="/blog/python-easy-args-kwargs">Python \*args and \*\*kwargs Made Easy</router-link>
- <router-link to="/builtin/tuple">tuple()</router-link>
- <router-link to="/builtin/dict">dict()</router-link>
