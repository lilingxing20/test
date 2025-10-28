"""
协程本质上是一种 可暂停和恢复执行的函数，通常在执行过程中遇到 await 关键字时挂起，等到某个操作完成后再继续执行。

  - 协程的特点：
    * 协程是一种轻量级的子程序，它可以被暂停并在需要的时候恢复执行。
    * 协程的调度由事件循环（event loop）来完成，它可以自动切换协程，因此可以实现并发执行。
    * 协程的实现可以用纯 Python 代码来实现，不需要像线程那样需要操作系统的帮助。
  - 协程的应用：
    * 异步 I/O：通过协程可以实现异步 I/O，即发起一个耗时操作（如读写文件、网络请求等）后，
    并不等待操作完成，而是直接切换到其他协程，当操作完成后再切换回来继续执行。
    * 并发编程：通过协程可以实现并发编程，即同时运行多个任务（协程）而不用等待，
    协程的调度由事件循环自动完成，可以有效提高程序的并发性。
    * 微任务（微线程）：通过协程可以实现微任务，即在一个线程中执行多个协程，
    这样可以避免多线程的复杂性。

asyncio模块：
  - asyncio模块是Python 3.4版本引入的标准库，它提供了用于编写异步代码的工具。
  - asyncio模块的主要概念：
    * 事件循环（event loop）：asyncio模块的核心，负责协程的调度和执行。
    * 协程（coroutine）：一个协程是一个可暂停和恢复执行的函数，可以用async关键字定义。
    * 任务（task）：一个任务就是一个协程的执行实例，可以把它看成是协程的容器。
    * 事件循环（event loop）：事件循环是一个循环，用于不断检查任务的状态并执行任务。

asyncio模块的主要功能：
  - 异步IO：asyncio模块提供了异步IO的支持，可以让程序异步地执行IO操作，不会阻塞线程。
  - 并发编程：asyncio模块提供了并发编程的支持，可以让程序同时执行多个任务。
  - 微任务：asyncio模块提供了微任务的支持，可以让程序在一个线程中执行多个协程。

协程函数（coroutine function）：
  - 定义：async def 函数名():
    * 关键字async：定义一个协程函数。
    * 关键字def：定义一个普通函数。
    * 函数名：协程函数的名称。
  - 调用：await 协程函数()
    * 关键字await：等待协程的执行结果。
    * 协程函数()：要调用的协程函数。

asyncio.sleep()函数：
  - 定义：asyncio.sleep(seconds)
    * seconds：等待的秒数。
  - 调用：await asyncio.sleep(seconds)
    * 关键字await：等待asyncio.sleep()的执行结果。
    * asyncio.sleep(seconds)：要调用的协程函数。

asyncio.sleep()也是一个async函数，所以线程不会等待asyncio.sleep()。
如果把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的async函数了，因此可以实现并发执行。

下面是一个简单的示例：使用 `async def` 定义一个协程函数，并使用`await`来等待其他协程。
"""

import time
import asyncio


async def run():
    print(f"{time.time()} Hello world!")
    # 异步调用 asyncio.sleep(1):
    await asyncio.sleep(1)
    print(f"{time.time()} Hello again!")


if __name__ == '__main__':
    # 要运行协程，可通过事件循环（asyncio）来启动它。
    # 可以通过 asyncio.run() 来运行协程。
    asyncio.run(run())


""" 运行结果：
1694502000.0 Hello world!
1694502001.0 Hello again!
"""
