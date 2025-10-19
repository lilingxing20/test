#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
deque的用法示例
deque是一个双端队列，可以在队列的两端进行添加和删除操作，效率高
"""

from collections import deque


def basic_usage():
    """基本用法：创建和基本操作"""
    # 创建一个空的deque
    dq1 = deque()
    print("基本用法:")
    
    # 在右端添加元素
    dq1.append(1)
    dq1.append(2)
    dq1.append(3)
    print(f"添加元素后: {dq1}")
    
    # 在左端添加元素
    dq1.appendleft(0)
    dq1.appendleft(-1)
    print(f"左端添加元素后: {dq1}")
    
    # 移除右端元素
    right_element = dq1.pop()
    print(f"移除的右端元素: {right_element}")
    print(f"移除后: {dq1}")
    
    # 移除左端元素
    left_element = dq1.popleft()
    print(f"移除的左端元素: {left_element}")
    print(f"移除后: {dq1}")


def init_with_iterable():
    """使用可迭代对象初始化deque"""
    # 使用列表初始化
    dq2 = deque([1, 2, 3, 4, 5])
    print(f"\n使用列表初始化: {dq2}")
    
    # 使用字符串初始化
    dq3 = deque("hello")
    print(f"使用字符串初始化: {dq3}")
    
    # 使用range初始化
    dq4 = deque(range(10))
    print(f"使用range初始化: {dq4}")


def maxlen_parameter():
    """使用maxlen参数创建固定大小的deque"""
    # 创建最大长度为3的deque
    dq5 = deque(maxlen=3)
    print(f"\n创建固定大小deque(maxlen=3)")
    
    # 添加元素直到达到最大长度
    dq5.append(1)
    dq5.append(2)
    dq5.append(3)
    print(f"添加3个元素: {dq5}")
    
    # 继续添加元素，旧元素会从另一端被移除
    dq5.append(4)
    print(f"添加第4个元素: {dq5}")  # 1被移除
    
    # 从左端添加元素，右端元素被移除
    dq5.appendleft(0)
    print(f"左端添加元素: {dq5}")  # 4被移除


def extend_methods():
    """使用extend和extendleft方法"""
    dq6 = deque([1, 2, 3])
    
    # extend方法：在右端扩展
    dq6.extend([4, 5, 6])
    print(f"\nextend扩展后: {dq6}")
    
    # extendleft方法：在左端扩展（注意：元素顺序会反转）
    dq6.extendleft([-2, -1, 0])
    print(f"extendleft扩展后: {dq6}")


def rotation():
    """旋转操作"""
    dq7 = deque(range(10))
    print(f"\n原始deque: {dq7}")
    
    # 向右旋转2步（正数表示向右旋转）
    dq7.rotate(2)
    print(f"向右旋转2步: {dq7}")
    
    # 向左旋转3步（负数表示向左旋转）
    dq7.rotate(-3)
    print(f"向左旋转3步: {dq7}")


def other_methods():
    """其他常用方法"""
    dq8 = deque([1, 2, 2, 3, 4, 2])
    print(f"\n原始deque: {dq8}")
    
    # count方法：统计元素出现次数
    count = dq8.count(2)
    print(f"元素2出现的次数: {count}")
    
    # remove方法：移除第一个匹配的元素
    dq8.remove(2)
    print(f"移除第一个2后: {dq8}")
    
    # clear方法：清空deque
    dq8.clear()
    print(f"清空后: {dq8}")


def practical_example():
    """实际应用示例：滑动窗口"""
    # 使用deque实现简单的滑动窗口
    def sliding_window(arr, window_size):
        # 使用deque作为窗口容器
        window = deque(maxlen=window_size)
        results = []
        
        for num in arr:
            window.append(num)
            # 当窗口达到指定大小时，计算窗口内的平均值
            if len(window) == window_size:
                results.append(sum(window) / window_size)
        
        return results
    
    # 测试滑动窗口
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    window_size = 3
    averages = sliding_window(data, window_size)
    
    print(f"\n滑动窗口示例 (窗口大小={window_size}):")
    print(f"原始数据: {data}")
    print(f"窗口平均值: {averages}")


def main():
    """主函数，演示deque的各种用法"""
    print("=== deque用法示例 ===")
    
    # 调用各个示例函数
    basic_usage()
    init_with_iterable()
    maxlen_parameter()
    extend_methods()
    rotation()
    other_methods()
    practical_example()


if __name__ == "__main__":
    main()

"""
运行结果：
=== deque用法示例 ===
基本用法:
添加元素后: deque([1, 2, 3])
左端添加元素后: deque([-1, 0, 1, 2, 3])
移除的右端元素: 3
移除后: deque([-1, 0, 1, 2])
移除的左端元素: -1
移除后: deque([0, 1, 2])

使用列表初始化: deque([1, 2, 3, 4, 5])
使用字符串初始化: deque(['h', 'e', 'l', 'l', 'o'])
使用range初始化: deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

创建固定大小deque(maxlen=3)
添加3个元素: deque([1, 2, 3], maxlen=3)
添加第4个元素: deque([2, 3, 4], maxlen=3)
左端添加元素: deque([0, 2, 3], maxlen=3)

extend扩展后: deque([1, 2, 3, 4, 5, 6])
extendleft扩展后: deque([0, -1, -2, 1, 2, 3, 4, 5, 6])

原始deque: deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
向右旋转2步: deque([8, 9, 0, 1, 2, 3, 4, 5, 6, 7])
向左旋转3步: deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

原始deque: deque([1, 2, 2, 3, 4, 2])
元素2出现的次数: 3
移除第一个2后: deque([1, 2, 3, 4, 2])
清空后: deque([])

滑动窗口示例 (窗口大小=3):
原始数据: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
窗口平均值: [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
"""
