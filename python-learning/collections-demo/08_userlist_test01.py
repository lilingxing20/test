#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UserList的用法示例
UserList是一个列表子类，提供了列表接口的实现，方便用户继承和扩展列表功能
"""

from collections import UserList


def basic_usage():
    """基本用法：使用和继承UserList"""
    print("基本用法:")
    
    # 直接使用UserList
    ul = UserList()
    ul.append(1)
    ul.append(2)
    ul.append(3)
    print(f"UserList实例: {ul}")
    print(f"类型: {type(ul)}")
    print(f"长度: {len(ul)}")
    
    # 从普通列表创建UserList
    regular_list = [4, 5, 6]
    ul_from_list = UserList(regular_list)
    print(f"从普通列表创建: {ul_from_list}")
    
    # 访问data属性，data存储实际的列表数据
    print(f"ul.data: {ul.data}")
    print(f"类型: {type(ul.data)}")
    
    # 支持列表的基本操作
    print(f"索引访问: {ul[1]}")
    print(f"切片操作: {ul[0:2]}")
    print(f"元素存在性: {2 in ul}")


class SortedList(UserList):
    """自动排序的列表实现"""
    def __init__(self, initlist=None, key=None):
        self.key = key  # 排序键函数，类似于sorted函数的key参数
        super().__init__(initlist)
        # 初始化时排序
        self._sort()
    
    def _sort(self):
        """对列表进行排序"""
        if self.data:
            self.data.sort(key=self.key)
    
    def append(self, item):
        """添加元素后排序"""
        super().append(item)
        self._sort()
    
    def extend(self, other):
        """扩展列表后排序"""
        super().extend(other)
        self._sort()
    
    def insert(self, i, item):
        """插入元素后排序（忽略索引，因为会重新排序）"""
        super().append(item)  # 直接添加到末尾，然后排序
        self._sort()
    
    def __setitem__(self, i, item):
        """设置元素值后排序"""
        super().__setitem__(i, item)
        self._sort()
    
    def reverse(self):
        """重写reverse方法，使其保持排序但顺序相反"""
        self._sort()  # 确保先排序
        self.data.reverse()  # 然后反转


class UniqueList(UserList):
    """不允许重复元素的列表实现"""
    def __init__(self, initlist=None):
        super().__init__()
        # 初始化时确保唯一性
        if initlist is not None:
            for item in initlist:
                self.append(item)
    
    def append(self, item):
        """只添加不存在的元素"""
        if item not in self.data:
            super().append(item)
    
    def extend(self, other):
        """扩展时只添加不存在的元素"""
        for item in other:
            self.append(item)
    
    def insert(self, i, item):
        """只插入不存在的元素"""
        if item not in self.data:
            super().insert(i, item)
    
    def __setitem__(self, i, item):
        """设置元素值时检查唯一性"""
        # 如果是切片操作，需要分别处理
        if isinstance(i, slice):
            # 获取切片范围
            start, stop, step = i.indices(len(self))
            # 检查新元素是否与非切片位置的元素重复
            existing_items = [self[j] for j in range(len(self)) if j < start or j >= stop]
            if any(x in existing_items for x in item):
                raise ValueError("Cannot set duplicate values")
        elif item in self.data and self.data[i] != item:
            # 单个索引且新值与列表中其他元素重复
            raise ValueError(f"Value {item} already exists")
        
        super().__setitem__(i, item)


class BoundedList(UserList):
    """有边界检查的列表实现"""
    def __init__(self, min_value=None, max_value=None, initlist=None):
        self.min_value = min_value
        self.max_value = max_value
        super().__init__()
        # 初始化时检查边界
        if initlist is not None:
            for item in initlist:
                self.append(item)
    
    def _check_bounds(self, item):
        """检查元素是否在边界范围内"""
        if self.min_value is not None and item < self.min_value:
            raise ValueError(f"Value {item} is below minimum {self.min_value}")
        if self.max_value is not None and item > self.max_value:
            raise ValueError(f"Value {item} is above maximum {self.max_value}")
    
    def append(self, item):
        """添加元素前检查边界"""
        self._check_bounds(item)
        super().append(item)
    
    def extend(self, other):
        """扩展前检查所有元素的边界"""
        # 先检查所有元素
        for item in other:
            self._check_bounds(item)
        # 全部检查通过后再扩展
        super().extend(other)
    
    def insert(self, i, item):
        """插入元素前检查边界"""
        self._check_bounds(item)
        super().insert(i, item)
    
    def __setitem__(self, i, item):
        """设置元素值前检查边界"""
        # 如果是切片操作，需要分别检查
        if isinstance(i, slice):
            for x in item:
                self._check_bounds(x)
        else:
            self._check_bounds(item)
        
        super().__setitem__(i, item)


def sorted_list_example():
    """自动排序列表示例"""
    print("\n自动排序列表示例:")
    
    # 创建自动排序列表
    sl = SortedList([5, 2, 8, 1, 9])
    print(f"初始化后: {sl}")
    
    # 添加元素
    sl.append(3)
    print(f"添加3后: {sl}")
    
    # 扩展列表
    sl.extend([6, 4])
    print(f"扩展[6,4]后: {sl}")
    
    # 使用键函数（按字符串长度排序）
    sl_str = SortedList(["apple", "banana", "cherry", "date"], key=len)
    print(f"按长度排序: {sl_str}")
    
    # 反转排序
    sl.reverse()
    print(f"反转后: {sl}")


def unique_list_example():
    """唯一元素列表示例"""
    print("\n唯一元素列表示例:")
    
    # 创建唯一元素列表
    ul = UniqueList([1, 2, 3, 2, 1, 4])
    print(f"初始化后（去重）: {ul}")
    
    # 尝试添加重复元素
    ul.append(3)
    print(f"尝试添加重复元素3后: {ul}")  # 应该没有变化
    
    # 添加新元素
    ul.append(5)
    print(f"添加新元素5后: {ul}")
    
    # 扩展列表
    ul.extend([4, 5, 6, 7])
    print(f"扩展[4,5,6,7]后（去重）: {ul}")
    
    # 尝试设置重复值
    try:
        ul[0] = 6  # 6已经存在
    except ValueError as e:
        print(f"预期的重复值错误: {e}")


def bounded_list_example():
    """有边界的列表示例"""
    print("\n有边界的列表示例:")
    
    # 创建0-100范围内的列表
    bl = BoundedList(min_value=0, max_value=100)
    
    # 添加有效值
    bl.append(42)
    bl.append(99)
    print(f"添加有效值后: {bl}")
    
    # 尝试添加超出范围的值
    try:
        bl.append(150)
    except ValueError as e:
        print(f"预期的上界错误: {e}")
    
    try:
        bl.append(-10)
    except ValueError as e:
        print(f"预期的下界错误: {e}")
    
    # 测试扩展
    try:
        bl.extend([50, 60, 101])  # 101超出范围
    except ValueError as e:
        print(f"扩展时的边界错误: {e}")
    print(f"扩展后的列表: {bl}")  # 应该没有变化


def main():
    """主函数，演示UserList的各种用法"""
    print("=== UserList用法示例 ===")
    
    # 调用各个示例函数
    basic_usage()
    sorted_list_example()
    unique_list_example()
    bounded_list_example()


if __name__ == "__main__":
    main()

"""
运行结果：
=== UserList用法示例 ===
基本用法:
UserList实例: [1, 2, 3]
类型: <class 'collections.UserList'>
长度: 3
从普通列表创建: [4, 5, 6]
ul.data: [1, 2, 3]
类型: <class 'list'>
索引访问: 2
切片操作: [1, 2]
元素存在性: True

自动排序列表示例:
初始化后: [1, 2, 5, 8, 9]
添加3后: [1, 2, 3, 5, 8, 9]
扩展[6,4]后: [1, 2, 3, 4, 5, 6, 8, 9]
按长度排序: ['date', 'apple', 'banana', 'cherry']
反转后: [9, 8, 6, 5, 4, 3, 2, 1]

唯一元素列表示例:
初始化后（去重）: [1, 2, 3, 4]
尝试添加重复元素3后: [1, 2, 3, 4]
添加新元素5后: [1, 2, 3, 4, 5]
扩展[4,5,6,7]后（去重）: [1, 2, 3, 4, 5, 6, 7]
预期的重复值错误: Value 6 already exists

有边界的列表示例:
添加有效值后: [42, 99]
预期的上界错误: Value 150 is above maximum 100
预期的下界错误: Value -10 is below minimum 0
扩展时的边界错误: Value 101 is above maximum 100
扩展后的列表: [42, 99]
"""
