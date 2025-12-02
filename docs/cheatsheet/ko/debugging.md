---
title: '파이썬 디버깅 - 파이썬 치트 시트'
description: '컴퓨터 프로그래밍 및 소프트웨어 개발에서 디버깅은 컴퓨터 프로그램, 소프트웨어 또는 시스템 내의 버그 (오작동을 유발하는 결함 또는 문제) 를 찾고 해결하는 과정입니다.'
labUrl: 'https://labex.io/ko/labs/python-python-debugging-633653?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python 디버깅
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikipedia.org/wiki/Debugging">버그 찾기 및 해결</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    컴퓨터 프로그래밍 및 소프트웨어 개발에서 디버깅은 컴퓨터 프로그램, 소프트웨어 또는 시스템 내에서 버그 (정상적인 작동을 방해하는 결함 또는 문제) 를 찾고 해결하는 프로세스입니다.
  </base-disclaimer-content>
</base-disclaimer>

## 예외 발생시키기

예외는 `raise` 문을 사용하여 발생시킵니다. 코드에서 `raise` 문은 다음으로 구성됩니다.

- `raise` 키워드
- `Exception()` 함수 호출
- `Exception()` 함수에 전달되는 유용한 오류 메시지가 포함된 문자열

```python
# raise 문: 사용자 지정 메시지로 예외를 수동으로 발생시킵니다.
raise Exception('This is the error message.')
```

```output
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    raise Exception('This is the error message.')
Exception: This is the error message.
```

<BaseQuiz id="cheatsheet-debugging-1" correct="B">
<template #question>
Python 에서 예외를 수동으로 발생시키는 데 사용되는 키워드는 무엇입니까?
</template>

<BaseQuizOption value="A">A. <code>throw</code></BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>raise</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>error</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>exception</code></BaseQuizOption>
<BaseQuizAnswer><code>raise</code> 키워드는 Python 에서 예외를 수동으로 발생시키는 데 사용됩니다. 내장 예외 또는 사용자 지정 예외를 발생시킬 수 있습니다.</BaseQuizAnswer>
</BaseQuiz>

일반적으로 예외를 처리하는 방법을 아는 것은 함수를 호출하는 코드이지 함수 자체가 아닙니다. 따라서 함수 내부에서는 `raise` 문을, 함수를 호출하는 코드에서는 `try` 및 `except` 문을 흔히 볼 수 있습니다.

```python
# 함수에서 예외 발생, 호출하는 코드에서 처리
def box_print(symbol, width, height):
    if len(symbol) != 1:
      raise Exception('Symbol must be a single character string.')
    if width <= 2:
      raise Exception('Width must be greater than 2.')
    if height <= 2:
      raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

# 함수 호출 시 예외 처리
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:  # 예외를 잡고 오류 메시지 출력
        print('An exception happened: ' + str(err))
```

```output
****
*  *
*  *
****
OOOOOOOOOOOOOOOOOOOO
O                  O
O                  O
O                  O
OOOOOOOOOOOOOOOOOOOO
An exception happened: Width must be greater than 2.
An exception happened: Symbol must be a single character string.
```

[예외 처리](/cheatsheet/exception-handling)에 대해 자세히 읽어보세요.

## 트레이스백을 문자열로 가져오기

`traceback`은 발생한 예외가 처리되지 않을 때 Python 이 표시하는 것입니다. 하지만 `traceback.format_exc()`를 호출하여 문자열로 얻을 수도 있습니다. 이 함수는 예외의 트레이스백 정보를 원하지만 `except` 문으로 예외를 우아하게 처리하고 싶을 때 유용합니다. 이 함수를 호출하기 전에 Python 의 `traceback` 모듈을 가져와야 합니다.

```python
# traceback.format_exc(): 로깅/디버깅을 위해 트레이스백을 문자열로 가져옵니다.
import traceback

try:
    raise Exception('This is the error message.')
except:
    with open('errorInfo.txt', 'w') as error_file:
        error_file.write(traceback.format_exc())  # 트레이스백을 파일에 씁니다.
    print('The traceback info was written to errorInfo.txt.')
```

```output
116
The traceback info was written to errorInfo.txt.
```

116 은 `write()` 메서드의 반환 값으로, 파일에 116 자가 기록되었음을 의미합니다. `traceback` 텍스트는 errorInfo.txt 에 기록되었습니다.

    Traceback (most recent call last):
      File "<pyshell#28>", line 2, in <module>
    Exception: This is the error message.

## 어설션 (Assertions)

어설션은 코드가 명백히 잘못된 작업을 수행하고 있지 않은지 확인하는 건전성 검사입니다. 이러한 건전성 검사는 `assert` 문을 통해 수행됩니다. 건전성 검사가 실패하면 `AssertionError` 예외가 발생합니다. 코드에서 `assert` 문은 다음으로 구성됩니다.

- `assert` 키워드
- 조건 (즉, `True` 또는 `False`로 평가되는 표현식)
- 쉼표
- 조건이 `False`일 때 표시할 `string`

```python
# assert 문: 조건을 확인하고, False 이면 AssertionError 를 발생시킵니다.
pod_bay_door_status = 'open'
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'  # 통과

pod_bay_door_status = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'  # AssertionError 발생
```

```output
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'
AssertionError: The pod bay doors need to be "open".
```

<BaseQuiz id="cheatsheet-debugging-2" correct="C">
<template #question>
<code>assert</code> 문이 실패하면 어떻게 됩니까?
</template>

<BaseQuizOption value="A">A. 프로그램이 계속 실행됩니다</BaseQuizOption>
<BaseQuizOption value="B">B. 경고가 출력됩니다</BaseQuizOption>
<BaseQuizOption value="C" correct>C. <code>AssertionError</code>가 발생하고 프로그램이 충돌해야 합니다</BaseQuizOption>
<BaseQuizOption value="D">D. 조건이 자동으로 수정됩니다</BaseQuizOption>
<BaseQuizAnswer><code>assert</code> 문이 실패하면 <code>AssertionError</code>가 발생합니다. 예외와 달리 assert 문은 try-except 로 처리해서는 안 됩니다. assert 가 실패하면 버그를 신속하게 찾는 데 도움이 되도록 프로그램이 충돌해야 합니다.</BaseQuizAnswer>
</BaseQuiz>

간단히 말해, assert 문은 "나는 이 조건이 참이라고 단언하며, 그렇지 않다면 프로그램 어딘가에 버그가 있는 것이다"라고 말합니다. 예외와 달리 코드는 try 및 except 로 assert 문을 처리해서는 안 됩니다. assert 가 실패하면 프로그램이 충돌해야 합니다. 이처럼 빠르게 실패함으로써 버그의 원래 원인과 버그를 처음 발견한 시점 사이의 시간을 단축할 수 있습니다. 이렇게 하면 버그를 유발하는 코드를 찾기 위해 확인해야 하는 코드 양이 줄어듭니다.

### 어설션 비활성화

Python 을 실행할 때 `-O` 옵션을 전달하여 어설션을 비활성화할 수 있습니다.

## 로깅 (Logging)

프로그램이 실행되는 동안 로그 메시지가 화면에 표시되도록 `logging` 모듈을 활성화하려면 프로그램 상단에 다음을 복사하십시오.

```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
```

<BaseQuiz id="cheatsheet-debugging-3" correct="A">
<template #question>
Python 에서 <code>logging</code> 모듈의 목적은 무엇입니까?
</template>

<BaseQuizOption value="A" correct>A. 디버깅 및 모니터링을 위해 프로그램 실행에 대한 정보를 기록하는 것</BaseQuizOption>
<BaseQuizOption value="B">B. 오류 발생을 방지하는 것</BaseQuizOption>
<BaseQuizOption value="C">C. 프로그램 실행 속도를 높이는 것</BaseQuizOption>
<BaseQuizOption value="D">D. 로그 메시지를 암호화하는 것</BaseQuizOption>
<BaseQuizAnswer><code>logging</code> 모듈을 사용하면 다양한 수준 (DEBUG, INFO, WARNING, ERROR, CRITICAL) 에서 프로그램 실행에 대한 정보를 기록할 수 있으며, 이는 디버깅 및 모니터링에 유용합니다.</BaseQuizAnswer>
</BaseQuiz>

숫자의 팩토리얼을 계산하는 함수를 작성했다고 가정해 봅시다. 수학에서 팩토리얼 4 는 1 × 2 × 3 × 4, 즉 24 입니다. 팩토리얼 7 은 1 × 2 × 3 × 4 × 5 × 6 × 7, 즉 5,040 입니다. 새 파일 편집기 창을 열고 다음 코드를 입력하십시오. 이 코드에는 버그가 있지만, 무엇이 잘못되고 있는지 파악하는 데 도움이 되도록 여러 로그 메시지도 입력할 것입니다. 프로그램을 factorialLog.py 로 저장합니다.

```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(0, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')
```

```output
2015-05-23 16:20:12,664 - DEBUG - Start of program
2015-05-23 16:20:12,664 - DEBUG - Start of factorial(5)
2015-05-23 16:20:12,665 - DEBUG - i is 0, total is 0
2015-05-23 16:20:12,668 - DEBUG - i is 1, total is 0
2015-05-23 16:20:12,670 - DEBUG - i is 2, total is 0
2015-05-23 16:20:12,673 - DEBUG - i is 3, total is 0
2015-05-23 16:20:12,675 - DEBUG - i is 4, total is 0
2015-05-23 16:20:12,678 - DEBUG - i is 5, total is 0
2015-05-23 16:20:12,680 - DEBUG - End of factorial(5)
0
2015-05-23 16:20:12,684 - DEBUG - End of program
```

## 로깅 수준 (Logging Levels)

로깅 수준은 로그 메시지를 중요도에 따라 분류하는 방법을 제공합니다. 중요도가 낮은 순서부터 높은 순서까지 다섯 가지 로깅 수준이 있으며, 표 10-1 에 설명되어 있습니다. 각 수준에서 메시지를 다른 로깅 함수를 사용하여 기록할 수 있습니다.

| 수준       | 로깅 함수            | 설명                                                                                                                           |
| :--------- | :------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| `DEBUG`    | `logging.debug()`    | 가장 낮은 수준. 작은 세부 사항에 사용됩니다. 일반적으로 문제 진단 시에만 이러한 메시지에 신경 씁니다.                          |
| `INFO`     | `logging.info()`     | 프로그램의 일반적인 이벤트에 대한 정보를 기록하거나 프로그램의 해당 지점에서 작동이 제대로 되고 있는지 확인하는 데 사용됩니다. |
| `WARNING`  | `logging.warning()`  | 프로그램 작동을 막지는 않지만 미래에 그럴 수 있는 잠재적인 문제를 나타내는 데 사용됩니다.                                      |
| `ERROR`    | `logging.error()`    | 프로그램이 무언가를 수행하지 못한 오류를 기록하는 데 사용됩니다.                                                               |
| `CRITICAL` | `logging.critical()` | 가장 높은 수준. 프로그램 실행을 완전히 중단했거나 중단하려고 하는 치명적인 오류를 나타내는 데 사용됩니다.                      |

<BaseQuiz id="cheatsheet-debugging-4" correct="D">
<template #question>
Python 에서 가장 낮은 로깅 수준은 무엇입니까?
</template>

<BaseQuizOption value="A">A. <code>INFO</code></BaseQuizOption>
<BaseQuizOption value="B">B. <code>WARNING</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>ERROR</code></BaseQuizOption>
<BaseQuizOption value="D" correct>D. <code>DEBUG</code></BaseQuizOption>
<BaseQuizAnswer>로깅 수준은 가장 낮은 수준부터 가장 높은 수준까지 <code>DEBUG</code>, <code>INFO</code>, <code>WARNING</code>, <code>ERROR</code>, <code>CRITICAL</code>입니다. <code>DEBUG</code>가 가장 낮은 수준이며 자세한 진단 정보에 사용됩니다.</BaseQuizAnswer>
</BaseQuiz>

## 로깅 비활성화

프로그램 디버깅을 마친 후에는 모든 로그 메시지가 화면을 어지럽히는 것을 원하지 않을 수 있습니다. `logging.disable()` 함수는 로깅 호출을 수동으로 제거하기 위해 프로그램으로 이동할 필요가 없도록 이를 비활성화합니다.

```python
import logging

logging.basicConfig(level=logging.INFO, format=' %(asctime)s -%(levelname)s - %(message)s')
logging.critical('Critical error! Critical error!')
```

```output
2015-05-22 11:10:48,054 - CRITICAL - Critical error! Critical error!
```

```python
logging.disable(logging.CRITICAL)
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')
```

## 파일에 로깅

로그 메시지를 화면에 표시하는 대신 텍스트 파일에 쓸 수 있습니다. `logging.basicConfig()` 함수는 다음과 같이 `filename` 키워드 인수를 사용합니다.

```python
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
```

<BaseQuiz id="cheatsheet-debugging-5" correct="B">
<template #question>
화면에 표시하는 대신 로그 메시지를 파일에 쓰려면 어떻게 해야 합니까?
</template>

<BaseQuizOption value="A">A. <code>logging.file()</code> 사용</BaseQuizOption>
<BaseQuizOption value="B" correct>B. <code>logging.basicConfig()</code>에 <code>filename</code> 매개변수 전달</BaseQuizOption>
<BaseQuizOption value="C">C. <code>logging.write()</code> 사용</BaseQuizOption>
<BaseQuizOption value="D">D. 로그는 항상 자동으로 파일에 기록됩니다</BaseQuizOption>
<BaseQuizAnswer>로그 메시지를 파일에 쓰려면 <code>logging.basicConfig()</code>에 <code>filename</code> 매개변수를 전달합니다. 이렇게 하면 모든 로그 메시지가 화면에 표시되는 대신 지정된 파일에 기록됩니다.</BaseQuizAnswer>
</BaseQuiz>

## 관련 링크

- <router-link to="/cheatsheet/exception-handling">예외 처리</router-link>
- <router-link to="/builtin/breakpoint">breakpoint()</router-link>
