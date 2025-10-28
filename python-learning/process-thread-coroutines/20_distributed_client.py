""" 分布式进程 Master/Worker 模型
连接服务，接收服务端任务并将消费结果放到另一个队列中
"""

from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    """继承自BaseManager的队列管理器类"""
    pass


# 注册方法，使得客户端可以访问
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')


def client():
    """客户端连接到任务队列并从中获取任务"""
    # 连接到服务器上指定的端口
    manager = QueueManager(address=('', 11202), authkey=b'a123456')
    manager.connect()

    task_queue = manager.get_task_queue()
    result_queue = manager.get_result_queue()
    print(f"Task queue: {task_queue}")
    print(f"Result queue: {result_queue}")

    # 处理任务
    while not task_queue.empty():
        task = task_queue.get()
        print(f"Processing task: {task}")
        result = task * 2  # 假设任务是乘以2
        result_queue.put(result)


if __name__ == '__main__':
    client()
