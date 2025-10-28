"""
ThreadLocal
在Python中，ThreadLocal是threading模块提供的一个类，用于在不同线程之间保持独立的数据。每个线程可以在ThreadLocal对象中存储自己的独立数据，这些数据对其他线程是不可见的。可通过ThreadLocal对象的_thread_local属性来存取属于该线程的特有数据
ThreadLocal使用场景：为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等。
"""

import threading


# 创建ThreadLocal对象来存储线程特定的数据库连接
db_connection = threading.local()


class DatabaseConnection:
    def __init__(self, thread_name):
        self.thread_name = thread_name
        self.connection = f"Connection for {thread_name}"

    def get_connection(self):
        return self.connection


def get_db_connection():
    if not hasattr(db_connection, "connection"):
        # 如果当前线程没有连接，则创建一个新的
        print(f"Creating new connection for {threading.current_thread().name}")
        db_connection.connection = DatabaseConnection(threading.current_thread().name)
    return db_connection.connection.get_connection()


def worker():
    print(f"Thread {threading.current_thread().name} uses {get_db_connection()}")


if __name__ == "__main__":
    # 三个线程分别使用同一个数据库连接
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


""" 运行结果：
Creating new connection for Thread-1
Creating new connection for Thread-2
Creating new connection for Thread-3
Thread Thread-1 uses Connection for Thread-1
Thread Thread-2 uses Connection for Thread-2
Thread Thread-3 uses Connection for Thread-3
"""
