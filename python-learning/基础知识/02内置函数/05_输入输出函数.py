"""
5. 输入输出函数
"""

#  print(), input()
print("Hello", "World", sep=", ")  # Hello, World
name = input("Enter your name: ")  # Enter your name: Lixx
print("Hello", name)  # Hello Lixx

# open() 文件操作
with open("test.txt", "w") as f:
    f.write("Hello")
with open("test.txt", "r") as f:
    content = f.read()
    print(content)  # Hello
