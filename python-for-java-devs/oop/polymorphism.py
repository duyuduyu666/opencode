#!/usr/bin/env python3
"""
多态 - Java vs Python 对比

关键差异:
- Python是duck typing，类型检查更宽松
- 不需要显式声明接口
- 方法签名可以不同 (Python的灵活性)

Java:                              Python:
void process(List<Animal> animals) def process_animals(animals):
for (Animal a : animals) {              for animal in animals:
    a.speak();                              animal.speak()
}                                      }

(需要Animal是同一类型或接口实现)    (只要有speak方法即可)
"""

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("子类必须实现speak方法")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

def make_speak(animals):
    """多态: 同一种调用，不同的行为"""
    for animal in animals:
        print(f"{animal.name} says: {animal.speak()}")

animals = [
    Dog("Buddy"),
    Cat("Whiskers"),
    Cow("Bessie")
]

make_speak(animals)

# Duck Typing示例
class Robot:
    def speak(self):
        return "Beep boop!"

class Person:
    def speak(self):
        return "Hello!"

def greet(obj):
    print(f"问候: {obj.speak()}")

print("\nDuck Typing:")
greet(Dog("Rex"))      # 有speak方法就可以
greet(Robot("R2D2"))  # 不需要继承关系
greet(Person("Tom"))   # 同样可以

# 运算符多态
class Number:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        return Number(self.value + other)
    
    def __str__(self):
        return str(self.value)

n1 = Number(10)
n2 = Number(20)
n3 = n1 + n2
print(f"\nn1 + n2 = {n3.value}")
n4 = n1 + 5
print(f"n1 + 5 = {n4.value}")

# 方法重写
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

def print_area(shape):
    print(f"面积: {shape.area():.2f}")

print("\n图形面积:")
print_area(Rectangle(5, 3))
print_area(Circle(4))
print_area(Shape())  # 0

# 抽象基类 (类似Java的抽象类)
from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def speak(self):
        pass
    
    def describe(self):
        return f"{self.name} makes sound: {self.speak()}"

class Duck(AbstractAnimal):
    def speak(self):
        return "Quack!"

duck = Duck("Donald")
print(f"\n抽象类示例:")
print(duck.describe())
