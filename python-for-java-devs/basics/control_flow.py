#!/usr/bin/env python3
"""
流程控制 - Java vs Python 对比

关键差异:
- if/elif/else: Python用elif，Java用else if
- for循环: Python用for-in，Java用for(;;)或for-each
- while循环: 基本相同
- switch: Python没有switch，用字典或match-case(Python 3.10+)

Java:                      Python:
if (condition) {           if condition:
    ...                        ...
} else if (cond2) {        elif cond2:
    ...                        ...
} else {                   else:
    ...                        ...
}

for (int i=0; i<n; i++)    for i in range(n):
    ...                         ...

for (int item : array)    for item in array:
    ...                         ...
"""

# if-elif-else
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"分数: {score}, 等级: {grade}")

# 简化的条件表达式
age = 20
category = "成人" if age >= 18 else "未成年"
print(f"年龄: {age}, 类别: {category}")

# match-case (Python 3.10+, 类似switch)
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown"

print(f"\nHTTP状态码: {http_status(200)}, {http_status(404)}")

# for循环 - Python的for是for-each
print("\n=== for循环示例 ===")

# range()生成序列
print("range(5):", list(range(5)))
print("range(1, 6):", list(range(1, 6)))
print("range(0, 10, 2):", list(range(0, 10, 2)))

# 遍历列表
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"水果: {fruit}")

# 遍历字符串
for char in "Python":
    print(f"字符: {char}")

# 带索引的遍历
for index, fruit in enumerate(fruits):
    print(f"索引 {index}: {fruit}")

# while循环
print("\n=== while循环示例 ===")
count = 0
while count < 5:
    print(f"count = {count}")
    count += 1

# break和continue (与Java相同)
print("\n=== break和continue ===")
for i in range(10):
    if i == 3:
        continue  # 跳过本次循环
    if i == 7:
        break     # 跳出循环
    print(i, end=" ")
print()

# pass (Python特有，占位符)
def empty_function():
    name = 56
    print(f"我是谁{name}")
empty_function()
# 循环的else (Python特有，循环正常结束时会执行)
print("\n=== 循环的else ===")
for i in range(3):
    print(f"迭代 {i}")
else:
    print("循环正常完成")

# 列表推导式 (Python特有，类似Java的Stream)
print("\n=== 列表推导式 ===")
squares = [x**2 for x in range(1, 6)]
print(f"平方数: {squares}")

even_squares = [x**2 for x in range(1, 6) if x % 2 == 0]
print(f"偶数的平方: {even_squares}")
