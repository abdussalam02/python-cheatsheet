---
title: Python Basics - Python Cheatsheet
description: Learn Python basics with our comprehensive guide covering operators, data types, variables, functions, and more. Perfect for beginners learning Python programming fundamentals.
labUrl: https://labex.io/labs/python-python-basics-633647?course=python-cheatsheet
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Basics
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

We all need to start somewhere, so how about doing it here. This guide covers the fundamental Python basics including operators, data types, variables, and core functions.

<base-disclaimer>
<base-disclaimer-title>
Python Basics Overview
</base-disclaimer-title>
<base-disclaimer-content>
The core Python basics every beginner should know:

- Variables and basic types
- Operators and expressions
- Strings and common methods
- Lists, tuples, and dictionaries
- Basic control flow (if, for, while)
- Simple functions

</base-disclaimer-content>
</base-disclaimer>

## Math Operators

From **highest** to **lowest** precedence:

| Operators | Operation         | Example         |
| --------- | ----------------- | --------------- |
| \*\*      | Exponent          | `2 ** 3 = 8`    |
| %         | Modulus/Remainder | `22 % 8 = 6`    |
| //        | Integer division  | `22 // 8 = 2`   |
| /         | Division          | `22 / 8 = 2.75` |
| \*        | Multiplication    | `3 * 3 = 9`     |
| -         | Subtraction       | `5 - 2 = 3`     |
| +         | Addition          | `2 + 2 = 4`     |

Examples of expressions:

```python
# Multiplication has higher precedence than addition
# So this evaluates as: 2 + (3 * 6) = 2 + 18 = 20
2 + 3 * 6
```

```output
20
```

```python
# Parentheses override operator precedence
# This evaluates as: 5 * 6 = 30
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
What is the result of this Python expression?

```python
4 + 2 * 3
```

</template>

<base-quiz-option value="A" correct>A. 10</base-quiz-option>
<base-quiz-option value="B">B. 18</base-quiz-option>
<base-quiz-option value="C">C. 12</base-quiz-option>
<base-quiz-option value="D">D. 20</base-quiz-option>
<base-quiz-answer value="A">Multiplication has higher precedence than addition, so this evaluates as: 4 + (2 \* 3) = 4 + 6 = 10</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Augmented Assignment Operators

| Operator    | Equivalent       |
| ----------- | ---------------- |
| `var += 1`  | `var = var + 1`  |
| `var -= 1`  | `var = var - 1`  |
| `var *= 1`  | `var = var * 1`  |
| `var /= 1`  | `var = var / 1`  |
| `var //= 1` | `var = var // 1` |
| `var %= 1`  | `var = var % 1`  |
| `var **= 1` | `var = var ** 1` |

Examples:

```python
# Augmented assignment: equivalent to greeting = greeting + ' world!'
greeting = 'Hello'
greeting += ' world!'
greeting
```

```output
'Hello world!'
```

```python
# Increment a number by 1
number = 1
number += 1
number
```

```output
2
```

```python
# Replicate list elements: equivalent to my_list = my_list * 3
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
What is the value of <code>x</code> after executing this code?

```python
x = 5
x += 3
```

</template>

<base-quiz-option value="A">A. 3</base-quiz-option>
<base-quiz-option value="B" correct>B. 8</base-quiz-option>
<base-quiz-option value="C">C. 5</base-quiz-option>
<base-quiz-option value="D">D. 15</base-quiz-option>
<base-quiz-answer value="B">The augmented assignment operator <code>+=</code> is equivalent to <code>x = x + 3</code>. So <code>x</code> starts as 5, then becomes 5 + 3 = 8.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Walrus Operator

The Walrus Operator allows assignment of variables within an expression while returning the value of the variable

Example:

```python
# Walrus operator assigns and returns value in one expression
# my_var is assigned "Hello World!" and then printed
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

The _Walrus Operator_, or **Assignment Expression Operator** was firstly introduced in 2018 via [PEP 572](https://peps.python.org/pep-0572/), and then officially released with **Python 3.8** in October 2019.

<base-disclaimer>
  <base-disclaimer-title>
    Syntax Semantics & Examples
  </base-disclaimer-title>
  <base-disclaimer-content>
  The <a href="https://peps.python.org/pep-0572/" target="_blank">PEP 572</a> provides the syntax, semantics and examples for the Walrus Operator.
  </base-disclaimer-content>
</base-disclaimer>

## Data Types

Understanding data types is one of the most important Python basics. Python has nine core built-in data types that cover almost everything you'll need:

| Data Type                                                  | Examples                                 | Description                           |
| ---------------------------------------------------------- | ---------------------------------------- | ------------------------------------- |
| **Numbers**                                                |                                          |                                       |
| <router-link to='/builtin/int'>`int`</router-link>         | `-2, -1, 0, 1, 2, 3, 4, 5`               | Whole numbers (integers)              |
| <router-link to='/builtin/float'>`float`</router-link>     | `-1.25, -1.0, -0.5, 0.0, 0.5, 1.0, 1.25` | Numbers with decimal points           |
| <router-link to='/builtin/complex'>`complex`</router-link> | `2+3j, complex(1, 4)`                    | Numbers with real and imaginary parts |
| **Text**                                                   |                                          |                                       |
| <router-link to='/builtin/str'>`str`</router-link>         | `'a', 'Hello!', "Python"`                | Text and characters                   |
| **Boolean**                                                |                                          |                                       |
| <router-link to='/builtin/bool'>`bool`</router-link>       | `True, False`                            | True or False values                  |
| **None**                                                   |                                          |                                       |
| `NoneType`                                                 | `None`                                   | Represents "no value" or "nothing"    |
| **Collections**                                            |                                          |                                       |
| <router-link to='/builtin/list'>`list`</router-link>       | `[1, 2, 3], ['a', 'b', 'c']`             | Ordered, changeable collections       |
| <router-link to='/builtin/dict'>`dict`</router-link>       | `{'name': 'Alice', 'age': 30}`           | Key-value pairs                       |
| <router-link to='/builtin/tuple'>`tuple`</router-link>     | `(1, 2, 3), ('a', 'b')`                  | Ordered, unchangeable collections     |
| <router-link to='/builtin/set'>`set`</router-link>         | `{1, 2, 3}, {'a', 'b', 'c'}`             | Unordered collections of unique items |

### Quick Examples

```python
# Numbers
age = 25                    # int
price = 19.99              # float
coordinate = 2 + 3j        # complex

# Text
name = "Alice"             # str

# Boolean
is_student = True          # bool

# None
result = None              # NoneType

# Collections
scores = [85, 92, 78]      # list
person = {'name': 'Bob', 'age': 30}  # dict
coordinates = (10, 20)     # tuple
unique_ids = {1, 2, 3}     # set
```

For a comprehensive guide with visual examples and detailed explanations of when to use each type, see: <router-link to="/blog/python-data-types">Python Data Types: A Visual Guide for Beginners</router-link>.

## Concatenation and Replication

String concatenation:

```python
# String concatenation: adjacent strings are automatically joined
'Alice' 'Bob'
```

```output
'AliceBob'
```

String replication:

```python
# String replication: repeat string multiple times
'Alice' * 5
```

```output
'AliceAliceAliceAliceAlice'
```

## Variables

Variables are a fundamental part of Python basics. You can name a variable anything as long as it obeys the following rules:

1. It can be only one word.

```python
# bad
my variable = 'Hello'

# good
var = 'Hello'
```

2. It can use only letters, numbers, and the underscore (`_`) character.

```python
# bad
%$@variable = 'Hello'

# good
my_var = 'Hello'

# good
my_var_2 = 'Hello'
```

3. It can't begin with a number.

```python
# this wont work
23_var = 'hello'
```

4. Variable name starting with an underscore (`_`) are considered as "unuseful".

```python
# _spam should not be used again in the code
_spam = 'Hello'
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
In Python basics, which of the following is a valid variable name?
</template>

<base-quiz-option value="A">A. <code>3value</code></base-quiz-option>
<base-quiz-option value="B">B. <code>user-name</code></base-quiz-option>
<base-quiz-option value="C" correct>C. <code>user_name</code></base-quiz-option>
<base-quiz-option value="D">D. <code>for</code></base-quiz-option>
<base-quiz-answer value="C"><code>user_name</code> is a valid variable name because it uses only letters, numbers, and underscores, and doesn't start with a number.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Comments

Inline comment:

```python
# This is a comment
```

Multiline comment:

```python
# This is a
# multiline comment
```

Code with a comment:

```python
a = 1  # initialization
```

Please note the two spaces in front of the comment.

Function docstring:

```python
def foo():
    """
    This is a function docstring
    You can also use:
    ''' Function Docstring '''
    """
```

## The print() Function

The `print()` function is one of the first Python basics you'll learn. It writes the value of the argument(s) it is given. [...] it handles multiple arguments, floating point-quantities, and strings. Strings are printed without quotes, and a space is inserted between items, so you can format things nicely:

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

### The end keyword

The keyword argument `end` can be used to avoid the newline after the output, or end the output with a different string:

```python
# Use end parameter to change what comes after each print statement
phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
for word in phrase:
    print(word, end='-')  # Use '-' instead of newline
```

```output
printed-with-a-dash-in-between-
```

### The sep keyword

The keyword `sep` specify how to separate the objects, if there is more than one:

```python
# Use sep parameter to specify separator between multiple arguments
print('cats', 'dogs', 'mice', sep=',')  # Comma-separated output
```

```output
cats,dogs,mice
```

## The input() Function

This function takes the input from the user and converts it into a string:

```python
# input() reads user input and returns it as a string
print('What is your name?')   # ask for their name
my_name = input()  # Wait for user to type and press Enter
print('Hi, {}'.format(my_name))
```

```output
What is your name?
Martha
Hi, Martha
```

`input()` can also set a default message without using `print()`:

```python
my_name = input('What is your name? ')  # default message
print('Hi, {}'.format(my_name))
```

```output
What is your name? Martha
Hi, Martha
```

It is also possible to use formatted strings to avoid using .format:

```python
# input() can display a prompt message directly
my_name = input('What is your name? ')  # Prompt and read in one call
print(f'Hi, {my_name}')  # f-string for string formatting
```

```output
What is your name? Martha
Hi, Martha
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
In Python basics, what type does `input()` return?
</template>

<base-quiz-option value="A">A. int</base-quiz-option>
<base-quiz-option value="B" correct>B. str</base-quiz-option>
<base-quiz-option value="C">C. float</base-quiz-option>
<base-quiz-option value="D">D. Depends on user input</base-quiz-option>
<base-quiz-answer value="B">The <code>input()</code> function always returns a string, regardless of what the user types. You need to convert it to other types if needed.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## The len() Function

Evaluates to the integer value of the number of characters in a string, list, dictionary, etc.:

```python
# len() returns the number of characters in a string
len('hello')  # Returns 5
```

```output
5
```

```python
# len() returns the number of items in a list
len(['cat', 3, 'dog'])  # Returns 3 (three items)
```

```output
3
```

<base-warning>
  <base-warning-title>Test of emptiness</base-warning-title>
  <base-warning-content>
    Test of emptiness of strings, lists, dictionaries, etc., should not use
    <code>len</code>, but prefer direct boolean evaluation.
  </base-warning-content>
</base-warning>

Test of emptiness example:

```python
a = [1, 2, 3]

# bad: unnecessary len() check
if len(a) > 0:  # evaluates to True
    print("the list is not empty!")
```

```output
the list is not empty!
```

```python
# good: direct boolean evaluation (Pythonic way)
if a:  # evaluates to True if list is not empty
    print("the list is not empty!")
```

```output
the list is not empty!
```

## The str(), int(), and float() Functions

These functions allow you to change the type of variable. For example, you can transform from an `integer` or `float` to a `string`:

```python
# Convert integer to string
str(29)  # Returns '29'
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

Or from a `string` to an `integer` or `float`:

```python
# Convert string to integer
int('11')  # Returns 11
```

```output
11
```

```python
# Convert string to float
float('3.14')  # Returns 3.14
```

```output
3.14
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
What is the result of this Python code?

```python
result = int('42')
type(result)
```

</template>

<base-quiz-option value="A">A. <code>str</code></base-quiz-option>
<base-quiz-option value="B">B. <code>float</code></base-quiz-option>
<base-quiz-option value="C" correct>C. <code>int</code></base-quiz-option>
<base-quiz-option value="D">D. <code>NoneType</code></base-quiz-option>
<base-quiz-answer value="C">The <code>int()</code> function converts a string to an integer. So <code>int('42')</code> returns the integer <code>42</code>, and <code>type(42)</code> returns <code>int</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Relevant Links

- <router-link to="/blog/python-data-types">Python Data Types: A Visual Guide for Beginners</router-link>
- <router-link to="/blog/python-comprehensions-step-by-step">Python Comprehensions Step-by-Step</router-link>
- <router-link to="/cheatsheet/control-flow">Control Flow</router-link>
- <router-link to="/cheatsheet/functions">Functions</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">Lists and Tuples</router-link>
- <router-link to="/cheatsheet/dictionaries">Dictionaries</router-link>
- <router-link to="/cheatsheet/sets">Sets</router-link>
- <router-link to="/cheatsheet/string-formatting">String Formatting</router-link>
