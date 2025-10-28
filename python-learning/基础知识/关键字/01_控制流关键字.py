"""
1. 控制流关键字
"""

# if/elif/else 条件判断
if 2 > 1:
    print("True")
elif 1 == 1:
    print("Equal")
else:
    print("False")


# for/while 循环
for i in range(3):
    print(i)  # 输出 0,1,2

count = 0
while count < 3:
    print(count)
    count += 1


# break/continue 循环控制
for i in range(5):
    if i == 3:
        break  # 终止循环
    if i == 1:
        continue  # 跳过本次循环
    print(i)
