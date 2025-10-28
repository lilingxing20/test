""" 分布式进程 Master/Worker 模型
启动服务端进程，将任务添加到队列中，等待客户端消费队列中的任务并且获取任务消费结果
"""

from multiprocessing import Process
from multiprocessing.managers import BaseManager
from queue import Queue


class QueueManager(BaseManager):
    """继承自BaseManager的队列管理器类"""
    pass


# 全局变量，单例模式，所有进程共享, 确保每次调用都返回同一个队列实例
task_queue = Queue()  # 任务队列
result_queue = Queue()  # 结果队列


def get_task_queue():
    """获取任务队列"""
    return task_queue


def get_result_queue():
    """获取结果队列"""
    return result_queue


# 注册队列获取函数
QueueManager.register('get_task_queue', callable=get_task_queue)
QueueManager.register('get_result_queue', callable=get_result_queue)


def start_manager():
    """启动分布式管理器
    
    Returns:
        QueueManager: 启动后的队列管理器实例
    """
    # 创建并启动管理器，监听所有网络接口的11202端口
    queue_manager = QueueManager(address=('', 11202), authkey=b'a123456')
    queue_manager.start()
    return queue_manager


def server():
    """模拟服务器端，启动Manager并添加任务到队列中"""
    manager = start_manager()  # 启动Manager，绑定到11202端口
    task_queue = manager.get_task_queue()  # 获取任务队列
    result_queue = manager.get_result_queue()  # 获取结果队列
    print(f"Task queue: {task_queue}")
    print(f"Result queue: {result_queue}")

    # 模拟添加任务到队列中
    for i in range(5):
        task_queue.put(i)
        print(f"Task {i} added to the task queue.")

    # 模拟获取任务的结果
    for _ in range(5):
        result = result_queue.get(timeout=100)
        print(f"Received result: {result}")

    # 关闭QueueManager
    manager.shutdown()


if __name__ == '__main__':
    # 启动服务器进程
    server_process = Process(target=server)
    server_process.start()
    server_process.join()
