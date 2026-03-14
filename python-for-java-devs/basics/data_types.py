#!/usr/bin/env python3
"""
数据类型 - Java vs Python 对比

Java基本类型:
    byte, short, int, long
    float, double
    char
    boolean

Python基本类型:
    int (整数，无限精度)
    float (浮点数)
    str (字符串)
    bool (布尔值)
    None (类似Java的null)

关键差异:
- Python没有char类型，用长度为1的字符串
- Python的int是无限精度的
- Python用None表示空值，不是null
"""

# 整数 - Python int无大小限制
python_int = 12345678901234567890
java_int_max = 2147483647
print(f"Python整数: {python_int}")
print(f"Java int最大值: {java_int_max}")

# 浮点数
pi = 3.14159
print(f"圆周率: {pi}")

# 字符串
text = "Hello Python"
print(f"字符串: {text}")
print(f"字符串长度: {len(text)}")
print(f"首字母大写: {text.capitalize()}")
print(f"替换: {text.replace('Python', 'World')}")

# 布尔值 (注意：首字母大写)
is_python_fun = True
is_java_fun = False
print(f"\n布尔值: is_python_fun={is_python_fun}, is_java_fun={is_java_fun}")

# None (类似Java的null)
nothing = None
print(f"None值: {nothing}")
print(f"检查None: {nothing is None}")

# 类型转换 (类似Java但语法不同)
num_str = "123"
int_num = int(num_str)          # String -> int
float_num = float(num_str)      # String -> float
str_num = str(123)              # int -> String
bool_val = bool(1)              # 非零为True
print(f"\n类型转换:")
print(f"int('123') = {int_num}")
print(f"float('123') = {float_num}")
print(f"str(123) = {str_num}")
print(f"bool(1) = {bool_val}")
print(f"bool(0) = {bool(0)}")

# 强制类型转换与Java类似
print(f"\n强制类型转换示例:")
print(f"int(3.7) = {int(3.7)}")  # 向下取整
print(f"round(3.7) = {round(3.7)}")  # 四舍五入
