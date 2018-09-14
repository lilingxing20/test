# -*- coding: utf-8 -*-
##
# RPC调用请求客户端的启动脚本
##
import rpc
# 主题
TOPIC = 'sendout_request'

# 消息体
msg = {'method': 'add',              # RPC调用的方法名
       'args':{'v1':2, 'v2':3}}      # 参数列表
rval = rpc.call(TOPIC, msg)          # 发送rpc.call请求
print('Succeed implementing RPC call. the return value is %d.\n' % rval)


