---
title: '파이썬 기초 - 파이썬 치트 시트'
description: '연산자, 데이터 유형, 변수, 함수 등을 다루는 포괄적인 가이드로 파이썬 기초를 배우세요. 파이썬 프로그래밍 기본기를 배우는 초보자에게 완벽합니다.'
labUrl: 'https://labex.io/ko/labs/python-python-basics-633647?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python 기본
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

우리 모두 어딘가에서 시작해야 하므로, 여기서 시작하는 것은 어떨까요. 이 가이드는 연산자, 데이터 유형, 변수 및 핵심 함수를 포함한 기본적인 Python 기초를 다룹니다.

<base-disclaimer>
<base-disclaimer-title>
Python 기본 개요
</base-disclaimer-title>
<base-disclaimer-content>
모든 초보자가 알아야 할 핵심 Python 기본 사항:

- 변수 및 기본 유형
- 연산자 및 표현식
- 문자열 및 일반적인 메서드
- 리스트, 튜플 및 딕셔너리
- 기본 제어 흐름 (if, for, while)
- 간단한 함수

</base-disclaimer-content>
</base-disclaimer>

## 수학 연산자

**가장 높음**에서 **가장 낮음** 우선순위 순:

| 연산자 | 연산        | 예시            |
| ------ | ----------- | --------------- |
| \*\*   | 거듭제곱    | `2 ** 3 = 8`    |
| %      | 나머지      | `22 % 8 = 6`    |
| //     | 정수 나누기 | `22 // 8 = 2`   |
| /      | 나누기      | `22 / 8 = 2.75` |
| \*     | 곱셈        | `3 * 3 = 9`     |
| -      | 뺄셈        | `5 - 2 = 3`     |
| +      | 덧셈        | `2 + 2 = 4`     |

표현식 예시:

```python
# 곱셈은 덧셈보다 우선순위가 높습니다
# 따라서 이것은 다음과 같이 평가됩니다: 2 + (3 * 6) = 2 + 18 = 20
2 + 3 * 6
```

```output
20
```

```python
# 괄호는 연산자 우선순위를 재정의합니다
# 이것은 다음과 같이 평가됩니다: 5 * 6 = 30
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
다음 Python 표현식의 결과는 무엇입니까?

```python
4 + 2 * 3
```

</template>

<base-quiz-option value="A" correct>A. 10</base-quiz-option>
<base-quiz-option value="B">B. 18</base-quiz-option>
<base-quiz-option value="C">C. 12</base-quiz-option>
<base-quiz-option value="D">D. 20</base-quiz-option>
<base-quiz-answer value="A">곱셈이 덧셈보다 우선순위가 높으므로, 이는 다음과 같이 평가됩니다: 4 + (2 \* 3) = 4 + 6 = 10</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 증감 할당 연산자

| 연산자      | 등가 표현        |
| ----------- | ---------------- |
| `var += 1`  | `var = var + 1`  |
| `var -= 1`  | `var = var - 1`  |
| `var *= 1`  | `var = var * 1`  |
| `var /= 1`  | `var = var / 1`  |
| `var //= 1` | `var = var // 1` |
| `var %= 1`  | `var = var % 1`  |
| `var **= 1` | `var = var ** 1` |

예시:

```python
# 증감 할당: greeting = greeting + ' world!'와 동일
greeting = 'Hello'
greeting += ' world!'
greeting
```

```output
'Hello world!'
```

```python
# 숫자를 1 만큼 증가
number = 1
number += 1
number
```

```output
2
```

```python
# 리스트 요소 복제: my_list = my_list * 3 와 동일
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
이 코드를 실행한 후 <code>x</code>의 값은 얼마입니까?

```python
x = 5
x += 3
```

</template>

<base-quiz-option value="A">A. 3</base-quiz-option>
<base-quiz-option value="B" correct>B. 8</base-quiz-option>
<base-quiz-option value="C">C. 5</base-quiz-option>
<base-quiz-option value="D">D. 15</base-quiz-option>
<base-quiz-answer value="B">증감 할당 연산자 <code>+=</code>는 <code>x = x + 3</code>과 동일합니다. 따라서 <code>x</code>는 5 로 시작하여 5 + 3 = 8 이 됩니다.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 월러스 연산자 (Walrus Operator)

월러스 연산자는 변수에 값을 할당하는 동시에 해당 변수의 값을 반환하여 표현식 내에서 변수 할당을 허용합니다.

예시:

```python
# 월러스 연산자는 하나의 표현식에서 값을 할당하고 반환합니다
# my_var 에 "Hello World!"가 할당된 다음 출력됩니다
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

_월러스 연산자_ 또는 **할당 표현식 연산자**는 [PEP 572](https://peps.python.org/pep-0572/)를 통해 2018 년에 처음 도입되었으며, 2019 년 10 월 **Python 3.8**과 함께 공식적으로 출시되었습니다.

<base-disclaimer>
  <base-disclaimer-title>
    구문 의미론 및 예시
  </base-disclaimer-title>
  <base-disclaimer-content>
  <a href="https://peps.python.org/pep-0572/" target="_blank">PEP 572</a>는 월러스 연산자에 대한 구문, 의미론 및 예시를 제공합니다.
  </base-disclaimer-content>
</base-disclaimer>

## 데이터 유형

데이터 유형을 이해하는 것은 가장 중요한 Python 기본 사항 중 하나입니다. Python 에는 필요한 거의 모든 것을 다루는 아홉 가지 핵심 내장 데이터 유형이 있습니다.

| 데이터 유형                                                | 예시                                     | 설명                                      |
| :--------------------------------------------------------- | :--------------------------------------- | :---------------------------------------- |
| **숫자**                                                   |                                          |                                           |
| <router-link to='/builtin/int'>`int`</router-link>         | `-2, -1, 0, 1, 2, 3, 4, 5`               | 정수 (whole numbers)                      |
| <router-link to='/builtin/float'>`float`</router-link>     | `-1.25, -1.0, -0.5, 0.0, 0.5, 1.0, 1.25` | 소수점이 있는 숫자                        |
| <router-link to='/builtin/complex'>`complex`</router-link> | `2+3j, complex(1, 4)`                    | 실수부와 허수부를 가진 숫자               |
| **텍스트**                                                 |                                          |                                           |
| <router-link to='/builtin/str'>`str`</router-link>         | `'a', 'Hello!', "Python"`                | 텍스트 및 문자                            |
| **불리언**                                                 |                                          |                                           |
| <router-link to='/builtin/bool'>`bool`</router-link>       | `True, False`                            | 참 또는 거짓 값                           |
| **None**                                                   |                                          |                                           |
| `NoneType`                                                 | `None`                                   | "값이 없음" 또는 "아무것도 없음"을 나타냄 |
| **컬렉션**                                                 |                                          |                                           |
| <router-link to='/builtin/list'>`list`</router-link>       | `[1, 2, 3], ['a', 'b', 'c']`             | 순서가 있고 변경 가능한 컬렉션            |
| <router-link to='/builtin/dict'>`dict`</router-link>       | `{'name': 'Alice', 'age': 30}`           | 키 - 값 쌍                                |
| <router-link to='/builtin/tuple'>`tuple`</router-link>     | `(1, 2, 3), ('a', 'b')`                  | 순서가 있고 변경 불가능한 컬렉션          |
| <router-link to='/builtin/set'>`set`</router-link>         | `{1, 2, 3}, {'a', 'b', 'c'}`             | 순서가 없고 고유한 항목의 컬렉션          |

### 간단한 예시

```python
# 숫자
age = 25                    # int
price = 19.99              # float
coordinate = 2 + 3j        # complex

# 텍스트
name = "Alice"             # str

# 불리언
is_student = True          # bool

# None
result = None              # NoneType

# 컬렉션
scores = [85, 92, 78]      # list
person = {'name': 'Bob', 'age': 30}  # dict
coordinates = (10, 20)     # tuple
unique_ids = {1, 2, 3}     # set
```

각 유형을 언제 사용해야 하는지에 대한 시각적 예시와 자세한 설명이 포함된 포괄적인 가이드는 다음을 참조하십시오: <router-link to="/blog/python-data-types">Python 데이터 유형: 초보자를 위한 시각적 가이드</router-link>.

## 연결 및 복제

문자열 연결:

```python
# 문자열 연결: 인접한 문자열은 자동으로 결합됩니다
'Alice' 'Bob'
```

```output
'AliceBob'
```

문자열 복제:

```python
# 문자열 복제: 문자열을 여러 번 반복
'Alice' * 5
```

```output
'AliceAliceAliceAliceAlice'
```

## 변수

변수는 Python 기본 사항의 기본 부분입니다. 다음 규칙만 준수하면 변수 이름을 자유롭게 지정할 수 있습니다.

1. 한 단어로만 구성될 수 있습니다.

```python
# 나쁨
my variable = 'Hello'

# 좋음
var = 'Hello'
```

2. 문자, 숫자 및 밑줄 (`_`) 문자만 사용할 수 있습니다.

```python
# 나쁨
%$@variable = 'Hello'

# 좋음
my_var = 'Hello'

# 좋음
my_var_2 = 'Hello'
```

3. 숫자로 시작할 수 없습니다.

```python
# 작동하지 않음
23_var = 'hello'
```

4. 밑줄 (`_`) 로 시작하는 변수 이름은 "사용되지 않는" 것으로 간주됩니다.

```python
# _spam 은 코드에서 다시 사용되어서는 안 됩니다
_spam = 'Hello'
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
Python 기본 사항에서 다음 중 유효한 변수 이름은 무엇입니까?
</template>

<base-quiz-option value="A">A. <code>3value</code></base-quiz-option>
<base-quiz-option value="B">B. <code>user-name</code></base-quiz-option>
<base-quiz-option value="C" correct>C. <code>user_name</code></base-quiz-option>
<base-quiz-option value="D">D. <code>for</code></base-quiz-option>
<base-quiz-answer value="C"><code>user_name</code>은 문자, 숫자 및 밑줄만 사용하고 숫자로 시작하지 않으므로 유효한 변수 이름입니다.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 주석

인라인 주석:

```python
# 이것은 주석입니다
```

여러 줄 주석:

```python
# 이것은
# 여러 줄 주석입니다
```

주석이 있는 코드:

```python
a = 1  # 초기화
```

주석 앞에 공백 두 칸에 유의하십시오.

함수 docstring:

```python
def foo():
    """
    이것은 함수 docstring 입니다
    다음도 사용할 수 있습니다:
    ''' 함수 Docstring '''
    """
```

## print() 함수

`print()` 함수는 가장 먼저 배우게 될 Python 기본 사항 중 하나입니다. 전달된 인수의 값을 출력합니다. [...] 여러 인수, 부동 소수점 수량 및 문자열을 처리합니다. 문자열은 따옴표 없이 인쇄되며 항목 사이에 공백이 삽입되어 형식을 깔끔하게 지정할 수 있습니다.

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

### end 키워드

`end` 키워드 인수를 사용하여 출력 후 줄 바꿈을 방지하거나 출력을 다른 문자열로 끝낼 수 있습니다.

```python
# end 매개변수를 사용하여 각 print 문 뒤에 오는 것을 변경합니다
phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
for word in phrase:
    print(word, end='-')  # 줄 바꿈 대신 '-' 사용
```

```output
printed-with-a-dash-in-between-
```

### sep 키워드

`sep` 키워드는 여러 개의 객체가 있을 경우 객체들을 구분하는 방법을 지정합니다.

```python
# sep 매개변수를 사용하여 여러 인수 사이의 구분 기호를 지정합니다
print('cats', 'dogs', 'mice', sep=',')  # 쉼표로 구분된 출력
```

```output
cats,dogs,mice
```

## input() 함수

이 함수는 사용자로부터 입력을 받아 문자열로 변환합니다.

```python
# input() 은 사용자 입력을 읽고 문자열로 반환합니다
print('What is your name?')   # 이름을 묻습니다
my_name = input()  # 사용자가 입력하고 Enter 를 누를 때까지 기다립니다
print('Hi, {}'.format(my_name))
```

```output
What is your name?
Martha
Hi, Martha
```

`input()`은 `print()`를 사용하지 않고도 기본 메시지를 설정할 수 있습니다.

```python
my_name = input('What is your name? ')  # 기본 메시지
print('Hi, {}'.format(my_name))
```

```output
What is your name? Martha
Hi, Martha
```

.format 을 사용하지 않기 위해 서식 지정된 문자열을 사용하는 것도 가능합니다.

```python
# input() 은 프롬프트 메시지를 직접 표시할 수 있습니다
my_name = input('What is your name? ')  # 한 번의 호출로 프롬프트 및 읽기
print(f'Hi, {my_name}')  # 문자열 서식 지정을 위한 f-string
```

```output
What is your name? Martha
Hi, Martha
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Python 기본 사항에서 `input()` 은 어떤 유형을 반환합니까?
</template>

<base-quiz-option value="A">A. int</base-quiz-option>
<base-quiz-option value="B" correct>B. str</base-quiz-option>
<base-quiz-option value="C">C. float</base-quiz-option>
<base-quiz-option value="D">D. 사용자 입력에 따라 다름</base-quiz-option>
<base-quiz-answer value="B"><code>input()</code> 함수는 사용자가 입력하는 내용에 관계없이 항상 문자열을 반환합니다. 필요한 경우 다른 유형으로 변환해야 합니다.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## len() 함수

문자열, 리스트, 딕셔너리 등의 문자 수, 항목 수를 정수 값으로 평가합니다.

```python
# len() 은 문자열의 문자 수를 반환합니다
len('hello')  # 5 반환
```

```output
5
```

```python
# len() 은 리스트의 항목 수를 반환합니다
len(['cat', 3, 'dog'])  # 3 반환 (세 항목)
```

```output
3
```

<base-warning>
  <base-warning-title>비어 있음 테스트</base-warning-title>
  <base-warning-content>
    문자열, 리스트, 딕셔너리 등의 비어 있음 테스트는
    <code>len</code>을 사용하는 대신 직접적인 불리언 평가를 선호해야 합니다.
  </base-warning-content>
</base-warning>

비어 있음 테스트 예시:

```python
a = [1, 2, 3]

# 나쁨: 불필요한 len() 확인
if len(a) > 0:  # True 로 평가됨
    print("the list is not empty!")
```

```output
the list is not empty!
```

```python
# 좋음: 직접적인 불리언 평가 (Pythonic 방식)
if a:  # 리스트가 비어 있지 않으면 True 로 평가됨
    print("the list is not empty!")
```

```output
the list is not empty!
```

## str(), int(), 및 float() 함수

이 함수들을 사용하면 변수의 유형을 변경할 수 있습니다. 예를 들어, `integer` 또는 `float`를 `string`으로 변환할 수 있습니다.

```python
# 정수를 문자열로 변환
str(29)  # '29' 반환
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

또는 `string`을 `integer` 또는 `float`로 변환할 수 있습니다.

```python
# 문자열을 정수로 변환
int('11')  # 11 반환
```

```output
11
```

```python
# 문자열을 float 으로 변환
float('3.14')  # 3.14 반환
```

```output
3.14
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
다음 Python 코드의 결과는 무엇입니까?

```python
result = int('42')
type(result)
```

</template>

<base-quiz-option value="A">A. <code>str</code></base-quiz-option>
<base-quiz-option value="B">B. <code>float</code></base-quiz-option>
<base-quiz-option value="C" correct>C. <code>int</code></base-quiz-option>
<base-quiz-option value="D">D. <code>NoneType</code></base-quiz-option>
<base-quiz-answer value="C"><code>int()</code> 함수는 문자열을 정수로 변환합니다. 따라서 <code>int('42')</code>는 정수 <code>42</code>를 반환하고 <code>type(42)</code>는 <code>int</code>를 반환합니다.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 관련 링크

- <router-link to="/blog/python-data-types">Python 데이터 유형: 초보자를 위한 시각적 가이드</router-link>
- <router-link to="/blog/python-comprehensions-step-by-step">Python Comprehensions 단계별 가이드</router-link>
- <router-link to="/cheatsheet/control-flow">제어 흐름</router-link>
- <router-link to="/cheatsheet/functions">함수</router-link>
- <router-link to="/cheatsheet/lists-and-tuples">리스트 및 튜플</router-link>
- <router-link to="/cheatsheet/dictionaries">딕셔너리</router-link>
- <router-link to="/cheatsheet/sets">집합 (Sets)</router-link>
- <router-link to="/cheatsheet/string-formatting">문자열 서식 지정</router-link>
