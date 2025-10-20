"""
itertools 模块
    提供了用于操作迭代器的函数，如组合、排列、循环等。
    常用函数：
        product()：计算多个可迭代对象的笛卡尔积。
        permutations()：计算可迭代对象的所有排列。
        combinations()：计算可迭代对象的所有组合。
        count()：生成从指定值开始的无限整数序列。
        cycle()：循环遍历可迭代对象。
        repeat()：重复生成指定值。
"""

import itertools


# count(start=0, step=1)
# 返回一个无限迭代器，从 start 开始，每次递增 step，默认是从 0 开始，步长为 1。
counter = itertools.count(1)
print(next(counter))
print(next(counter))
"""执行结果：
1
2
...
"""

counter = itertools.count(10, 20)
print(next(counter))
print(next(counter))
"""执行结果：
10
30
...
"""


# 创建一个无限的迭代器，重复遍历输入的可迭代对象。
cs = itertools.cycle([1, 2])
print(next(cs))  # 1
print(next(cs))  # 2
print(next(cs))  # 1
"""执行结果：
1
2
1
...
"""

cs = itertools.cycle("这雨，出生于天，死于大地。中间的过程，便是人生。")
print(next(cs))
print(next(cs))
"""执行结果：
这
雨
"""


# repeat(object, times=None)
# 返回一个迭代器，重复返回同一个对象 times 次。如果 times 不指定，则默认无限次重复。
r0 = itertools.repeat("王林", 2)
print(next(r0))
print(next(r0))
"""执行结果：
王林
王林
...
"""


items = ['王林', '李慕婉', '红蝶']
# permutations(iterable, r=None)
# 返回输入元素的所有排列组合（按顺序的排列组合）。如果给定参数 r，则返回所有 r 长度的排列。
perms = itertools.permutations(items, 2)
for perm in perms:
    print(perm)
"""执行结果：
('王林', '李慕婉')
('王林', '红蝶')
('李慕婉', '王林')
('李慕婉', '红蝶')
('红蝶', '王林')
('红蝶', '李慕婉')
"""

# combinations(iterable, r)
# 返回输入元素的所有 r 长度的组合，组合中的元素是无序的。
combs = itertools.combinations(items, 2)
for c in combs:
    print(c)
"""执行结果：
('王林', '李慕婉')
('王林', '红蝶')
('李慕婉', '红蝶')
"""

# combinations_with_replacement(iterable, r)
# 返回所有 r 长度的组合，并允许元素重复。
combs = itertools.combinations_with_replacement(items, 2)
for c in combs:
    print(c)
""" 执行结果：
('王林', '王林')
('王林', '李慕婉')
('王林', '红蝶')
('李慕婉', '李慕婉')
('李慕婉', '红蝶')
('红蝶', '红蝶')
"""


# product(*iterables, repeat=1)
# 返回多个可迭代对象的笛卡尔积。可以通过 repeat 参数指定重复次数。
items = ['王林', '李慕婉']
prod = itertools.product(items, repeat=2)
for p in prod:
    print(p)
""" 执行结果：
('王林', '王林')
('王林', '李慕婉')
('李慕婉', '王林')
('李慕婉', '李慕婉')
"""

# chain(*iterables)
# 将多个可迭代对象连接成一个大的迭代器，按顺序返回每个元素。
chain_obj = itertools.chain('ABC', '123')
print(list(chain_obj))
""" 执行结果：
['A', 'B', 'C', '1', '2', '3']
"""


# zip_longest(*iterables, fillvalue=None)
# 类似 zip()，但会填充较短的可迭代对象，使它们的长度一致，直到最长的迭代器耗尽。
a = [1, 2, 3]
b = ['a', 'b']
zipped = itertools.zip_longest(a, b, fillvalue='x')
print(list(zipped))
""" 执行结果：
[(1, 'a'), (2, 'b'), (3, 'x')]
"""


# islice(iterable, start, stop, step)
# 返回一个迭代器，表示输入可迭代对象的一个切片，类似于切片操作，但是它是懒加载的（按需计算）。
items = range(10)
sliced = itertools.islice(items, 2, 8, 2)
print(list(sliced))
""" 执行结果：
[2, 4, 6]
"""


# groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key,group in itertools.groupby("王王麻麻子小林子"):
    print(key, list(group))
""" 执行结果：
王  ['王', '王']
麻 ['麻', '麻']
子 ['子']
小 ['小']
林 ['林']
子 ['子']
"""
