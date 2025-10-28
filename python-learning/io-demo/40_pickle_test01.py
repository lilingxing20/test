""" pickle模块
Python 的 pickle模块可实现序列化和反序列化，即将对象序列化成字节流，并将字节流反序列化成对象。

序列化：将对象转换成字节流的过程称为序列化，反之，将字节流转换成对象称为反序列化。

pickle模块提供了两个函数：

- dump(obj, file, protocol=None, *, fix_imports=True)
- load(file, *, fix_imports=True, encoding="ASCII", errors="strict")

其中，dump()函数用于将对象序列化成文件，load()函数用于将文件反序列化成对象。

注意：
  - 序列化对象时，只能序列化那些支持 pickle 模块的对象，比如说自定义的类、列表、字典等。
  - 反序列化对象时，只能反序列化那些序列化过的对象，否则会报错。
  - 序列化和反序列化的对象必须是同一个程序的，即使是不同版本的 Python 也不行。
  - 序列化的对象越复杂，序列化所需的时间也越长。
  - 建议只用于本地数据存储，不用于网络传输。
  - 建议使用 JSON 格式来代替 pickle 格式，因为 JSON 格式更简单、更易读。
"""

import os
import pickle

# 定义一个类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 获取当前文件路径
current_dir = os.path.dirname(os.path.abspath(__file__))
# 切换到当前目录
os.chdir(current_dir)

# 实例化一个对象
print('实例化一个对象')
p = Person('Alice', 25)
print(p.name, p.age)  # 输出：Alice 25

# 序列化对象
print('序列化对象')
with open('person.pkl', 'wb') as f:
    pickle.dump(p, f)
print("序列化文件已保存到 person.pkl")

# 反序列化对象
print('反序列化对象')
with open('person.pkl', 'rb') as f:
    p2 = pickle.load(f)

print(p2.name, p2.age)  # 输出：Alice 25


""" 运行结果：
实例化一个对象
Alice 25
序列化对象
序列化文件已保存到 person.pkl
反序列化对象
Alice 25
"""
