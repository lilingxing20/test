#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
defaultdict的用法示例
defaultdict是一个字典子类，可以为不存在的键提供默认值
"""

from collections import defaultdict


def basic_usage():
    """基本用法：创建和使用defaultdict"""
    print("基本用法:")
    
    # 创建一个默认值为int类型的defaultdict（默认为0）
    dd_int = defaultdict(int)
    print(f"defaultdict(int)创建后: {dict(dd_int)}")  # 空字典
    
    # 访问不存在的键会自动创建并设置默认值
    dd_int['a'] += 1  # 等同于 dd_int['a'] = dd_int['a'] + 1，但无需检查键是否存在
    dd_int['b'] += 2
    print(f"访问并修改后: {dict(dd_int)}")
    
    # 创建一个默认值为list类型的defaultdict（默认为空列表）
    dd_list = defaultdict(list)
    dd_list['fruits'].append('apple')
    dd_list['fruits'].append('banana')
    dd_list['vegetables'].append('carrot')
    print(f"defaultdict(list)示例: {dict(dd_list)}")
    
    # 创建一个默认值为set类型的defaultdict（默认为空集合）
    dd_set = defaultdict(set)
    dd_set['colors'].add('red')
    dd_set['colors'].add('blue')
    dd_set['colors'].add('red')  # 重复元素不会被添加到集合中
    print(f"defaultdict(set)示例: {dict(dd_set)}")


def using_default_factory():
    """使用不同类型的default_factory"""
    print("\n使用不同类型的default_factory:")
    
    # 默认值为0（int）
    dd_int = defaultdict(int)
    print(f"int默认值: {dd_int['new_key']}")
    
    # 默认值为空列表（list）
    dd_list = defaultdict(list)
    print(f"list默认值: {dd_list['new_key']}")
    
    # 默认值为空字典（dict）
    dd_dict = defaultdict(dict)
    print(f"dict默认值: {dd_dict['new_key']}")
    
    # 默认值为空字符串（str）
    dd_str = defaultdict(str)
    print(f"str默认值: {dd_str['new_key']!r}")  # !r 显示原始字符串表示
    
    # 默认值为1.0（float）
    dd_float = defaultdict(float)
    print(f"float默认值: {dd_float['new_key']}")
    
    # 使用自定义函数作为default_factory
    def default_value():
        return "Not Set"
    
    dd_custom = defaultdict(default_value)
    print(f"自定义默认值: {dd_custom['new_key']}")


def practical_examples():
    """实际应用示例"""
    print("\n实际应用示例:")
    
    # 示例1：词频统计（比普通字典更简洁）
    def word_frequency(text):
        words = text.lower().split()
        freq = defaultdict(int)
        
        for word in words:
            # 不需要检查word是否已经在freq中
            freq[word] += 1
        
        return freq
    
    sample_text = "hello world hello python hello collections"
    freq = word_frequency(sample_text)
    print(f"词频统计: {dict(freq)}")
    
    # 示例2：分组数据
    def group_by_first_letter(words):
        grouped = defaultdict(list)
        
        for word in words:
            if word:  # 确保单词不为空
                # 直接添加到相应的列表，无需检查键是否存在
                grouped[word[0].lower()].append(word)
        
        return grouped
    
    words = ['apple', 'Banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
    grouped_words = group_by_first_letter(words)
    print(f"\n按首字母分组: {dict(grouped_words)}")
    
    # 示例3：嵌套的defaultdict
    def nested_defaultdict():
        # 创建一个嵌套的defaultdict，用于存储多层级数据
        # 这里使用lambda函数来创建嵌套的defaultdict
        nested_dd = defaultdict(lambda: defaultdict(list))
        
        # 存储数据
        nested_dd['users']['active'].append('Alice')
        nested_dd['users']['active'].append('Bob')
        nested_dd['users']['inactive'].append('Charlie')
        nested_dd['products']['electronics'].append('Laptop')
        nested_dd['products']['electronics'].append('Phone')
        nested_dd['products']['furniture'].append('Chair')
        
        # 转换为普通字典以便更好地显示
        result = {}
        for outer_key, inner_dict in nested_dd.items():
            result[outer_key] = dict(inner_dict)
        
        return result
    
    nested_data = nested_defaultdict()
    print(f"\n嵌套defaultdict示例: {nested_data}")
    
    # 示例4：图的邻接表表示
    def build_graph(edges):
        graph = defaultdict(list)
        
        for source, destination in edges:
            graph[source].append(destination)
            graph[destination].append(source)  # 无向图
        
        return graph
    
    edges = [(1, 2), (1, 3), (2, 4), (3, 4), (3, 5)]
    graph = build_graph(edges)
    print(f"\n图的邻接表表示: {dict(graph)}")


def difference_with_regular_dict():
    """与普通字典的区别"""
    print("\n与普通字典的区别:")
    
    # 使用普通字典
    regular_dict = {}
    try:
        # 普通字典访问不存在的键会抛出KeyError
        value = regular_dict['non_existent']
    except KeyError:
        print("普通字典访问不存在的键抛出KeyError")
    
    # 使用defaultdict
    dd = defaultdict(int)
    # defaultdict访问不存在的键会返回默认值
    value = dd['non_existent']
    print(f"defaultdict访问不存在的键返回: {value}")
    
    # 注意：访问不存在的键后，该键会被添加到defaultdict中
    print(f"访问后defaultdict的内容: {dict(dd)}")


def handling_custom_types():
    """处理自定义类型作为默认值"""
    print("\n处理自定义类型作为默认值:")
    
    # 定义一个自定义类
    class Counter:
        def __init__(self):
            self.count = 0
        
        def increment(self):
            self.count += 1
        
        def __str__(self):
            return f"Counter({self.count})"
    
    # 创建一个默认值为Counter实例的defaultdict
    counters = defaultdict(Counter)
    
    # 使用
    counters['a'].increment()
    counters['a'].increment()
    counters['b'].increment()
    
    # 显示结果
    result = {k: str(v) for k, v in counters.items()}
    print(f"自定义类型作为默认值: {result}")


def main():
    """主函数，演示defaultdict的各种用法"""
    print("=== defaultdict用法示例 ===")
    
    # 调用各个示例函数
    basic_usage()
    using_default_factory()
    practical_examples()
    difference_with_regular_dict()
    handling_custom_types()


if __name__ == "__main__":
    main()

"""
运行结果：
=== defaultdict用法示例 ===
基本用法:
defaultdict(int)创建后: {}
访问并修改后: {'a': 1, 'b': 2}
defaultdict(list)示例: {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']}
defaultdict(set)示例: {'colors': {'red', 'blue'}}

使用不同类型的default_factory:
int默认值: 0
list默认值: []
dict默认值: {}
str默认值: ''
float默认值: 0.0
自定义默认值: Not Set

实际应用示例:
词频统计: {'hello': 3, 'world': 1, 'python': 1, 'collections': 1}

按首字母分组: {'a': ['apple'], 'b': ['Banana'], 'c': ['cherry'], 'd': ['date'], 'e': ['elderberry'], 'f': ['fig'], 'g': ['grape']}

嵌套defaultdict示例: {'users': {'active': ['Alice', 'Bob'], 'inactive': ['Charlie']}, 'products': {'electronics': ['Laptop', 'Phone'], 'furniture': ['Chair']}}

图的邻接表表示: {1: [2, 3], 2: [1, 4], 3: [1, 4, 5], 4: [2, 3], 5: [3]}

与普通字典的区别:
普通字典访问不存在的键抛出KeyError
defaultdict访问不存在的键返回: 0
访问后defaultdict的内容: {'non_existent': 0}

处理自定义类型作为默认值:
自定义类型作为默认值: {'a': 'Counter(2)', 'b': 'Counter(1)'}
"""
