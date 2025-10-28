""" 闭包的核心使用场景:
3. 装饰器实现
装饰器本质上是闭包的应用，用于在不修改原函数代码的情况下增强函数功能。
示例：日志装饰器
"""

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"开始执行函数: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"函数执行完毕, 结果: {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

if __name__ == '__main__':
    add(2, 3)


""" 运行结果：
开始执行函数: add
函数执行完毕, 结果: 5
"""
