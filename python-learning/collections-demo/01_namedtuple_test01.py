#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
namedtuple的用法示例
namedtuple是一个工厂函数，用于创建一个新的元组子类，并为每个元素指定一个名称
"""

from collections import namedtuple


def basic_usage():
    """基本用法：创建和使用命名元组"""
    # 创建一个名为'Point'的命名元组类，包含'x'和'y'两个字段
    Point = namedtuple('Point', ['x', 'y'])
    
    # 创建命名元组实例
    p1 = Point(10, 20)
    print(f"基本用法 - p1: {p1}")
    
    # 通过字段名访问元素
    print(f"p1.x = {p1.x}, p1.y = {p1.y}")
    
    # 通过索引访问元素（保持了元组的特性）
    print(f"p1[0] = {p1[0]}, p1[1] = {p1[1]}")
    
    # 解包操作（保持了元组的特性）
    x, y = p1
    print(f"解包: x = {x}, y = {y}")


def using_string_fields():
    """使用空格分隔的字符串来定义字段名"""
    # 使用空格分隔的字符串定义字段
    Rectangle = namedtuple('Rectangle', 'width height')
    
    r1 = Rectangle(100, 50)
    print(f"\n使用字符串字段 - r1: {r1}")
    print(f"面积: {r1.width * r1.height}")


def namedtuple_methods():
    """namedtuple的特殊方法"""
    Person = namedtuple('Person', ['name', 'age', 'city'])
    p = Person('Alice', 30, 'New York')
    
    # _fields: 返回字段名的元组
    print(f"\n字段名: {p._fields}")
    
    # _asdict(): 将命名元组转换为OrderedDict
    p_dict = p._asdict()
    print(f"转换为字典: {p_dict}")
    
    # _replace(): 创建一个新的实例，替换指定字段的值
    p_new = p._replace(age=31)
    print(f"替换后的实例: {p_new}")
    print(f"原实例不变: {p}")
    
    # _make(): 从可迭代对象创建实例
    p2 = Person._make(['Bob', 25, 'Boston'])
    print(f"通过_make创建实例: {p2}")


def inheritance_example():
    """继承命名元组创建子类"""
    # 基类
    Animal = namedtuple('Animal', ['name', 'species'])
    
    # 创建子类
    class Pet(Animal):
        def speak(self):
            if self.species == 'dog':
                return 'Woof!'
            elif self.species == 'cat':
                return 'Meow!'
            else:
                return '...'
    
    pet1 = Pet('Rex', 'dog')
    pet2 = Pet('Whiskers', 'cat')
    
    print(f"\n继承示例:")
    print(f"{pet1.name} says: {pet1.speak()}")
    print(f"{pet2.name} says: {pet2.speak()}")


def default_values():
    """为命名元组设置默认值"""
    # 方法1: 使用_replace设置默认值
    Node = namedtuple('Node', ['value', 'left', 'right'])
    Node.__new__.__defaults__ = (None, None, None)  # 设置默认值
    
    # 只提供部分参数
    n1 = Node(10)
    n2 = Node(20, n1)
    
    print(f"\n默认值示例:")
    print(f"n1: {n1}")
    print(f"n2: {n2}")


def main():
    """主函数，演示namedtuple的各种用法"""
    print("=== namedtuple用法示例 ===")
    
    # 调用各个示例函数
    basic_usage()
    using_string_fields()
    namedtuple_methods()
    inheritance_example()
    default_values()


if __name__ == "__main__":
    main()

"""
运行结果：
=== namedtuple用法示例 ===
基本用法 - p1: Point(x=10, y=20)
p1.x = 10, p1.y = 20
p1[0] = 10, p1[1] = 20
解包: x = 10, y = 20

使用字符串字段 - r1: Rectangle(width=100, height=50)
面积: 5000

字段名: ('name', 'age', 'city')
转换为字典: {'name': 'Alice', 'age': 30, 'city': 'New York'}
替换后的实例: Person(name='Alice', age=31, city='New York')
原实例不变: Person(name='Alice', age=30, city='New York')
通过_make创建实例: Person(name='Bob', age=25, city='Boston')

继承示例:
Rex says: Woof!
Whiskers says: Meow!

默认值示例:
n1: Node(value=10, left=None, right=None)
n2: Node(value=20, left=Node(value=10, left=None, right=None), right=None)
"""
