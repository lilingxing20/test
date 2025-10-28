"""
异常处理try-except-else-finally
"""

try:
    a = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError as e:
    print("ZeroDivisionError", e)
else: # else 在没有任何异常的时候执行
    print("No Error")
finally:
    print("finally")


""" 运行结果：
ZeroDivisionError
finally
"""
