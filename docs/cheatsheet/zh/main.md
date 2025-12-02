---
title: 'Python 主函数 - Python 速查表'
description: '是顶级代码执行范围的名称。当从标准输入、脚本或交互式提示符读取时，模块的名称被设置为 main。'
labUrl: 'https://labex.io/zh/labs/python-python-main-function-633661?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
主顶层脚本环境
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## 是什么

`__main__` 是顶层代码执行所在作用域的名称。
当一个模块从标准输入、脚本或交互式提示中读取时，其 **name** 被设置为等于 `__main__`。

模块可以通过检查自身的 `__name__` 来发现它是否在主作用域中运行，这允许使用一种常见的惯用法来有条件地执行模块中的代码。当它作为脚本运行或使用 `python -m` 运行时执行，但导入时不会：

```python
# __name__ == "__main__": 检查脚本是否被直接运行（未被导入）
if __name__ == "__main__":  # 脚本运行时为 True，导入时为 False
    # 仅在作为脚本运行时执行
    main()
```

对于包而言，通过包含一个 **main**.py 模块可以实现相同效果，当使用 -m 运行该模块时，其内容将被执行。

例如，我们正在开发一个设计为用作模块的脚本，我们应该这样做：

```python
# 示例：函数可以被导入，但测试代码仅在直接执行时运行
def add(a, b):
    return a+b

if __name__ == "__main__":  # 仅在文件被执行时运行，而不是被导入时运行
    add(3, 5)
```

<BaseQuiz id="cheatsheet-main-1" correct="B">
<template #question>
当一个 Python 文件作为脚本直接运行时，<code>__name__</code> 的值是多少？
</template>

<BaseQuizOption value="A">A. 文件名</BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>"**main**"</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>None</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>True</code></BaseQuizOption>
<BaseQuizAnswer>当一个 Python 文件作为脚本直接运行时，<code>**name**</code> 被设置为 <code>"**main**"</code>。当文件被导入为一个模块时，<code>**name**</code> 被设置为模块的名称。</BaseQuizAnswer>
</BaseQuiz>

## 优点

1. 每个 Python 模块都有其定义的 `__name__`，如果它是 `__main__`，则意味着该模块是用户独立运行的，我们可以执行相应的适当操作。
2. 如果你将此脚本作为模块导入到另一个脚本中，**name** 将被设置为脚本/模块的名称。
3. Python 文件可以充当可重用的模块，也可以充当独立程序。
4. `if __name__ == "__main__":` 用于仅在文件被直接运行时执行某些代码，而不是在被导入时执行。

<BaseQuiz id="cheatsheet-main-2" correct="A">
<template #question>
使用 <code>if __name__ == "__main__":</code> 的主要目的是什么？
</template>

<BaseQuizOption value="A" correct>A. 仅在文件被直接运行时执行代码，而不是在被导入时执行</BaseQuizOption>
<BaseQuizOption value="B">B. 防止文件被导入</BaseQuizOption>
<BaseQuizOption value="C">C. 使文件执行速度更快</BaseQuizOption>
<BaseQuizOption value="D">D. 向其他模块隐藏代码</BaseQuizOption>
<BaseQuizAnswer><code>if **name** == "**main**":</code> 惯用法允许 Python 文件同时充当可重用的模块和独立程序。只有当文件被直接执行而不是被导入时，该代码块内的代码才会运行。</BaseQuizAnswer>
</BaseQuiz>

## 相关链接

- <router-link to="/cheatsheet/functions">函数</router-link>
- <router-link to="/cheatsheet/packaging">打包</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">使用 Poetry 和 VSCode 的 Python 项目。第一部分</router-link>
- <router-link to="/builtin/import">import()</router-link>
