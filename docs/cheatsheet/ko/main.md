---
title: '파이썬 메인 함수 - 파이썬 치트 시트'
description: '최상위 코드가 실행되는 범위를 나타냅니다. 모듈 이름은 표준 입력, 스크립트 또는 대화형 프롬프트에서 읽을 때 main 으로 설정됩니다.'
labUrl: 'https://labex.io/ko/labs/python-python-main-function-633661?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
메인 최상위 스크립트 환경
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## What is it

`__main__`은 최상위 코드가 실행되는 범위의 이름입니다.
모듈의 **이름**은 표준 입력, 스크립트 또는 대화형 프롬프트에서 읽을 때 `__main__`과 같게 설정됩니다.

모듈은 자신의 `__name__`을 확인하여 메인 범위에서 실행 중인지 여부를 확인할 수 있으며, 이를 통해 모듈 내에서 코드를 조건부로 실행하는 일반적인 관용구를 사용할 수 있습니다. 스크립트로 실행되거나 `python -m`으로 실행될 때는 실행되지만, 가져오기 (import) 될 때는 실행되지 않습니다.

```python
# __name__ == "__main__": 스크립트가 직접 실행되는지 확인 (가져오기 시 아님)
if __name__ == "__main__":  # 스크립트로 실행될 때 True, 가져오기 시 False
    # 스크립트로 실행될 때만 실행
    main()
```

패키지의 경우, **main**.py 모듈을 포함하여 동일한 효과를 얻을 수 있으며, 이 모듈의 내용은 해당 모듈이 -m 으로 실행될 때 실행됩니다.

예를 들어, 모듈로 사용되도록 설계된 스크립트를 개발하는 경우 다음과 같이 해야 합니다.

```python
# 예시: 함수는 가져올 수 있지만, 테스트 코드는 직접 실행될 때만 실행됨
def add(a, b):
    return a+b

if __name__ == "__main__":  # 파일이 직접 실행될 때만 실행됨, 가져오기 시 실행 안 됨
    add(3, 5)
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
파이썬 파일을 스크립트로 직접 실행할 때 <code>__name__</code>의 값은 무엇입니까?
</template>

<base-quiz-option value="A">A. 파일 이름</base-quiz-option>
<base-quiz-option value="B" correct>B. <code>"**main**"</code></base-quiz-option>
<base-quiz-option value="C">C. <code>None</code></base-quiz-option>
<base-quiz-option value="D">D. <code>True</code></base-quiz-option>
<base-quiz-answer value="B">파이썬 파일을 스크립트로 직접 실행하면 <code>**name**</code>은 <code>"**main**"</code>으로 설정됩니다. 파일이 모듈로 가져와지면 <code>**name**</code>은 모듈 이름으로 설정됩니다.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Advantages

1. 모든 파이썬 모듈에는 `__name__`이 정의되어 있으며, 이것이 `__main__`인 경우 사용자가 모듈을 독립적으로 실행하고 있음을 의미하며, 이에 따라 적절한 조치를 취할 수 있습니다.
2. 이 스크립트를 다른 스크립트에서 모듈로 가져오면 **이름**은 스크립트/모듈의 이름으로 설정됩니다.
3. 파이썬 파일은 재사용 가능한 모듈 또는 독립 실행형 프로그램 역할을 할 수 있습니다.
4. `if __name__ == "__main__":`은 파일이 직접 실행될 때만 특정 코드를 실행하고, 가져오기될 때는 실행하지 않도록 하는 데 사용됩니다.

<base-quiz>
<base-quiz-question correct="A">
<template #question>
<code>if __name__ == "__main__":</code>을 사용하는 주된 목적은 무엇입니까?
</template>

<base-quiz-option value="A" correct>A. 파일이 직접 실행될 때만 코드를 실행하고, 가져오기될 때는 실행하지 않음</base-quiz-option>
<base-quiz-option value="B">B. 파일이 가져와지는 것을 방지</base-quiz-option>
<base-quiz-option value="C">C. 파일 실행 속도를 높임</base-quiz-option>
<base-quiz-option value="D">D. 다른 모듈로부터 코드를 숨김</base-quiz-option>
<base-quiz-answer value="A"><code>if **name** == "**main**":</code> 관용구는 파이썬 파일이 재사용 가능한 모듈과 독립 실행형 프로그램 역할을 모두 수행할 수 있도록 합니다. 이 블록 안의 코드는 파일이 직접 실행될 때만 실행되며, 가져와질 때는 실행되지 않습니다.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Relevant links

- <router-link to="/cheatsheet/functions">Functions</router-link>
- <router-link to="/cheatsheet/packaging">Packaging</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Python projects with Poetry and VSCode. Part 1</router-link>
- <router-link to="/builtin/import">import()</router-link>
