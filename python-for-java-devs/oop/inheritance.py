#!/usr/bin/env python3
"""
继承 - Java vs Python 对比

关键差异:
- 定义时直接在类名后加(父类名)
- super()调用父类，无需传递self
- 可以多重继承 (Java只能单继承+多接口)
- 方法重写完全一样

Java:                              Python:
class Dog extends Animal {         class Dog(Animal):
    @Override                          def bark(self):
    public void bark() {                  print("Woof!")
        System.out.println("Woof!");   }
    }
}
"""

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        return "Some sound"
    
    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age})"

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # 调用父类构造函数
        self.breed = breed
    
    def speak(self):
        return "Woof!"
    
    def fetch(self):
        return f"{self.name} fetches the ball"

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Tweet!"

dog = Dog("Buddy", 3, "Golden Retriever")
cat = Cat("Whiskers", 2, "Orange")
bird = Bird("Tweety", 1)

print(dog)
print(f"叫声: {dog.speak()}")
print(f"{dog.fetch()}")
print()
print(cat)
print(f"叫声: {cat.speak()}")
print(f"毛色: {cat.color}")
print()
print(bird)
print(f"叫声: {bird.speak()}")

# isinstance和issubclass
print(f"\nisinstance(dog, Animal): {isinstance(dog, Animal)}")
print(f"issubclass(Dog, Animal): {issubclass(Dog, Animal)}")
print(f"isinstance(cat, Dog): {isinstance(cat, Dog)}")

# 多重继承
class Flyable:
    def fly(self):
        return f"{self.name} is flying"

class Bat(Animal, Flyable):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def speak(self):
        return "Screech!"

bat = Bat("Bruce", 2)
print(f"\n{bat}")
print(f"叫声: {bat.speak()}")
print(f"{bat.fly()}")

# MRO (方法解析顺序)
print(f"\nBat的MRO: {Bat.__mro__}")

# super()的其他用法
class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent构造函数: {name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # 只调用父类的__init__
        self.age = age
        print(f"Child构造函数: {age}")

print("\n多重继承:")
child = Child("Alice", 5)
