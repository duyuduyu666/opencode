#!/usr/bin/env python3
"""
运算符 - Java vs Python 对比

大部分运算符是相同的，但有一些差异:
- 整数除法: Java用/得到整数，Python3用/得到浮点数
- 幂运算: Java用Math.pow()，Python用**
- 取整除法: Python用//
- 位运算: 语法相同，但无>>><<<运算符

Java:                Python:
+ - * /              + - * / **
%                    %
++ --                +=1 -=1 (无++/--运算符)
< > <= >=            相同
== !=                相同
&& || !              and or not
& | ^ ~              相同
<< >>                相同
?: (三元运算符)      result = x if condition else y
"""

# 算术运算符
a, b = 10, 3
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")        # Python3返回float
print(f"a // b = {a // b}")      # 整除
print(f"a % b = {a % b}")        # 取余
print(f"a ** b = {a ** b}")      # 幂运算 (Java: Math.pow(a, b))

# 比较运算符 (相同)
print(f"\na > b: {a > b}")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")

# 逻辑运算符 (注意: 使用单词)
x, y = True, False
print(f"\nx = {x}, y = {y}")
print(f"x and y: {x and y}")    # && 
print(f"x or y: {x or y}")       # ||
print(f"not x: {not x}")         # !

# 三元运算符 (Java: condition ? true_val : false_val)
# Python: true_val if condition else false_val
age = 20
status = "成年人" if age >= 18 else "未成年人"
print(f"\n三元运算符: age={age}, status={status}")

# 位运算符 (相同)
c, d = 8, 4  # 1000 & 0100 = 0000
print(f"\nc = {c}, d = {d}")
print(f"c & d (AND): {c & d}")
print(f"c | d (OR): {c | d}")
print(f"c ^ d (XOR): {c ^ d}")
print(f"~c (NOT): {~c}")
print(f"c << 1 (左移): {c << 1}")
print(f"c >> 1 (右移): {c >> 1}")

# 赋值运算符
e = 10
e += 5  # e = e + 5
print(f"\ne += 5: {e}")
e -= 3
print(f"e -= 3: {e}")
e *= 2
print(f"e *= 2: {e}")
e /= 4
print(f"e /= 4: {e}")

# 身份运算符 (检查是否是同一个对象)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"\n身份运算符:")
print(f"list1 is list2: {list1 is list2}")  # False，内容相同但不同对象
print(f"list1 is list3: {list1 is list3}")  # True，同一个对象
print(f"list1 is not list2: {list1 is not list2}")

# 成员运算符 (Python特有)
fruits = ["apple", "banana", "orange"]
print(f"\n成员运算符:")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")
