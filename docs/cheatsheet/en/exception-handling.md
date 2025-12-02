---
title: Python Exception Handling - Python Cheatsheet
description: In Python, exception handling is the process of responding to the occurrence of exceptions.
labUrl: https://labex.io/labs/python-python-exception-handling-633656?course=python-cheatsheet
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Exception Handling
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikipedia.org/wiki/Exception_handling">Exception handling</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    In computing and computer programming, exception handling is the process of responding to the occurrence of exceptions – anomalous or exceptional conditions requiring special processing.
  </base-disclaimer-content>
</base-disclaimer>

Python has many [built-in exceptions](https://docs.python.org/3/library/exceptions.html) that are raised when a program encounters an error, and most external libraries, like the popular [Requests](https://requests.readthedocs.io/en/latest), include his own [custom exceptions](https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions) that we will need to deal to.

## Basic exception handling

You can't divide by zero, that is a mathematical true, and if you try to do it in Python, the interpreter will raise the built-in exception [ZeroDivisionError](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError):

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

Let's say we don't want our program to stop its execution or show the user an output he will not understand. Say we want to print a useful and clear message, then we need to **_handle_** the exception with the `try` and `except` keywords:

```python
# try-except: handle exceptions gracefully
def divide(dividend , divisor):
    try:  # Try to execute this code
        print(dividend / divisor)
    except ZeroDivisionError:  # Catch specific exception type
        print('You can not divide by 0')

divide(dividend=10, divisor=5)
```

```output
2
```

```python
divide(dividend=10, divisor=0)
```

```output
You can not divide by 0
```

<BaseQuiz id="cheatsheet-exception-handling-1" correct="A">
<template #question>
What keywords are used to handle exceptions in Python?
</template>

<BaseQuizOption value="A" correct>A. <code>try</code> and <code>except</code></BaseQuizOption>
<BaseQuizOption value="B">B. <code>catch</code> and <code>handle</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>error</code> and <code>rescue</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>if</code> and <code>else</code></BaseQuizOption>
<BaseQuizAnswer>Python uses <code>try</code> to mark code that might raise an exception, and <code>except</code> to handle specific exceptions that occur.</BaseQuizAnswer>
</BaseQuiz>

## Handling Multiple exceptions using one exception block

You can also handle multiple exceptions in one line like the following without the need to create multiple exception blocks.

```python
# Handle multiple exceptions in one except block
def divide(dividend , divisor):
    try:
        if (dividend == 10):
          var = 'str' + 1  # This will raise TypeError
        else:
          print(dividend / divisor)
    except (ZeroDivisionError, TypeError) as error:  # Catch multiple exception types
        print(error)  # Print the error message

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
Can you handle multiple exception types in a single <code>except</code> block?
</template>

<BaseQuizOption value="A">A. No, you must use separate <code>except</code> blocks for each exception type</BaseQuizOption>
<BaseQuizOption value="B" correct>B. Yes, by putting them in a tuple like <code>except (Exception1, Exception2)</code></BaseQuizOption>
<BaseQuizOption value="C">C. Yes, but only if they are related</BaseQuizOption>
<BaseQuizOption value="D">D. No, Python doesn't support this</BaseQuizOption>
<BaseQuizAnswer>You can handle multiple exception types in one <code>except</code> block by putting them in a tuple: <code>except (ZeroDivisionError, TypeError) as error:</code></BaseQuizAnswer>
</BaseQuiz>

## Finally code in exception handling

The code inside the `finally` section is always executed, no matter if an exception has been raised or not:

```python
# finally block: always executes regardless of exceptions
def divide(dividend , divisor):
    try:
        print(dividend / divisor)
    except ZeroDivisionError:
        print('You can not divide by 0')
    finally:  # Always executes, even if exception occurs
        print('Execution finished')

divide(dividend=10, divisor=5)
```

```output
2.0
Execution finished
```

```python
divide(dividend=10, divisor=0)
```

```output
You can not divide by 0
Execution finished
```

<BaseQuiz id="cheatsheet-exception-handling-3" correct="C">
<template #question>
When does the <code>finally</code> block execute?
</template>

<BaseQuizOption value="A">A. Only when an exception occurs</BaseQuizOption>
<BaseQuizOption value="B">B. Only when no exception occurs</BaseQuizOption>
<BaseQuizOption value="C" correct>C. Always, regardless of whether an exception occurred or not</BaseQuizOption>
<BaseQuizOption value="D">D. Never</BaseQuizOption>
<BaseQuizAnswer>The <code>finally</code> block always executes, whether an exception occurred or not. It's useful for cleanup code that must run regardless of the outcome.</BaseQuizAnswer>
</BaseQuiz>

## Custom Exceptions

Custom exceptions initialize by creating a `class` that inherits from the base `Exception` class of Python, and are raised using the `raise` keyword:

```python
# Custom exception: create by inheriting from Exception class
class MyCustomException(Exception):
    pass

raise MyCustomException  # Raise the custom exception
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyCustomException
```

To declare a custom exception message, you can pass it as a parameter:

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

Handling a custom exception is the same as any other:

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
How do you create a custom exception in Python?
</template>

<BaseQuizOption value="A" correct>A. Create a class that inherits from the <code>Exception</code> class</BaseQuizOption>
<BaseQuizOption value="B">B. Use the <code>@exception</code> decorator</BaseQuizOption>
<BaseQuizOption value="C">C. Call <code>Exception.create()</code></BaseQuizOption>
<BaseQuizOption value="D">D. Import it from a special module</BaseQuizOption>
<BaseQuizAnswer>Custom exceptions are created by defining a class that inherits from the base <code>Exception</code> class. You can then raise and handle them just like built-in exceptions.</BaseQuizAnswer>
</BaseQuiz>

## Relevant links

- <router-link to="/cheatsheet/control-flow">Control Flow</router-link>
- <router-link to="/builtin/breakpoint">breakpoint()</router-link>
- <router-link to="/builtin/isinstance">isinstance()</router-link>
- <router-link to="/builtin/issubclass">issubclass()</router-link>
