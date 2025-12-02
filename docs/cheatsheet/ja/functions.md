---
title: 'Python 関数 - Python チートシート'
description: 'Python では、関数は単一のタスクを実行するために使用される、整理されたコードブロックです。'
labUrl: 'https://labex.io/ja/labs/python-python-functions-633658?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python 関数
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikiversity.org/wiki/Programming_Fundamentals/Functions">Programming Functions</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    関数とは、単一のタスクを実行するために使用される、整理されたコードのブロックです。これらはアプリケーションに優れたモジュール性と再利用性を提供します。
  </base-disclaimer-content>
</base-disclaimer>

## Function Arguments

関数は `arguments` と `return values` を受け取ることができます。

次の例では、関数 **say_hello** は引数 "name" を受け取り、挨拶を出力します。

```python
# Define a function that takes one argument
def say_hello(name):
   print(f'Hello {name}')

# Call the function with a string argument
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

## Keyword Arguments

コードの可読性を向上させるために、できる限り明示的であるべきです。これは、関数内で `Keyword Arguments` を使用することで実現できます。

```python
# Function with multiple parameters
def say_hi(name, greeting):
   print(f"{greeting} {name}")

# Positional arguments: order matters
say_hi('John', 'Hello')
```

```output
Hello John
```

```python
# Keyword arguments: order doesn't matter, more readable
say_hi(name='Anna', greeting='Hi')
```

```output
Hi Anna
```

<BaseQuiz id="cheatsheet-functions-1" correct="C">
<template #question>
What is the main advantage of using keyword arguments in Python functions?
</template>

<BaseQuizOption value="A">A. They execute faster</BaseQuizOption>
<BaseQuizOption value="B">B. They use less memory</BaseQuizOption>
<BaseQuizOption value="C" correct>C. They improve code readability and order doesn't matter</BaseQuizOption>
<BaseQuizOption value="D">D. They prevent errors</BaseQuizOption>
<BaseQuizAnswer>Keyword arguments improve code readability by making it clear what each argument represents, and they allow you to pass arguments in any order.</BaseQuizAnswer>
</BaseQuiz>

## Return Values

`def` ステートメントを使用して関数を作成する場合、`return` ステートメントで返り値を指定できます。return ステートメントは以下で構成されます。

- `return` キーワード。

- 関数が返す値または式。

```python
# Function that returns a value using return statement
def sum_two_numbers(number_1, number_2):
   return number_1 + number_2

# Call function and store the returned value
result = sum_two_numbers(7, 8)
print(result)
```

```output
15
```

<BaseQuiz id="cheatsheet-functions-2" correct="A">
<template #question>
What keyword is used to return a value from a function in Python?
</template>

<BaseQuizOption value="A" correct>A. <code>return</code></BaseQuizOption>
<BaseQuizOption value="B">B. <code>output</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>yield</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>exit</code></BaseQuizOption>
<BaseQuizAnswer>The <code>return</code> keyword is used to return a value from a function. If no return statement is used, the function returns <code>None</code>.</BaseQuizAnswer>
</BaseQuiz>

## Local and Global Scope

- グローバルスコープのコードはローカル変数を使用できません。

- ただし、ローカルスコープはグローバル変数にアクセスできます。

- 関数のローカルスコープ内のコードは、他のローカルスコープの変数を使用できません。

- 異なるスコープにある場合、異なる変数に同じ名前を使用できます。つまり、spam という名前のローカル変数と、同じく spam という名前のグローバル変数が存在し得ます。

```python
# Global variable: accessible everywhere
global_variable = 'I am available everywhere'

def some_function():
    print(global_variable)  # Can access global variable
    # Local variable: only exists within this function
    local_variable = "only available within this function"
    print(local_variable)

# This will raise NameError: local_variable doesn't exist in global scope
print(local_variable)
```

```output
Traceback (most recent call last):
  File "<stdin>", line 10, in <module>
NameError: name 'local_variable' is not defined
```

## The global Statement

関数内からグローバル変数を変更する必要がある場合は、global ステートメントを使用します。

```python
# Use 'global' keyword to modify global variable from inside function
def spam():
    global eggs  # Declare that we're modifying the global variable
    eggs = 'spam'  # This changes the global variable

eggs = 'global'
spam()  # Function modifies global variable
print(eggs)  # Prints 'spam', not 'global'
```

```output
spam
```

<BaseQuiz id="cheatsheet-functions-3" correct="B">
<template #question>
What keyword must you use inside a function to modify a global variable?
</template>

<BaseQuizOption value="A">A. <code>nonlocal</code></BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>global</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>extern</code></BaseQuizOption>
<BaseQuizOption value="D">D. No keyword needed</BaseQuizOption>
<BaseQuizAnswer>The <code>global</code> keyword must be used inside a function to modify a global variable. Without it, Python will create a local variable instead.</BaseQuizAnswer>
</BaseQuiz>

変数がローカルスコープにあるかグローバルスコープにあるかを判断するには、次の 4 つのルールがあります。

1. 変数がグローバルスコープ（つまり、すべての関数の外側）で使用されている場合、それは常にグローバル変数です。

1. 関数内にその変数に関するグローバルステートメントがある場合、それはグローバル変数です。

1. それ以外の場合、関数内でその変数が代入ステートメントで使用されている場合、それはローカル変数です。

1. ただし、変数が代入ステートメントで使用されていない場合、それはグローバル変数です。

## Lambda Functions

Python において、ラムダ関数は単一行の無名関数であり、任意の数の引数を取ることができますが、式は 1 つしか持つことができません。

<base-disclaimer>
  <base-disclaimer-title>
    From the <a target="_blank" href="https://docs.python.org/3/library/ast.html?highlight=lambda#function-and-class-definitions">Python 3 Tutorial</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    lambda は、式の中で使用できる最小限の関数定義です。FunctionDef とは異なり、body は単一のノードを保持します。
  </base-disclaimer-content>
</base-disclaimer>

<base-warning>
  <base-warning-title>
    Single line expression
  </base-warning-title>
  <base-warning-content>
    ラムダ関数は、単一行のコードのような式のみを評価できます。
  </base-warning-content>
</base-warning>

この関数：

```python
# Regular function definition
def add(x, y):
    return x + y

add(5, 3)
```

```output
8
```

は、_ラムダ_ 関数：

```python
# Lambda function: anonymous function defined in one line
# Syntax: lambda arguments: expression
add = lambda x, y: x + y
add(5, 3)
```

```output
8
```

と同等です。

<BaseQuiz id="cheatsheet-functions-4" correct="D">
<template #question>
What is a lambda function in Python?
</template>

<BaseQuizOption value="A">A. A function that can only be called once</BaseQuizOption>
<BaseQuizOption value="B">B. A function that takes no arguments</BaseQuizOption>
<BaseQuizOption value="C">C. A function that returns multiple values</BaseQuizOption>
<BaseQuizOption value="D" correct>D. A single-line anonymous function that can have any number of arguments but only one expression</BaseQuizOption>
<BaseQuizAnswer>A lambda function is an anonymous, single-line function defined using the <code>lambda</code> keyword. It can take any number of arguments but can only contain a single expression.</BaseQuizAnswer>
</BaseQuiz>

通常のネストされた関数と同様に、ラムダも辞書式クロージャとして機能します。

```python
# Lambda closure: lambda function that captures variable from outer scope
def make_adder(n):
    return lambda x: x + n  # Lambda captures 'n' from outer function

# Create functions that add different amounts
plus_3 = make_adder(3)  # Returns lambda that adds 3
plus_5 = make_adder(5)  # Returns lambda that adds 5

plus_3(4)  # Returns 4 + 3 = 7
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

<BaseQuiz id="cheatsheet-functions-5" correct="A">
<template #question>
What does a lambda closure allow you to do?
</template>

<BaseQuizOption value="A" correct>A. Capture variables from the outer scope</BaseQuizOption>
<BaseQuizOption value="B">B. Modify global variables without the global keyword</BaseQuizOption>
<BaseQuizOption value="C">C. Return multiple values</BaseQuizOption>
<BaseQuizOption value="D">D. Execute code asynchronously</BaseQuizOption>
<BaseQuizAnswer>Lambda closures allow lambda functions to capture and use variables from their enclosing scope, similar to regular nested functions.</BaseQuizAnswer>
</BaseQuiz>

## Relevant links

- <router-link to="/blog/python-easy-args-kwargs">\*args and \*\*kwargs explained</router-link>
- <router-link to="/cheatsheet/args-and-kwargs">Args and Kwargs</router-link>
- <router-link to="/cheatsheet/decorators">Decorators</router-link>
- <router-link to="/cheatsheet/control-flow">Control Flow</router-link>
- <router-link to="/cheatsheet/basics">Basics</router-link>
- <router-link to="/builtin">Built-in Functions</router-link>
