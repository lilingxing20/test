"""
3. 异常处理关键字
"""


# try/except/else/finally
try:
    result = 10 / 0
except ZeroDivisionError:
    print("不能除以0")
else:
    print("无异常时执行")
finally:
    print("总是执行")


# raise 抛出异常
if not isinstance(5, str):
    raise TypeError("需要字符串类型")
