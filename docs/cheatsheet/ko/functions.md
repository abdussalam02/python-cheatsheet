---
title: '파이썬 함수 - 파이썬 치트 시트'
description: '파이썬에서 함수는 단일 작업을 수행하기 위해 구성된 코드 블록입니다.'
labUrl: 'https://labex.io/ko/labs/python-python-functions-633658?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python 함수
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikiversity.org/wiki/Programming_Fundamentals/Functions">프로그래밍 함수</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    함수는 단일 작업을 수행하기 위해 사용되는 구성된 코드 블록입니다. 함수는 애플리케이션에 더 나은 모듈성과 재사용성을 제공합니다.
  </base-disclaimer-content>
</base-disclaimer>

## 함수 인수 (Function Arguments)

함수는 `인수(arguments)`를 받고 `반환 값(return values)`을 가질 수 있습니다.

다음 예제에서 **say_hello** 함수는 "name" 인수를 받아 인사말을 출력합니다.

```python
# 하나의 인수를 받는 함수 정의
def say_hello(name):
   print(f'Hello {name}')

# 문자열 인수로 함수 호출
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

## 키워드 인수 (Keyword Arguments)

코드 가독성을 높이기 위해 가능한 한 명시적이어야 합니다. `키워드 인수(Keyword Arguments)`를 사용하여 함수에서 이를 달성할 수 있습니다.

```python
# 여러 매개변수를 가진 함수
def say_hi(name, greeting):
   print(f"{greeting} {name}")

# 위치 인수: 순서가 중요함
say_hi('John', 'Hello')
```

```output
Hello John
```

```python
# 키워드 인수: 순서는 중요하지 않으며, 가독성이 높음
say_hi(name='Anna', greeting='Hi')
```

```output
Hi Anna
```

<BaseQuiz id="cheatsheet-functions-1" correct="C">
<template #question>
Python 함수에서 키워드 인수를 사용하는 주된 이점은 무엇입니까?
</template>

<BaseQuizOption value="A">A. 더 빠르게 실행됩니다</BaseQuizOption>
<BaseQuizOption value="B">B. 메모리를 덜 사용합니다</BaseQuizOption>
<BaseQuizOption value="C" correct>C. 코드 가독성을 높이고 순서가 중요하지 않습니다</BaseQuizOption>
<BaseQuizOption value="D">D. 오류를 방지합니다</BaseQuizOption>
<BaseQuizAnswer>키워드 인수는 각 인수가 무엇을 나타내는지 명확하게 하여 코드 가독성을 높이고 인수를 어떤 순서로든 전달할 수 있게 해줍니다.</BaseQuizAnswer>
</BaseQuiz>

## 반환 값 (Return Values)

`def` 문을 사용하여 함수를 만들 때, `return` 문으로 반환 값이 무엇이 되어야 하는지 지정할 수 있습니다. 반환문은 다음으로 구성됩니다.

- `return` 키워드.

- 함수가 반환해야 하는 값 또는 표현식.

```python
# return 문을 사용하여 값을 반환하는 함수
def sum_two_numbers(number_1, number_2):
   return number_1 + number_2

# 함수를 호출하고 반환된 값을 저장
result = sum_two_numbers(7, 8)
print(result)
```

```output
15
```

<BaseQuiz id="cheatsheet-functions-2" correct="A">
<template #question>
Python 에서 함수로부터 값을 반환하기 위해 사용되는 키워드는 무엇입니까?
</template>

<BaseQuizOption value="A" correct>A. <code>return</code></BaseQuizOption>
<BaseQuizOption value="B">B. <code>output</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>yield</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>exit</code></BaseQuizOption>
<BaseQuizAnswer><code>return</code> 키워드는 함수에서 값을 반환하는 데 사용됩니다. return 문을 사용하지 않으면 함수는 <code>None</code>을 반환합니다.</BaseQuizAnswer>
</BaseQuiz>

## 지역 및 전역 범위 (Local and Global Scope)

- 전역 범위의 코드는 지역 변수를 사용할 수 없습니다.

- 그러나 지역 범위는 전역 변수에 접근할 수 있습니다.

- 함수 지역 범위 내의 코드는 다른 지역 범위의 변수를 사용할 수 없습니다.

- 서로 다른 범위에 있는 경우 동일한 이름을 가진 여러 변수를 사용할 수 있습니다. 즉, spam 이라는 지역 변수와 spam 이라는 전역 변수가 모두 존재할 수 있습니다.

```python
# 전역 변수: 어디서든 접근 가능
global_variable = 'I am available everywhere'

def some_function():
    print(global_variable)  # 전역 변수에 접근 가능
    # 지역 변수: 이 함수 내에서만 존재함
    local_variable = "only available within this function"
    print(local_variable)

# NameError 발생: local_variable 는 전역 범위에 존재하지 않음
print(local_variable)
```

```output
Traceback (most recent call last):
  File "<stdin>", line 10, in <module>
NameError: name 'local_variable' is not defined
```

## global 문 (The global Statement)

함수 내에서 전역 변수를 수정해야 하는 경우, global 문을 사용합니다.

```python
# 함수 내부에서 전역 변수를 수정하기 위해 'global' 키워드 사용
def spam():
    global eggs  # 전역 변수를 수정하고 있음을 선언
    eggs = 'spam'  # 이것은 전역 변수를 변경함

eggs = 'global'
spam()  # 함수가 전역 변수를 수정함
print(eggs)  # 'spam'을 출력함, 'global'이 아님
```

```output
spam
```

<BaseQuiz id="cheatsheet-functions-3" correct="B">
<template #question>
전역 변수를 수정하기 위해 함수 내에서 반드시 사용해야 하는 키워드는 무엇입니까?
</template>

<BaseQuizOption value="A">A. <code>nonlocal</code></BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>global</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>extern</code></BaseQuizOption>
<BaseQuizOption value="D">D. 키워드가 필요 없음</BaseQuizOption>
<BaseQuizAnswer>전역 변수를 수정하려면 함수 내에서 <code>global</code> 키워드를 사용해야 합니다. 이것이 없으면 Python 은 대신 지역 변수를 생성합니다.</BaseQuizAnswer>
</BaseQuiz>

변수가 지역 범위에 있는지 전역 범위에 있는지 판단하는 네 가지 규칙이 있습니다.

1. 변수가 전역 범위 (즉, 모든 함수 외부) 에서 사용되는 경우, 항상 전역 변수입니다.

1. 함수 내에 해당 변수에 대한 전역 문이 있는 경우, 전역 변수입니다.

1. 그렇지 않고, 함수 내에서 할당문에서 변수가 사용되는 경우, 지역 변수입니다.

1. 하지만 변수가 할당문에서 사용되지 않는 경우, 전역 변수입니다.

## 람다 함수 (Lambda Functions)

Python 에서 람다 함수는 단일 표현식만 가질 수 있지만, 임의의 수의 인수를 가질 수 있는 한 줄짜리 익명 함수입니다.

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://docs.python.org/3/library/ast.html?highlight=lambda#function-and-class-definitions">Python 3 튜토리얼</a>에서 발췌
  </base-disclaimer-title>
  <base-disclaimer-content>
    lambda 는 표현식 내에서 사용될 수 있는 최소한의 함수 정의입니다. FunctionDef 와 달리 body 는 단일 노드를 포함합니다.
  </base-disclaimer-content>
</base-disclaimer>

<base-warning>
  <base-warning-title>
    단일 라인 표현식
  </base-warning-title>
  <base-warning-content>
    람다 함수는 단일 라인의 코드와 같은 표현식만 평가할 수 있습니다.
  </base-warning-content>
</base-warning>

이 함수:

```python
# 일반 함수 정의
def add(x, y):
    return x + y

add(5, 3)
```

```output
8
```

다음 _람다_ 함수와 동등합니다.

```python
# 람다 함수: 한 줄로 정의된 익명 함수
# 구문: lambda 인수: 표현식
add = lambda x, y: x + y
add(5, 3)
```

```output
8
```

<BaseQuiz id="cheatsheet-functions-4" correct="D">
<template #question>
Python 에서 람다 함수란 무엇입니까?
</template>

<BaseQuizOption value="A">A. 한 번만 호출할 수 있는 함수</BaseQuizOption>
<BaseQuizOption value="B">B. 인수를 받지 않는 함수</BaseQuizOption>
<BaseQuizOption value="C">C. 여러 값을 반환하는 함수</BaseQuizOption>
<BaseQuizOption value="D" correct>D. 임의의 수의 인수를 가질 수 있지만 단 하나의 표현식만 가질 수 있는 단일 라인 익명 함수</BaseQuizOption>
<BaseQuizAnswer>람다 함수는 <code>lambda</code> 키워드를 사용하여 정의된 익명, 단일 라인 함수입니다. 여러 인수를 가질 수 있지만 단일 표현식만 포함할 수 있습니다.</BaseQuizAnswer>
</BaseQuiz>

일반 중첩 함수와 마찬가지로 람다도 렉시컬 클로저로 작동합니다.

```python
# 람다 클로저: 외부 범위의 변수를 캡처하는 람다 함수
def make_adder(n):
    return lambda x: x + n  # 람다가 외부 함수로부터 'n'을 캡처함

# 다른 양을 더하는 함수 생성
plus_3 = make_adder(3)  # 3 을 더하는 람다를 반환
plus_5 = make_adder(5)  # 5 를 더하는 람다를 반환

plus_3(4)  # 4 + 3 = 7 반환
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
람다 클로저는 무엇을 가능하게 합니까?
</template>

<BaseQuizOption value="A" correct>A. 외부 범위의 변수 캡처</BaseQuizOption>
<BaseQuizOption value="B">B. global 키워드 없이 전역 변수 수정</BaseQuizOption>
<BaseQuizOption value="C">C. 여러 값 반환</BaseQuizOption>
<BaseQuizOption value="D">D. 코드를 비동기적으로 실행</BaseQuizOption>
<BaseQuizAnswer>람다 클로저는 람다 함수가 일반 중첩 함수와 유사하게 포함된 범위의 변수를 캡처하고 사용할 수 있도록 합니다.</BaseQuizAnswer>
</BaseQuiz>

## 관련 링크

- <router-link to="/blog/python-easy-args-kwargs">\*args 및 \*\*kwargs 설명</router-link>
- <router-link to="/cheatsheet/args-and-kwargs">Args 및 Kwargs</router-link>
- <router-link to="/cheatsheet/decorators">데코레이터</router-link>
- <router-link to="/cheatsheet/control-flow">제어 흐름</router-link>
- <router-link to="/cheatsheet/basics">기본 사항</router-link>
- <router-link to="/builtin">내장 함수</router-link>
