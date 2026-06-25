---
title: Python vars() built-in function - Python Cheat Sheet
description: Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python vars() built-in function
</base-title>

<base-disclaimer>
  <base-disclaimer-title>
    From the <a target="_blank" href="https://docs.python.org/3/library/functions.html#vars">Python 3 documentation</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.
  </base-disclaimer-content>
</base-disclaimer>

## Introduction

The `vars()` function returns the `__dict__` attribute of an object. This dictionary contains the object's writable attributes. It's a convenient way to see all the attributes of an object at once.

If called with no argument, `vars()` acts like `locals()`, returning a dictionary of the local symbol table.

### Examples

**Getting the attributes of an object:**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_person = Person("Dwight", 35)
print(vars(my_person))
```

```output
{'name': 'Dwight', 'age': 35}
```

**Using `vars()` with no arguments:**

```python
def my_function():
    x = 10
    print(vars())

my_function()
```

```output
{'x': 10}
```

## Relevant links

- <router-link to="/cheatsheet/oop-basics">Cheat Sheet: OOP Basics</router-link>
- <router-link to="/cheatsheet/debugging">Cheat Sheet: Debugging</router-link>
- <router-link to="/cheatsheet/dictionaries">Cheat Sheet: Dictionaries</router-link>
- <router-link to="/builtin/dir">dir()</router-link>
- <router-link to="/builtin/object">object()</router-link>
- <router-link to="/builtin/globals">globals()</router-link>
- <router-link to="/builtin/locals">locals()</router-link>
