#!/usr/bin/env python3
"""
接口/抽象类 - Java vs Python 对比

Java中有interface关键字，Python中没有。

Python实现接口的方式:
1. 抽象基类 (Abstract Base Class) - abc模块
2. Protocol (Python 3.8+) - 结构子类型
3. duck typing - 不需要显式声明

Java:                              Python (方式1 - ABC):
public interface Drawable {         class Drawable(ABC):
    void draw();                        @abstractmethod
}                                       def draw(self): pass

public class Circle                 class Circle(Drawable):
    implements Drawable {               def draw(self):
    @Override                               print("Drawing circle")
    public void draw() {               }
        // ...
    }
}
"""

from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass
    
    def description(self):
        return "A drawable object"

class Circle(Drawable):
    def draw(self):
        print("Drawing circle")

class Square(Drawable):
    def draw(self):
        print("Drawing square")

def render_shape(drawable):
    drawable.draw()

print("=== 抽象基类示例 ===")
render_shape(Circle())
render_shape(Square())

# Protocol (Python 3.8+) - 类似Java接口
from typing import Protocol

class Printable(Protocol):
    def print_data(self) -> str:
        ...

class Report:
    def print_data(self) -> str:
        return "Printing report"

class DataLogger:
    def print_data(self) -> str:
        return "Logging data"

def process(processor: Printable):
    print(processor.print_data())

print("\n=== Protocol示例 ===")
process(Report())
process(DataLogger())

# 组合多个"接口"
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return "Quack!"
    
    def fly(self):
        return f"{self.name} is flying"
    
    def swim(self):
        return f"{self.name} is swimming"

print("\n=== 多接口示例 ===")
duck = Duck("Donald")
print(duck.speak())
print(duck.fly())
print(duck.swim())

# 检查是否实现接口
print(f"\nisinstance(duck, Flyable): {isinstance(duck, Flyable)}")
print(f"isinstance(duck, Swimmable): {isinstance(duck, Swimmable)}")

# Mixin (Python特有的多重继承模式)
class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {message}")

class DatabaseMixin:
    def save(self):
        print("Saving to database")

class User(LoggerMixin, DatabaseMixin):
    def __init__(self, name):
        self.name = name
    
    def create(self):
        self.log(f"Creating user: {self.name}")
        self.save()

print("\n=== Mixin示例 ===")
user = User("Alice")
user.create()
