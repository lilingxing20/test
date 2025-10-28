""" logging 模块
logging 模块是一个用于生成日志记录的标准库，通过 logging 模块，可以灵活地设置多个日志处理器（Handler），分别将日志输出到不同的地方，比如控制台、文件、邮件等。常用的处理器有：
  - StreamHandler: 将日志输出到控制台。
  - FileHandler: 将日志输出到文件。
  - SMTPHandler: 将日志通过电子邮件发送。

格式化
  - %(asctime)s: 日志时间戳
  - %(name)s: 记录器的名称
  - %(levelname)s: 日志级别
  - %(message)s: 日志消息

"""

import logging


# 0. 设置基本配置
logging.basicConfig(level=logging.DEBUG,  # 设置最低日志级别
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 设置日志格式

# 1. 生成不同级别的日志信息
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")


""" 运行结果：
2025-10-26 23:21:25,805 - root - DEBUG - This is a debug message
2025-10-26 23:21:25,805 - root - INFO - This is an info message
2025-10-26 23:21:25,805 - root - WARNING - This is a warning message
2025-10-26 23:21:25,805 - root - ERROR - This is an error message
2025-10-26 23:21:25,805 - root - CRITICAL - This is a critical message
"""
