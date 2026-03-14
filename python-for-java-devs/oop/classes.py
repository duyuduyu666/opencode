#!/usr/bin/env python3
"""
类定义 - Java vs Python 对比

关键差异:
- class关键字后直接跟类名
- 构造函数是__init__，不是类名
- 所有实例方法第一个参数必须是self (类似Java的this)
- 属性无需声明，直接在__init__中赋值
- 没有public/private关键字，用_或__表示访问控制

Java:                          Python:
public class Person {          class Person:
    private String name;           def __init__(self, name):
    private int age;                   self.name = name
                                       self.age = age
    public Person(String name,         def greet(self):
        int age) {                         print(f"Hello, I'm {self.name}")
        this.name = name;
        this.age = age;
    }

    public void greet() {
        System.out.println("Hello");
    }
}
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, I'm {self.name}, {self.age} years old"
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

person1 = Person("Alice", 25)
print(person1)
print(person1.greet())
print(f"姓名: {person1.name}")
print(f"年龄: {person1.age}")

# 访问控制 (Python约定)
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # 受保护属性，单下划线约定
        self.__pin = "1234"      # 私有属性，双下划线会名称改编
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

account = BankAccount(1000)
print(f"\n账户余额: {account.get_balance()}")
account.deposit(500)
print(f"存款后余额: {account.get_balance()}")
account.withdraw(200)
print(f"取款后余额: {account.get_balance()}")

# 类属性 vs 实例属性
class Circle:
    pi = 3.14159  # 类属性，所有实例共享
    
    def __init__(self, radius=1):
        self.radius = radius  # 实例属性
    
    def area(self):
        return Circle.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * Circle.pi * self.radius

c1 = Circle(5)
c2 = Circle(2)
print(f"\n圆1半径: {c1.radius}, 面积: {c1.area():.2f}")
print(f"圆2半径: {c2.radius}, 面积: {c2.area():.2f}")
print(f"类属性pi: {Circle.pi}")

# 类方法 和 静态方法
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def create_zero(cls):
        return cls()

print(f"\n静态方法: MathUtils.add(3, 5) = {MathUtils.add(3, 5)}")

# 运算符重载
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(f"\nv1 + v2 = {v1 + v2}")
print(f"v1 * 3 = {v1 * 3}")
