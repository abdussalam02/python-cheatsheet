---
title: 'Função Principal Python - Folha de Dicas Python'
description: 'É o nome do escopo em que o código de nível superior é executado. O nome de um módulo é definido como main quando lido da entrada padrão, de um script ou de um prompt interativo.'
labUrl: 'https://labex.io/pt/labs/python-python-main-function-633661?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Ambiente de script de nível superior principal
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

## O que é

`__main__` é o nome do escopo em que o código de nível superior é executado.
O **nome** de um módulo é definido como igual a `__main__` quando lido da entrada padrão, de um script ou de um prompt interativo.

Um módulo pode descobrir se está sendo executado no escopo principal verificando seu próprio `__name__`, o que permite um idioma comum para executar código condicionalmente em um módulo. Quando é executado como um script ou com `python -m`, mas não quando é importado:

```python
# __name__ == "__main__": verifica se o script é executado diretamente (não importado)
if __name__ == "__main__":  # Verdadeiro quando executado como script, Falso quando importado
    # executa somente se executado como script
    main()
```

Para um pacote, o mesmo efeito pode ser alcançado incluindo um módulo **main.py**, cujo conteúdo será executado quando o módulo for executado com -m.

Por exemplo, estamos desenvolvendo um script projetado para ser usado como um módulo, devemos fazer:

```python
# Exemplo: a função pode ser importada, mas o código de teste só é executado quando executado diretamente
def add(a, b):
    return a+b

if __name__ == "__main__":  # Só é executado quando o arquivo é executado, não quando importado
    add(3, 5)
```

<base-quiz>
<base-quiz-question correct="B" id="cheatsheet-main-1">
<template #question>
Qual é o valor de <code>__name__</code> quando um arquivo Python é executado diretamente como um script?
</template>

<base-quiz-option value="A">A. O nome do arquivo</base-quiz-option>
<base-quiz-option value="B" correct>B. <code>"**main**"</code></base-quiz-option>
<base-quiz-option value="C">C. <code>None</code></base-quiz-option>
<base-quiz-option value="D">D. <code>True</code></base-quiz-option>
<base-quiz-answer value="B">Quando um arquivo Python é executado diretamente como um script, <code>**name**</code> é definido como <code>"**main**"</code>. Quando o arquivo é importado como um módulo, <code>**name**</code> é definido como o nome do módulo.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Vantagens

1. Todo módulo Python tem seu `__name__` definido e, se for `__main__`, implica que o módulo está sendo executado de forma independente pelo usuário, e podemos tomar as ações apropriadas correspondentes.
2. Se você importar este script como um módulo em outro script, o **nome** é definido como o nome do script/módulo.
3. Arquivos Python podem funcionar como módulos reutilizáveis ou como programas autônomos.
4. `if __name__ == "__main__":` é usado para executar algum código somente se o arquivo for executado diretamente e não estiver sendo importado.

<base-quiz>
<base-quiz-question correct="A" id="cheatsheet-main-2">
<template #question>
Qual é o principal objetivo de usar <code>if __name__ == "__main__":</code>?
</template>

<base-quiz-option value="A" correct>A. Executar código somente quando o arquivo é executado diretamente, não quando importado</base-quiz-option>
<base-quiz-option value="B">B. Impedir que o arquivo seja importado</base-quiz-option>
<base-quiz-option value="C">C. Fazer o arquivo executar mais rápido</base-quiz-option>
<base-quiz-option value="D">D. Ocultar código de outros módulos</base-quiz-option>
<base-quiz-answer value="A">O idioma <code>if **name** == "**main**":</code> permite que um arquivo Python funcione tanto como um módulo reutilizável quanto como um programa autônomo. O código dentro deste bloco só é executado quando o arquivo é executado diretamente, não quando é importado.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Links relevantes

- <router-link to="/cheatsheet/functions">Funções</router-link>
- <router-link to="/cheatsheet/packaging">Empacotamento</router-link>
- <router-link to="/blog/python-projects-with-poetry-and-vscode-part-1">Projetos Python com Poetry e VSCode. Parte 1</router-link>
- <router-link to="/builtin/import">import()</router-link>
