---
title: Python Main function - Python Cheatsheet
description: is the name of the scope in which top-level code executes. A module's name is set equal to main when read from standard input, a script, or from an interactive prompt.
labUrl: https://labex.io/labs/python-python-main-function-633661?course=python-cheatsheet
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Main top-level script environment
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## What is it

`__main__` is the name of the scope in which top-level code executes.
A module’s **name** is set equal to `__main__` when read from standard input, a script, or from an interactive prompt.

A module can discover whether it is running in the main scope by checking its own `__name__`, which allows a common idiom for conditionally executing code in a module. When it is run as a script or with `python -m` but not when it is imported:

```python
# __name__ == "__main__": check if script is run directly (not imported)
if __name__ == "__main__":  # True when run as script, False when imported
    # execute only if run as a script
    main()
```

For a package, the same effect can be achieved by including a **main**.py module, the contents of which will be executed when the module is run with -m.

For example, we are developing a script designed to be used as a module, we should do:

```python
# Example: function can be imported, but test code only runs when executed directly
def add(a, b):
    return a+b

if __name__ == "__main__":  # Only runs when file is executed, not when imported
    add(3, 5)
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
What is the value of <code>__name__</code> when a Python file is run directly as a script?
</template>

<base-quiz-option value="A">A. The filename</base-quiz-option>
<base-quiz-option value="B" correct>B. <code>"**main**"</code></base-quiz-option>
<base-quiz-option value="C">C. <code>None</code></base-quiz-option>
<base-quiz-option value="D">D. <code>True</code></base-quiz-option>
<base-quiz-answer value="B">When a Python file is run directly as a script, <code>**name**</code> is set to <code>"**main**"</code>. When the file is imported as a module, <code>**name**</code> is set to the module's name.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Advantages

1. Every Python module has it’s `__name__` defined and if this is `__main__`, it implies that the module is run standalone by the user, and we can do corresponding appropriate actions.
2. If you import this script as a module in another script, the **name** is set to the name of the script/module.
3. Python files can act as either reusable modules, or as standalone programs.
4. `if __name__ == "__main__":` is used to execute some code only if the file is run directly, and is not being imported.

<base-quiz>
<base-quiz-question correct="A">
<template #question>
What is the main purpose of using <code>if __name__ == "__main__":</code>?
</template>

<base-quiz-option value="A" correct>A. To execute code only when the file is run directly, not when imported</base-quiz-option>
<base-quiz-option value="B">B. To prevent the file from being imported</base-quiz-option>
<base-quiz-option value="C">C. To make the file execute faster</base-quiz-option>
<base-quiz-option value="D">D. To hide code from other modules</base-quiz-option>
<base-quiz-answer value="A">The <code>if **name** == "**main**":</code> idiom allows a Python file to act as both a reusable module and a standalone program. Code inside this block only runs when the file is executed directly, not when it's imported.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Relevant links

- <router-link to="/cheatsheet/functions">Functions</router-link>
- <router-link to="/cheatsheet/packaging">Packaging</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Python projects with Poetry and VSCode. Part 1</router-link>
- <router-link to="/builtin/import">import()</router-link>
