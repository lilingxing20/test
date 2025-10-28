""" 闭包的高级应用
2. 闭包与面向对象编程
闭包可以实现类似面向对象编程中的封装和状态保持，有时比类更轻量。
示例：闭包实现对象特性
"""


def person(name):
    age = 0
    def get_age():
        return age
    def set_age(new_age):
        nonlocal age
        age = new_age
    def info():
        return f"{name}, {age}岁"
    return {'get_age': get_age, 'set_age': set_age, 'info': info}


if __name__ == "__main__":
    # 初始person
    p = person("张三")
    # 打印信息
    print(p['info']())  # 输出: 张三, 0岁
    # 更新age
    p['set_age'](25)
    # 打印信息
    print(p['info']())  # 输出: 张三, 25岁


""" 运行结果：
张三, 0岁
张三, 25岁
"""
