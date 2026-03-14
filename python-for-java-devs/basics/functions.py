#!/usr/bin/env python3
"""
函数 - Java vs Python 对比

关键差异:
- 定义关键字: def (Java用返回类型)
- 参数: 无需类型声明，可有默认值
- 返回值: return (Java用方法名声明返回类型)
- 可变参数: *args (类似Java的VarArgs ...)
- 关键字参数: **kwargs
- 没有方法重载，但有默认参数和*args

Java:                           Python:
public int add(int a, int b) {  def add(a, b):
    return a + b;                   return a + b
}                               }

public void print(String msg)   def print_msg(msg="Hello"):
{                                   print(msg)
    System.out.println(msg);
}
"""

# 基本函数定义
def greet(name):
    return f"Hello, {name}!"

print(greet("Python"))

# 带默认参数的函数
def greet_with_default(name="World"):
    return f"Hello, {name}!"

print(greet_with_default())
print(greet_with_default("Alice"))

# 多参数函数
def add(a, b):
    return a + b

def subtract(a, b=0, c=0):
    return a - b - c

print(f"\nadd(3, 5) = {add(3, 5)}")
print(f"subtract(10, 3) = {subtract(10, 3)}")
print(f"subtract(10, 3, 2) = {subtract(10, 3, 2)}")

# 可变参数 (*args类似Java的VarArgs)
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"\nsum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")

# 关键字参数
def introduce(name, age, city="Beijing"):
    return f"我叫{name}，今年{age}岁，来自{city}"

print(f"\n{introduce('Alice', 25)}")
print(f"{introduce('Bob', 30, city='Shanghai')}")
print(f"{introduce(age=28, name='Charlie')}")

# **kwargs (关键字可变参数)
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print("\n")
print_info(name="Alice", age=25, city="Beijing")

# 函数作为参数
def apply_operation(a, b, operation):
    return operation(a, b)

def multiply(x, y):
    return x * y

print(f"\napply_operation(3, 4, multiply) = {apply_operation(3, 4, multiply)}")

# Lambda表达式 (类似Java的Lambda)
square = lambda x: x ** 2
print(f"square(5) = {square(5)}")

add_numbers = lambda x, y: x + y
print(f"add_numbers(3, 7) = {add_numbers(3, 7)}")

# Lambda与内置函数结合
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"\n原始列表: {numbers}")
print(f"平方后: {squared}")

filtered = list(filter(lambda x: x > 3, numbers))
print(f"过滤大于3: {filtered}")

# 递归函数
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"\n5! = {factorial(5)}")

# 装饰器 (Python特有)
def my_decorator(func):
    def wrapper():
        print("调用函数前")
        func()
        print("调用函数后")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

print("\n装饰器示例:")
say_hello()

# 生成器 (Python特有)
def count_up_to(max_val):
    count = 1
    while count <= max_val:
        yield count
        count += 1

print("\n生成器示例:")
for num in count_up_to(5):
    print(num, end=" ")
print()
