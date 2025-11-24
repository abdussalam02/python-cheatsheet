---
title: 'Python OOP Grundlagen - Python Spickzettel'
description: 'Die objektorientierte Programmierung (OOP) ist ein Programmierparadigma, das sich um das Konzept der Objekte dreht, welche Instanzen von Klassen sind. OOP-Prinzipien sind grundlegende Konzepte, die das Design und die Entwicklung von Software auf objektorientierte Weise leiten. In Python wird OOP durch die Verwendung von Klassen und Objekten unterstützt. Hier sind einige der grundlegenden OOP-Prinzipien in Python.'
labUrl: 'https://labex.io/de/labs/python-python-oop-basics-633662?course=python-cheatsheet'
---

<base-title :title="frontmatter.title" :description="frontmatter.description">
Python OOP Grundlagen
</base-title>

<base-lab-url :url="frontmatter.labUrl" />

<base-disclaimer>
  <base-disclaimer-title>
    <a href="https://en.wikipedia.org/wiki/Object-oriented_programming">Objektorientierte Programmierung</a>
  </base-disclaimer-title>
  <base-disclaimer-content>
    Objektorientierte Programmierung (OOP) ist ein Programmierparadigma, das auf dem Konzept der „Objekte“ basiert, welche Daten und Code enthalten können. Die Daten liegen in Form von Feldern vor (oft als Attribute oder Eigenschaften bekannt) und der Code in Form von Prozeduren (oft als Methoden bekannt).
  </base-disclaimer-content>
</base-disclaimer>

## Kapselung (Encapsulation)

Kapselung ist eines der fundamentalen Konzepte der objektorientierten Programmierung, das hilft, die Daten und Methoden eines Objekts vor unbefugtem Zugriff und Modifikation zu schützen. Es ist eine Methode, um Datenabstraktion zu erreichen, was bedeutet, dass die Implementierungsdetails eines Objekts vor der Außenwelt verborgen bleiben und nur die wesentlichen Informationen offengelegt werden.

In Python kann Kapselung durch die Verwendung von Zugriffsmodifikatoren erreicht werden. Zugriffsmodifikatoren sind Schlüsselwörter, die die Zugänglichkeit von Attributen und Methoden in einer Klasse definieren. Die drei in Python verfügbaren Zugriffsmodifikatoren sind öffentlich (public), privat (private) und geschützt (protected). Python verfügt jedoch nicht über eine explizite Methode zur Definition von Zugriffsmodifikatoren wie einige andere Programmiersprachen wie Java und C++. Stattdessen verwendet es die Konvention, Unterstrichpräfixe zu verwenden, um das Zugriffsniveau anzuzeigen.

Im gegebenen Codebeispiel hat die Klasse `MyClass` zwei Attribute, `_protected_var` und `__private_var`. `_protected_var` ist durch die Verwendung eines einzelnen Unterstrichpräfixes als geschützt gekennzeichnet. Dies bedeutet, dass auf das Attribut innerhalb der Klasse und ihrer Unterklassen zugegriffen werden kann, aber nicht außerhalb der Klasse. `__private_var` ist durch die Verwendung von zwei Unterstrichpräfixen als privat gekennzeichnet. Dies bedeutet, dass auf das Attribut nur innerhalb der Klasse und nicht außerhalb der Klasse zugegriffen werden kann, nicht einmal in ihren Unterklassen.

Wenn wir ein Objekt der Klasse `MyClass` erstellen, können wir auf das Attribut `_protected_var` über den Objektnamen mit einem einzelnen Unterstrichpräfix zugreifen. Wir können jedoch nicht auf das Attribut `__private_var` über den Objektnamen zugreifen, da es vor der Außenwelt verborgen ist. Wenn wir versuchen, auf das Attribut `__private_var` zuzugreifen, erhalten wir einen `AttributeError`, wie im Code gezeigt.

Zusammenfassend lässt sich sagen, dass Kapselung ein wichtiges Konzept in der objektorientierten Programmierung ist, das hilft, die Implementierungsdetails eines Objekts zu schützen. In Python können wir Kapselung durch die Verwendung von Zugriffsmodifikatoren und Unterstrichpräfixen zur Angabe des Zugriffsniveaus erreichen.

```python
# Define a class named MyClass
class MyClass:

    # Constructor method that initializes the class object
    def __init__(self):

        # Define a protected variable with an initial value of 10
        # The variable name starts with a single underscore, which indicates protected access
        self._protected_var = 10

        # Define a private variable with an initial value of 20
        # The variable name starts with two underscores, which indicates private access
        self.__private_var = 20

# Create an object of MyClass class
obj = MyClass()

# Access the protected variable using the object name and print its value
# The protected variable can be accessed outside the class but
# it is intended to be used within the class or its subclasses
print(obj._protected_var)   # output: 10

# Try to access the private variable using the object name and print its value
# The private variable cannot be accessed outside the class, even by its subclasses
# This will raise an AttributeError because the variable is not accessible outside the class
print(obj.__private_var)    # AttributeError: 'MyClass' object has no attribute '__private_var'

```

<base-quiz>
<base-quiz-question correct="B">
<template #question>
How do you indicate a protected variable in Python?
</template>

<base-quiz-option value="A">A. Two underscores prefix: <code>**variable</code></base-quiz-option>
<base-quiz-option value="B" correct>B. Single underscore prefix: <code>_variable</code></base-quiz-option>
<base-quiz-option value="C">C. No underscore needed</base-quiz-option>
<base-quiz-option value="D">D. Three underscores prefix: <code>_**variable</code></base-quiz-option>
<base-quiz-answer value="B">In Python, a single underscore prefix (<code>\_variable</code>) indicates a protected variable, which is a convention meaning it should be used within the class or its subclasses. Two underscores (<code>\_\_variable</code>) indicate a private variable.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Vererbung (Inheritance)

Vererbung fördert die Wiederverwendung von Code und ermöglicht es Ihnen, eine Hierarchie von Klassen zu erstellen, die gemeinsame Attribute und Methoden teilen. Sie hilft dabei, sauberen und organisierten Code zu erstellen, indem zusammengehörige Funktionalitäten an einem Ort gehalten und das Konzept der Modularität gefördert wird. Die Basisklasse, von der eine neue Klasse abgeleitet wird, wird auch als Elternklasse bezeichnet, und die neue Klasse wird als Kindklasse oder Unterklasse bezeichnet.

Im Code definieren wir eine Klasse namens `Animal`, die eine Konstruktormethode hat, die das Klassenobjekt mit einem `name`-Attribut und einer Methode namens `speak` initialisiert. Die Methode `speak` ist in der Klasse `Animal` definiert, hat aber keinen Körper.

Anschließend definieren wir zwei Unterklassen namens `Dog` und `Cat`, die von der Klasse `Animal` erben. Diese Unterklassen überschreiben die Methode `speak` der Klasse `Animal`.

Wir erstellen ein `Dog`-Objekt mit dem Attributnamen "Rover" und ein `Cat`-Objekt mit dem Attributnamen "Whiskers". Wir rufen die Methode `speak` des `Dog`-Objekts mit `dog.speak()` auf, und es wird "Woof!" ausgegeben, weil die Methode `speak` der Klasse `Dog` die Methode `speak` der Klasse `Animal` überschreibt. In ähnlicher Weise rufen wir die Methode `speak` des `Cat`-Objekts mit `cat.speak()` auf, und es wird "Meow!" ausgegeben, weil die Methode `speak` der Klasse `Cat` die Methode `speak` der Klasse `Animal` überschreibt.

```python
# Define a class named Animal
class Animal:

    # Constructor method that initializes the class object with a name attribute
    def __init__(self, name):
        self.name = name

    # Method that is defined in the Animal class but does not have a body
    # This method will be overridden in the subclasses of Animal
    def speak(self):
        print("")

# Define a subclass named Dog that inherits from the Animal class
class Dog(Animal):

    # Override the speak method of the Animal class
    def speak(self):
        print("Woof!")

# Define a subclass named Cat that inherits from the Animal class
class Cat(Animal):

    # Override the speak method of the Animal class
    def speak(self):
        print("Meow!")

# Create a Dog object with a name attribute "Rover"
dog = Dog("Rover")

# Create a Cat object with a name attribute "Whiskers"
cat = Cat("Whiskers")

# Call the speak method of the Dog class and print the output
# The speak method of the Dog class overrides the speak method of the Animal class
# Therefore, when we call the speak method of the Dog object, it will print "Woof!"
dog.speak()   # output: Woof!

# Call the speak method of the Cat class and print the output
# The speak method of the Cat class overrides the speak method of the Animal class
# Therefore, when we call the speak method of the Cat object, it will print "Meow!"
cat.speak()   # output: Meow!

```

<base-quiz>
<base-quiz-question correct="A">
<template #question>
What is inheritance in Python OOP?
</template>

<base-quiz-option value="A" correct>A. A mechanism where a class can inherit attributes and methods from another class</base-quiz-option>
<base-quiz-option value="B">B. A way to copy objects</base-quiz-option>
<base-quiz-option value="C">C. A method to delete classes</base-quiz-option>
<base-quiz-option value="D">D. A built-in function</base-quiz-option>
<base-quiz-answer value="A">Inheritance allows a class (child/subclass) to inherit attributes and methods from another class (parent/base class). This promotes code reuse and allows you to create a hierarchy of classes.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Polymorphismus (Polymorphism)

Polymorphismus ist ein wichtiges Konzept in der objektorientierten Programmierung, das es ermöglicht, Code zu schreiben, der mit Objekten verschiedener Klassen auf einheitliche Weise arbeiten kann. In Python wird Polymorphismus durch die Verwendung von Methodenüberschreibung (Method Overriding) oder Methodenüberladung (Method Overloading) erreicht.

Methodenüberschreibung liegt vor, wenn eine Unterklasse ihre eigene Implementierung einer Methode bereitstellt, die bereits in ihrer Elternklasse definiert ist. Dies ermöglicht es der Unterklasse, das Verhalten der Methode zu ändern, ohne deren Namen oder Signatur zu ändern.

Methodenüberladung liegt vor, wenn mehrere Methoden denselben Namen, aber unterschiedliche Parameter haben. Python unterstützt Methodenüberladung nicht direkt, aber sie kann durch Standardargumente oder Argumente variabler Länge erreicht werden.

Polymorphismus erleichtert das Schreiben von flexiblem und wiederverwendbarem Code. Er ermöglicht es Ihnen, Code zu schreiben, der mit verschiedenen Objekten arbeiten kann, ohne deren spezifische Typen kennen zu müssen.

```python
#The Shape class is defined with an abstract area method, which is intended to be overridden by subclasses.
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    # The Rectangle class is defined with an __init__ method that initializes
    # width and height instance variables.
    # It also defines an area method that calculates and returns
    # the area of a rectangle using the width and height instance variables.
    def __init__(self, width, height):
        self.width = width  # Initialize width instance variable
        self.height = height  # Initialize height instance variable

    def area(self):
        return self.width * self.height  # Return area of rectangle


 # The Circle class is defined with an __init__ method
 # that initializes a radius instance variable.
 # It also defines an area method that calculates and
 # returns the area of a circle using the radius instance variable.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Initialize radius instance variable

    def area(self):
        return 3.14 * self.radius ** 2  # Return area of circle using pi * r^2

# The shapes list is created with one Rectangle object and one Circle object. The for
# loop iterates over each object in the list and calls the area method of each object
# The output will be the area of the rectangle (20) and the area of the circle (153.86).
shapes = [Rectangle(4, 5), Circle(7)]  # Create a list of Shape objects
for shape in shapes:
    print(shape.area())  # Output the area of each Shape object

```

<base-quiz>
<base-quiz-question correct="C">
<template #question>
What is polymorphism in Python OOP?
</template>

<base-quiz-option value="A">A. Creating multiple classes with the same name</base-quiz-option>
<base-quiz-option value="B">B. Hiding implementation details</base-quiz-option>
<base-quiz-option value="C" correct>C. The ability to use objects of different classes in a uniform way through a common interface</base-quiz-option>
<base-quiz-option value="D">D. Copying objects</base-quiz-option>
<base-quiz-answer value="C">Polymorphism allows you to write code that can work with objects of different classes in a uniform way. Different classes can implement the same method name, and Python will call the appropriate implementation based on the object's type.</base-quiz-answer>
</base-quiz-question>
</base-quiz>

## Abstraktion (Abstraction)

Abstraktion ist ein wichtiges Konzept in der objektorientierten Programmierung (OOP), da es Ihnen ermöglicht, sich auf die wesentlichen Merkmale eines Objekts oder Systems zu konzentrieren und dabei Details zu ignorieren, die für den aktuellen Kontext nicht relevant sind. Durch die Reduzierung der Komplexität und das Verbergen unnötiger Details kann Abstraktion dazu beitragen, Code modularer, leichter lesbar und einfacher zu warten zu machen.

In Python kann Abstraktion durch die Verwendung von abstrakten Klassen oder Schnittstellen (Interfaces) erreicht werden. Eine abstrakte Klasse ist eine Klasse, die nicht direkt instanziiert werden kann, sondern von anderen Klassen abgeleitet werden soll. Sie enthält oft abstrakte Methoden ohne Implementierung, die eine Vorlage dafür bieten, wie die Unterklasse implementiert werden soll. Dies ermöglicht es dem Programmierer, eine gemeinsame Schnittstelle für eine Gruppe verwandter Klassen zu definieren und jeder Klasse dennoch ihr eigenes spezifisches Verhalten zu ermöglichen.

Eine Schnittstelle hingegen ist eine Sammlung von Methodensignaturen, die eine Klasse implementieren muss, um als „kompatibel“ mit der Schnittstelle zu gelten. Schnittstellen werden oft verwendet, um eine gemeinsame Reihe von Methoden zu definieren, die mehrere Klassen implementieren können, wodurch sie in bestimmten Kontexten austauschbar verwendet werden können.

Python unterstützt abstrakte Klassen oder Schnittstellen nicht nativ, aber sie können mithilfe des `abc` (abstract base class) Moduls implementiert werden. Dieses Modul stellt die Klasse `ABC` und den Dekorator `abstractmethod` bereit, die zur Definition abstrakter Klassen und Methoden verwendet werden können.

Insgesamt ist Abstraktion ein mächtiges Werkzeug zur Verwaltung von Komplexität und zur Verbesserung der Codequalität in der objektorientierten Programmierung, und Python bietet eine Reihe von Optionen zur Erreichung von Abstraktion in Ihrem Code.

```python
# Import the abc module to define abstract classes and methods
from abc import ABC, abstractmethod

# Define an abstract class called Shape that has an abstract method called area
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Define a Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implement the area method for Rectangles
    def area(self):
        return self.width * self.height

# Define a Circle class that also inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implement the area method for Circles
    def area(self):
        return 3.14 * self.radius ** 2

# Create a list of shapes that includes both Rectangles and Circles
shapes = [Rectangle(4, 5), Circle(7)]

# Loop through each shape in the list and print its area
for shape in shapes:
    print(shape.area())

```

Dies sind einige der grundlegenden OOP-Prinzipien in Python. Diese Seite wird derzeit überarbeitet und es werden bald detailliertere Beispiele und Erklärungen folgen.

## Relevante Links

- <router-link to="/cheatsheet/functions">Funktionen</router-link>
- <router-link to="/cheatsheet/decorators">Dekoratoren</router-link>
- <router-link to="/cheatsheet/exception-handling">Fehlerbehandlung</router-link>
- <router-link to="/cheatsheet/dataclasses">Dataclasses</router-link>
- <router-link to="/builtin/object">object()</router-link>
- <router-link to="/builtin/classmethod">classmethod()</router-link>
- <router-link to="/builtin/staticmethod">staticmethod()</router-link>
- <router-link to="/builtin/property">property()</router-link>
- <router-link to="/builtin/isinstance">isinstance()</router-link>
- <router-link to="/builtin/issubclass">issubclass()</router-link>
- <router-link to="/builtin/super">super()</router-link>
