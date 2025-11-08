""" 动态参数解包
Python允许在函数调用时使用动态参数解包。

语法：
*args：用于接收任意数量的位置参数，将其打包成一个元组。
**kwargs：用于接收任意数量的关键字参数，将其打包成一个字典。

示例：
```python
def my_func(*args, **kwargs):
    print(args)
    print(kwargs)
    my_func(1, 2, 3, a=4, b=5)
```
输出：
```
(1, 2, 3)
{'a': 4, 'b': 5}
```
在调用my_func时，可以传入任意数量的位置参数和任意数量的关键字参数，并将其解包成元组和字典。
注意：
1. 位置参数必须在关键字参数之前。
2. 关键字参数必须在位置参数之后。
3. 解包时，必须传入参数名。
4. 解包时，参数名必须与函数定义时参数名一致。
5. 解包时，参数名可以用下划线代替。
6. 解包时，参数名可以省略。
7. 解包时，参数名可以重名。 
8. 解包时，参数名可以不按顺序传入。
9. 解包时，参数名可以传入None。
10. 解包时，参数名可以传入空元组或字典。
11. 解包时，参数名可以传入不完整元组或字典。
12. 解包时，参数名可以传入重复的关键字参数。
13. 解包时，参数名可以传入不合法的关键字参数。
"""


def arg_unpacker(a, *args, **kwargs):
    print(f'a: {a}')
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')

arg_unpacker(1, 2, 3, key1='value1', key2='value2')
# 输出：
# a: 1
# args: (2, 3)
# kwargs: {'key1': 'value1', 'key2': 'value2'}


# 示例2：
# 计算1到10的偶数平方和偶数的和
print("8.1 动态参数解包示例2：")
def sum_of_squares_and_evens(*args):
    even_sum = 0
    square_sum = 0
    for arg in args:
        if arg % 2 == 0:
            even_sum += arg
            square_sum += arg ** 2
    return even_sum, square_sum

print(sum_of_squares_and_evens(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# 输出：
# (30, 255)


# 示例3：
# 计算1到10的偶数平方和偶数的和
print("8.2 动态参数解包示例3：")
def sum_of_squares_and_evens(*args):
    even_sum = 0
    square_sum = 0
    for arg in args:
        if arg % 2 == 0:
            even_sum += arg
            square_sum += arg ** 2
    return even_sum, square_sum

print(sum_of_squares_and_evens(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# 输出：
# (30, 255)
