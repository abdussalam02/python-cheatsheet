---
title: 'Tratamento de Exceções em Python - Guia Rápido Python'
description: 'Em Python, o tratamento de exceções é o processo de resposta à ocorrência de exceções.'
labUrl: 'https://labex.io/pt/labs/python-python-exception-handling-633656?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Tratamento de Exceções em Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikipedia.org/wiki/Exception_handling">Tratamento de Exceções</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Em computação e programação de computadores, o tratamento de exceções é o processo de responder à ocorrência de exceções – condições anômalas ou excepcionais que requerem processamento especial.
  </base-disclaimer-content>
</base-disclaimer>

Python tem muitas [exceções embutidas](https://docs.python.org/3/library/exceptions.html) que são levantadas quando um programa encontra um erro, e a maioria das bibliotecas externas, como a popular [Requests](https://requests.readthedocs.io/en/latest), inclui suas próprias [exceções personalizadas](https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions) com as quais precisaremos lidar.

## Tratamento básico de exceções

Você não pode dividir por zero, isso é uma verdade matemática, e se você tentar fazer isso em Python, o interpretador levantará a exceção embutida [ZeroDivisionError](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError):

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

Digamos que não queremos que nosso programa pare sua execução ou mostre ao usuário uma saída que ele não entenderá. Se quisermos imprimir uma mensagem útil e clara, então precisamos **_tratar_** a exceção com as palavras-chave `try` e `except`:

```python
# try-except: trata exceções graciosamente
def divide(dividend , divisor):
    try:  # Tenta executar este código
        print(dividend / divisor)
    except ZeroDivisionError:  # Captura o tipo de exceção específico
        print('Você não pode dividir por 0')

divide(dividend=10, divisor=5)
```

```output
2
```

```python
divide(dividend=10, divisor=0)
```

```output
Você não pode dividir por 0
```

<BaseQuiz id="cheatsheet-exception-handling-1" correct="A">
<template #question>
Quais palavras-chave são usadas para tratar exceções em Python?
</template>

<BaseQuizOption value="A" correct>A. <code>try</code> e <code>except</code></BaseQuizOption>
<BaseQuizOption value="B">B. <code>catch</code> e <code>handle</code></BaseQuizOption>
<BaseQuizOption value="C">C. <code>error</code> e <code>rescue</code></BaseQuizOption>
<BaseQuizOption value="D">D. <code>if</code> e <code>else</code></BaseQuizOption>
<BaseQuizAnswer>Python usa <code>try</code> para marcar o código que pode levantar uma exceção, e <code>except</code> para tratar exceções específicas que ocorrem.</BaseQuizAnswer>
</BaseQuiz>

## Tratamento de Múltiplas exceções usando um bloco de exceção

Você também pode tratar múltiplas exceções em uma única linha como a seguinte, sem a necessidade de criar múltiplos blocos de exceção.

```python
# Trata múltiplas exceções em um único bloco except
def divide(dividend , divisor):
    try:
        if (dividend == 10):
          var = 'str' + 1  # Isso levantará TypeError
        else:
          print(dividend / divisor)
    except (ZeroDivisionError, TypeError) as error:  # Captura múltiplos tipos de exceção
        print(error)  # Imprime a mensagem de erro

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

<BaseQuiz id="cheatsheet-exception-handling-2" correct="B">
<template #question>
Você pode tratar múltiplos tipos de exceção em um único bloco <code>except</code>?
</template>

<BaseQuizOption value="A">A. Não, você deve usar blocos <code>except</code> separados para cada tipo de exceção</BaseQuizOption>
<BaseQuizOption value="B" correct>B. Sim, colocando-os em uma tupla como <code>except (Exception1, Exception2)</code></BaseQuizOption>
<BaseQuizOption value="C">C. Sim, mas apenas se estiverem relacionados</BaseQuizOption>
<BaseQuizOption value="D">D. Não, Python não suporta isso</BaseQuizOption>
<BaseQuizAnswer>Você pode tratar múltiplos tipos de exceção em um único bloco <code>except</code> colocando-os em uma tupla: <code>except (ZeroDivisionError, TypeError) as error:</code></BaseQuizAnswer>
</BaseQuiz>

## Código Finally no tratamento de exceções

O código dentro da seção `finally` é sempre executado, independentemente de uma exceção ter sido levantada ou não:

```python
# Bloco finally: sempre executa independentemente de exceções
def divide(dividend , divisor):
    try:
        print(dividend / divisor)
    except ZeroDivisionError:
        print('Você não pode dividir por 0')
    finally:  # Sempre executa, mesmo se a exceção ocorrer
        print('Execução finalizada')

divide(dividend=10, divisor=5)
```

```output
2.0
Execução finalizada
```

```python
divide(dividend=10, divisor=0)
```

```output
Você não pode dividir por 0
Execução finalizada
```

<BaseQuiz id="cheatsheet-exception-handling-3" correct="C">
<template #question>
Quando o bloco <code>finally</code> é executado?
</template>

<BaseQuizOption value="A">A. Apenas quando uma exceção ocorre</BaseQuizOption>
<BaseQuizOption value="B">B. Apenas quando nenhuma exceção ocorre</BaseQuizOption>
<BaseQuizOption value="C" correct>C. Sempre, independentemente de uma exceção ter ocorrido ou não</BaseQuizOption>
<BaseQuizOption value="D">D. Nunca</BaseQuizOption>
<BaseQuizAnswer>O bloco <code>finally</code> sempre é executado, quer uma exceção tenha ocorrido ou não. É útil para código de limpeza que deve ser executado independentemente do resultado.</BaseQuizAnswer>
</BaseQuiz>

## Exceções Personalizadas

Exceções personalizadas são inicializadas criando uma `class` que herda da classe base `Exception` do Python, e são levantadas usando a palavra-chave `raise`:

```python
# Exceção personalizada: criada herdando da classe Exception
class MyCustomException(Exception):
    pass

raise MyCustomException  # Levanta a exceção personalizada
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyCustomException
```

Para declarar uma mensagem de exceção personalizada, você pode passá-la como um parâmetro:

```python
class MyCustomException(Exception):
    pass

raise MyCustomException('Uma mensagem personalizada para minha exceção personalizada')
```

```output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyCustomException: Uma mensagem personalizada para minha exceção personalizada
```

Tratar uma exceção personalizada é o mesmo que qualquer outra:

```python
try:
    raise MyCustomException('Uma mensagem personalizada para minha exceção personalizada')
except MyCustomException:
    print('Minha exceção personalizada foi levantada')
```

```output
Minha exceção personalizada foi levantada
```

<BaseQuiz id="cheatsheet-exception-handling-4" correct="A">
<template #question>
Como você cria uma exceção personalizada em Python?
</template>

<BaseQuizOption value="A" correct>A. Criando uma classe que herda da classe <code>Exception</code></BaseQuizOption>
<BaseQuizOption value="B">B. Usando o decorador <code>@exception</code></BaseQuizOption>
<BaseQuizOption value="C">C. Chamando <code>Exception.create()</code></BaseQuizOption>
<BaseQuizOption value="D">D. Importando-a de um módulo especial</BaseQuizOption>
<BaseQuizAnswer>Exceções personalizadas são criadas definindo uma classe que herda da classe base <code>Exception</code>. Você pode então levantá-las e tratá-las como exceções embutidas.</BaseQuizAnswer>
</BaseQuiz>

## Links relevantes

- <router-link to="/cheatsheet/control-flow">Fluxo de Controle</router-link>
- <router-link to="/builtin/breakpoint">breakpoint()</router-link>
- <router-link to="/builtin/isinstance">isinstance()</router-link>
- <router-link to="/builtin/issubclass">issubclass()</router-link>
