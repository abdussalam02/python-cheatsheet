---
title: 'Python OOP の基本 - Python チートシート'
description: 'オブジェクト指向プログラミング（OOP）は、クラスのインスタンスであるオブジェクトの概念を中心としたプログラミングパラダイムです。OOP の原則は、オブジェクト指向的な方法でソフトウェアの設計と開発を導く基本的な概念です。Python では、クラスとオブジェクトの使用によって OOP がサポートされています。ここでは、Python における基本的な OOP の原則をいくつか紹介します。'
labUrl: 'https://labex.io/ja/labs/python-python-oop-basics-633662?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python OOP の基本
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a href="https://en.wikipedia.org/wiki/Object-oriented_programming">オブジェクト指向プログラミング</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    オブジェクト指向プログラミング（OOP）は、「オブジェクト」の概念に基づいたプログラミングパラダイムであり、オブジェクトはデータとコードを含むことができます。データはフィールド（属性やプロパティとも呼ばれる）の形で、コードはプロシージャ（メソッドとも呼ばれる）の形をとります。
  </base-disclaimer-content>
</base-disclaimer>

## カプセル化 (Encapsulation)

カプセル化は、オブジェクト指向プログラミングの基本概念の 1 つであり、オブジェクトのデータとメソッドを不正なアクセスや変更から保護するのに役立ちます。これはデータ抽象化を達成する方法であり、オブジェクトの実装の詳細が外部から隠され、本質的な情報のみが公開されることを意味します。

Python では、カプセル化はアクセス修飾子を使用することで実現できます。アクセス修飾子は、クラス内の属性とメソッドのアクセシビリティを定義するキーワードです。Python で利用可能な 3 つのアクセス修飾子は、public、private、protected です。ただし、Python には Java や C++ などの他のプログラミング言語のようにアクセス修飾子を明示的に定義する方法はありません。代わりに、アクセスレベルを示すためにアンダースコアのプレフィックスを使用する規約を採用しています。

提供されたコード例では、MyClass というクラスには、\_protected_var と\_\_private_var という 2 つの属性があります。\_protected_var は、単一のアンダースコアプレフィックスを使用して protected としてマークされています。これは、その属性がクラス内およびそのサブクラス内でアクセス可能であることを意味しますが、クラス外からはアクセスできません。\_\_private_var は、2 つのアンダースコアプレフィックスを使用して private としてマークされています。これは、その属性がクラス内でのみアクセス可能であり、サブクラスであってもクラス外からはアクセスできないことを意味します。

MyClass クラスのオブジェクトを作成すると、オブジェクト名に単一のアンダースコアプレフィックスを付けて\_protected_var 属性にアクセスできます。しかし、非公開であるため、オブジェクト名を使用して\_\_private_var 属性にアクセスすることはできません。 \_\_private_var 属性にアクセスしようとすると、コードに示されているように AttributeError が発生します。

要約すると、カプセル化はオブジェクト指向プログラミングにおいて重要な概念であり、オブジェクトの実装の詳細を保護するのに役立ちます。Python では、アクセス修飾子を使用し、アンダースコアプレフィックスを使用してアクセスレベルを示すことで、カプセル化を実現できます。

```python
# MyClass という名前のクラスを定義
class MyClass:

    # クラスオブジェクトを初期化するコンストラクタメソッド
    def __init__(self):

        # 初期値が 10 の protected 変数を定義
        # 変数名は単一のアンダースコアで始まるため、protected アクセスを示します
        self._protected_var = 10

        # 初期値が 20 の private 変数を定義
        # 変数名は 2 つのアンダースコアで始まるため、private アクセスを示します
        self.__private_var = 20

# MyClass クラスのオブジェクトを作成
obj = MyClass()

# オブジェクト名と単一のアンダースコアプレフィックスを使用して protected 変数をアクセスし、その値を出力
# protected 変数はクラス外からアクセス可能ですが、
# クラス内またはそのサブクラス内での使用を意図しています
print(obj._protected_var)   # 出力：10

# オブジェクト名を使用して private 変数をアクセスし、その値を出力しようとします
# private 変数はサブクラスであってもクラス外からアクセスできないため、
# クラス外からアクセスすることはできません。これは AttributeError を発生させます
print(obj.__private_var)    # AttributeError: 'MyClass' object has no attribute '__private_var'

```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
Python で protected 変数を指定するにはどうすればよいですか？
</template>

<base-quiz-option value="A">A. 2 つのアンダースコアプレフィックス：<code>**variable</code></base-quiz-option>
<base-quiz-option value="B" correct>B. 単一のアンダースコアプレフィックス：<code>_variable</code></base-quiz-option>
<base-quiz-option value="C">C. アンダースコアは不要</base-quiz-option>
<base-quiz-option value="D">D. 3 つのアンダースコアプレフィックス：<code>_**variable</code></base-quiz-option>
<base-quiz-answer value="B">Python では、単一のアンダースコアプレフィックス（<code>\_variable</code>）が protected 変数を表し、クラス内またはそのサブクラス内で使用されるべきであることを示す規約です。2 つのアンダースコア（<code>\_\_variable</code>）は private 変数を表します。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 継承 (Inheritance)

継承はコードの再利用を促進し、共通の属性とメソッドを共有するクラスの階層を作成できるようにします。関連する機能を一箇所にまとめ、モジュール性の概念を促進することで、クリーンで整理されたコードの作成に役立ちます。新しいクラスが派生する基本クラスは親クラスとも呼ばれ、新しいクラスは子クラスまたはサブクラスとして知られています。

コードでは、名前属性と speak メソッドを持つコンストラクタメソッドを持つ Animal というクラスを定義します。speak メソッドは Animal クラスで定義されていますが、本体はありません。

次に、Animal クラスから継承する Dog と Cat という 2 つのサブクラスを定義します。これらのサブクラスは、Animal クラスの speak メソッドをオーバーライドします。

名前属性 "Rover" を持つ Dog オブジェクトと、名前属性 "Whiskers" を持つ Cat オブジェクトを作成します。dog.speak() を使用して Dog オブジェクトの speak メソッドを呼び出すと、Dog クラスの speak メソッドが Animal クラスの speak メソッドをオーバーライドしているため、「Woof!」と出力されます。同様に、cat.speak() を使用して Cat オブジェクトの speak メソッドを呼び出すと、Cat クラスの speak メソッドが Animal クラスの speak メソッドをオーバーライドしているため、「Meow!」と出力されます。

```python
# Animal という名前のクラスを定義
class Animal:

    # name 属性でクラスオブジェクトを初期化するコンストラクタメソッド
    def __init__(self, name):
        self.name = name

    # Animal クラスで定義されているが、本体を持たないメソッド
    # このメソッドは Animal のサブクラスでオーバーライドされます
    def speak(self):
        print("")

# Animal クラスから継承する Dog という名前のサブクラスを定義
class Dog(Animal):

    # Animal クラスの speak メソッドをオーバーライド
    def speak(self):
        print("Woof!")

# Animal クラスから継承する Cat という名前のサブクラスを定義
class Cat(Animal):

    # Animal クラスの speak メソッドをオーバーライド
    def speak(self):
        print("Meow!")

# 名前属性 "Rover" を持つ Dog オブジェクトを作成
dog = Dog("Rover")

# 名前属性 "Whiskers" を持つ Cat オブジェクトを作成
cat = Cat("Whiskers")

# Dog クラスの speak メソッドを呼び出し、出力を印刷
# Dog クラスの speak メソッドは Animal クラスの speak メソッドをオーバーライドします
# したがって、Dog オブジェクトの speak メソッドを呼び出すと、「Woof!」が出力されます
dog.speak()   # 出力：Woof!

# Cat クラスの speak メソッドを呼び出し、出力を印刷
# Cat クラスの speak メソッドは Animal クラスの speak メソッドをオーバーライドします
# したがって、Cat オブジェクトの speak メソッドを呼び出すと、「Meow!」が出力されます
cat.speak()   # 出力：Meow!

```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
Python における継承とは何ですか？
</template>

<base-quiz-option value="A" correct>A. クラスが別のクラスから属性とメソッドを継承できるメカニズム</base-quiz-option>
<base-quiz-option value="B">B. オブジェクトをコピーする方法</base-quiz-option>
<base-quiz-option value="C">C. クラスを削除する方法</base-quiz-option>
<base-quiz-option value="D">D. ビルトイン関数</base-quiz-option>
<base-quiz-answer value="A">継承により、クラス（子クラス/サブクラス）は別のクラス（親クラス/基本クラス）から属性とメソッドを継承できます。これによりコードの再利用が促進され、クラスの階層を作成できます。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 多態性 (Polymorphism)

多態性（ポリモーフィズム）は、オブジェクト指向プログラミングにおける重要な概念であり、異なるクラスのオブジェクトに対して統一された方法でコードを記述できるようにします。Python では、多態性はメソッドのオーバーライドまたはメソッドのオーバーロードを使用することで実現されます。

メソッドのオーバーライドとは、サブクラスが親クラスですでに定義されているメソッドに対して独自のメソッド実装を提供することです。これにより、メソッドの名前やシグネチャを変更することなく、サブクラスがメソッドの動作を変更できるようになります。

メソッドのオーバーロードとは、複数のメソッドが同じ名前を持ちながら異なるパラメータを持つことです。Python はメソッドのオーバーロードを直接サポートしていませんが、デフォルト引数や可変長引数を使用して実現できます。

多態性は、柔軟で再利用可能なコードの記述を容易にします。これにより、オブジェクトの特定の型を知る必要なく、さまざまなオブジェクトで動作するコードを記述できるようになります。

```python
# Shape クラスは、サブクラスによってオーバーライドされることを意図した抽象的な area メソッドで定義されています。
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    # Rectangle クラスは、width と height のインスタンス変数を初期化する__init__メソッドで定義されています。
    # また、width と height のインスタンス変数を使用して長方形の面積を計算して返す area メソッドも定義されています。
    def __init__(self, width, height):
        self.width = width  # width インスタンス変数を初期化
        self.height = height  # height インスタンス変数を初期化

    def area(self):
        return self.width * self.height  # 長方形の面積を返す


 # Circle クラスは、radius インスタンス変数を初期化する__init__メソッドで定義されています。
 # また、radius インスタンス変数を使用して円の面積を計算して返す area メソッドも定義されています。
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # radius インスタンス変数を初期化

    def area(self):
        return 3.14 * self.radius ** 2  # pi * r^2 を使用して円の面積を返す

# shapes リストは、1 つの Rectangle オブジェクトと 1 つの Circle オブジェクトで作成されます。for
# ループはリスト内の各オブジェクトを反復処理し、各オブジェクトの area メソッドを呼び出します
# 出力は長方形の面積（20）と円の面積（153.86）になります。
shapes = [Rectangle(4, 5), Circle(7)]  # Shape オブジェクトのリストを作成
for shape in shapes:
    print(shape.area())  # 各 Shape オブジェクトの面積を出力

```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
Python における多態性とは何ですか？
</template>

<base-quiz-option value="A">A. 同じ名前の複数のクラスを作成すること</base-quiz-option>
<base-quiz-option value="B">B. 実装の詳細を隠蔽すること</base-quiz-option>
<base-quiz-option value="C" correct>C. 共通のインターフェースを介して異なるクラスのオブジェクトを統一された方法で使用できる能力</base-quiz-option>
<base-quiz-option value="D">D. オブジェクトのコピー</base-quiz-option>
<base-quiz-answer value="C">多態性により、オブジェクトの特定の型を知ることなく、さまざまなクラスのオブジェクトに対して統一された方法で動作するコードを記述できます。異なるクラスが同じメソッド名を実装でき、Python はオブジェクトの型に基づいて適切な実装を呼び出します。</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## 抽象化 (Abstraction)

抽象化は、オブジェクト指向プログラミング（OOP）において重要な概念であり、現在のコンテキストに関連のない詳細を無視しながら、オブジェクトまたはシステムの必須機能に焦点を当てることができます。複雑さを軽減し、不要な詳細を隠すことで、抽象化はコードをよりモジュール化し、読みやすく、保守しやすくするのに役立ちます。

Python では、抽象化は抽象クラスまたはインターフェースを使用して実現できます。抽象クラスは直接インスタンス化できないクラスですが、他のクラスによってサブクラス化されることを意図しています。実装を持たない抽象メソッドを含むことが多く、サブクラスがどのように実装されるべきかのテンプレートを提供します。これにより、プログラマは関連するクラスのグループに共通のインターフェースを定義しながら、各クラスが独自の特定の動作を持つことを許可できます。

一方、インターフェースは、そのインターフェースと「互換性がある」と見なされるためにクラスが実装しなければならないメソッドシグネチャの集合です。インターフェースは、複数のクラスが実装できる共通のメソッドセットを定義するためによく使用され、特定のコンテキストでそれらを交換可能に使用できるようにします。

Python には、抽象クラスやインターフェースの組み込みサポートはありませんが、abc（abstract base class）モジュールを使用して実装できます。このモジュールは、ABC クラスと abstractmethod デコレータを提供し、これらを使用して抽象クラスとメソッドを定義できます。

全体として、抽象化はオブジェクト指向プログラミングにおける複雑さを管理し、コード品質を向上させるための強力なツールであり、Python はコードで抽象化を達成するためのさまざまなオプションを提供します。

```python
# abc モジュールをインポートして抽象クラスとメソッドを定義
from abc import ABC, abstractmethod

# area という抽象メソッドを持つ Shape という抽象クラスを定義
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Shape から継承する Rectangle クラスを定義
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Rectangle の area メソッドを実装
    def area(self):
        return self.width * self.height

# Shape から継承する Circle クラスも定義
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Circle の area メソッドを実装
    def area(self):
        return 3.14 * self.radius ** 2

# Rectangle と Circle の両方を含む shapes のリストを作成
shapes = [Rectangle(4, 5), Circle(7)]

# リスト内の各シェイプをループし、その面積を出力
for shape in shapes:
    print(shape.area())

```

これらは Python における基本的な OOP の原則の一部です。このページは現在作成中で、より詳細な例と説明が間もなく公開されます。

## 関連リンク

- <router-link to="/cheatsheet/functions">関数 (Functions)</router-link>
- <router-link to="/cheatsheet/decorators">デコレータ (Decorators)</router-link>
- <router-link to="/cheatsheet/exception-handling">例外処理 (Exception Handling)</router-link>
- <router-link to="/cheatsheet/dataclasses">データクラス (Dataclasses)</router-link>
- <router-link to="/builtin/object">object()</router-link>
- <router-link to="/builtin/classmethod">classmethod()</router-link>
- <router-link to="/builtin/staticmethod">staticmethod()</router-link>
- <router-link to="/builtin/property">property()</router-link>
- <router-link to="/builtin/isinstance">isinstance()</router-link>
- <router-link to="/builtin/issubclass">issubclass()</router-link>
- <router-link to="/builtin/super">super()</router-link>
