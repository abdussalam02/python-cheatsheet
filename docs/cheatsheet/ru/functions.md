---
title: 'Функции Python - Шпаргалка по Python'
description: 'В Python функция — это блок организованного кода, используемый для выполнения одной задачи.'
labUrl: 'https://labex.io/ru/labs/python-python-functions-633658?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Функции Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikiversity.org/wiki/Programming_Fundamentals/Functions">Programming Functions</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Функция — это блок организованного кода, используемый для выполнения одной задачи. Они обеспечивают лучшую модульность для вашего приложения и возможность повторного использования.
  </base-disclaimer-content>
</base-disclaimer>

## Аргументы функции

Функция может принимать `аргументы` и `возвращать значения`:

В следующем примере функция **say_hello** принимает аргумент "name" и выводит приветствие:

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

## Именованные аргументы (Keyword Arguments)

Чтобы улучшить читаемость кода, мы должны быть максимально явными. Мы можем добиться этого в наших функциях, используя `Keyword Arguments`:

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

## Возвращаемые значения (Return Values)

При создании функции с помощью оператора `def` вы можете указать, какое должно быть возвращаемое значение, с помощью оператора `return`. Оператор возврата состоит из следующего:

- Ключевое слово `return`.

- Значение или выражение, которое должна вернуть функция.

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

## Локальная и глобальная области видимости (Local and Global Scope)

- Код в глобальной области видимости не может использовать локальные переменные.

- Однако локальная область видимости может получать доступ к глобальным переменным.

- Код в локальной области видимости функции не может использовать переменные из любой другой локальной области видимости.

- Вы можете использовать одно и то же имя для разных переменных, если они находятся в разных областях видимости. То есть, может существовать локальная переменная с именем `spam` и глобальная переменная с тем же именем `spam`.

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

## Оператор global

Если вам нужно изменить глобальную переменную изнутри функции, используйте оператор `global`:

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

Существуют четыре правила, определяющие, находится ли переменная в локальной или глобальной области видимости:

1. Если переменная используется в глобальной области видимости (то есть вне всех функций), то это всегда глобальная переменная.

1. Если в функции есть оператор `global` для этой переменной, это глобальная переменная.

1. В противном случае, если переменная используется в операторе присваивания внутри функции, это локальная переменная.

1. Но если переменная не используется в операторе присваивания, это глобальная переменная.

## Функции Lambda

В Python функция lambda — это однострочная анонимная функция, которая может иметь любое количество аргументов, но только одно выражение.

<base-disclaimer>
  <base-disclaimer-title>
    From the <a target="_blank" href="https://docs.python.org/3/library/ast.html?highlight=lambda#function-and-class-definitions">Python 3 Tutorial</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    lambda is a minimal function definition that can be used inside an expression. Unlike FunctionDef, body holds a single node.
  </base-disclaimer-content>
</base-disclaimer>

<base-warning>
  <base-warning-title>
    Single line expression
  </base-warning-title>
  <base-warning-content>
    Lambda functions can only evaluate an expression, like a single line of code.
  </base-warning-content>
</base-warning>

Эта функция:

```python
# Regular function definition
def add(x, y):
    return x + y

add(5, 3)
```

```output
8
```

Эквивалентна функции _lambda_:

```python
# Lambda function: anonymous function defined in one line
# Syntax: lambda arguments: expression
add = lambda x, y: x + y
add(5, 3)
```

```output
8
```

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

Как и обычные вложенные функции, лямбда-функции также работают как лексические замыкания:

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

## Соответствующие ссылки

- <router-link to="/blog/python-easy-args-kwargs">\*args и \*\*kwargs объяснены</router-link>
- <router-link to="/cheatsheet/args-and-kwargs">Args и Kwargs</router-link>
- <router-link to="/cheatsheet/decorators">Декораторы</router-link>
- <router-link to="/cheatsheet/control-flow">Управление потоком</router-link>
- <router-link to="/cheatsheet/basics">Основы</router-link>
- <router-link to="/builtin">Встроенные функции</router-link>
