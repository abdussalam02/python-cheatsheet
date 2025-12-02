---
title: 'Formatação de Strings Python - Guia Rápido Python'
description: 'Se você usa Python 3.6+, as f-strings são a maneira recomendada para formatar strings.'
labUrl: 'https://labex.io/pt/labs/python-python-string-formatting-633667?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Formatação de Strings em Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    Da <a href="https://docs.python.org/3/library/stdtypes.html?highlight=sprintf#printf-style-string-formatting">documentação do Python 3</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    As operações de formatação descritas aqui (<b>operador %</b>) exibem uma variedade de peculiaridades que levam a um número de erros comuns [...]. Usar os mais novos <a href="#formatted-string-literals-or-f-strings">literais de string formatados</a> [...] ajuda a evitar esses erros. Essas alternativas também fornecem abordagens mais poderosas, flexíveis e extensíveis para formatar texto.
  </base-disclaimer-content>
</base-disclaimer>

## operador %

<base-warning>
  <base-warning-title>
    Prefira Literais de String
  </base-warning-title>
  <base-warning-content>
    Para código novo, o uso de <a href="#strformat">str.format</a>, ou <a href="#formatted-string-literals-or-f-strings">literais de string formatados</a> (Python 3.6+) em vez do operador <code>%</code> é fortemente recomendado.
  </base-warning-content>
</base-warning>

```python
# operador %: formatação de string estilo antigo (não recomendado para código novo)
name = 'Pete'
'Hello %s' % name  # %s = placeholder de string
```

```output
"Hello Pete"
```

Podemos usar o especificador de formato `%d` para converter um valor int em uma string:

```python
num = 5
'I have %d apples' % num
```

```output
"I have 5 apples"
```

## str.format

O Python 3 introduziu uma nova maneira de fazer formatação de strings que foi posteriormente retroportada para o Python 2.7. Isso torna a sintaxe para formatação de strings mais regular.

```python
# método str.format(): formatação de string moderna (Python 2.7+)
name = 'John'
age = 20

"Hello I'm {}, my age is {}".format(name, age)  # {} = placeholder
```

```output
"Hello I'm John, my age is 20"
```

```python
"Hello I'm {0}, my age is {1}".format(name, age)
```

```output
"Hello I'm John, my age is 20"
```

## Literais de String Formatados ou f-Strings

Se você estiver usando Python 3.6+, as `f-Strings` de string são a maneira recomendada de formatar strings.

<base-disclaimer>
  <base-disclaimer-title>
    Da <a href="https://docs.python.org/3/reference/lexical_analysis.html#f-strings">documentação do Python 3</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Um literal de string formatado ou f-string é um literal de string que é prefixado com <code>f</code> ou <code>F</code>. Essas strings podem conter campos de substituição, que são expressões delimitadas por chaves {}. Embora outros literais de string sempre tenham um valor constante, as strings formatadas são realmente expressões avaliadas em tempo de execução.
  </base-disclaimer-content>
</base-disclaimer>

```python
# f-string: maneira recomendada de formatar strings (Python 3.6+)
name = 'Elizabeth'
f'Hello {name}!'  # prefixo f permite expressões em {}
```

```output
'Hello Elizabeth!'
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-string-formatting-1">
<template #question>
Qual prefixo é usado para f-strings em Python?
</template>

<base-quiz-option value="A">A. <code>fmt</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>f</code> ou <code>F</code></base-quiz-option>
<base-quiz-option value="C">C. <code>format</code></base-quiz-option>
<base-quiz-option value="D">D. <code>str</code></base-quiz-option>
<base-quiz-answer value="B">As f-strings são prefixadas com <code>f</code> ou <code>F</code> antes da aspa de abertura. Elas permitem incorporar expressões dentro de chaves <code>{}</code>.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

É até possível fazer aritmética em linha com isso:

```python
# f-strings suportam expressões: podem incluir cálculos dentro de {}
a = 5
b = 10
f'Five plus ten is {a + b} and not {2 * (a + b)}.'  # Avalia expressões
```

```output
'Five plus ten is 15 and not 30.'
```

### f-Strings de Múltiplas Linhas

```python
name = 'Robert'
messages = 12
(
f'Hi, {name}. '
f'You have {messages} unread messages'
)
```

```output
'Hi, Robert. You have 12 unread messages'
```

### O especificador =

Isso imprimirá a expressão e seu valor:

```python
# especificador =: imprime o nome da variável e o valor (Python 3.8+)
from datetime import datetime
now = datetime.now().strftime("%b/%d/%Y - %H:%M:%S")
f'date and time: {now=}'  # Imprime "now='Nov/14/2022 - 20:50:01'"
```

```output
"date and time: now='Nov/14/2022 - 20:50:01'"
```

### Adicionando espaços ou caracteres

```python
name = 'Robert'
f"{name.upper() = :-^20}"
```

```output
'name.upper() = -------ROBERT-------'
```

```python
f"{name.upper() = :^20}"
```

```output
'name.upper() =        ROBERT       '
```

```python
f"{name.upper() = :20}"
```

```output
'name.upper() = ROBERT              '
```

## Formatação de Dígitos

Adicionando separador de milhares

```python
a = 10000000
f"{a:,}"
```

```output
'10,000,000'
```

Arredondamento

```python
a = 3.1415926
f"{a:.2f}"
```

```output
'3.14'
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-string-formatting-2">
<template #question>
O que <code>f"{a:.2f}"</code> faz?
</template>

<base-quiz-option value="A">A. Arredonda o número para o inteiro mais próximo</base-quiz-option>
<base-quiz-option value="B">B. Formata como uma porcentagem</base-quiz-option>
<base-quiz-option value="C" correct>C. Formata o número como um float com 2 casas decimais</base-quiz-option>
<base-quiz-option value="D">D. Converte para notação científica</base-quiz-option>
<base-quiz-answer value="C">O especificador de formato <code>:.2f</code> formata um número como um float com exatamente 2 casas decimais. O <code>.2</code> especifica a precisão, e <code>f</code> significa formato float.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Exibindo como Porcentagem

```python
a = 0.816562
f"{a:.2%}"
```

```output
'81.66%'
```

### Tabela de formatação de números

| Número     | Formato | Saída     | Descrição                                                         |
| ---------- | ------- | --------- | ----------------------------------------------------------------- |
| 3.1415926  | {:.2f}  | 3.14      | Formata float com 2 casas decimais                                |
| 3.1415926  | {:+.2f} | +3.14     | Formata float com 2 casas decimais e sinal                        |
| -1         | {:+.2f} | -1.00     | Formata float com 2 casas decimais e sinal                        |
| 2.71828    | {:.0f}  | 3         | Formata float sem casas decimais                                  |
| 4          | {:0>2d} | 04        | Preenche o número com zeros (preenchimento à esquerda, largura 2) |
| 4          | {:x<4d} | 4xxx      | Preenche o número com x's (preenchimento à direita, largura 4)    |
| 10         | {:x<4d} | 10xx      | Preenche o número com x's (preenchimento à direita, largura 4)    |
| 1000000    | {:,}    | 1,000,000 | Formato de número com separador de vírgula                        |
| 0.35       | {:.2%}  | 35.00%    | Formata porcentagem                                               |
| 1000000000 | {:.2e}  | 1.00e+09  | Notação de expoente                                               |
| 11         | {:11d}  | 11        | Alinhado à direita (padrão, largura 10)                           |
| 11         | {:<11d} | 11        | Alinhado à esquerda (largura 10)                                  |
| 11         | {:^11d} | 11        | Alinhado ao centro (largura 10)                                   |

## Template Strings

Um mecanismo mais simples e menos poderoso, mas é recomendado ao lidar com strings geradas por usuários. Devido à sua menor complexidade, as template strings são uma escolha mais segura.

```python
from string import Template
name = 'Elizabeth'
t = Template('Hey $name!')
t.substitute(name=name)
```

```output
'Hey Elizabeth!'
```

## Links Relevantes

- <router-link to="/cheatsheet/manipulating-strings">Manipulando Strings</router-link>
- <router-link to="/blog/python-data-types">Post do Blog sobre Tipos de Dados Python</router-link>
- <router-link to="/builtin/format">format()</router-link>
- <router-link to="/builtin/print">print()</router-link>
- <router-link to="/builtin/str">str()</router-link>
- <router-link to="/builtin/repr">repr()</router-link>
- <router-link to="/builtin/ascii">ascii()</router-link>
