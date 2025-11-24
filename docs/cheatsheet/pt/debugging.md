---
title: 'Depuração Python - Folha de Dicas Python'
description: 'Em programação de computadores e desenvolvimento de software, depuração é o processo de encontrar e resolver bugs (defeitos ou problemas que impedem a operação correta) em programas de computador, software ou sistemas.'
labUrl: 'https://labex.io/pt/labs/python-python-debugging-633653?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Depuração Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikipedia.org/wiki/Debugging">Encontrar e resolver bugs</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Em programação de computadores e desenvolvimento de software, depuração é o processo de encontrar e resolver bugs (defeitos ou problemas que impedem a operação correta) em programas de computador, software ou sistemas.
  </base-disclaimer-content>
</base-disclaimer>

## Levantando Exceções

Exceções são levantadas com uma instrução `raise`. No código, uma instrução `raise` consiste no seguinte:

- A palavra-chave `raise`
- Uma chamada para a função `Exception()`
- Uma string com uma mensagem de erro útil passada para a função `Exception()`

```python
# instrução raise: levanta manualmente uma exceção com uma mensagem personalizada
raise Exception('This is the error message.')
```

```output
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    raise Exception('This is the error message.')
Exception: This is the error message.
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Qual palavra-chave é usada para levantar manualmente uma exceção em Python?
</template>

<base-quiz-option value="A">A. <code>throw</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>raise</code></base-quiz-option>
<base-quiz-option value="C">C. <code>error</code></base-quiz-option>
<base-quiz-option value="D">D. <code>exception</code></base-quiz-option>
<base-quiz-answer value="B">A palavra-chave <code>raise</code> é usada para levantar manualmente uma exceção em Python. Você pode levantar exceções embutidas ou exceções personalizadas.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Tipicamente, é o código que chama a função, e não a função em si, que sabe como lidar com uma exceção. Assim, você verá comumente uma instrução `raise` dentro de uma função e as instruções `try` e `except` no código que chama a função.

```python
# Levantar exceções na função, tratá-las no código de chamada
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

# Tratar exceções ao chamar a função
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:  # Captura a exceção e imprime a mensagem de erro
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

Leia mais sobre [Tratamento de Exceções](/cheatsheet/exception-handling).

## Obtendo o Traceback como uma string

O `traceback` é exibido pelo Python sempre que uma exceção levantada não é tratada. Mas você também pode obtê-lo como uma string chamando traceback.format_exc(). Esta função é útil se você deseja as informações do traceback de uma exceção, mas também quer que uma instrução `except` trate a exceção graciosamente. Você precisará importar o módulo `traceback` do Python antes de chamar esta função.

```python
# traceback.format_exc(): obter traceback como string para log/depuração
import traceback

try:
    raise Exception('This is the error message.')
except:
    with open('errorInfo.txt', 'w') as error_file:
        error_file.write(traceback.format_exc())  # Escreve o traceback no arquivo
    print('The traceback info was written to errorInfo.txt.')
```

```output
116
The traceback info was written to errorInfo.txt.
```

O 116 é o valor de retorno do método `write()`, já que 116 caracteres foram escritos no arquivo. O texto do `traceback` foi escrito em errorInfo.txt.

    Traceback (most recent call last):
      File "<pyshell#28>", line 2, in <module>
    Exception: This is the error message.

## Assertions (Asserções)

Uma asserção é uma verificação de sanidade para garantir que seu código não esteja fazendo algo obviamente errado. Essas verificações de sanidade são realizadas por instruções `assert`. Se a verificação de sanidade falhar, uma exceção `AssertionError` é levantada. No código, uma instrução `assert` consiste no seguinte:

- A palavra-chave `assert`
- Uma condição (ou seja, uma expressão que avalia para `True` ou `False`)
- Uma vírgula
- Uma `string` para exibir quando a condição for `False`

```python
# instrução assert: verifica a condição, levanta AssertionError se for Falsa
pod_bay_door_status = 'open'
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'  # Passa

pod_bay_door_status = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'  # Levanta AssertionError
```

```output
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'
AssertionError: The pod bay doors need to be "open".
```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
O que acontece quando uma instrução <code>assert</code> falha?
</template>

<base-quiz-option value="A">A. O programa continua a ser executado</base-quiz-option>
<base-quiz-option value="B">B. Um aviso é impresso</base-quiz-option>
<base-quiz-option value="C" correct>C. Uma <code>AssertionError</code> é levantada e o programa deve travar</base-quiz-option>
<base-quiz-option value="D">D. A condição é corrigida automaticamente</base-quiz-option>
<base-quiz-answer value="C">Quando uma instrução <code>assert</code> falha, ela levanta uma <code>AssertionError</code>. Ao contrário das exceções, as instruções assert não devem ser capturadas com try-except; se uma asserção falhar, seu programa deve travar para ajudá-lo a encontrar bugs rapidamente.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Em linguagem simples, uma instrução assert diz: "Eu assserto que esta condição é verdadeira, e se não for, há um bug em algum lugar do programa." Ao contrário das exceções, seu código não deve lidar com instruções assert com try e except; se uma asserção falhar, seu programa deve travar. Ao falhar rapidamente assim, você encurta o tempo entre a causa original do bug e quando você percebe o bug pela primeira vez. Isso reduzirá a quantidade de código que você terá que verificar antes de encontrar o código que está causando o bug.

### Desabilitando Asserções

As asserções podem ser desabilitadas passando a opção `-O` ao executar o Python.

## Logging (Registro de Logs)

Para habilitar o módulo `logging` a exibir mensagens de log na sua tela enquanto seu programa é executado, copie o seguinte para o topo do seu programa:

```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Qual é o propósito do módulo <code>logging</code> em Python?
</template>

<base-quiz-option value="A" correct>A. Registrar informações sobre a execução do programa para depuração e monitoramento</base-quiz-option>
<base-quiz-option value="B">B. Prevenir que erros ocorram</base-quiz-option>
<base-quiz-option value="C">C. Acelerar a execução do programa</base-quiz-option>
<base-quiz-option value="D">D. Criptografar mensagens de log</base-quiz-option>
<base-quiz-answer value="A">O módulo <code>logging</code> permite registrar informações sobre a execução do seu programa em diferentes níveis (DEBUG, INFO, WARNING, ERROR, CRITICAL), o que é útil para depuração e monitoramento.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Digamos que você escreveu uma função para calcular o fatorial de um número. Em matemática, fatorial 4 é 1 × 2 × 3 × 4, ou 24. Fatorial 7 é 1 × 2 × 3 × 4 × 5 × 6 × 7, ou 5.040. Abra uma nova janela de editor de arquivos e insira o seguinte código. Ele tem um bug, mas você também inserirá várias mensagens de log para se ajudar a descobrir o que está dando errado. Salve o programa como factorialLog.py.

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

## Níveis de Logging

Os níveis de logging fornecem uma maneira de categorizar suas mensagens de log por importância. Existem cinco níveis de logging, descritos na Tabela 10-1 do menos para o mais importante. Mensagens podem ser registradas em cada nível usando uma função de logging diferente.

| Nível      | Função de Logging    | Descrição                                                                                                                                |
| ---------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `DEBUG`    | `logging.debug()`    | O nível mais baixo. Usado para pequenos detalhes. Geralmente você se importa com essas mensagens apenas ao diagnosticar problemas.       |
| `INFO`     | `logging.info()`     | Usado para registrar informações sobre eventos gerais no seu programa ou confirmar que as coisas estão funcionando no ponto do programa. |
| `WARNING`  | `logging.warning()`  | Usado para indicar um problema potencial que não impede o programa de funcionar, mas pode fazê-lo no futuro.                             |
| `ERROR`    | `logging.error()`    | Usado para registrar um erro que fez o programa falhar ao fazer algo.                                                                    |
| `CRITICAL` | `logging.critical()` | O nível mais alto. Usado para indicar um erro fatal que causou ou está prestes a causar a parada total da execução do programa.          |

<base-quiz>
<base-quiz-question correct="D">
<template #question>
Qual é o nível de logging mais baixo em Python?
</template>

<base-quiz-option value="A">A. <code>INFO</code></base-quiz-option>
<base-quiz-option value="B">B. <code>WARNING</code></base-quiz-option>
<base-quiz-option value="C">C. <code>ERROR</code></base-quiz-option>
<base-quiz-option value="D" correct>D. <code>DEBUG</code></base-quiz-option>
<base-quiz-answer value="D">Os níveis de logging do mais baixo para o mais alto são: <code>DEBUG</code>, <code>INFO</code>, <code>WARNING</code>, <code>ERROR</code>, <code>CRITICAL</code>. <code>DEBUG</code> é o nível mais baixo, usado para informações detalhadas de diagnóstico.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Desabilitando Logging

Depois de depurar seu programa, provavelmente você não quer que todas essas mensagens de log poluam a tela. A função logging.disable() as desabilita para que você não precise entrar no seu programa e remover todas as chamadas de logging manualmente.

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

## Logging para um Arquivo

Em vez de exibir as mensagens de log na tela, você pode escrevê-las em um arquivo de texto. A função `logging.basicConfig()` aceita um argumento de palavra-chave `filename`, assim:

```python
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Como você escreve mensagens de log em um arquivo em vez de exibi-las na tela?
</template>

<base-quiz-option value="A">A. Usando <code>logging.file()</code></base-quiz-option>
<base-quiz-option value="B" correct>B. Passando o parâmetro <code>filename</code> para <code>logging.basicConfig()</code></base-quiz-option>
<base-quiz-option value="C">C. Usando <code>logging.write()</code></base-quiz-option>
<base-quiz-option value="D">D. Logs são sempre escritos em arquivos automaticamente</base-quiz-option>
<base-quiz-answer value="B">Para escrever mensagens de log em um arquivo, passe o parâmetro <code>filename</code> para <code>logging.basicConfig()</code>. Isso escreverá todas as mensagens de log no arquivo especificado em vez de exibi-las na tela.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Links Relevantes

- <router-link to="/cheatsheet/exception-handling">Tratamento de Exceções</router-link>
- <router-link to="/builtin/breakpoint">breakpoint()</router-link>
