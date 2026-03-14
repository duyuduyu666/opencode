# Java开发者Python学习项目

本项目专为有Java背景的开发者设计，通过对比Java和Python的语法差异，帮助快速掌握Python。

## 项目结构

```
python-for-java-devs/
├── README.md
├── basics/              # 基础语法对比
│   ├── hello_world.py
│   ├── variables.py
│   ├── data_types.py
│   ├── operators.py
│   ├── control_flow.py
│   └── functions.py
├── oop/                # 面向对象编程
│   ├── classes.py
│   ├── inheritance.py
│   ├── polymorphism.py
│   └── interfaces.py
├── data_structures/    # 数据结构
│   ├── lists.py
│   ├── dictionaries.py
│   ├── sets.py
│   └── tuples.py
├── exercises/          # 练习项目
│   ├── exercise1.py
│   ├── exercise2.py
│   └── project/
└── requirements.txt
```

## 学习路线

1. **基础语法** - 变量、数据类型、运算符、流程控制、函数
2. **面向对象** - 类、继承、多态、接口/抽象类
3. **数据结构** - 列表、字典、集合、元组
4. **实战练习** - 简单的Python项目实践

## 运行方式

```bash
# 运行单个文件
python basics/hello_world.py

# 安装依赖（如有）
pip install -r requirements.txt
```

## 核心差异速查

| 特性 | Java | Python |
|------|------|--------|
| 类型声明 | 静态类型 `int a = 1` | 动态类型 `a = 1` |
| 代码块 | `{}` 大括号 | 缩进 |
| 方法定义 | `public void foo()` | `def foo(self):` |
| 继承 | `extends` | 无关键字，直接写父类 |
| 接口 | `interface` | 使用抽象类或Protocol |
| 字符串 | `String` | `str` |
| 循环 | `for(int i=0; i<n; i++)` | `for i in range(n)` |
