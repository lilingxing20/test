# -*- coding: utf-8 -*-
##
# 服务器端的启动脚本
##
import service

# 创建RPC服务
srv = service.Service()
# 启动RPC服务
srv.start()

while True:
    # 监听RPC服务
    srv.drain_events()
