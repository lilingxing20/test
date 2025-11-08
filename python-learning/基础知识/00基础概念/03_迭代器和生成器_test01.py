""" 
迭代器和生成器
  1. 迭代器: iter()函数可以将可迭代对象转换为迭代器对象。
  2. 生成器: range()函数返回一个生成器对象，该对象可以生成一个无限序列，而不必一次性生成所有元素。
  3. 自定义生成器: yield关键字可以让函数变成一个生成器函数。

内存占用对比
  1. 生成器：通过yield按需生成数据，每次只保留当前值，避免一次性加载全部数据到内存。
  2. 迭代器：需手动实现next()方法，虽然也能按需生成数据，但代码冗长且可能引入额外开销。

适用场景
  1. 生成器：适合处理无限序列或大数据流（如斐波那契数列、文件逐行读取），语法简洁且内存占用更低。
  2. 迭代器：适用于需要自定义遍历逻辑的场景，但实现复杂度较高。

性能差异
  1. 内存效率：生成器因惰性计算和更少的代码冗余，通常比迭代器更优。 
  2. 执行速度：迭代器可能因手动实现的优化逻辑更快，但差异通常较小。
"""

# 迭代器: iter()函数可以将可迭代对象转换为迭代器对象。
my_iter = iter([10, 20, 30, 40, 50])
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# 生成器: range()函数返回一个生成器对象，该对象可以生成一个无限序列，而不必一次性生成所有元素。
my_gen = (x**2 for x in range(10))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

# 自定义生成器: yield关键字可以让函数变成一个生成器函数。
def count_up(n):
    """Counts up from 0 to n."""
    i = 0
    value = 10
    while i < n:
        yield value
        value += 10
        i += 1
for i in count_up(5):
    print(i)
