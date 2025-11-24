---
title: '파이썬 예외 처리 - 파이썬 치트 시트'
description: '파이썬에서 예외 처리는 예외 발생에 대응하는 프로세스입니다.'
labUrl: 'https://labex.io/ko/labs/python-python-exception-handling-633656?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python 예외 처리
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikipedia.org/wiki/Exception_handling">예외 처리</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    컴퓨팅 및 컴퓨터 프로그래밍에서 예외 처리는 특별한 처리가 필요한 비정상적이거나 예외적인 조건인 예외의 발생에 대응하는 프로세스입니다.
  </base-disclaimer-content>
</base-disclaimer>

Python 에는 프로그램이 오류에 직면했을 때 발생하는 많은 [내장 예외 (built-in exceptions)](https://docs.python.org/3/library/exceptions.html)가 있으며, 인기 있는 [Requests](https://requests.readthedocs.io/en/latest)와 같은 대부분의 외부 라이브러리에는 우리가 처리해야 할 고유한 [사용자 정의 예외 (custom exceptions)](https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions)가 포함되어 있습니다.

## 기본 예외 처리

0 으로 나눌 수 없다는 것은 수학적 사실이며, Python 에서 시도하면 인터프리터는 내장 예외인 [ZeroDivisionError](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError)를 발생시킵니다.

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

프로그램 실행이 중단되거나 사용자가 이해하지 못할 출력을 표시하지 않도록 하고 싶다고 가정해 봅시다. 유용하고 명확한 메시지를 인쇄하려면 `try` 및 `except` 키워드를 사용하여 예외를 **_처리_**해야 합니다.

```python
# try-except: 예외를 우아하게 처리
def divide(dividend , divisor):
    try:  # 이 코드를 실행해 보세요
        print(dividend / divisor)
    except ZeroDivisionError:  # 특정 예외 유형을 포착
        print('0 으로 나눌 수 없습니다')

divide(dividend=10, divisor=5)
```

```output
2
```

```python
divide(dividend=10, divisor=0)
```

```output
0으로 나눌 수 없습니다
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Python 에서 예외를 처리하는 데 사용되는 키워드는 무엇입니까?
</template>

<base-quiz-option value="A" correct>A. <code>try</code> 및 <code>except</code></base-quiz-option>
<base-quiz-option value="B">B. <code>catch</code> 및 <code>handle</code></base-quiz-option>
<base-quiz-option value="C">C. <code>error</code> 및 <code>rescue</code></base-quiz-option>
<base-quiz-option value="D">D. <code>if</code> 및 <code>else</code></base-quiz-option>
<base-quiz-answer value="A">Python 은 예외를 발생시킬 수 있는 코드를 표시하기 위해 <code>try</code>를 사용하고, 발생하는 특정 예외를 처리하기 위해 <code>except</code>를 사용합니다.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 단일 예외 블록을 사용한 여러 예외 처리

여러 예외 블록을 만들 필요 없이 다음과 같이 한 줄에서 여러 예외를 처리할 수도 있습니다.

```python
# 하나의 except 블록에서 여러 예외 처리
def divide(dividend , divisor):
    try:
        if (dividend == 10):
          var = 'str' + 1  # 이것은 TypeError 를 발생시킵니다
        else:
          print(dividend / divisor)
    except (ZeroDivisionError, TypeError) as error:  # 여러 예외 유형 포착
        print(error)  # 오류 메시지 출력

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

<base-quiz>
<base-quiz-question correct="B">
<template #question>
단일 <code>except</code> 블록에서 여러 예외 유형을 처리할 수 있습니까?
</template>

<base-quiz-option value="A">A. 아니요, 각 예외 유형에 대해 별도의 <code>except</code> 블록을 사용해야 합니다</base-quiz-option>
<base-quiz-option value="B" correct>B. 예, <code>except (Exception1, Exception2)</code>와 같이 튜플로 묶으면 가능합니다</base-quiz-option>
<base-quiz-option value="C">C. 예, 하지만 관련이 있는 경우에만 가능합니다</base-quiz-option>
<base-quiz-option value="D">D. 아니요, Python 은 이를 지원하지 않습니다</base-quiz-option>
<base-quiz-answer value="B"><code>except (ZeroDivisionError, TypeError) as error:</code>와 같이 튜플로 묶으면 단일 <code>except</code> 블록에서 여러 예외 유형을 처리할 수 있습니다.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 예외 처리의 Finally 코드

`finally` 섹션 내부의 코드는 예외가 발생했는지 여부와 관계없이 항상 실행됩니다.

```python
# finally 블록: 예외 발생 여부와 관계없이 항상 실행
def divide(dividend , divisor):
    try:
        print(dividend / divisor)
    except ZeroDivisionError:
        print('0 으로 나눌 수 없습니다')
    finally:  # 예외가 발생하더라도 항상 실행됩니다
        print('실행 완료')

divide(dividend=10, divisor=5)
```

```output
2.0
실행 완료
```

```python
divide(dividend=10, divisor=0)
```

```output
0으로 나눌 수 없습니다
실행 완료
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
<code>finally</code> 블록은 언제 실행됩니까?
</template>

<base-quiz-option value="A">A. 예외가 발생했을 때만</base-quiz-option>
<base-quiz-option value="B">B. 예외가 발생하지 않았을 때만</base-quiz-option>
<base-quiz-option value="C" correct>C. 예외 발생 여부와 관계없이 항상</base-quiz-option>
<base-quiz-option value="D">D. 절대 실행되지 않음</base-quiz-option>
<base-quiz-answer value="C"><code>finally</code> 블록은 예외 발생 여부와 관계없이 항상 실행됩니다. 결과에 관계없이 실행되어야 하는 정리 코드에 유용합니다.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 사용자 정의 예외

사용자 정의 예외는 Python 의 기본 `Exception` 클래스를 상속하는 `class`를 생성하여 초기화되며 `raise` 키워드를 사용하여 발생시킵니다.

```python
# 사용자 정의 예외: Exception 클래스 상속을 통해 생성
class MyCustomException(Exception):
    pass

raise MyCustomException  # 사용자 정의 예외 발생
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyCustomException
```

사용자 정의 예외 메시지를 선언하려면 매개변수로 전달할 수 있습니다.

```python
class MyCustomException(Exception):
    pass

raise MyCustomException('내 사용자 정의 예외에 대한 사용자 정의 메시지')
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyCustomException: 내 사용자 정의 예외에 대한 사용자 정의 메시지
```

사용자 정의 예외를 처리하는 것은 다른 예외와 동일합니다.

```python
try:
    raise MyCustomException('내 사용자 정의 예외에 대한 사용자 정의 메시지')
except MyCustomException:
    print('내 사용자 정의 예외가 발생했습니다')
```

```output
내 사용자 정의 예외가 발생했습니다
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Python 에서 사용자 정의 예외를 만드는 방법은 무엇입니까?
</template>

<base-quiz-option value="A" correct>A. <code>Exception</code> 클래스를 상속하는 클래스 생성</base-quiz-option>
<base-quiz-option value="B">B. <code>@exception</code> 데코레이터 사용</base-quiz-option>
<base-quiz-option value="C">C. <code>Exception.create()</code> 호출</base-quiz-option>
<base-quiz-option value="D">D. 특수 모듈에서 가져오기</base-quiz-option>
<base-quiz-answer value="A">사용자 정의 예외는 기본 <code>Exception</code> 클래스를 상속하는 클래스를 정의하여 생성됩니다. 그런 다음 내장 예외처럼 발생시키고 처리할 수 있습니다.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 관련 링크

- <router-link to="/cheatsheet/control-flow">제어 흐름</router-link>
- <router-link to="/builtin/breakpoint">breakpoint()</router-link>
- <router-link to="/builtin/isinstance">isinstance()</router-link>
- <router-link to="/builtin/issubclass">issubclass()</router-link>
