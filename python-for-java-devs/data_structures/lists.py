#!/usr/bin/env python3
"""
列表 (List) - Java vs Python 对比

Java:                              Python:
List<String> list =                fruits = ["apple", "banana", "orange"]
    new ArrayList<>();             
    list.add("apple");             # 直接创建

ArrayList vs LinkedList            list vs deque
                                  # List更灵活

关键差异:
- Python列表可以包含不同类型元素
- 支持负索引
- 内置函数丰富
- 切片操作
"""

fruits = ["apple", "banana", "orange"]
print(f"列表: {fruits}")
print(f"长度: {len(fruits)}")

# 访问元素 (支持负索引)
print(f"fruits[0] = {fruits[0]}")
print(f"fruits[-1] = {fruits[-1]}")

# 切片操作
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\nnumbers: {numbers}")
print(f"numbers[2:5] = {numbers[2:5]}")      # [2, 3, 4]
print(f"numbers[:5] = {numbers[:5]}")        # [0, 1, 2, 3, 4]
print(f"numbers[5:] = {numbers[5:]}")        # [5, 6, 7, 8, 9]
print(f"numbers[::2] = {numbers[::2]}")      # 步长2
print(f"numbers[::-1] = {numbers[::-1]}")    # 反转

# 修改列表
fruits[0] = "mango"
print(f"\n修改后: {fruits}")

fruits.append("grape")
print(f"append: {fruits}")

fruits.insert(1, "pear")
print(f"insert: {fruits}")

fruits.remove("banana")
print(f"remove: {fruits}")

popped = fruits.pop()
print(f"pop: {popped}, 剩余: {fruits}")

# 列表推导式
squares = [x**2 for x in range(1, 6)]
print(f"\n平方数: {squares}")

even_numbers = [x for x in range(10) if x % 2 == 0]
print(f"偶数: {even_numbers}")

# 列表操作
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"\n合并: {combined}")

repeated = [1, 2] * 3
print(f"重复: {repeated}")

# 排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\n原始: {numbers}")
numbers.sort()
print(f"排序后: {numbers}")

sorted_desc = sorted(numbers, reverse=True)
print(f"降序: {sorted_desc}")

# 列表方法
words = ["apple", "banana", "apple", "cherry", "banana"]
print(f"\nwords: {words}")
print(f"count('apple'): {words.count('apple')}")
print(f"index('banana'): {words.index('banana')}")
print(f"reverse: {words.reverse()}")

# List comprehension with condition
matrix = [[i*j for j in range(3)] for i in range(3)]
print(f"\n二维列表: {matrix}")

# zip - 合并多个列表
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
scores = [90, 85, 95]

for name, age, score in zip(names, ages, scores):
    print(f"{name}: {age}岁, 分数: {score}")

# any, all
print(f"\nany([False, True, False]): {any([False, True, False])}")
print(f"all([True, True, False]): {all([True, True, False])}")

# enumerate - 带索引的迭代
for index, fruit in enumerate(fruits):
    print(f"索引 {index}: {fruit}")
