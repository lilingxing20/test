# -*- coding: utf-8 -*-
##
# 主要用于创建和管理RPC服务
##
import rpc
import manager
import dispatcher

# 定义主题交换机的主题
TOPIC = 'sendout_request'

class Service(object):
    def __init__(self):
        self.topic = TOPIC
        # 定义处理RPC请求方法
        self.manager = manager.Manager()

    def start(self):
        # 创建RbbitMQ连接
        self.conn = rpc.create_connection()
        # 创建分发器
        rpc_dispatcher = dispatcher.RpcDispatcher(self.manager)
        # 创建主题消费者
        self.conn.create_consumer(self.topic, rpc_dispatcher)
        # 激活主题消费者
        self.conn.consume()

    def drain_events(self):
        # 用来接收和处理RPC请求
        self.conn.drain_events()

