#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Counter的用法示例
Counter是一个字典子类，用于统计可哈希对象的出现次数
"""

from collections import Counter


def basic_usage():
    """基本用法：创建和使用Counter"""
    print("基本用法:")
    
    # 从可迭代对象创建Counter
    words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    word_counts = Counter(words)
    print(f"单词计数: {word_counts}")
    
    # 从字符串创建Counter
    text = "hello world"
    char_counts = Counter(text)
    print(f"字符计数: {char_counts}")
    
    # 从字典创建Counter
    counts_dict = {'a': 3, 'b': 5, 'c': 2}
    counter_from_dict = Counter(counts_dict)
    print(f"从字典创建: {counter_from_dict}")
    
    # 访问元素计数
    print(f"'apple'出现的次数: {word_counts['apple']}")
    print(f"不存在的键返回0: {word_counts['grape']}")


def common_patterns():
    """Counter的常见操作模式"""
    # 创建一个Counter
    cnt = Counter(['a', 'a', 'a', 'b', 'b', 'c', 'd', 'd', 'd', 'd'])
    print(f"\n原始Counter: {cnt}")
    
    # elements()方法：返回一个迭代器，包含所有元素（按计数重复）
    elements = sorted(cnt.elements())
    print(f"所有元素: {elements}")
    
    # most_common()方法：返回最常见的元素和它们的计数
    print(f"最常见的2个元素: {cnt.most_common(2)}")
    print(f"所有元素按频率排序: {cnt.most_common()}")
    
    # subtract()方法：减去另一个计数器或可迭代对象
    cnt.subtract(['a', 'b', 'c', 'c', 'c'])
    print(f"减去后的结果: {cnt}")


def arithmetic_operations():
    """Counter的算术操作"""
    # 创建两个Counter
    cnt1 = Counter(a=3, b=2, c=1)
    cnt2 = Counter(a=1, b=4, d=2)
    
    print(f"\n算术操作:")
    print(f"cnt1: {cnt1}")
    print(f"cnt2: {cnt2}")
    
    # 加法：合并两个计数器
    print(f"cnt1 + cnt2: {cnt1 + cnt2}")
    
    # 减法：减去另一个计数器（只保留计数大于0的元素）
    print(f"cnt1 - cnt2: {cnt1 - cnt2}")
    print(f"cnt2 - cnt1: {cnt2 - cnt1}")
    
    # 交集：取两个计数器中计数较小的值
    print(f"cnt1 & cnt2: {cnt1 & cnt2}")
    
    # 并集：取两个计数器中计数较大的值
    print(f"cnt1 | cnt2: {cnt1 | cnt2}")
    
    # 补充：更新cnt1
    cnt1.update({'b': 3, 'e': 2})
    print(f"更新后的cnt1: {cnt1}")


def practical_examples():
    """实际应用示例"""
    print("\n实际应用示例:")
    
    # 示例1：文本分析
    def analyze_text(text):
        # 转换为小写并过滤非字母字符
        cleaned_text = ''.join(c.lower() for c in text if c.isalpha() or c.isspace())
        # 分词
        words = cleaned_text.split()
        # 统计单词频率
        word_counts = Counter(words)
        
        # 返回结果
        return {
            'total_words': len(words),
            'unique_words': len(word_counts),
            'most_common': word_counts.most_common(5)
        }
    
    sample_text = "This is a sample text. This text is used for demonstrating the Counter class. "
    sample_text += "Counter is a useful tool for text analysis."
    
    analysis_result = analyze_text(sample_text)
    print("文本分析结果:")
    print(f"总单词数: {analysis_result['total_words']}")
    print(f"独特单词数: {analysis_result['unique_words']}")
    print(f"最常见的5个单词: {analysis_result['most_common']}")
    
    # 示例2：找出字符串中出现次数最多的字符
    def most_frequent_char(s):
        # 过滤掉空格
        s = s.replace(' ', '')
        if not s:
            return None
        
        char_counts = Counter(s)
        # 获取出现次数最多的字符
        most_common = char_counts.most_common(1)
        return most_common[0] if most_common else None
    
    test_string = "programming is fun and challenging"
    frequent_char = most_frequent_char(test_string)
    print(f"\n字符串 '{test_string}' 中出现次数最多的字符: {frequent_char}")


def handling_edge_cases():
    """处理边界情况"""
    print("\n边界情况处理:")
    
    # 空Counter
    empty_counter = Counter()
    print(f"空Counter: {empty_counter}")
    print(f"访问不存在的键: {empty_counter['anything']}")
    
    # 包含0和负数的Counter
    mixed_counter = Counter(a=3, b=0, c=-1)
    print(f"包含0和负数的Counter: {mixed_counter}")
    
    # 算术操作会过滤掉0和负数
    print(f"转换为正常Counter: {+mixed_counter}")  # 使用一元加号过滤非正数
    
    # 清除所有计数
    mixed_counter.clear()
    print(f"清除后的Counter: {mixed_counter}")


def main():
    """主函数，演示Counter的各种用法"""
    print("=== Counter用法示例 ===")
    
    # 调用各个示例函数
    basic_usage()
    common_patterns()
    arithmetic_operations()
    practical_examples()
    handling_edge_cases()


if __name__ == "__main__":
    main()

"""
运行结果：
=== Counter用法示例 ===
基本用法:
单词计数: Counter({'apple': 3, 'banana': 2, 'orange': 1})
字符计数: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
从字典创建: Counter({'b': 5, 'a': 3, 'c': 2})
'apple'出现的次数: 3
不存在的键返回0: 0

原始Counter: Counter({'d': 4, 'a': 3, 'b': 2, 'c': 1})
所有元素: ['a', 'a', 'a', 'b', 'b', 'c', 'd', 'd', 'd', 'd']
最常见的2个元素: [('d', 4), ('a', 3)]
所有元素按频率排序: [('d', 4), ('a', 3), ('b', 2), ('c', 1)]
减去后的结果: Counter({'d': 4, 'a': 2, 'b': 1, 'c': -2})

算术操作:
cnt1: Counter({'a': 3, 'b': 2, 'c': 1})
cnt2: Counter({'b': 4, 'd': 2, 'a': 1})
cnt1 + cnt2: Counter({'b': 6, 'a': 4, 'd': 2, 'c': 1})
cnt1 - cnt2: Counter({'a': 2, 'c': 1})
cnt2 - cnt1: Counter({'b': 2, 'd': 2})
cnt1 & cnt2: Counter({'b': 2, 'a': 1})
cnt1 | cnt2: Counter({'b': 4, 'a': 3, 'd': 2, 'c': 1})
更新后的cnt1: Counter({'b': 5, 'a': 3, 'e': 2, 'c': 1})

实际应用示例:
文本分析结果:
总单词数: 22
独特单词数: 14
最常见的5个单词: [('is', 3), ('text', 3), ('this', 2), ('a', 2), ('for', 2)]

字符串 'programming is fun and challenging' 中出现次数最多的字符: ('n', 5)

边界情况处理:
空Counter: Counter()
访问不存在的键: 0
包含0和负数的Counter: Counter({'a': 3, 'b': 0, 'c': -1})
转换为正常Counter: Counter({'a': 3})
清除后的Counter: Counter()
"""
