""" 自定义的日志器
日志器（Logger），创建自定义的日志器来进行更复杂的日志管理：
"""

import logging
import os


# 获取当前文件路径
current_dir = os.path.dirname(os.path.abspath(__file__))
# 切换工作目录为当前文件所在目录
os.chdir(current_dir)


# 创建自定义的日志器
logger = logging.getLogger('my_logger')

# 设置日志级别
logger.setLevel(logging.DEBUG)

# 创建控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 创建文件处理器
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# 创建日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 添加处理器
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 生成日志
logger.info('This is an info message')
logger.debug('This is a debug message')
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")


""" 运行结果：
"""
