#!/usr/bin/env python3
"""
Hello World - Java vs Python 对比

Java:
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

Python:
print("Hello, World!")

关键差异:
- Java需要类和方法包装，Python直接执行
- Python无需main方法（但可以用if __name__ == "__main__"）
"""

print("Hello, World!")
print("你好，Python!")

# 多行输出
print("第一行", "第二行", "第三行")

# 格式化输出
name = "Java开发者"
age = 5
print(f"我是{name}，学习Python已经{age}年了")

# 传统格式化（类似Java的String.format）
print("我是{}，学习Python已经{}年了".format(name, age))
