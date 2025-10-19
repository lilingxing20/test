"""
psutil 是一个跨平台库，用于获取系统信息，如 CPU、内存、磁盘、网络等。
  1. 安装 psutil 库
     pip install psutil
  2. 导入 psutil 库
     import psutil
  3. 获取系统信息
     cpu_info = psutil.cpu_percent(interval=1)
     print(f"CPU 使用率: {cpu_info}%")
     mem_info = psutil.virtual_memory()
     print(f"内存使用率: {mem_info.percent}%")
     disk_info = psutil.disk_usage('/')
     print(f"磁盘使用率: {disk_info.percent}%")
     net_info = psutil.net_io_counters()
     print(f"网络流量: 接收 {net_info.bytes_recv} 字节, 发送 {net_info.bytes_sent} 字节")
     # 其他系统信息获取方法类似，如 psutil.disk_partitions() 获取磁盘分区信息
     disk_partitions = psutil.disk_partitions()
     for partition in disk_partitions:
        print(partition)
        # 其他属性如 device, fstype, opts 等也可以打印
        print(f"  设备: {partition.device}")
        print(f"  文件系统类型: {partition.fstype}")
        print(f"  挂载选项: {partition.opts}")
        print(f"  挂载点: {partition.mountpoint}")
    
  4. 其他系统信息获取方法
     psutil 还提供了许多其他方法来获取系统信息，如 psutil.users() 获取当前登录用户信息、psutil.sensors_temperatures() 获取传感器温度等。
     可以根据需要调用这些方法来获取系统的详细信息。
"""

import psutil


# 1. 获取 cpu 信息
# cpu 物理核数
r0 = psutil.cpu_count(logical=False)
print(f"物理核数: {r0}")
# cpu 逻辑核数
r1 = psutil.cpu_count()
print(f"逻辑核数: {r1}")

# 获取每个 CPU 核心的使用率
usage = psutil.cpu_percent(interval=1)
print(f"总体 CPU 使用率: {usage}%")
percpu_usage = psutil.cpu_percent(percpu=True, interval=1)
print(f"每个 CPU 核心的使用率: {percpu_usage}")

# cpu空闲时间
r0 = psutil.cpu_times()
print(f"用户时间: {r0.user}")
print(f"系统时间: {r0.system}")
print(f"空闲时间: {r0.idle}")

# 2. 获取内存信息
# 获取系统的虚拟内存
memory = psutil.virtual_memory()
print(f"总内存: {memory.total}")
print(f"已用内存: {memory.used}")
print(f"空闲内存: {memory.free}")
print(f"内存使用百分比: {memory.percent}%")
# 获取交换内存
swap = psutil.swap_memory()
print(f"交换总内存: {swap.total}")
print(f"交换已用内存: {swap.used}")
print(f"交换空闲内存: {swap.free}")
print(f"交换内存使用百分比: {swap.percent}%")

# 3. 获取磁盘信息
# 3.1 获取磁盘分区
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"设备: {partition.device}, 挂载点: {partition.mountpoint}, 文件系统类型: {partition.fstype}")

# 3.2 获取磁盘使用情况
disk_usage = psutil.disk_usage('/')
print(f"磁盘总空间: {disk_usage.total}")
print(f"磁盘已用: {disk_usage.used}")
print(f"磁盘使用百分比: {disk_usage.percent}%")


# 4. 获取网络信息
# 4.1 获取网络接口状态
net_io = psutil.net_io_counters()
print(f"发送字节数: {net_io.bytes_sent}")
print(f"接收字节数: {net_io.bytes_recv}")

# 4.2 获取每个网络接口的统计
net_if_addrs = psutil.net_if_addrs()
for interface, addrs in net_if_addrs.items():
    print(f"接口 {interface}:")
    for addr in addrs:
        print(f"  {addr.family}, {addr.address}")

# 5. 获取进程信息
# 5.1 获取所有进程的 PID 和名称
for proc in psutil.process_iter(['pid', 'name']):
    print(f"进程 {proc.info['pid']} 名称: {proc.info['name']}")

# 5.2 获取指定进程的内存和CPU使用情况
pid = 1234  # 替换为实际进程 ID
try:
    proc = psutil.Process(pid)
    print(f"进程 {pid} CPU 使用率: {proc.cpu_percent(interval=1)}%")
    print(f"进程 {pid} 内存使用: {proc.memory_info().rss} bytes")
except psutil.NoSuchProcess:
    print(f"进程 {pid} 不存在")

# 6. 获取系统信息
# 6.1 获取系统启动时间
boot_time = psutil.boot_time()
print(f"系统启动时间: {boot_time}")

# 6.2 获取当前的系统时间
import datetime
print(f"当前时间: {datetime.datetime.now()}")

# 6.3 获取系统负载（1、5、15分钟的平均负载）
load = psutil.getloadavg()
print(f"1分钟平均负载: {load[0]}")
print(f"5分钟平均负载: {load[1]}")
print(f"15分钟平均负载: {load[2]}")

# 6.4 获取系统的用户登录信息
users = psutil.users()
for user in users:
    print(f"用户 {user.name} 登录时间: {user.started}")
