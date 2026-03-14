#!/usr/bin/env python3
"""
变量声明 - Java vs Python 对比

Java (静态类型):
    int age = 25;
    String name = "Alice";
    double salary = 5000.50;
    boolean isActive = true;

Python (动态类型):
    age = 25              # int
    name = "Alice"        # str
    salary = 5000.50      # float
    is_active = True      # bool (注意：Python用True/False，不是true/false)

关键差异:
- Java: 先声明类型，再赋值
- Python: 直接赋值，类型由值自动推断
- Python变量名用snake_case，Java用camelCase
"""

age = 25
name = "Alice"
salary = 5000.50
is_active = True

print(f"年龄: {age}, 类型: {type(age)}")
print(f"姓名: {name}, 类型: {type(name)}")
print(f"薪资: {salary}, 类型: {type(salary)}")
print(f"激活: {is_active}, 类型: {type(is_active)}")

# 多个变量同时赋值
x, y, z = 1, 2, 3
a = b = c = 0  # 多个变量指向同一个值

# 类型注解 (类似Java的类型声明，但只是提示)
age: int = 25
name: str = "Alice"
salary: float = 5000.50

# 检查类型
print(f"\n类型检查:")
print(f"isinstance(age, int): {isinstance(age, int)}")
print(f"isinstance(name, str): {isinstance(name, str)}")

# 变量交换 (Java需要临时变量，Python一行搞定)
a, b = 10, 20
a, b = b, a  # 直接交换
print(f"\n交换后: a={a}, b={b}")
