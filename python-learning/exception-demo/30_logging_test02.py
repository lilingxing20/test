import logging
import os


# 获取当前文件路径
current_dir = os.path.dirname(os.path.abspath(__file__))
# 切换工作目录为当前文件所在目录
os.chdir(current_dir)


# 将日志记录到文件中
logging.basicConfig(filename='app.log', 
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

# 查看当前目录中的.log日志文件
print([f for f in os.listdir(current_dir) if f.endswith('.log')])


""" 运行结果：
['app.log']
"""
