#!/usr/bin/env python3
"""
集合 (Set) - Java vs Python 对比

Java:                              Python:
Set<String> set =                  fruits = {"apple", "banana", "orange"}
    new HashSet<>();             
set.add("apple");                  fruits.add("grape")

HashSet, TreeSet, LinkedHashSet   set, frozenset

关键差异:
- set是可变集合，frozenset是不可变集合
- 集合操作语法更简洁
- 无序但可迭代
"""

# 创建集合
fruits = {"apple", "banana", "orange"}
print(f"集合: {fruits}")

# 添加元素
fruits.add("grape")
print(f"添加后: {fruits}")

# 添加多个元素
fruits.update(["mango", "pear"])
print(f"update后: {fruits}")

# 删除元素
fruits.remove("banana")  # 不存在会抛异常
print(f"remove后: {fruits}")

fruits.discard("cherry")  # 不存在不会抛异常
print(f"discard后: {fruits}")

# 集合操作
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"\nset1: {set1}")
print(f"set2: {set2}")

# 并集
union = set1 | set2
union2 = set1.union(set2)
print(f"并集: {union}")

# 交集
intersection = set1 & set2
intersection2 = set1.intersection(set2)
print(f"交集: {intersection}")

# 差集 (set1中有但set2中没有的)
difference = set1 - set2
difference2 = set1.difference(set2)
print(f"差集: {difference}")

# 对称差集 (不同时在两个集合中的)
sym_diff = set1 ^ set2
sym_diff2 = set1.symmetric_difference(set2)
print(f"对称差集: {sym_diff}")

# 子集和超集
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

print(f"\nset_a: {set_a}")
print(f"set_b: {set_b}")
print(f"set_a是set_b的子集: {set_a.issubset(set_b)}")
print(f"set_b是set_a的超集: {set_b.issuperset(set_a)}")

# 集合推导式
squares = {x**2 for x in range(1, 6)}
print(f"\n平方数集合: {squares}")

even = {x for x in range(10) if x % 2 == 0}
print(f"偶数集合: {even}")

# frozenset (不可变集合)
fs = frozenset([1, 2, 3])
print(f"\nfrozenset: {fs}")
# fs.add(4)  # 会报错

# 检查元素
print(f"\n1 in set1: {1 in set1}")
print(f"10 in set1: {10 in set1}")

# 清空集合
set3 = {1, 2, 3}
set3.clear()
print(f"\n清空后: {set3}")

# 去重
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = set(numbers)
print(f"\n原始: {numbers}")
print(f"去重: {unique}")

# 集合去重并保持顺序 (Python 3.7+)
# 使用dict.fromkeys
unique_ordered = list(dict.fromkeys(numbers))
print(f"去重保持顺序: {unique_ordered}")
