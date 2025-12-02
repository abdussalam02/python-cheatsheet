---
title: 'Функция Python Main - Шпаргалка по Python'
description: 'Имя области, в которой выполняется код верхнего уровня. Имя модуля устанавливается равным main при чтении из стандартного ввода, скрипта или интерактивной подсказки.'
labUrl: 'https://labex.io/ru/labs/python-python-main-function-633661?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Основная среда сценариев верхнего уровня
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## Что это такое

`__main__` — это имя области, в которой выполняется код верхнего уровня.
**Имя** модуля устанавливается равным `__main__`, когда он считывается из стандартного ввода, сценария или интерактивной подсказки.

Модуль может определить, выполняется ли он в основной области, проверив свое собственное `__name__`, что позволяет использовать распространенный идиом для условного выполнения кода в модуле. Когда он запускается как сценарий или с помощью `python -m`, но не когда он импортируется:

```python
# __name__ == "__main__": проверка, запущен ли сценарий напрямую (не импортирован)
if __name__ == "__main__":  # True, если запущен как сценарий, False, если импортирован
    # выполняется только при запуске в качестве сценария
    main()
```

Для пакета тот же эффект может быть достигнут путем включения модуля **main**.py, содержимое которого будет выполнено, когда модуль запускается с помощью -m.

Например, если мы разрабатываем сценарий, предназначенный для использования в качестве модуля, мы должны сделать следующее:

```python
# Пример: функцию можно импортировать, но тестовый код выполняется только при прямом запуске
def add(a, b):
    return a+b

if __name__ == "__main__":  # Выполняется только при запуске файла, а не при импорте
    add(3, 5)
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-main-1">
<template #question>
Каково значение <code>__name__</code>, когда файл Python запускается напрямую как сценарий?
</template>

<base-quiz-option value="A">A. Имя файла</base-quiz-option>
<base-quiz-option value="B" correct>B. <code>"**main**"</code></base-quiz-option>
<base-quiz-option value="C">C. <code>None</code></base-quiz-option>
<base-quiz-option value="D">D. <code>True</code></base-quiz-option>
<base-quiz-answer value="B">Когда файл Python запускается напрямую как сценарий, <code>**name**</code> устанавливается в <code>"**main**"</code>. Когда файл импортируется как модуль, <code>**name**</code> устанавливается в имя модуля.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Преимущества

1. Каждый модуль Python имеет определенное `__name__`, и если оно равно `__main__`, это означает, что модуль запускается пользователем автономно, и мы можем предпринять соответствующие действия.
2. Если вы импортируете этот сценарий как модуль в другой сценарий, **имя** устанавливается в имя сценария/модуля.
3. Файлы Python могут выступать либо в качестве многократно используемых модулей, либо в качестве автономных программ.
4. `if __name__ == "__main__":` используется для выполнения некоторого кода только в том случае, если файл запускается напрямую, а не импортируется.

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-main-2">
<template #question>
Какова основная цель использования <code>if __name__ == "__main__":</code>?
</template>

<base-quiz-option value="A" correct>A. Выполнять код только при прямом запуске файла, а не при импорте</base-quiz-option>
<base-quiz-option value="B">B. Предотвратить импорт файла</base-quiz-option>
<base-quiz-option value="C">C. Сделать выполнение файла быстрее</base-quiz-option>
<base-quiz-option value="D">D. Скрыть код от других модулей</base-quiz-option>
<base-quiz-answer value="A">Идиома <code>if **name** == "**main**":</code> позволяет файлу Python выступать как в качестве многократно используемого модуля, так и в качестве автономной программы. Код внутри этого блока выполняется только при прямом запуске файла, а не при его импорте.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Связанные ссылки

- <router-link to="/cheatsheet/functions">Функции</router-link>
- <router-link to="/cheatsheet/packaging">Упаковка</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Проекты Python с Poetry и VSCode. Часть 1</router-link>
- <router-link to="/builtin/import">import()</router-link>
