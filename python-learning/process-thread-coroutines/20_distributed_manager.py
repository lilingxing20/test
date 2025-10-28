""" 分布式进程 Master/Worker 模型
启动一个 manager 并暴露网络端口，用于分布式任务处理。
"""

from multiprocessing.managers import BaseManager
from queue import Queue


class QueueManager(BaseManager):
    """继承自BaseManager的队列管理器类"""
    pass


def get_task_queue():
    """获取任务队列"""
    return Queue()


def get_result_queue():
    """获取结果队列"""
    return Queue()


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


if __name__ == '__main__':
    manager = start_manager()
    print("Server started, waiting for client connections...")
