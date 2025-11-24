---
title: '파이썬 JSON 및 YAML - 파이썬 치트 시트'
description: 'JSON 은 JavaScript Object Notation 의 약자로, 데이터를 저장하고 전송하기 위한 경량 형식입니다. JSON 은 서버에서 웹 페이지로 데이터를 보낼 때 자주 사용됩니다.'
labUrl: 'https://labex.io/ko/labs/python-python-json-and-yaml-633659?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
JSON 및 YAML
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## JSON

JSON 은 JavaScript Object Notation 의 약자로, 데이터를 저장하고 전송하기 위한 경량 형식입니다. JSON 은 종종 서버에서 웹 페이지로 데이터가 전송될 때 사용됩니다.

```python
# JSON 파일 읽기: json.load() 는 파일 객체에서 JSON 을 구문 분석합니다
import json
with open("filename.json", "r") as f:  # 읽기 모드로 파일 열기
    content = json.load(f)  # JSON 을 구문 분석하여 Python dict/list 반환
```

다음 내용으로 JSON 파일을 작성합니다:

```python
# JSON 파일 쓰기: json.dump() 는 Python 객체를 JSON 으로 씁니다
import json

content = {"name": "Joe", "age": 20}
with open("filename.json", "w") as f:  # 쓰기 모드로 파일 열기
    json.dump(content, f, indent=2)  # 2 칸 들여쓰기로 JSON 쓰기
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Python 딕셔너리를 JSON 파일에 쓰는 데 사용되는 함수는 무엇입니까?
</template>

<base-quiz-option value="A">A. <code>json.write()</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>json.dump()</code></base-quiz-option>
<base-quiz-option value="C">C. <code>json.save()</code></base-quiz-option>
<base-quiz-option value="D">D. <code>json.export()</code></base-quiz-option>
<base-quiz-answer value="B"><code>json.dump()</code> 함수는 Python 객체 (딕셔너리 등) 를 JSON 파일에 씁니다. <code>json.load()</code>는 JSON 파일을 읽는 데 사용됩니다.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## YAML

JSON 과 비교할 때, YAML 은 훨씬 더 나은 인간 유지 관리성을 허용하며 주석을 추가할 수 있는 기능을 제공합니다. 사람이 편집해야 하는 구성 파일에 편리한 선택입니다.

YAML 파일에 접근할 수 있게 해주는 두 가지 주요 라이브러리가 있습니다:

- [PyYaml](https://pypi.python.org/pypi/PyYAML)
- [Ruamel.yaml](https://pypi.python.org/pypi/ruamel.yaml)

가상 환경에서 `pip install`을 사용하여 설치하십시오.

첫 번째 라이브러리가 사용하기는 더 쉽지만, 두 번째 라이브러리인 Ruamel 은 YAML 사양을 훨씬 더 잘 구현하며 예를 들어 주석을 변경하지 않고 YAML 내용을 수정할 수 있도록 합니다.

다음과 같이 YAML 파일을 엽니다:

```python
# ruamel.yaml 라이브러리를 사용하여 YAML 파일 읽기
from ruamel.yaml import YAML

with open("filename.yaml") as f:
    yaml=YAML()  # YAML 파서 인스턴스 생성
    yaml.load(f)  # YAML 을 구문 분석하여 Python dict/list 반환
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
JSON 에 비해 YAML 의 장점은 무엇입니까?
</template>

<base-quiz-option value="A">A. YAML 파일이 더 작습니다</base-quiz-option>
<base-quiz-option value="B">B. YAML 구문 분석이 더 빠릅니다</base-quiz-option>
<base-quiz-option value="C" correct>C. YAML 은 주석을 허용하며 인간이 읽기 쉽습니다</base-quiz-option>
<base-quiz-option value="D">D. YAML 은 Python 에 내장되어 있습니다</base-quiz-option>
<base-quiz-answer value="C">YAML 은 JSON 보다 주석을 허용하며 인간이 읽기 쉽기 때문에 사람이 편집해야 하는 구성 파일에 편리한 선택입니다.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Anyconfig

[Anyconfig](https://pypi.python.org/pypi/anyconfig)는 기본 구성 파일 형식을 완전히 추상화할 수 있게 해주는 매우 유용한 패키지입니다. JSON, YAML, TOML 등에서 Python 딕셔너리를 로드할 수 있습니다.

다음과 같이 설치하십시오:

```bash
pip install anyconfig
```

사용법:

```python
# anyconfig: 다양한 형식 (JSON, YAML, TOML 등) 의 구성 파일 로드
import anyconfig
conf1 = anyconfig.load("/path/to/foo/conf.d/a.yml")  # 형식을 자동 감지
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
anyconfig 라이브러리는 무엇을 할 수 있게 해줍니까?
</template>

<base-quiz-option value="A" correct>A. 형식을 지정하지 않고 다양한 형식 (JSON, YAML, TOML) 의 구성 파일을 로드</base-quiz-option>
<base-quiz-option value="B">B. 다른 구성 형식 간 변환</base-quiz-option>
<base-quiz-option value="C">C. 구성 파일 구문 검증</base-quiz-option>
<base-quiz-option value="D">D. 구성 파일 암호화</base-quiz-option>
<base-quiz-answer value="A">anyconfig 라이브러리는 기본 구성 파일 형식을 추상화하여 어떤 형식이 사용되는지 알 필요 없이 JSON, YAML, TOML 등에서 Python 딕셔너리를 로드할 수 있게 해줍니다.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 관련 링크

- <router-link to="/cheatsheet/reading-and-writing-files">파일 읽기 및 쓰기</router-link>
- <router-link to="/cheatsheet/dictionaries">Python 딕셔너리</router-link>
- <router-link to="/modules/json-module">json 모듈</router-link>
- <router-link to="/blog/python-pathlib-essentials">모든 개발자가 알아야 할 10 가지 필수 파일 시스템 작업</router-link>
- <router-link to="/builtin/open">open()</router-link>
- <router-link to="/builtin/dict">dict()</router-link>
