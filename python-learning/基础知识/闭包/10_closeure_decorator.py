""" 闭包的高级应用
1. 闭包与装饰器结合
闭包是Python装饰器的基础，理解闭包有助于深入掌握装饰器。
示例：带参数的装饰器
"""


def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("args: ", args)
            print("kwargs: ", kwargs)
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(num_times=3)
def greet(id, name, age):
    print(f"Hello {name}, id: {id}, age: {age}")


if __name__ == "__main__":
    greet(1001, "LiLei", age=20)


""" 运行结果：
Hello World
Hello World
Hello World
"""
