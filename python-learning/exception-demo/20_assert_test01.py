"""
Assert 断言

断言失败，抛出 AssertionError
"""

def assert_test(n):
    n = int(n)
    assert n > 0
    return 10/n

def main():
    try:
        assert assert_test(5)
    except AssertionError:
        print("AssertionError")
    else:
        print("No Error")
    finally:
        print("finally")
        
    try:
        assert assert_test(0)
    except AssertionError:
        print("AssertionError")
    else:
        print("No Error")
    finally:
        print("finally")


if __name__ == "__main__":
    main()


""" 运行结果：
No Error
finally
AssertionError
finally
"""

"""
注： 运行时使用 -O xxx.py 可以跳过断言(可将assert看成pass)
运行结果：
No Error
finally
No Error
finally
"""
