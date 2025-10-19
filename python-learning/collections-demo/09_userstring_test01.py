#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UserString的用法示例
UserString是一个字符串子类，提供了字符串接口的实现，方便用户继承和扩展字符串功能
"""

from collections import UserString


def basic_usage():
    """基本用法：使用和继承UserString"""
    print("基本用法:")
    
    # 直接使用UserString
    us = UserString("Hello, World!")
    print(f"UserString实例: {us}")
    print(f"类型: {type(us)}")
    print(f"长度: {len(us)}")
    
    # 访问data属性，data存储实际的字符串数据
    print(f"us.data: {us.data}")
    print(f"类型: {type(us.data)}")
    
    # 支持字符串的基本操作
    print(f"索引访问: {us[7]}")
    print(f"切片操作: {us[0:5]}")
    print(f"元素存在性: {'World' in us}")
    print(f"连接操作: {us + ' Welcome!'}")
    print(f"重复操作: {us * 2}")


class TruncatedString(UserString):
    """自动截断到指定长度的字符串"""
    def __init__(self, seq='', max_length=10):
        self.max_length = max_length
        # 初始化时截断
        if len(seq) > max_length:
            seq = seq[:max_length]
        super().__init__(seq)
    
    def __setitem__(self, index, value):
        """设置字符时保持长度限制"""
        # 这里只处理单个字符的设置
        if isinstance(index, int):
            self.data = self.data[:index] + value + self.data[index+1:]
        else:
            # 对于切片操作，需要重新检查长度
            new_data = list(self.data)
            new_data[index] = value
            new_data = ''.join(new_data)
            # 如果超过最大长度，截断
            if len(new_data) > self.max_length:
                new_data = new_data[:self.max_length]
            self.data = new_data
    
    def append(self, string):
        """添加字符串并保持长度限制"""
        self.data = (self.data + string)[:self.max_length]
    
    def __add__(self, other):
        """自定义加法操作，保持长度限制"""
        result = super().__add__(other)
        # 创建新的TruncatedString实例并确保长度限制
        return TruncatedString(result, self.max_length)


class CaseInsensitiveString(UserString):
    """大小写不敏感的字符串"""
    def __init__(self, seq=''):
        super().__init__(str(seq))  # 确保是字符串
    
    def __eq__(self, other):
        """相等比较不区分大小写"""
        if isinstance(other, UserString):
            return self.data.lower() == other.data.lower()
        return self.data.lower() == str(other).lower()
    
    def __ne__(self, other):
        """不等比较不区分大小写"""
        return not self.__eq__(other)
    
    def __contains__(self, item):
        """包含检查不区分大小写"""
        if isinstance(item, UserString):
            return item.data.lower() in self.data.lower()
        return str(item).lower() in self.data.lower()
    
    def startswith(self, prefix, start=0, end=None):
        """startswith方法不区分大小写"""
        if end is None:
            end = len(self.data)
        return self.data[start:end].lower().startswith(str(prefix).lower())
    
    def endswith(self, suffix, start=0, end=None):
        """endswith方法不区分大小写"""
        if end is None:
            end = len(self.data)
        return self.data[start:end].lower().endswith(str(suffix).lower())
    
    def find(self, sub, start=0, end=None):
        """find方法不区分大小写"""
        if end is None:
            end = len(self.data)
        # 转换为小写进行查找
        lower_data = self.data[start:end].lower()
        lower_sub = str(sub).lower()
        return lower_data.find(lower_sub)
    
    def index(self, sub, start=0, end=None):
        """index方法不区分大小写"""
        result = self.find(sub, start, end)
        if result == -1:
            raise ValueError(f"substring not found: {sub}")
        return result


class SanitizedString(UserString):
    """自动清理特殊字符的字符串"""
    def __init__(self, seq='', allowed_chars=None, replacement='_'):
        self.allowed_chars = allowed_chars  # 允许的字符集
        self.replacement = replacement  # 替换字符
        # 初始化时清理
        clean_seq = self._sanitize(seq)
        super().__init__(clean_seq)
    
    def _sanitize(self, string):
        """清理字符串，替换不允许的字符"""
        if self.allowed_chars is None:
            return string
        
        result = []
        for char in string:
            if char in self.allowed_chars:
                result.append(char)
            else:
                result.append(self.replacement)
        return ''.join(result)
    
    def __setitem__(self, index, value):
        """设置字符时进行清理"""
        # 清理要设置的值
        clean_value = self._sanitize(value)
        # 对于单个字符
        if isinstance(index, int):
            if len(clean_value) > 0:
                self.data = self.data[:index] + clean_value[0] + self.data[index+1:]
        else:
            # 对于切片
            self.data = self.data[:index.start] + clean_value + self.data[index.stop:]
    
    def append(self, string):
        """添加字符串时进行清理"""
        clean_string = self._sanitize(string)
        self.data += clean_string
    
    def __add__(self, other):
        """加法操作时清理"""
        clean_other = self._sanitize(str(other))
        return SanitizedString(
            self.data + clean_other,
            self.allowed_chars,
            self.replacement
        )


def truncated_string_example():
    """自动截断字符串示例"""
    print("\n自动截断字符串示例:")
    
    # 创建最大长度为10的TruncatedString
    ts = TruncatedString("Hello, World!", max_length=10)
    print(f"初始化后（已截断）: {ts}")
    
    # 尝试添加更多字符
    ts.append(" Welcome!")
    print(f"添加后（保持10个字符）: {ts}")
    
    # 测试加法操作
    new_ts = ts + "Test"
    print(f"加法操作后: {new_ts}")
    
    # 创建新的TruncatedString
    ts2 = TruncatedString("12345", max_length=8)
    print(f"ts2初始值: {ts2}")
    ts2.append("67890")
    print(f"ts2添加后（最多8个字符）: {ts2}")


def case_insensitive_example():
    """大小写不敏感字符串示例"""
    print("\n大小写不敏感字符串示例:")
    
    # 创建大小写不敏感字符串
    cis1 = CaseInsensitiveString("Hello")
    cis2 = CaseInsensitiveString("hello")
    
    # 比较操作
    print(f"cis1: {cis1}, cis2: {cis2}")
    print(f"cis1 == cis2: {cis1 == cis2}")
    print(f"cis1 == 'HELLO': {cis1 == 'HELLO'}")
    
    # 包含检查
    print(f"'WORLD' in CaseInsensitiveString('Hello World'): {'WORLD' in CaseInsensitiveString('Hello World')}")
    
    # startswith和endswith
    cis = CaseInsensitiveString("Hello, World!")
    print(f"startswith('hello'): {cis.startswith('hello')}")
    print(f"endswith('world!'): {cis.endswith('world!')}")
    
    # find和index
    print(f"find('WORLD'): {cis.find('WORLD')}")
    try:
        print(f"index('WORLD'): {cis.index('WORLD')}")
    except ValueError as e:
        print(f"index错误: {e}")


def sanitized_string_example():
    """清理字符串示例"""
    print("\n清理字符串示例:")
    
    # 只允许字母、数字和下划线
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')
    
    # 创建清理字符串
    ss = SanitizedString("Hello@World#123!", allowed_chars=allowed_chars)
    print(f"初始化后（已清理）: {ss}")
    
    # 尝试添加含有特殊字符的字符串
    ss.append("-test$string")
    print(f"添加后（已清理）: {ss}")
    
    # 创建文件名安全的字符串
    filename_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-')
    unsafe_filename = "My Document (2023).pdf"
    safe_filename = SanitizedString(unsafe_filename, allowed_chars=filename_chars)
    print(f"原始文件名: {unsafe_filename}")
    print(f"安全文件名: {safe_filename}")


def main():
    """主函数，演示UserString的各种用法"""
    print("=== UserString用法示例 ===")
    
    # 调用各个示例函数
    basic_usage()
    truncated_string_example()
    case_insensitive_example()
    sanitized_string_example()


if __name__ == "__main__":
    main()

"""
运行结果：
=== UserString用法示例 ===
基本用法:
UserString实例: Hello, World!
类型: <class 'collections.UserString'>
长度: 13
us.data: Hello, World!
类型: <class 'str'>
索引访问: W
切片操作: Hello
元素存在性: True
连接操作: Hello, World! Welcome!
重复操作: Hello, World!Hello, World!

自动截断字符串示例:
初始化后（已截断）: Hello, Wor
添加后（保持10个字符）: Hello, Wor
加法操作后: Hello, Wor
ts2初始值: 12345
ts2添加后（最多8个字符）: 12345678

大小写不敏感字符串示例:
cis1: Hello, cis2: hello
cis1 == cis2: True
cis1 == 'HELLO': True
'WORLD' in CaseInsensitiveString('Hello World'): True
startswith('hello'): True
endswith('world!'): True
find('WORLD'): 7
index('WORLD'): 7

清理字符串示例:
初始化后（已清理）: Hello_World_123_
添加后（已清理）: Hello_World_123__test_string
原始文件名: My Document (2023).pdf
安全文件名: My_Document__2023__pdf
"""
