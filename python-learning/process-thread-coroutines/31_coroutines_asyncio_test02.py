"""
asyncio.gather()同时调度多个async函数；如果把asyncio.sleep()换成真正的IO操作，则多个并发的IO操作实际上可以由一个线程并发执行。
"""

import asyncio
import threading


async def task(name):
    print("Start task: %s (%s)" % (name, threading.current_thread()))
    await asyncio.sleep(2)
    print("End task: %s" % name)
    return name


async def main():
    # 并发运行任务, 等待任务的执行，并获取执行结果
    r0 = await asyncio.gather(task('task1'), task('task2'), task('task3'))
    print(r0)


if __name__ == '__main__':
    asyncio.run(main())


""" 运行结果：
Start task: task1 (<_MainThread(MainThread, started 8474183680)>)
Start task: task2 (<_MainThread(MainThread, started 8474183680)>)
Start task: task3 (<_MainThread(MainThread, started 8474183680)>)
End task: task1
End task: task2
End task: task3
['task1', 'task2', 'task3']
"""
