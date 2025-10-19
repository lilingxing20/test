#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ChainMap的用法示例
ChainMap是一个字典子类，可以将多个字典合并为一个视图
"""

from collections import ChainMap


def basic_usage():
    """基本用法：创建和使用ChainMap"""
    print("基本用法:")
    
    # 创建几个字典
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    dict3 = {'a': 10, 'e': 5}  # 注意'a'键在dict1中也存在
    
    # 创建ChainMap
    chain = ChainMap(dict1, dict2, dict3)
    
    print(f"dict1: {dict1}")
    print(f"dict2: {dict2}")
    print(f"dict3: {dict3}")
    print(f"ChainMap: {chain}")
    
    # 访问键
    # 当多个字典有相同的键时，返回第一个遇到的键的值
    print(f"chain['a'] = {chain['a']}")  # 来自dict1
    print(f"chain['c'] = {chain['c']}")  # 来自dict2
    print(f"chain['e'] = {chain['e']}")  # 来自dict3
    
    # 检查键是否存在
    print(f"'a' in chain: {'a' in chain}")
    print(f"'f' in chain: {'f' in chain}")
    
    # 遍历ChainMap
    print("遍历ChainMap:")
    for key, value in chain.items():
        print(f"{key}: {value}")


def updating_behavior():
    """更新操作的行为"""
    print("\n更新操作的行为:")
    
    # 创建字典和ChainMap
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    chain = ChainMap(dict1, dict2)
    
    print(f"原始ChainMap: {chain}")
    
    # 更新操作只会修改第一个字典
    chain['a'] = 100  # 修改dict1中的'a'
    print(f"修改'a'后: {chain}")
    print(f"dict1现在: {dict1}")  # dict1被修改
    
    # 添加新键值对也只会添加到第一个字典
    chain['new_key'] = 999
    print(f"添加新键后: {chain}")
    print(f"dict1现在: {dict1}")  # dict1被修改
    print(f"dict2没有变化: {dict2}")
    
    # 删除键也只会从第一个字典中删除
    try:
        del chain['a']
        print(f"删除'a'后: {chain}")
        print(f"dict1现在: {dict1}")
    except KeyError as e:
        print(f"删除错误: {e}")
    
    # 尝试删除不在第一个字典中的键会引发KeyError
    try:
        del chain['c']  # 'c'在dict2中，但不在dict1中
    except KeyError as e:
        print(f"尝试删除不在第一个字典中的键'c': {e}")


def underlying_maps():
    """访问和操作底层映射列表"""
    print("\n访问和操作底层映射列表:")
    
    dict1 = {'a': 1}
    dict2 = {'b': 2}
    dict3 = {'c': 3}
    chain = ChainMap(dict1, dict2, dict3)
    
    # maps属性返回底层字典列表
    print(f"底层映射列表: {chain.maps}")
    
    # 可以直接修改底层字典
    chain.maps[0]['a'] = 100  # 修改dict1
    chain.maps[1]['b'] = 200  # 修改dict2
    print(f"修改底层字典后: {chain}")
    
    # 可以向maps列表添加新的字典
    new_dict = {'d': 4}
    chain.maps.append(new_dict)
    print(f"添加新字典后: {chain}")
    
    # 可以从maps列表中移除字典
    chain.maps.pop()
    print(f"移除最后一个字典后: {chain}")


def new_child():
    """使用new_child()方法创建新的ChainMap"""
    print("\n使用new_child()方法:")
    
    # 创建父ChainMap
    parent = ChainMap({'a': 1, 'b': 2}, {'c': 3})
    
    # 创建子ChainMap，添加一个新的空字典在最前面
    child = parent.new_child()
    print(f"父ChainMap: {parent}")
    print(f"子ChainMap: {child}")
    
    # 可以在创建子ChainMap时提供一个字典
    child_with_dict = parent.new_child({'a': 100, 'x': 999})
    print(f"带初始字典的子ChainMap: {child_with_dict}")
    
    # 修改子ChainMap只会影响最前面的字典
    child['a'] = 200
    print(f"修改子ChainMap后: {child}")
    print(f"父ChainMap保持不变: {parent}")
    
    # parents属性返回没有第一个字典的ChainMap
    print(f"child.parents: {child.parents}")


def practical_examples():
    """实际应用示例"""
    print("\n实际应用示例:")
    
    # 示例1：配置管理
    # 在配置系统中，可以有默认配置、全局配置和用户配置
    default_config = {
        'port': 8080,
        'host': 'localhost',
        'debug': False
    }
    
    global_config = {
        'port': 80,
        'host': '0.0.0.0'
    }
    
    user_config = {
        'debug': True,
        'api_key': 'user123'
    }
    
    # 使用ChainMap合并配置，优先级为：user_config > global_config > default_config
    config = ChainMap(user_config, global_config, default_config)
    
    print("配置管理示例:")
    print(f"默认配置: {default_config}")
    print(f"全局配置: {global_config}")
    print(f"用户配置: {user_config}")
    print(f"最终合并配置: {config}")
    print(f"实际使用的端口: {config['port']}")
    print(f"实际使用的调试模式: {config['debug']}")
    
    # 示例2：命令行参数、环境变量和配置文件的优先级处理
    # 这是一个简化的例子，实际应用中可能会结合argparse和os.environ
    def get_settings():
        # 配置文件设置
        config_file = {
            'output_dir': './default_output',
            'max_retries': 3
        }
        
        # 环境变量（这里模拟）
        env_vars = {
            'output_dir': '/tmp/output',
            'log_level': 'INFO'
        }
        
        # 命令行参数（这里模拟）
        cmd_args = {
            'max_retries': 5,
            'verbose': True
        }
        
        # 优先级：命令行参数 > 环境变量 > 配置文件
        settings = ChainMap(cmd_args, env_vars, config_file)
        return settings
    
    settings = get_settings()
    print("\n设置优先级示例:")
    print(f"合并后的设置: {settings}")
    print(f"最终的输出目录: {settings['output_dir']}")
    print(f"最终的最大重试次数: {settings['max_retries']}")


def performance_considerations():
    """性能考虑"""
    print("\n性能考虑:")
    print("1. ChainMap不会创建新字典，而是维护对原始字典的引用")
    print("2. 查找操作需要按顺序检查每个字典，因此字典数量越多，查找可能越慢")
    print("3. 修改操作（插入、更新、删除）只影响第一个字典，因此性能良好")
    print("4. 适合需要保持多个字典独立性同时又要统一访问的场景")


def main():
    """主函数，演示ChainMap的各种用法"""
    print("=== ChainMap用法示例 ===")
    
    # 调用各个示例函数
    basic_usage()
    updating_behavior()
    underlying_maps()
    new_child()
    practical_examples()
    performance_considerations()


if __name__ == "__main__":
    main()

"""
运行结果：
=== ChainMap用法示例 ===
基本用法:
创建ChainMap: ChainMap({'a': 1}, {'b': 2}, {'c': 3})
获取键'a': 1
获取键'b': 2
获取键'c': 3
获取不存在的键'z': KeyError
遍历ChainMap: a=1, b=2, c=3
键的集合: {'a', 'b', 'c'}
值的集合: {1, 2, 3}
键值对: dict_items([('a', 1), ('b', 2), ('c', 3)])

更新操作行为:
修改第一个字典: ChainMap({'a': 100, 'b': 2}, {'c': 3})
添加新键值对: ChainMap({'a': 100, 'b': 2, 'd': 4}, {'c': 3})
删除键'a': ChainMap({'b': 2, 'd': 4}, {'c': 3})
修改不在第一个字典中的键'b': ChainMap({'b': 999, 'd': 4}, {'c': 3})
更新dict1后: ChainMap({'b': 2, 'new_key': 999}, {'c': 3, 'd': 4})
dict1现在: {'b': 2, 'new_key': 999}
尝试删除不在第一个字典中的键'c': "Key not found in the first mapping: 'c'"

访问和操作底层映射列表:
底层映射列表: [{'a': 1}, {'b': 2}, {'c': 3}]
修改底层字典后: ChainMap({'a': 100}, {'b': 200}, {'c': 3})
添加新字典后: ChainMap({'a': 100}, {'b': 200}, {'c': 3}, {'d': 4})
移除最后一个字典后: ChainMap({'a': 100}, {'b': 200}, {'c': 3})

使用new_child()方法:
父ChainMap: ChainMap({'a': 1, 'b': 2}, {'c': 3})
子ChainMap: ChainMap({}, {'a': 1, 'b': 2}, {'c': 3})
带初始字典的子ChainMap: ChainMap({'a': 100, 'x': 999}, {'a': 1, 'b': 2}, {'c': 3})
修改子ChainMap后: ChainMap({'a': 200}, {'a': 1, 'b': 2}, {'c': 3})
父ChainMap保持不变: ChainMap({'a': 1, 'b': 2}, {'c': 3})
child.parents: ChainMap({'a': 1, 'b': 2}, {'c': 3})

实际应用示例:
配置管理示例:
默认配置: {'port': 8080, 'host': 'localhost', 'debug': False}
全局配置: {'port': 80, 'host': '0.0.0.0'}
用户配置: {'debug': True, 'api_key': 'user123'}
最终合并配置: ChainMap({'debug': True, 'api_key': 'user123'}, {'port': 80, 'host': '0.0.0.0'}, {'port': 8080, 'host': 'localhost', 'debug': False})
实际使用的端口: 80
实际使用的调试模式: True

设置优先级示例:
合并后的设置: ChainMap({'max_retries': 5, 'verbose': True}, {'output_dir': '/tmp/output', 'log_level': 'INFO'}, {'output_dir': './default_output', 'max_retries': 3})
最终的输出目录: /tmp/output
最终的最大重试次数: 5

性能考虑:
1. ChainMap不会创建新字典，而是维护对原始字典的引用
2. 查找操作需要按顺序检查每个字典，因此字典数量越多，查找可能越慢
3. 修改操作（插入、更新、删除）只影响第一个字典，因此性能良好
4. 适合需要保持多个字典独立性同时又要统一访问的场景
"""
