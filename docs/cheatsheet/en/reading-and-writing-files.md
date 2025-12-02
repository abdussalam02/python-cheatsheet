---
title: Reading and writing files - Python Cheatsheet
description: To read/write to a file in Python, you will want to use the with statement, which will close the file for you after you are done, managing the available resources for you.
labUrl: https://labex.io/labs/python-python-reading-and-writing-files-633663?course=python-cheatsheet
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Reading and Writing Files
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

For a more in-depth look at file and directory path manipulation, see the <router-link to="/cheatsheet/file-directory-path">File and directory Paths</router-link> page.

## The file Reading/Writing process

To read/write to a file in Python, you will want to use the `with`
statement, which will close the file for you after you are done, managing the available resources for you.

## Opening and reading files

The `open` function opens a file and return a corresponding file object.

```python
# Read file using 'with' statement: automatically closes file when done
with open('/home/labex/project/hi.txt') as hello_file:
    hello_content = hello_file.read()  # Read entire file content

hello_content
```

```output
'Hello World!'
```

<BaseQuiz id="cheatsheet-reading-and-writing-files-1" correct="A">
<template #question>
What is the main advantage of using the <code>with</code> statement when opening files?
</template>

<BaseQuizOption value="A" correct>A. The file is automatically closed when done, even if an error occurs</BaseQuizOption>
<BaseQuizOption value="B">B. Files open faster</BaseQuizOption>
<BaseQuizOption value="C">C. Files can be opened in read and write mode simultaneously</BaseQuizOption>
<BaseQuizOption value="D">D. Files are automatically compressed</BaseQuizOption>
<BaseQuizAnswer>The <code>with</code> statement ensures the file is automatically closed when the block exits, even if an exception occurs. This helps manage resources properly.</BaseQuizAnswer>
</BaseQuiz>

Alternatively, you can use the _readlines()_ method to get a list of string values from the file, one string for each line of text:

```python
# readlines() method: returns list of strings, one per line
with open('sonnet29.txt') as sonnet_file:
    sonnet_file.readlines()  # Returns list with each line as a string
```

```output
['When, in disgrace with fortune and men's eyes,\n',
 ' I all alone beweep my  outcast state,\n',
 "And trouble deaf heaven with my bootless cries,\n",
 "And look upon myself and curse my fate,']
```

You can also iterate through the file line by line:

```python
# Iterate through file line by line (memory efficient for large files)
with open('sonnet29.txt') as sonnet_file:
    for line in sonnet_file:  # File object is iterable
        print(line, end='')  # Print without extra newline
```

```output
When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,
```

## Writing to files

```python
# Write to file: 'w' mode overwrites existing file
with open('bacon.txt', 'w') as bacon_file:  # 'w' = write mode
    bacon_file.write('Hello world!\n')  # Returns number of characters written
```

```output
13
```

```python
# Append to file: 'a' mode appends to existing file
with open('bacon.txt', 'a') as bacon_file:  # 'a' = append mode
    bacon_file.write('Bacon is not a vegetable.')
```

```output
25
```

```python
with open('bacon.txt') as bacon_file:
    content = bacon_file.read()

print(content)
```

```output
Hello world!
Bacon is not a vegetable.
```

<BaseQuiz id="cheatsheet-reading-and-writing-files-2" correct="B">
<template #question>
What is the difference between opening a file with mode <code>'w'</code> and mode <code>'a'</code>?
</template>

<BaseQuizOption value="A">A. <code>'w'</code> is for reading, <code>'a'</code> is for writing</BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>'w'</code> overwrites the file, <code>'a'</code> appends to the file</BaseQuizOption>
<BaseQuizOption value="C">C. <code>'w'</code> is for Windows, <code>'a'</code> is for Apple</BaseQuizOption>
<BaseQuizOption value="D">D. There is no difference</BaseQuizOption>
<BaseQuizAnswer>Mode <code>'w'</code> opens the file for writing and overwrites any existing content. Mode <code>'a'</code> opens the file for appending, adding new content to the end of the file.</BaseQuizAnswer>
</BaseQuiz>

## Relevant links

- <router-link to="/cheatsheet/file-directory-path">File and directory Paths</router-link>
- <router-link to="/cheatsheet/json-yaml">JSON and YAML</router-link>
- <router-link to="/blog/python-pathlib-essentials">10 Essential File System Operations Every Developer Should Know</router-link>
- <router-link to="/builtin/open">open()</router-link>
- <router-link to="/builtin/print">print()</router-link>
