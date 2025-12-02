---
title: '파이썬 패키징 - 파이썬 치트시트'
description: 'setup.py 및 pyproject.toml 을 사용하여 파이썬 프로젝트를 패키징하는 방법을 알아보세요. PEP-517, PEP-518, PEP-660 사양을 통한 최신 파이썬 패키징 접근 방식을 이해합니다.'
labUrl: 'https://labex.io/ko/labs/python-python-setup-py-633666?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python 패키징
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-warning>
  <base-warning-title>
    '논란의 여지가 있는' 의견
  </base-warning-title>
  <base-warning-content>
    Python 패키지를 패키징하고 배포하기 위해 <code>setup.py</code>를 사용하는 것은 때때로 매우 어려울 수 있습니다. <a target="_blank" href="https://python-poetry.org/">Poetry</a> 및 <a target="_blank" href="https://docs.astral.sh/uv/">UV</a>와 같은 최신 도구는 패키징을 <b>훨씬 더 쉽게</b> 만들 뿐만 아니라 종속성을 매우 편리하게 관리할 수 있도록 도와줍니다. 특히 UV 는 기존 도구보다 10~100 배 빠르다는 점이 주목할 만합니다.
  </base-warning-content>
</base-warning>

Poetry 에 대한 추가 정보가 필요하면 다음 문서를 읽어보십시오.

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Poetry 및 VSCode 를 사용한 Python 프로젝트. 1 부</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Poetry 및 VSCode 를 사용한 Python 프로젝트. 2 부</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Poetry 및 VSCode 를 사용한 Python 프로젝트. 3 부</router-link>

매우 빠른 Python 패키지 관리자인 UV 에 대한 포괄적인 가이드는 다음을 참조하십시오. <router-link to="/blog/python-uv-package-manager">UV: 초고속 Python 패키지 관리자</router-link>.

## 소개

Python 패키징은 Python 프로젝트를 배포 및 설치할 수 있도록 준비하는 과정입니다. 주요 접근 방식은 두 가지가 있습니다. 전통적인 <code>setup.py</code> 방식과 최신 <code>pyproject.toml</code> 방식 (PEP-517, PEP-518 및 PEP-660 에 정의됨) 입니다.

프로젝트 구조 관리에 필수적인 파일 및 디렉터리 경로 처리 방법에 대한 포괄적인 가이드는 <router-link to="/cheatsheet/file-directory-path">파일 및 디렉터리 경로</router-link> 페이지를 참조하십시오.

## 전통적인 접근 방식: setup.py

<code>setup.py</code> 파일은 전통적인 Python 프로젝트의 핵심입니다. 이 파일은 프로젝트에 대한 모든 메타데이터를 설명합니다. 프로젝트를 설명하는 풍부한 메타데이터 세트를 제공하기 위해 프로젝트에 추가할 수 있는 필드가 꽤 많습니다. 그러나 이름, 버전 및 패키지라는 세 가지 필수 필드만 있습니다. 이름 필드는 Python Package Index(PyPI) 에 패키지를 게시하려는 경우 고유해야 합니다. 버전 필드는 프로젝트의 다른 릴리스를 추적합니다. 패키지 필드는 프로젝트 내에서 Python 소스 코드를 배치한 위치를 설명합니다.

이를 통해 Python 패키지를 쉽게 설치할 수 있습니다. 종종 다음을 작성하는 것으로 충분합니다.

```bash
python setup.py install
```

그러면 모듈이 자체적으로 설치됩니다.

### 예시: setup.py

초기 setup.py 에는 라이선스에 대한 정보도 포함되며, long_description 필드에 README.txt 파일을 재사용합니다. 모양은 다음과 같습니다.

```python
# setup.py: 배포를 위한 패키지 메타데이터 정의
from distutils.core import setup
setup(
   name='pythonCheatsheet',  # 패키지 이름 (PyPI 에서 고유해야 함)
   version='0.1',  # 버전 번호
   packages=['pipenv',],  # 포함할 패키지 목록
   license='MIT',  # 라이선스 유형
   long_description=open('README.txt').read(),  # 파일에서 설명 읽기
)
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-packaging-1">
<template #question>
<code>setup.py</code> 파일에서 요구되는 세 가지 필드는 무엇입니까?
</template>

<base-quiz-option value="A">A. name, author, license</base-quiz-option>
<base-quiz-option value="B">B. name, description, packages</base-quiz-option>
<base-quiz-option value="C" correct>C. name, version, packages</base-quiz-option>
<base-quiz-option value="D">D. name, version, license</base-quiz-option>
<base-quiz-answer value="C"><code>setup.py</code>의 세 가지 필수 필드는 <code>name</code>(패키지 이름, PyPI 에서 고유해야 함), <code>version</code>(릴리스 추적) 및 <code>packages</code>(Python 소스 코드가 위치한 곳 설명) 입니다.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 최신 접근 방식: pyproject.toml

<code>pyproject.toml</code> 파일은 Python 프로젝트 구성을 위한 최신 표준입니다 (PEP-517, PEP-518, PEP-660). 이 파일은 빌드 시스템 요구 사항과 프로젝트 메타데이터를 단일의 선언적 파일 형식으로 지정하는 통합된 방법을 제공합니다.

### pyproject.toml 의 이점

- **선언적**: 모든 프로젝트 메타데이터가 한 곳에 위치
- **빌드 시스템 독립적**: setuptools, poetry, flit 및 기타 빌드 백엔드와 함께 작동
- **코드 실행 없음**: setup.py 보다 안전하고 예측 가능함
- **표준화됨**: 더 나은 도구 지원을 위해 PEP 표준 준수

### 예시: pyproject.toml

setuptools 를 사용하는 기본 <code>pyproject.toml</code> 예시는 다음과 같습니다.

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "pythonCheatsheet"
version = "0.1"
description = "A Python cheatsheet package"
readme = "README.txt"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=22.0",
]
```

### pyproject.toml 에서 설치하기

<code>pyproject.toml</code>을 사용하면 pip 을 사용하여 패키지를 설치할 수 있습니다.

```bash
pip install .
```

또는 편집 가능한 모드에서는 다음과 같습니다.

```bash
pip install -e .
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-packaging-2">
<template #question>
<code>pyproject.toml</code>이 <code>setup.py</code>보다 갖는 주요 이점은 무엇입니까?
</template>

<base-quiz-option value="A">A. 실행 속도가 더 빠릅니다</base-quiz-option>
<base-quiz-option value="B" correct>B. 선언적이며, 더 안전하고 (코드 실행 없음), PEP 표준을 따릅니다</base-quiz-option>
<base-quiz-option value="C">C. 구성이 덜 필요합니다</base-quiz-option>
<base-quiz-option value="D">D. Python 3.10 이상에서만 작동합니다</base-quiz-option>
<base-quiz-answer value="B"><code>pyproject.toml</code> 접근 방식은 선언적이며 (모든 메타데이터가 한 곳에 위치), <code>setup.py</code>처럼 코드를 실행하지 않으므로 더 안전하고, 더 나은 도구 지원을 위해 PEP 표준 (PEP-517, PEP-518, PEP-660) 을 따릅니다.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 올바른 접근 방식 선택

- **`setup.py` 사용**: 레거시 프로젝트를 다루거나 세밀한 제어가 필요한 경우
- **`pyproject.toml` 사용**: 새 프로젝트의 경우 (권장), 최신 표준이며 더 나은 도구 지원을 제공합니다.

추가 정보를 보려면 [공식 문서](http://docs.python.org/3.11/install/index.html)를 방문하십시오.

## 관련 링크

- <router-link to="/cheatsheet/virtual-environments">가상 환경</router-link>
- <router-link to="/cheatsheet/file-directory-path">파일 및 디렉터리 경로</router-link>
- <router-link to="/blog/python-uv-package-manager">UV: 초고속 Python 패키지 관리자</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Poetry 및 VSCode 를 사용한 Python 프로젝트. 1 부</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Poetry 및 VSCode 를 사용한 Python 프로젝트. 2 부</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Poetry 및 VSCode 를 사용한 Python 프로젝트. 3 부</router-link>
- <router-link to="/builtin/import">import()</router-link>
