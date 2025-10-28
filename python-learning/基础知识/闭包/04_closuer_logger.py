""" 闭包的核心使用场景:
4. 延迟执行与回调
闭包可以捕获外部函数的变量，并在内部函数中延迟执行逻辑，适合需要"延迟计算"的场景。
示例：日志记录器
"""

def create_logger(prefix):
    def logger(message):
        print(f"[{prefix}] {message}")
    return logger


if __name__ == "__main__":
    log_error = create_logger("ERROR")
    log_warning = create_logger("WARNING")

    log_error("系统崩溃!")  # 输出: [ERROR] 系统崩溃!
    log_warning("内存不足!")  # 输出: [WARNING] 内存不足!


""" 运行结果：
[ERROR] 系统崩溃!
[WARNING] 内存不足!
"""
