"""
3. 序列操作函数
"""

# len(), sorted(), reversed(), enumerate()
print(len("hello"))  # 5 序列长度
print(sorted([3,1,2], reverse=True))  # [3,2,1] 排序（降序）

for i, v in enumerate(["a", "b"]):
    print(f"{i}:{v}")  # 0:a 1:b 枚举（索引和值）

# zip(), filter(), map()
names = ["Alice", "Bob"]
ages = [25, 30]
print(list(zip(names, ages)))  # [('Alice',25), ('Bob',30)] 压缩（对应元素打包）

print(list(filter(lambda x: x>0, [-1,0,1])))  # [1] 过滤（保留符合条件的元素）
print(list(map(str.upper, ["a", "b"])))  # ['A','B'] 映射（对元素进行转换）
