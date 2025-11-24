---
title: 'Python 치트 시트: 파일 읽기 및 쓰기'
description: 'Python 에서 파일을 읽거나 쓰려면 with 문을 사용해야 합니다. 이 문은 작업 완료 후 자동으로 파일을 닫아 리소스를 효율적으로 관리해 줍니다.'
labUrl: 'https://labex.io/ko/labs/python-python-reading-and-writing-files-633663?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
파일 읽기 및 쓰기
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

파일 및 디렉터리 경로 조작에 대한 자세한 내용은 <router-link to="/cheatsheet/file-directory-path">파일 및 디렉터리 경로</router-link> 페이지를 참조하십시오.

## 파일 읽기/쓰기 프로세스

Python 에서 파일에 읽기/쓰기를 하려면 `with` 문을 사용하는 것이 좋습니다. 이 문은 작업이 끝난 후 파일을 자동으로 닫아 리소스 관리를 처리해 줍니다.

## 파일 열기 및 읽기

`open` 함수는 파일을 열고 해당 파일 객체를 반환합니다.

```python
# 'with' 문을 사용하여 파일 읽기: 완료되면 파일이 자동으로 닫힘
with open('/home/labex/project/hi.txt') as hello_file:
    hello_content = hello_file.read()  # 파일 전체 내용 읽기

hello_content
```

```output
'Hello World!'
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
파일을 열 때 <code>with</code> 문을 사용하는 주된 이점은 무엇입니까?
</template>

<base-quiz-option value="A" correct>A. 오류가 발생하더라도 작업이 완료되면 파일이 자동으로 닫힙니다</base-quiz-option>
<base-quiz-option value="B">B. 파일 열기가 더 빠릅니다</base-quiz-option>
<base-quiz-option value="C">C. 파일을 읽기 및 쓰기 모드로 동시에 열 수 있습니다</base-quiz-option>
<base-quiz-option value="D">D. 파일이 자동으로 압축됩니다</base-quiz-option>
<base-quiz-answer value="A"><code>with</code> 문은 예외가 발생하더라도 블록을 벗어날 때 파일이 자동으로 닫히도록 보장합니다. 이는 리소스를 적절하게 관리하는 데 도움이 됩니다.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

또는 _readlines()_ 메서드를 사용하여 파일에서 문자열 값 목록을 가져올 수 있으며, 텍스트의 각 줄에 대해 하나의 문자열이 포함됩니다.

```python
# readlines() 메서드: 각 줄에 대해 하나의 문자열을 포함하는 목록 반환
with open('sonnet29.txt') as sonnet_file:
    sonnet_file.readlines()  # 각 줄을 문자열로 포함하는 목록 반환
```

```output
['When, in disgrace with fortune and men's eyes,\n',
 ' I all alone beweep my  outcast state,\n',
 "And trouble deaf heaven with my bootless cries,\n",
 "And look upon myself and curse my fate,']
```

파일을 줄 단위로 반복할 수도 있습니다.

```python
# 파일을 줄 단위로 반복 (대용량 파일에 메모리 효율적)
with open('sonnet29.txt') as sonnet_file:
    for line in sonnet_file:  # 파일 객체는 반복 가능함
        print(line, end='')  # 추가 줄 바꿈 없이 출력
```

```output
When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,
```

## 파일에 쓰기

```python
# 파일에 쓰기: 'w' 모드는 기존 파일을 덮어씁니다
with open('bacon.txt', 'w') as bacon_file:  # 'w' = 쓰기 모드
    bacon_file.write('Hello world!\n')  # 작성된 문자 수 반환
```

```output
13
```

```python
# 파일에 추가: 'a' 모드는 기존 파일에 추가합니다
with open('bacon.txt', 'a') as bacon_file:  # 'a' = 추가 모드
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

<base-quiz>
<base-quiz-question correct="B">
<template #question>
<code>'w'</code> 모드로 파일을 여는 것과 <code>'a'</code> 모드로 파일을 여는 것의 차이점은 무엇입니까?
</template>

<base-quiz-option value="A">A. <code>'w'</code>는 읽기용이고, <code>'a'</code>는 쓰기용입니다</base-quiz-option>
<base-quiz-option value="B" correct>B. <code>'w'</code>는 파일을 덮어쓰고, <code>'a'</code>는 파일에 추가합니다</base-quiz-option>
<base-quiz-option value="C">C. <code>'w'</code>는 Windows 용이고, <code>'a'</code>는 Apple 용입니다</base-quiz-option>
<base-quiz-option value="D">D. 차이점이 없습니다</base-quiz-option>
<base-quiz-answer value="B"><code>'w'</code> 모드는 파일을 쓰기용으로 열고 기존 내용을 덮어씁니다. <code>'a'</code> 모드는 파일을 추가용으로 열고 새 내용을 파일 끝에 추가합니다.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 관련 링크

- <router-link to="/cheatsheet/file-directory-path">파일 및 디렉터리 경로</router-link>
- <router-link to="/cheatsheet/json-yaml">JSON 및 YAML</router-link>
- <router-link to="/blog/python-pathlib-essentials">모든 개발자가 알아야 할 10 가지 필수 파일 시스템 작업</router-link>
- <router-link to="/builtin/open">open()</router-link>
- <router-link to="/builtin/print">print()</router-link>
