---
title: 'Python 正则表达式 - Python 速查表'
description: '正则表达式（Regex）是一串字符序列，用于在文本中指定搜索模式，并被字符串搜索算法使用。'
labUrl: 'https://labex.io/zh/labs/python-python-regular-expressions-633664?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
正则表达式
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikipedia.org/wiki/Regular_expression">正则表达式</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    正则表达式（缩写为 regex [...]）是一系列字符，用于在文本中指定搜索模式。[...] 用于字符串搜索算法，对字符串执行“查找”或“查找和替换”操作，或用于输入验证。
  </base-disclaimer-content>
</base-disclaimer>

1. 使用 `import re` 导入 regex 模块。
2. 使用 `re.compile()` 函数创建 Regex 对象。（记住使用原始字符串。）
3. 将要搜索的字符串传递给 Regex 对象的 `search()` 方法。这将返回一个 `Match` 对象。
4. 调用 Match 对象的 `group()` 方法以返回实际匹配文本的字符串。

Python 中所有的 regex 函数都在 re 模块中：

```python
# Import re module for regular expression operations
import re
```

## Regex 符号

| 符号                     | 匹配内容                                   |
| :----------------------- | :----------------------------------------- |
| `?`                      | 前一个组的零个或一个。                     |
| `*`                      | 前一个组的零个或多个。                     |
| `+`                      | 前一个组的一个或多个。                     |
| `{n}`                    | 前一个组的正好 n 个。                      |
| `{n,}`                   | 前一个组的 n 个或更多。                    |
| `{,m}`                   | 前一个组的 0 到 m 个。                     |
| `{n,m}`                  | 前一个组的至少 n 个且至多 m 个。           |
| `{n,m}?` 或 `*?` 或 `+?` | 对前一个组执行非贪婪匹配。                 |
| `^spam`                  | 意味着字符串必须以 spam 开头。             |
| `spam$`                  | 意味着字符串必须以 spam 结尾。             |
| `.`                      | 任何字符，换行符除外。                     |
| `\d`, `\w`, 和 `\s`      | 分别表示数字、单词或空格字符。             |
| `\D`, `\W`, 和 `\S`      | 分别表示非数字、非单词或非空格的任何字符。 |
| `[abc]`                  | 方括号之间的任何字符（如 a、b、 ）。       |
| `[^abc]`                 | 方括号之间以外的任何字符。                 |

## 匹配 regex 对象

```python
# re.compile(): create regex pattern object (use raw string r'' to avoid escaping)
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # Pattern: 3 digits-3 digits-4 digits

mo = phone_num_regex.search('My number is 415-555-4242.')  # Search for pattern

print(f'Phone number found: {mo.group()}')  # group() returns matched text
```

```output
Phone number found: 415-555-4242
```

## 使用圆括号进行分组

```python
# Parentheses create groups: group(1) returns first group, group(2) returns second
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')  # Two groups in parentheses
mo = phone_num_regex.search('My number is 415-555-4242.')

mo.group(1)  # Returns first group: '415'
```

```output
'415'
```

```python
mo.group(2)
```

```output
'555-4242'
```

```python
mo.group(0)
```

```output
'415-555-4242'
```

```python
mo.group()
```

```output
'415-555-4242'
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-regular-expressions-1">
<template #question>
当在匹配对象上调用 <code>group()</code> 时，它返回什么？
</template>

<base-quiz-option value="A" correct>A. 整个匹配的文本</base-quiz-option>
<base-quiz-option value="B">B. 仅第一个组</base-quiz-option>
<base-quiz-option value="C">C. 所有组作为一个列表</base-quiz-option>
<base-quiz-option value="D">D. 匹配的索引</base-quiz-option>
<base-quiz-answer value="A"><code>group()</code> 方法（或 <code>group(0)</code>）返回整个匹配的文本。要获取特定组，请使用 <code>group(1)</code>、<code>group(2)</code> 等。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

要一次性检索所有组，请使用 `groups()` 方法：

```python
# groups(): returns tuple of all groups
mo.groups()  # Returns ('415', '555-4242')
```

```output
('415', '555-4242')
```

```python
area_code, main_number = mo.groups()

print(area_code)
```

```output
415
```

```python
print(main_number)
```

```output
555-4242
```

## 使用管道进行多重分组

您可以在任何想要匹配多个表达式中的一个的地方使用 `|` 字符。

```python
hero_regex = re.compile (r'Batman|Tina Fey')

mo1 = hero_regex.search('Batman and Tina Fey.')
mo1.group()
```

```output
'Batman'
```

```python
mo2 = hero_regex.search('Tina Fey and Batman.')
mo2.group()
```

```output
'Tina Fey'
```

您也可以在正则表达式中使用管道来匹配多个模式中的一个：

```python
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel')

mo.group()
```

```output
'Batmobile'
```

```python
mo.group(1)
```

```output
'mobile'
```

## 使用问号进行可选匹配

`?` 字符将它前面的组标记为模式的可选部分。

```python
bat_regex = re.compile(r'Bat(wo)?man')

mo1 = bat_regex.search('The Adventures of Batman')
mo1.group()
```

```output
'Batman'
```

```python
mo2 = bat_regex.search('The Adventures of Batwoman')
mo2.group()
```

```output
'Batwoman'
```

## 使用星号匹配零个或多个

`*`（星号）表示“匹配零个或多个”。位于星号之前的组可以在文本中出现任意次数。

```python
bat_regex = re.compile(r'Bat(wo)*man')
mo1 = bat_regex.search('The Adventures of Batman')
mo1.group()
```

```output
'Batman'
```

```python
mo2 = bat_regex.search('The Adventures of Batwoman')
mo2.group()
```

```output
'Batwoman'
```

```python
mo3 = bat_regex.search('The Adventures of Batwowowowoman')
mo3.group()
```

```output
'Batwowowowoman'
```

## 使用加号匹配一个或多个

`+`（加号）表示匹配一个或多个。加号前面的组必须至少出现一次：

```python
bat_regex = re.compile(r'Bat(wo)+man')

mo1 = bat_regex.search('The Adventures of Batwoman')
mo1.group()
```

```output
'Batwoman'
```

```python
mo2 = bat_regex.search('The Adventures of Batwowowowoman')
mo2.group()
```

```output
'Batwowowowoman'
```

```python
mo3 = bat_regex.search('The Adventures of Batman')
mo3 is None
```

```output
True
```

## 使用花括号匹配特定重复次数

如果你有一个你想重复特定次数的组，在你的正则表达式中跟在组后面加上花括号中的数字：

```python
ha_regex = re.compile(r'(Ha){3}')

mo1 = ha_regex.search('HaHaHa')
mo1.group()
```

```output
'HaHaHa'
```

```python
mo2 = ha_regex.search('Ha')
mo2 is None
```

```output
True
```

你可以用花括号之间的最小和最大值来指定一个范围，而不是一个数字。例如，正则表达式 (Ha){3,5} 将匹配 'HaHaHa'、'HaHaHaHa' 和 'HaHaHaHaHa'。

```python
ha_regex = re.compile(r'(Ha){2,3}')
mo1 = ha_regex.search('HaHaHaHa')
mo1.group()
```

```output
'HaHaHa'
```

## 贪婪匹配和非贪婪匹配

Python 的正则表达式默认是贪婪的：在有歧义的情况下，它们会匹配尽可能长的字符串。花括号的非贪婪版本（匹配最短字符串）在闭合花括号后跟一个问号。

```python
greedy_ha_regex = re.compile(r'(Ha){3,5}')

mo1 = greedy_ha_regex.search('HaHaHaHaHa')
mo1.group()
```

```output
'HaHaHaHaHa'
```

```python
non_greedy_ha_regex = re.compile(r'(Ha){3,5}?')
mo2 = non_greedy_ha_regex.search('HaHaHaHaHa')
mo2.group()
```

```output
'HaHaHa'
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-regular-expressions-2">
<template #question>
什么使得正则表达式模式成为非贪婪的？
</template>

<base-quiz-option value="A">A. 使用 <code>_</code> 而不是 <code>+</code></base-quiz-option>
<base-quiz-option value="B" correct>B. 在量词后添加一个 <code>?</code> (例如 <code>_?</code>, <code>+?</code>, <code>{3,5}?</code>)</base-quiz-option>
<base-quiz-option value="C">C. 使用圆括号</base-quiz-option>
<base-quiz-option value="D">D. 使用方括号</base-quiz-option>
<base-quiz-answer value="B">在 <code>\*</code>、<code>+</code> 或 <code>{n,m}</code> 等量词后添加 <code>?</code> 会使其成为非贪婪的，匹配最短的可能字符串而不是最长的。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## findall() 方法

`findall()` 方法将返回搜索字符串中所有匹配项的字符串列表。

```python
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups

phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
```

```output
['415-555-9999', '212-555-0000']
```

## 创建自定义字符类

您可以使用方括号定义自己的字符类。例如，字符类 _[aeiouAEIOU]_ 将匹配任何元音字母，包括大小写。

```python
vowel_regex = re.compile(r'[aeiouAEIOU]')
vowel_regex.findall('Robocop eats baby food. BABY FOOD.')
```

```output
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
```

您也可以通过使用连字符包含字母或数字的范围。例如，字符类 _[a-zA-Z0-9]_ 将匹配所有小写字母、大写字母和数字。

通过在字符类的开方括号后放置一个脱字符号 (`^`)，您可以创建一个负字符类，它将匹配字符类中不包含的所有字符：

```python
consonant_regex = re.compile(r'[^aeiouAEIOU]')
consonant_regex.findall('Robocop eats baby food. BABY FOOD.')
```

```output
['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
```

## 脱字符号和美元符号字符

- 您也可以在正则表达式的开头使用脱字符号 `^` 来指示匹配必须发生在搜索文本的开头。

- 同样，您可以在正则表达式的末尾放置一个美元符号 `$` 来指示字符串必须以该正则表达式模式结尾。

- 您可以同时使用 `^` 和 `$` 来指示整个字符串必须匹配该正则表达式。

正则表达式字符串 `r'^Hello'` 匹配以 'Hello' 开头的字符串：

```python
begins_with_hello = re.compile(r'^Hello')
begins_with_hello.search('Hello world!')
```

```output
<_sre.SRE_Match object; span=(0, 5), match='Hello'>
```

```python
begins_with_hello.search('He said hello.') is None
```

```output
True
```

正则表达式字符串 `r'\d\$'` 匹配以 0 到 9 的数字字符结尾的字符串：

```python
whole_string_is_num = re.compile(r'^\d+$')

whole_string_is_num.search('1234567890')
```

```output
<_sre.SRE_Match object; span=(0, 10), match='1234567890'>
```

```python
whole_string_is_num.search('12345xyz67890') is None
```

```output
True
```

```python
whole_string_is_num.search('12 34567890') is None
```

```output
True
```

## 通配符字符

正则表达式中的 `.`（点）字符将匹配除换行符外的任何字符：

```python
at_regex = re.compile(r'.at')

at_regex.findall('The cat in the hat sat on the flat mat.')
```

```output
['cat', 'hat', 'sat', 'lat', 'mat']
```

## 使用点星号匹配所有内容

```python
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')

mo = name_regex.search('First Name: Al Last Name: Sweigart')
mo.group(1)
```

```output
'Al'
```

```python
mo.group(2)
```

```output
'Sweigart'
```

`.*` 默认使用贪婪模式：它总是会尝试匹配尽可能多的文本。要以非贪婪方式匹配任何和所有文本，请使用点、星号和问号 (`.*?`)。问号告诉 Python 以非贪婪方式匹配：

```python
non_greedy_regex = re.compile(r'<.*?>')
mo = non_greedy_regex.search('<To serve man> for dinner.>')
mo.group()
```

```output
'<To serve man>'
```

```python
greedy_regex = re.compile(r'<.*>')
mo = greedy_regex.search('<To serve man> for dinner.>')
mo.group()
```

```output
'<To serve man> for dinner.>'
```

## 使用点字符匹配换行符

点星号会匹配除换行符外的所有内容。通过将 `re.DOTALL` 作为第二个参数传递给 `re.compile()`，您可以使点字符匹配所有字符，包括换行符：

```python
no_newline_regex = re.compile('.*')
no_newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
```

```output
'Serve the public trust.'
```

```python
newline_regex = re.compile('.*', re.DOTALL)
newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
```

```output
'Serve the public trust.\nProtect the innocent.\nUphold the law.'
```

## 忽略大小写匹配

要使正则表达式忽略大小写，您可以将 `re.IGNORECASE` 或 `re.I` 作为第二个参数传递给 `re.compile()`：

```python
robocop = re.compile(r'robocop', re.I)

robocop.search('Robocop is part man, part machine, all cop.').group()
```

```output
'Robocop'
```

```python
robocop.search('ROBOCOP protects the innocent.').group()
```

```output
'ROBOCOP'
```

```python
robocop.search('Al, why does your programming book talk about robocop so much?').group()
```

```output
'robocop'
```

## 使用 sub() 方法替换字符串

Regex 对象的 `sub()` 方法接收两个参数：

1. 第一个参数是要替换任何匹配项的字符串。
2. 第二个参数是正则表达式的字符串。

`sub()` 方法返回一个已应用替换的字符串：

```python
names_regex = re.compile(r'Agent \w+')

names_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
```

```output
'CENSORED gave the secret documents to CENSORED.'
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-regular-expressions-3">
<template #question>
<code>sub()</code> 方法的作用是什么？
</template>

<base-quiz-option value="A">A. 查找字符串中的所有匹配项</base-quiz-option>
<base-quiz-option value="B" correct>B. 用替换字符串替换所有匹配项</base-quiz-option>
<base-quiz-option value="C">C. 在匹配处分割字符串</base-quiz-option>
<base-quiz-option value="D">D. 验证字符串格式</base-quiz-option>
<base-quiz-answer value="B"><code>sub()</code> 方法用替换字符串替换模式的所有匹配项。它返回一个应用了替换的新字符串。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 管理复杂的 Regexes

为了告诉 `re.compile()` 函数忽略正则表达式字符串中的空格和注释，“详细模式”可以通过将变量 `re.VERBOSE` 作为第二个参数传递给 `re.compile()` 来启用。

现在，而不是像这样难以阅读的正则表达式：

```python
phone_regex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
```

您可以像这样将正则表达式分布在多行上并添加注释：

```python
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-regular-expressions-4">
<template #question>
传递给 <code>re.compile()</code> 的 <code>re.VERBOSE</code> 会做什么？
</template>

<base-quiz-option value="A" correct>A. 允许在 regex 模式中使用空格和注释以提高可读性</base-quiz-option>
<base-quiz-option value="B">B. 使 regex 忽略大小写</base-quiz-option>
<base-quiz-option value="C">C. 使点字符匹配换行符</base-quiz-option>
<base-quiz-option value="D">D. 加快 regex 匹配速度</base-quiz-option>
<base-quiz-answer value="A"><code>re.VERBOSE</code> 标志允许您在正则表达式模式中添加空格和注释，使复杂的正则表达式更具可读性，同时不影响模式匹配。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 相关链接

- <router-link to="/cheatsheet/manipulating-strings">字符串操作</router-link>
- <router-link to="/cheatsheet/string-formatting">字符串格式化</router-link>
- <router-link to="/blog/python-data-types">Python 数据类型博客文章</router-link>
- <router-link to="/builtin/compile">compile()</router-link>
