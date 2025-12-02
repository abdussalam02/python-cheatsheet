---
title: 'Отладка Python - Шпаргалка по Python'
description: 'В программировании отладка — это процесс поиска и устранения ошибок (дефектов или проблем, препятствующих корректной работе) в компьютерных программах, программном обеспечении или системах.'
labUrl: 'https://labex.io/ru/labs/python-python-debugging-633653?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Отладка Python
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a target="_blank" href="https://en.wikipedia.org/wiki/Debugging">Поиск и устранение ошибок</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    В компьютерном программировании и разработке программного обеспечения отладка — это процесс поиска и устранения ошибок (дефектов или проблем, препятствующих корректной работе) в компьютерных программах, программном обеспечении или системах.
  </base-disclaimer-content>
</base-disclaimer>

## Вызов исключений

Исключения вызываются с помощью оператора `raise`. В коде оператор `raise` состоит из следующего:

- Ключевое слово `raise`
- Вызов функции `Exception()`
- Строка с полезным сообщением об ошибке, переданная в функцию `Exception()`

```python
# оператор raise: вручную вызвать исключение с пользовательским сообщением
raise Exception('This is the error message.')
```

```output
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    raise Exception('This is the error message.')
Exception: This is the error message.
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-debugging-1">
<template #question>
Какое ключевое слово используется для ручного вызова исключения в Python?
</template>

<base-quiz-option value="A">A. <code>throw</code></base-quiz-option>
<base-quiz-option value="B" correct>B. <code>raise</code></base-quiz-option>
<base-quiz-option value="C">C. <code>error</code></base-quiz-option>
<base-quiz-option value="D">D. <code>exception</code></base-quiz-option>
<base-quiz-answer value="B">Ключевое слово <code>raise</code> используется для ручного вызова исключения в Python. Вы можете вызывать встроенные исключения или пользовательские исключения.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Обычно код, который вызывает функцию, а не сама функция, знает, как обработать исключение. Поэтому вы часто увидите оператор `raise` внутри функции, а операторы `try` и `except` — в коде, вызывающем функцию.

```python
# Вызов исключений в функции, обработка их в вызывающем коде
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

# Обработка исключений при вызове функции
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:  # Перехват исключения и вывод сообщения об ошибке
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

Подробнее об [Обработке исключений](/cheatsheet/exception-handling).

## Получение трассировки как строки

Трассировка (`traceback`) отображается Python всякий раз, когда вызванное исключение остается необработанным. Но ее также можно получить в виде строки, вызвав `traceback.format_exc()`. Эта функция полезна, если вам нужна информация из трассировки исключения, но вы также хотите, чтобы блок `except` корректно обработал исключение. Вам потребуется импортировать модуль `traceback` Python перед вызовом этой функции.

```python
# traceback.format_exc(): получить трассировку как строку для логирования/отладки
import traceback

try:
    raise Exception('This is the error message.')
except:
    with open('errorInfo.txt', 'w') as error_file:
        error_file.write(traceback.format_exc())  # Записать трассировку в файл
    print('The traceback info was written to errorInfo.txt.')
```

```output
116
The traceback info was written to errorInfo.txt.
```

Число 116 — это возвращаемое значение метода `write()`, поскольку в файл было записано 116 символов. Текст `traceback` был записан в errorInfo.txt.

    Traceback (most recent call last):
      File "<pyshell#28>", line 2, in <module>
    Exception: This is the error message.

## Утверждения (Assertions)

Утверждение — это проверка здравого смысла, чтобы убедиться, что ваш код не делает ничего заведомо неправильного. Эти проверки здравого смысла выполняются операторами `assert`. Если проверка здравого смысла не пройдена, вызывается исключение `AssertionError`. В коде оператор `assert` состоит из следующего:

- Ключевое слово `assert`
- Условие (т.е. выражение, которое возвращает `True` или `False`)
- Запятая
- `string` для отображения, когда условие равно `False`

```python
# оператор assert: проверить условие, вызвать AssertionError, если False
pod_bay_door_status = 'open'
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'  # Проходит

pod_bay_door_status = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'  # Вызывает AssertionError
```

```output
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'
AssertionError: The pod bay doors need to be "open".
```

<base-quiz>
<base-quiz-question correct="C" id="cheatsheet-debugging-2">
<template #question>
Что происходит, когда оператор <code>assert</code> завершается неудачей?
</template>

<base-quiz-option value="A">A. Программа продолжает выполнение</base-quiz-option>
<base-quiz-option value="B">B. Выводится предупреждение</base-quiz-option>
<base-quiz-option value="C" correct>C. Вызывается <code>AssertionError</code>, и программа должна аварийно завершиться</base-quiz-option>
<base-quiz-option value="D">D. Условие исправляется автоматически</base-quiz-option>
<base-quiz-answer value="C">Когда оператор <code>assert</code> завершается неудачей, он вызывает <code>AssertionError</code>. В отличие от исключений, операторы assert не следует перехватывать с помощью try-except; если assert не проходит, ваша программа должна аварийно завершиться, чтобы помочь вам быстро найти ошибки.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Проще говоря, оператор assert гласит: «Я утверждаю, что это условие истинно, а если нет, то где-то в программе есть ошибка». В отличие от исключений, ваш код не должен обрабатывать операторы assert с помощью try и except; если assert не проходит, ваша программа должна аварийно завершиться. Такой быстрый отказ сокращает время между первопричиной ошибки и первым обнаружением ошибки. Это уменьшит объем кода, который вам придется проверять, прежде чем найти код, вызывающий ошибку.

### Отключение утверждений

Утверждения можно отключить, передав опцию `-O` при запуске Python.

## Логирование (Logging)

Чтобы модуль `logging` отображал сообщения журнала на экране по мере выполнения вашей программы, скопируйте следующее в начало вашей программы:

```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
```

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-debugging-3">
<template #question>
Какова цель модуля <code>logging</code> в Python?
</template>

<base-quiz-option value="A" correct>A. Запись информации о выполнении программы для отладки и мониторинга</base-quiz-option>
<base-quiz-option value="B">B. Предотвращение возникновения ошибок</base-quiz-option>
<base-quiz-option value="C">C. Ускорение выполнения программы</base-quiz-option>
<base-quiz-option value="D">D. Шифрование сообщений журнала</base-quiz-option>
<base-quiz-answer value="A">Модуль <code>logging</code> позволяет записывать информацию о выполнении вашей программы на разных уровнях (DEBUG, INFO, WARNING, ERROR, CRITICAL), что полезно для отладки и мониторинга.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

Предположим, вы написали функцию для вычисления факториала числа. В математике факториал 4 равен 1 × 2 × 3 × 4, или 24. Факториал 7 равен 1 × 2 × 3 × 4 × 5 × 6 × 7, или 5040. Откройте новое окно редактора файлов и введите следующий код. В нем есть ошибка, но вы также добавите несколько сообщений журнала, чтобы помочь себе выяснить, что идет не так. Сохраните программу как factorialLog.py.

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

## Уровни логирования

Уровни логирования предоставляют способ категоризировать ваши сообщения журнала по важности. Существует пять уровней логирования, описанных в Таблице 10-1 от наименее до наиболее важных. Сообщения могут быть занесены в журнал на каждом уровне с использованием разной функции логирования.

| Уровень    | Функция логирования  | Описание                                                                                                                                      |
| ---------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `DEBUG`    | `logging.debug()`    | Самый низкий уровень. Используется для мелких деталей. Обычно вас интересуют эти сообщения только при диагностике проблем.                    |
| `INFO`     | `logging.info()`     | Используется для записи информации об общих событиях в вашей программе или для подтверждения того, что все работает в нужной точке программы. |
| `WARNING`  | `logging.warning()`  | Используется для указания на потенциальную проблему, которая не мешает работе программы, но может сделать это в будущем.                      |
| `ERROR`    | `logging.error()`    | Используется для записи ошибки, из-за которой программа не смогла что-то сделать.                                                             |
| `CRITICAL` | `logging.critical()` | Самый высокий уровень. Используется для указания на фатальную ошибку, которая вызвала или вот-вот вызовет полную остановку работы программы.  |

<base-quiz>
<base-quiz-question correct="D" id="cheatsheet-debugging-4">
<template #question>
Какой самый низкий уровень логирования в Python?
</template>

<base-quiz-option value="A">A. <code>INFO</code></base-quiz-option>
<base-quiz-option value="B">B. <code>WARNING</code></base-quiz-option>
<base-quiz-option value="C">C. <code>ERROR</code></base-quiz-option>
<base-quiz-option value="D" correct>D. <code>DEBUG</code></base-quiz-option>
<base-quiz-answer value="D">Уровни логирования от самого низкого к самому высокому: <code>DEBUG</code>, <code>INFO</code>, <code>WARNING</code>, <code>ERROR</code>, <code>CRITICAL</code>. <code>DEBUG</code> — самый низкий уровень, используемый для подробной диагностической информации.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Отключение логирования

После того как вы отладили свою программу, вы, вероятно, не захотите, чтобы все эти сообщения журнала загромождали экран. Функция `logging.disable()` отключает их, чтобы вам не приходилось вручную удалять все вызовы логирования в вашей программе.

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

## Логирование в файл

Вместо отображения сообщений журнала на экране вы можете записать их в текстовый файл. Функция `logging.basicConfig()` принимает именованный аргумент `filename`, вот так:

```python
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-debugging-5">
<template #question>
Как записать сообщения журнала в файл вместо отображения их на экране?
</template>

<base-quiz-option value="A">A. Использовать <code>logging.file()</code></base-quiz-option>
<base-quiz-option value="B" correct>B. Передать параметр <code>filename</code> в <code>logging.basicConfig()</code></base-quiz-option>
<base-quiz-option value="C">C. Использовать <code>logging.write()</code></base-quiz-option>
<base-quiz-option value="D">D. Журналы всегда записываются в файлы автоматически</base-quiz-option>
<base-quiz-answer value="B">Чтобы записать сообщения журнала в файл, передайте параметр <code>filename</code> в <code>logging.basicConfig()</code>. Это запишет все сообщения журнала в указанный файл вместо отображения их на экране.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Связанные ссылки

- <router-link to="/cheatsheet/exception-handling">Обработка исключений</router-link>
- <router-link to="/builtin/breakpoint">breakpoint()</router-link>
