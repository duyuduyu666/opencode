#!/usr/bin/env python3
"""
字典 (Dictionary) - Java vs Python 对比

Java:                              Python:
Map<String, Integer> map =         scores = {
    new HashMap<>();                    "Alice": 90,
map.put("Alice", 90);                  "Bob": 85
int score = map.get("Alice");      }                              
                                  score = scores["Alice"]
HashMap, TreeMap, LinkedHashMap    dict, collections.OrderedDict

关键差异:
- Python字典是哈希表实现
- 键可以是任何不可变类型
- 语法更简洁
- 内置丰富方法
"""

# 创建字典
scores = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 92
}
print(f"字典: {scores}")

# 访问值
print(f"Alice的分数: {scores['Alice']}")
print(f"Bob的分数: {scores.get('Bob')}")

# get的安全访问
print(f"不存在的键: {scores.get('David', 0)}")  # 默认值

# 修改字典
scores["Bob"] = 88  # 更新
print(f"\n更新后: {scores}")

scores["David"] = 78  # 添加
print(f"添加后: {scores}")

del scores["Alice"]  # 删除
print(f"删除后: {scores}")

# 遍历字典
print("\n遍历字典:")
for key in scores:
    print(f"{key}: {scores[key]}")

for key, value in scores.items():
    print(f"学生: {key}, 分数: {value}")

# 字典推导式
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

name_to_age = {name: age for name, age in zip(names, ages)}
print(f"\n姓名到年龄: {name_to_age}")

# 嵌套字典
students = {
    "Alice": {"age": 25, "score": 90},
    "Bob": {"age": 30, "score": 85}
}
print(f"\n嵌套字典: {students}")
print(f"Alice的分数: {students['Alice']['score']}")

# 合并字典
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}  # b会被dict2覆盖
print(f"\n合并: {merged}")

# 常用方法
print(f"\nkeys: {list(scores.keys())}")
print(f"values: {list(scores.values())}")
print(f"items: {list(scores.items())}")

# fromkeys
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
print(f"\nfromkeys: {default_dict}")

# setdefault
d = {"a": 1}
d.setdefault("b", 2)
d.setdefault("a", 99)  # 不覆盖已存在的
print(f"setdefault: {d}")

# pop和popitem
d = {"a": 1, "b": 2, "c": 3}
popped = d.pop("a")
print(f"\npop('a'): {popped}, 剩余: {d}")
popped_item = d.popitem()
print(f"popitem(): {popped_item}, 剩余: {d}")

# update
d1 = {"a": 1}
d2 = {"b": 2}
d1.update(d2)
d1.update(c=3, d=4)
print(f"update后: {d1}")

# defaultdict (需要导入)
from collections import defaultdict
dd = defaultdict(int)  # 默认值为0
dd["a"] += 1
print(f"\ndefaultdict: {dd}")
