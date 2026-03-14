#!/usr/bin/env python3
"""
元组 (Tuple) - Java vs Python 对比

Java:                              Python:
不支持原生元组，                  point = (10, 20)
可以用数组或List                 point[0], point[1]

关键差异:
- 元组是不可变的列表
- 可以用作字典的键
- 语法更简洁
- 支持解包
"""

# 创建元组
point = (10, 20)
print(f"元组: {point}")
print(f"类型: {type(point)}")

# 单元素元组需要逗号
single = (1,)  # 不是 (1)
print(f"\n单元素元组: {single}, 类型: {type(single)}")

# 访问元素
print(f"point[0] = {point[0]}")
print(f"point[-1] = {point[-1]}")

# 切片
numbers = (0, 1, 2, 3, 4, 5)
print(f"\nnumbers: {numbers}")
print(f"numbers[1:4] = {numbers[1:4]}")

# 元组解包 (类似Java的多变量赋值)
x, y = point
print(f"\n解包: x={x}, y={y}")

# 多个变量解包
a, b, c = (1, 2, 3)
print(f"a={a}, b={b}, c={c}")

# 使用*解包剩余元素
first, *middle, last = (1, 2, 3, 4, 5)
print(f"first={first}, middle={middle}, last={last}")

# 元组操作
t1 = (1, 2, 3)
t2 = (4, 5, 6)
combined = t1 + t2
print(f"\n合并: {combined}")

repeated = t1 * 3
print(f"重复: {repeated}")

# 元组方法
print(f"\nt1.count(2): {t1.count(2)}")
print(f"t1.index(2): {t1.index(2)}")

# 元组作为字典的键
location = {
    (35.6762, 139.6503): "Tokyo",
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}
print(f"\n元组作为键: {location}")

# 函数返回多个值 (返回元组)
def get_statistics(numbers):
    return min(numbers), max(numbers), sum(numbers)

min_val, max_val, total = get_statistics([1, 2, 3, 4, 5])
print(f"\n统计: min={min_val}, max={max_val}, sum={total}")

# 命名元组 (namedtuple)
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(f"\n命名元组: {p}")
print(f"p.x = {p.x}, p.y = {p.y}")
print(f"p[0] = {p[0]}, p[1] = {p[1]}")

# 元组 vs 列表
print(f"\n=== 元组 vs 列表 ===")
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

# 列表可变，元组不可变
# my_list.append(4)  # OK
# my_tuple.append(4)  # Error

print(f"列表大小: {my_list.__sizeof__()}")
print(f"元组大小: {my_tuple.__sizeof__()}")  # 元组更小

# 元组推导式 (生成器表达式，不是元组推导式)
gen = (x**2 for x in range(1, 6))
print(f"\n生成器: {gen}")
print(f"转换为元组: {tuple(gen)}")

# 元组比较
print(f"\n(1, 2) < (1, 3): {(1, 2) < (1, 3)}")
print(f"(1, 2) < (2, 1): {(1, 2) < (2, 1)}")
