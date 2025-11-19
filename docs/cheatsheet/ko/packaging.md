---
title: 'Python Packaging - Python 치트 시트'
description: 'setup.py 및 pyproject.toml을 사용하여 Python 프로젝트를 패키징하는 방법을 배웁니다. PEP-517, PEP-518 및 PEP-660 사양을 사용한 Python 패키징의 현대적인 접근 방식을 이해합니다.'
labUrl: 'https://labex.io/ko/labs/python-python-setup-py-633666?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python Packaging
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-warning>
  <base-warning-title>
    '논란의 여지가 있는' 의견
  </base-warning-title>
  <base-warning-content>
    `setup.py`를 사용하여 Python 패키지를 패키징하고 배포하는 것은 때때로 매우 까다로울 수 있습니다. <a target="_blank" href="https://python-poetry.org/">Poetry</a> 및 <a target="_blank" href="https://docs.astral.sh/uv/">UV</a>와 같은 최신 도구는 패키징을 훨씬 더 쉽게 만들 뿐만 아니라 종속성을 매우 편리하게 관리할 수 있도록 도와줍니다. 특히 UV 는 기존 도구보다 10~100 배 빠르다는 점이 주목할 만합니다.
  </base-warning-content>
</base-warning>

Poetry 에 대한 자세한 정보를 원하시면 다음 문서를 읽어보실 수 있습니다.

- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Poetry 및 VSCode 를 사용한 Python 프로젝트. 파트 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Poetry 및 VSCode 를 사용한 Python 프로젝트. 파트 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Poetry 및 VSCode 를 사용한 Python 프로젝트. 파트 3</router-link>

매우 빠른 Python 패키지 관리자인 UV 에 대한 포괄적인 가이드는 다음을 참조하십시오: <router-link to="/blog/python-uv-package-manager">UV: 초고속 Python 패키지 관리자</router-link>.

## 소개

Python 패키징은 Python 프로젝트를 배포 및 설치용으로 준비하는 프로세스입니다. 두 가지 주요 접근 방식이 있습니다: 전통적인 `setup.py` 방법과 현대적인 `pyproject.toml` 접근 방식 (PEP-517, PEP-518 및 PEP-660에 정의됨).

프로젝트 구조 관리에 필수적인 파일 및 디렉터리 경로 처리 방법에 대한 포괄적인 가이드는 <router-link to="/cheatsheet/file-directory-path">파일 및 디렉터리 경로</router-link> 페이지를 참조하십시오.

## 전통적인 접근 방식: setup.py

`setup.py` 파일은 전통적인 Python 프로젝트의 핵심입니다. 프로젝트에 대한 모든 메타데이터를 설명합니다. 프로젝트에 풍부한 메타데이터 세트를 제공하기 위해 추가할 수 있는 필드가 꽤 많습니다. 하지만 필수 필드는 name, version, packages 세 가지뿐입니다. name 필드는 Python 패키지 인덱스 (PyPI) 에 패키지를 게시하려는 경우 고유해야 합니다. version 필드는 프로젝트의 다른 릴리스를 추적합니다. package 필드는 프로젝트 내에서 Python 소스 코드를 어디에 두었는지 설명합니다.

이를 통해 Python 패키지를 쉽게 설치할 수 있습니다. 종종 다음을 작성하는 것만으로 충분합니다.

```bash
python setup.py install
```

그러면 모듈이 자체적으로 설치됩니다.

### 예시: setup.py

초기 setup.py 는 라이선스에 대한 정보도 포함하며, long_description 필드에 README.txt 파일을 재사용할 것입니다. 이것은 다음과 같이 보일 것입니다.

```python
# setup.py: define package metadata for distribution
from distutils.core import setup
setup(
   name='pythonCheatsheet',  # Package name (must be unique on PyPI)
   version='0.1',  # Version number
   packages=['pipenv',],  # List of packages to include
   license='MIT',  # License type
   long_description=open('README.txt').read(),  # Read description from file
)
```

## 현대적인 접근 방식: pyproject.toml

`pyproject.toml` 파일은 Python 프로젝트 구성의 현대적인 표준입니다 (PEP-517, PEP-518, PEP-660). 단일 선언적 파일 형식으로 빌드 시스템 요구 사항 및 프로젝트 메타데이터를 지정하는 통합된 방법을 제공합니다.

### pyproject.toml 의 이점

- **선언적**: 모든 프로젝트 메타데이터를 한 곳에
- **빌드 시스템 독립적**: setuptools, poetry, flit 및 기타 빌드 백엔드와 함께 작동
- **코드 실행 없음**: setup.py 보다 안전하고 예측 가능
- **표준화**: 더 나은 도구 지원을 위해 PEP 표준 준수

### 예시: pyproject.toml

setuptools 를 사용한 기본 `pyproject.toml` 예제는 다음과 같습니다:

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "pythonCheatsheet"
version = "0.1"
description = "Python 치트 시트 패키지"
readme = "README.txt"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "귀하의 이름", email = "your.email@example.com"}
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

### pyproject.toml 에서 설치

`pyproject.toml` 을 사용하면 pip 를 사용하여 패키지를 설치할 수 있습니다:

```bash
pip install .
```

또는 편집 가능한 모드에서:

```bash
pip install -e .
```

## 올바른 접근 방식 선택

- **`setup.py` 사용**: 레거시 프로젝트를 작업하거나 세밀한 제어가 필요한 경우
- **`pyproject.toml` 사용**: 새 프로젝트의 경우 (권장), 현대적인 표준이며 더 나은 도구 지원을 제공합니다

더 많은 정보를 원하시면 [공식 문서](http://docs.python.org/3.11/install/index.html)를 방문하십시오.

## 관련 링크

- <router-link to="/cheatsheet/virtual-environments">가상 환경</router-link>
- <router-link to="/cheatsheet/file-directory-path">파일 및 디렉터리 경로</router-link>
- <router-link to="/blog/python-uv-package-manager">UV: 초고속 Python 패키지 관리자</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Poetry 및 VSCode 를 사용한 Python 프로젝트. 파트 1</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">Poetry 및 VSCode 를 사용한 Python 프로젝트. 파트 2</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-3">Poetry 및 VSCode 를 사용한 Python 프로젝트. 파트 3</router-link>
- <router-link to="/builtin/import">import()</router-link>

