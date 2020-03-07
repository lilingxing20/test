# -*- coding: utf-8 -*-
##
# 将客户端发布的消息分发给相应的方法处理
##
class RpcDispatcher(object):
    def __init__(self, callback):
        self.callback = callback

    def dispatch(self, method, **kwargs):
        # 如果Manager对象定义了method方法，则执行method方法
        if hasattr(self.callback, method):
            return getattr(self.callback, method)(**kwargs)
        # 否则，报错
        print('No such RPC method: %s\n' % method)

