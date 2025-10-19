#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OrderedDict的用法示例
OrderedDict是一个字典子类，能够记住键值对的插入顺序
虽然Python 3.7+中普通字典也保留插入顺序，但OrderedDict提供额外功能
"""

from collections import OrderedDict


def basic_usage():
    """基本用法：创建和使用OrderedDict"""
    print("基本用法:")
    
    # 创建一个OrderedDict
    od = OrderedDict()
    
    # 添加键值对
    od['a'] = 1
    od['b'] = 2
    od['c'] = 3
    od['d'] = 4
    
    print(f"OrderedDict: {od}")
    
    # 遍历OrderedDict - 按照插入顺序
    print("遍历（按照插入顺序）:")
    for key, value in od.items():
        print(f"{key}: {value}")
    
    # 从普通字典创建（注意：在Python 3.7+中，普通字典也保留插入顺序）
    regular_dict = {'z': 26, 'y': 25, 'x': 24}
    od_from_dict = OrderedDict(regular_dict)
    print(f"从普通字典创建: {od_from_dict}")
    
    # 从键值对列表创建
    items = [('one', 1), ('two', 2), ('three', 3)]
    od_from_items = OrderedDict(items)
    print(f"从键值对列表创建: {od_from_items}")


def unique_features():
    """OrderedDict的独特功能"""
    print("\nOrderedDict的独特功能:")
    
    # 创建OrderedDict
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
    print(f"原始OrderedDict: {od}")
    
    # move_to_end()方法：将指定的键移动到末尾
    od.move_to_end('a')
    print(f"将'a'移到末尾: {od}")
    
    # move_to_end()方法：指定last=False将键移到开头
    od.move_to_end('d', last=False)
    print(f"将'd'移到开头: {od}")
    
    # popitem()方法：默认移除并返回最后一个键值对
    last_item = od.popitem()
    print(f"移除的最后一个键值对: {last_item}")
    print(f"移除后: {od}")
    
    # popitem(last=False)：移除并返回第一个键值对
    first_item = od.popitem(last=False)
    print(f"移除的第一个键值对: {first_item}")
    print(f"移除后: {od}")


def equality_comparison():
    """比较操作 - OrderedDict比较时考虑顺序"""
    print("\n比较操作:")
    
    # 创建两个具有相同键值但顺序不同的OrderedDict
    od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    od2 = OrderedDict([('b', 2), ('a', 1), ('c', 3)])
    
    # OrderedDict比较时考虑顺序
    print(f"od1: {od1}")
    print(f"od2: {od2}")
    print(f"od1 == od2: {od1 == od2}")  # 即使键值相同，但顺序不同，所以不相等
    
    # 与普通字典比较时，不考虑顺序
    regular_dict = {'a': 1, 'b': 2, 'c': 3}
    print(f"regular_dict: {regular_dict}")
    print(f"od1 == regular_dict: {od1 == regular_dict}")  # 相等，因为键值对相同


def reordering():
    """重新排序OrderedDict"""
    print("\n重新排序:")
    
    # 创建OrderedDict
    od = OrderedDict([('c', 3), ('a', 1), ('b', 2), ('d', 4)])
    print(f"原始OrderedDict: {od}")
    
    # 按键排序
    sorted_od_by_key = OrderedDict(sorted(od.items(), key=lambda x: x[0]))
    print(f"按键排序: {sorted_od_by_key}")
    
    # 按值排序
    sorted_od_by_value = OrderedDict(sorted(od.items(), key=lambda x: x[1]))
    print(f"按值排序: {sorted_od_by_value}")
    
    # 逆序
    reversed_od = OrderedDict(reversed(list(od.items())))
    print(f"逆序: {reversed_od}")


def update_and_delete():
    """更新和删除操作"""
    print("\n更新和删除操作:")
    
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print(f"原始OrderedDict: {od}")
    
    # 更新现有键的值
    od['a'] = 10
    print(f"更新'a'的值后: {od}")
    
    # 添加新键值对
    od['e'] = 5
    print(f"添加新键值对后: {od}")
    
    # 删除键值对
    del od['b']
    print(f"删除'b'后: {od}")
    
    # pop方法
    popped_value = od.pop('c')
    print(f"弹出'c'的值: {popped_value}")
    print(f"弹出后: {od}")
    
    # clear方法
    od.clear()
    print(f"清空后: {od}")


def practical_examples():
    """实际应用示例"""
    print("\n实际应用示例:")
    
    # 示例1：LRU缓存（最近最少使用缓存）的简单实现
    class LRUCache:
        def __init__(self, capacity):
            self.capacity = capacity
            self.cache = OrderedDict()
        
        def get(self, key):
            if key not in self.cache:
                return -1
            # 将访问的键移到末尾（表示最近使用）
            self.cache.move_to_end(key)
            return self.cache[key]
        
        def put(self, key, value):
            if key in self.cache:
                # 更新值并移到末尾
                self.cache[key] = value
                self.cache.move_to_end(key)
            else:
                # 如果缓存已满，删除最久未使用的项（第一个）
                if len(self.cache) >= self.capacity:
                    self.cache.popitem(last=False)
                # 添加新项
                self.cache[key] = value
        
        def __str__(self):
            return str(self.cache)
    
    # 测试LRU缓存
    lru_cache = LRUCache(3)
    lru_cache.put('a', 1)
    lru_cache.put('b', 2)
    lru_cache.put('c', 3)
    print(f"LRU缓存初始状态: {lru_cache}")
    
    print(f"获取'a': {lru_cache.get('a')}")  # 'a'现在是最近使用的
    print(f"缓存状态: {lru_cache}")
    
    lru_cache.put('d', 4)  # 'b'应该被移除，因为它是最久未使用的
    print(f"添加'd'后: {lru_cache}")
    
    # 示例2：维护历史记录
    def maintain_ordered_history(actions, max_history=5):
        history = OrderedDict()
        
        for action_id, action in actions:
            # 如果达到最大历史记录且不是更新现有记录，则移除最旧的
            if len(history) >= max_history and action_id not in history:
                history.popitem(last=False)
            # 添加或更新操作
            history[action_id] = action
        
        return history
    
    actions = [(1, "登录"), (2, "浏览页面"), (3, "添加商品"), 
               (4, "结账"), (5, "支付"), (6, "登出")]
    ordered_history = maintain_ordered_history(actions)
    print(f"\n有序历史记录: {ordered_history}")


def main():
    """主函数，演示OrderedDict的各种用法"""
    print("=== OrderedDict用法示例 ===")
    
    # 调用各个示例函数
    basic_usage()
    unique_features()
    equality_comparison()
    reordering()
    update_and_delete()
    practical_examples()


if __name__ == "__main__":
    main()

"""
运行结果：
=== OrderedDict用法示例 ===
基本用法:
OrderedDict: OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
遍历（按照插入顺序）:
a: 1
b: 2
c: 3
d: 4
从普通字典创建: OrderedDict({'z': 26, 'y': 25, 'x': 24})
从键值对列表创建: OrderedDict({'one': 1, 'two': 2, 'three': 3})

OrderedDict的独特功能:
原始OrderedDict: OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
将'a'移到末尾: OrderedDict({'b': 2, 'c': 3, 'd': 4, 'a': 1})
将'd'移到开头: OrderedDict({'d': 4, 'b': 2, 'c': 3, 'a': 1})
移除的最后一个键值对: ('a', 1)
移除后: OrderedDict({'d': 4, 'b': 2, 'c': 3})
移除的第一个键值对: ('d', 4)
移除后: OrderedDict({'b': 2, 'c': 3})

比较操作:
od1: OrderedDict({'a': 1, 'b': 2, 'c': 3})
od2: OrderedDict({'b': 2, 'a': 1, 'c': 3})
od1 == od2: False
regular_dict: {'a': 1, 'b': 2, 'c': 3}
od1 == regular_dict: True

重新排序:
原始OrderedDict: OrderedDict({'c': 3, 'a': 1, 'b': 2, 'd': 4})
按键排序: OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
按值排序: OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
逆序: OrderedDict({'d': 4, 'b': 2, 'a': 1, 'c': 3})

更新和删除操作:
原始OrderedDict: OrderedDict({'a': 1, 'b': 2, 'c': 3})
更新'a'的值后: OrderedDict({'a': 10, 'b': 2, 'c': 3})
添加新键值对后: OrderedDict({'a': 10, 'b': 2, 'c': 3, 'e': 5})
删除'b'后: OrderedDict({'a': 10, 'c': 3, 'e': 5})
弹出'c'的值: 3
弹出后: OrderedDict({'a': 10, 'e': 5})
清空后: OrderedDict()

实际应用示例:
LRU缓存初始状态: OrderedDict({'a': 1, 'b': 2, 'c': 3})
获取'a': 1
缓存状态: OrderedDict({'b': 2, 'c': 3, 'a': 1})
添加'd'后: OrderedDict({'c': 3, 'a': 1, 'd': 4})

有序历史记录: OrderedDict({2: '浏览页面', 3: '添加商品', 4: '结账', 5: '支付', 6: '登出'})
"""
