""" 闭包的核心使用场景:
5. 状态保持
闭包可以用于在函数调用之间保持状态，而无需使用全局变量或类。
示例：平均值计算器
"""

def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return averager


if __name__ == "__main__":
    avg = make_averager()
    print(avg(10))  # 10.0
    print(avg(20))  # 15.0
    print(avg(30))  # 20.0


""" 运行结果：
10.0
15.0
20.0
"""
