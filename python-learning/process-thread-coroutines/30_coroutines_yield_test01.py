"""
Python 中的 协程（coroutines） 又称微线程，纤程，是一种用于实现并发操作的编程方式，它是基于生成器（generator）和 asyncio 库的一种异步编程模型。
协程可以使得 Python 在处理 I/O 密集型任务时，不需要等待任务完成，可以继续处理其他任务。
Python中的协程是基于generator实现的，在 generator 中，我们不但可以通过 for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。
但Python的 yield 不但可以返回一个值，它还可以接收调用者发出的参数。
"""

from calendar import c


def consumer():
    cr = ''
    while True:
        # 接收生产者 send 的数据
        n = yield cr
        if not n: # 如果没有数据直接结束
            print('[CONSUMER] Consumer exit.')
            return
        print('[CONSUMER] Consuming %s...' % n)
        cr = '200 OK'


def produce(c):
    # 启动协程，调用生成器的 `__next__` 方法，进入 `yield` 暂停状态
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        pr = c.send(n) # 将数据发送给消费者，并接收消费者的响应
        print('[PRODUCER] Consumer return: %s' % pr)
    c.close() # 关闭消费者协程


if __name__ == '__main__':
    consumer = consumer()
    produce(consumer)


""" 运行结果：
[PRODUCER] Producing 1...
[CONSUMER] Consuming 1...
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 2...
[CONSUMER] Consuming 2...
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 3...
[CONSUMER] Consuming 3...
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 4...
[CONSUMER] Consuming 4...
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 5...
[CONSUMER] Consuming 5...
[PRODUCER] Consumer return: 200 OK
"""
