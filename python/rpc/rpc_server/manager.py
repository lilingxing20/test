# -*- coding: utf-8 -*-
##
# 定义了处理RPC调用请求的方法
##

class Manager(object):
    def add(self, v1=0, v2=0):
        rval = v1 + v2
        print("%(v1)d + %(v2)d is %(rval)d\n" %locals())
        return rval
