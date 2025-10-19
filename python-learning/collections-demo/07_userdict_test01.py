#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UserDict的用法示例
UserDict是一个字典子类，提供了字典接口的实现，方便用户继承和扩展字典功能
"""

from collections import UserDict


def basic_usage():
    """基本用法：使用和继承UserDict"""
    print("基本用法:")
    
    # 直接使用UserDict
    ud = UserDict()
    ud['a'] = 1
    ud['b'] = 2
    print(f"UserDict实例: {ud}")
    print(f"类型: {type(ud)}")
    print(f"是否包含'a': {'a' in ud}")
    
    # 从普通字典创建UserDict
    regular_dict = {'c': 3, 'd': 4}
    ud_from_dict = UserDict(regular_dict)
    print(f"从普通字典创建: {ud_from_dict}")
    
    # 访问data属性，data存储实际的字典数据
    print(f"ud.data: {ud.data}")
    print(f"类型: {type(ud.data)}")


class CaseInsensitiveDict(UserDict):
    """大小写不敏感的字典实现"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 初始化时转换所有键为小写
        self._convert_keys_to_lower()
    
    def _convert_keys_to_lower(self):
        """将所有键转换为小写"""
        for key in list(self.data.keys()):
            if isinstance(key, str):
                lower_key = key.lower()
                if lower_key != key:
                    self.data[lower_key] = self.data.pop(key)
    
    def __getitem__(self, key):
        """获取值时，将键转换为小写"""
        if isinstance(key, str):
            key = key.lower()
        return self.data[key]
    
    def __setitem__(self, key, value):
        """设置值时，将键转换为小写"""
        if isinstance(key, str):
            key = key.lower()
        self.data[key] = value
    
    def __contains__(self, key):
        """检查键是否存在时，将键转换为小写"""
        if isinstance(key, str):
            key = key.lower()
        return key in self.data
    
    def __delitem__(self, key):
        """删除键时，将键转换为小写"""
        if isinstance(key, str):
            key = key.lower()
        del self.data[key]


class LimitedSizeDict(UserDict):
    """固定大小的字典实现"""
    def __init__(self, size_limit, *args, **kwargs):
        self.size_limit = size_limit
        super().__init__(*args, **kwargs)
        # 如果初始数据超过大小限制，保留最后添加的项
        self._check_size_limit()
    
    def _check_size_limit(self):
        """检查并确保字典不超过大小限制"""
        while len(self.data) > self.size_limit:
            # 删除第一个添加的项（这里使用键的顺序，实际应用可能需要更复杂的逻辑）
            self.data.pop(next(iter(self.data)))
    
    def __setitem__(self, key, value):
        """添加新项时检查大小限制"""
        self.data[key] = value
        self._check_size_limit()


class ValidatedDict(UserDict):
    """带值验证的字典实现"""
    def __init__(self, validator=None, *args, **kwargs):
        self.validator = validator or (lambda x: True)  # 默认验证器总是返回True
        super().__init__(*args, **kwargs)
        # 验证初始数据
        self._validate_all()
    
    def _validate_all(self):
        """验证所有现有值"""
        for key, value in list(self.data.items()):
            if not self.validator(value):
                raise ValueError(f"Invalid value for key '{key}': {value}")
    
    def _validate_value(self, value):
        """验证单个值"""
        if not self.validator(value):
            raise ValueError(f"Invalid value: {value}")
    
    def __setitem__(self, key, value):
        """设置值前进行验证"""
        self._validate_value(value)
        self.data[key] = value
    
    def update(self, *args, **kwargs):
        """更新前进行验证"""
        # 先创建一个临时字典来验证所有值
        temp_dict = {}
        if args:
            if len(args) > 1:
                raise TypeError("update expected at most 1 argument")
            other = args[0]
            if isinstance(other, dict):
                temp_dict.update(other)
            elif hasattr(other, "keys"):
                temp_dict.update({k: other[k] for k in other.keys()})
            else:
                temp_dict.update({k: v for k, v in other})
        temp_dict.update(kwargs)
        
        # 验证所有值
        for value in temp_dict.values():
            self._validate_value(value)
        
        # 验证通过后再更新
        self.data.update(temp_dict)


def case_insensitive_example():
    """大小写不敏感字典示例"""
    print("\n大小写不敏感字典示例:")
    
    # 创建大小写不敏感的字典
    ci_dict = CaseInsensitiveDict()
    ci_dict['Name'] = 'John'
    ci_dict['AGE'] = 30
    ci_dict['city'] = 'New York'
    
    print(f"字典内容: {ci_dict}")
    print(f"访问'name': {ci_dict['name']}")  # 注意小写'name'
    print(f"访问'Name': {ci_dict['Name']}")  # 注意大写'Name'
    print(f"访问'age': {ci_dict['age']}")
    print(f"'CITY' in dict: {'CITY' in ci_dict}")
    
    # 修改值
    ci_dict['NAME'] = 'Jane'
    print(f"修改后访问'name': {ci_dict['name']}")
    
    # 删除键
    del ci_dict['City']
    print(f"删除'City'后: {ci_dict}")


def limited_size_example():
    """固定大小字典示例"""
    print("\n固定大小字典示例:")
    
    # 创建大小限制为3的字典
    limited_dict = LimitedSizeDict(3)
    
    # 添加项
    limited_dict['a'] = 1
    limited_dict['b'] = 2
    limited_dict['c'] = 3
    print(f"添加3个项后: {limited_dict}")
    
    # 添加第4个项，最旧的项'a'应该被移除
    limited_dict['d'] = 4
    print(f"添加第4个项后: {limited_dict}")
    
    # 从现有字典创建，超过大小限制
    large_dict = {'x': 10, 'y': 20, 'z': 30, 'w': 40}
    limited_from_large = LimitedSizeDict(2, large_dict)
    print(f"从大字典创建大小为2的字典: {limited_from_large}")


def validated_dict_example():
    """带验证的字典示例"""
    print("\n带验证的字典示例:")
    
    # 创建只接受整数值的字典
    int_validator = lambda x: isinstance(x, int)
    int_dict = ValidatedDict(int_validator)
    
    # 添加有效值
    int_dict['a'] = 10
    int_dict['b'] = 20
    print(f"有效整数字典: {int_dict}")
    
    # 尝试添加无效值
    try:
        int_dict['c'] = 'not an int'
    except ValueError as e:
        print(f"预期的验证错误: {e}")
    
    # 创建范围验证的字典
    range_validator = lambda x: isinstance(x, int) and 0 <= x <= 100
    range_dict = ValidatedDict(range_validator)
    
    range_dict['score1'] = 85
    range_dict['score2'] = 92
    print(f"范围验证字典: {range_dict}")
    
    # 尝试添加超出范围的值
    try:
        range_dict['score3'] = 150
    except ValueError as e:
        print(f"预期的范围错误: {e}")
    
    # 测试update方法
    try:
        range_dict.update({'score4': 75, 'score5': 120})  # score5超出范围
    except ValueError as e:
        print(f"update验证错误: {e}")
    print(f"update后的字典: {range_dict}")  # 应该没有变化，因为update应该整体成功或失败


def main():
    """主函数，演示UserDict的各种用法"""
    print("=== UserDict用法示例 ===")
    
    # 调用各个示例函数
    basic_usage()
    case_insensitive_example()
    limited_size_example()
    validated_dict_example()


if __name__ == "__main__":
    main()

"""
运行结果：
=== UserDict用法示例 ===
基本用法:
UserDict实例: {'a': 1, 'b': 2}
类型: <class 'collections.UserDict'>
是否包含'a': True
从普通字典创建: {'c': 3, 'd': 4}
ud.data: {'a': 1, 'b': 2}
类型: <class 'dict'>

大小写不敏感字典示例:
字典内容: {'name': 'John', 'age': 30, 'city': 'New York'}
访问'name': John
访问'Name': John
访问'age': 30
'CITY' in dict: True
修改后访问'name': Jane
删除'City'后: {'name': 'Jane', 'age': 30}

固定大小字典示例:
添加3个项后: {'a': 1, 'b': 2, 'c': 3}
添加第4个项后: {'b': 2, 'c': 3, 'd': 4}
从大字典创建大小为2的字典: {'z': 30, 'w': 40}

带验证的字典示例:
有效整数字典: {'a': 10, 'b': 20}
预期的验证错误: Invalid value: not an int
范围验证字典: {'score1': 85, 'score2': 92}
预期的范围错误: Invalid value: 150
update验证错误: Invalid value: 120
update后的字典: {'score1': 85, 'score2': 92}
"""
