"""
datetime 日期时间工具，常用于获取当前时间、格式化时间、进行日期和时间计算、解析和格式化日期字符串等。
通过 timedelta，你可以轻松进行日期的加减操作，而 strftime 和 strptime 则帮助你处理不同格式的时间字符串。
  1. 获取当前时间
  2. 获取当前时间的时间戳
  3. 格式化时间
  4. 日期和时间计算
  5. 解析和格式化日期字符串
  6. 时间戳转换
  7. 时间差计算
  8. 时间格式化
  9. 时间比较
  10. 时间格式化
  11. 将时间转为时间戳
  12. timestamp转换为datetime
  13. datetime转为string
  14. string转为datetime
  15. datetime 加减操作
  16. 时区转换
"""

# datetime模块 => 包含一个datetime类
from datetime import datetime, timezone, timedelta
from traceback import print_tb


# 1. 获取当前时间
print("1. 获取当前时间")
print(datetime.now())
print(datetime.now().timestamp())
print(datetime.now().timestamp() * 1000)  # 毫秒级时间戳
print(int(datetime.now().timestamp() * 1000))  # 整数位表示毫秒
print(int(datetime.now().timestamp()))  # 整数位表示秒

# 2. 获取时间戳
print("2. 获取当前时间的时间戳")
print("时间戳 是以GMT/UTC时间1970-01-01T00:00:00为起点，到当前具体时间的秒数")
# 获取 UTC 时间
utc_now = datetime.now(timezone.utc)
utc_timestamp = utc_now.timestamp()
print(utc_now, utc_timestamp)
# 获取 CST 时间（中国标准时间，东八区）
cst_now = datetime.now(timezone(timedelta(hours=8)))
cst_timestamp = cst_now.timestamp()
print(cst_now, cst_timestamp)

# 3. 格式化时间
print("3. 格式化时间")
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.now().strftime("%Y-%m-%d"))
print(datetime.now().strftime("%Y-%m-%d %H:%M"))
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 微秒级时间戳
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])  # 毫秒级时间戳
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-6])  # 微秒级时间戳

# 4. 日期和时间计算
print("4. 日期和时间计算")
print(datetime.now() + timedelta(hours=1))
print(datetime.now() - timedelta(days=10, hours=1))

# 5. 解析和格式化日期字符串
print("5. 解析和格式化日期字符串")
print(datetime.strptime("2025-02-17 12:45:30", "%Y-%m-%d %H:%M:%S"))

# 6. 时间戳转换
print("6. 时间戳转换")
print(datetime.fromtimestamp(1708144330.0))  # 本地时间：操作系统设定的时区

# 7. 时间差计算
print("7. 时间差计算")
print(datetime.now() - datetime(2025, 10, 10, 11, 11, 11))

# 8. 时间格式化
print("8. 时间格式化")
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 微秒级时间戳
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])  # 毫秒级时间戳
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-6])  # 微秒级时间戳

# 9. 时间比较
print("9. 时间比较")
print(datetime.now() > datetime(2025, 10, 10, 11, 11, 11))

# 10. 时间格式化
print("10. 时间格式化")
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 微秒级时间戳
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])  # 毫秒级时间戳
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-6])  # 微秒级时间戳

# 11. 将时间转为时间戳
print("11. 将时间转为时间戳")
dt = datetime(2025, 10, 10, 11, 11, 11)
print(dt.timestamp())  # 整数位表示秒

# 12. timestamp转换为datetime
print("12. timestamp转换为datetime")
tp = dt.timestamp()
print(datetime.fromtimestamp(tp))  # 本地时间：操作系统设定的时区
print(datetime.fromtimestamp(tp, timezone.utc))  # UTC时间

# 13. datetime转为string《string format time》
print("13. datetime转为string《string format time》")
print(datetime.strftime(dt, "%Y年%m月%d %H:%M:%S"))
print(datetime.strftime(datetime.now(), '%a, %b %d %H:%M'))

# 14. string转为datetime《string parse time》
print("14. string转为datetime")
dt_obj = datetime.strptime("2025-02-17 12:45:30", "%Y-%m-%d %H:%M:%S")
print(type(dt_obj), dt_obj)

# 15. datetime加减
print("15. datetime加减")
"""
对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。
加减可以直接用+和-运算符，不过需要导入timedelta这个类
"""
now = datetime.now()
print(now + timedelta(hours=1))
print(now - timedelta(days=10, hours=1))

# 16. 时区转换
print("16. 时区转换")
# 获取当前时区
print("16.1 获取当前时区")
print(datetime.now().astimezone().tzinfo)
# 创建时区UTC+8:00
print("16.2 创建时区UTC+8:00")
tz_utc_8 = timezone(timedelta(hours=8))
print(datetime.now())
# 强行设置为UTC+8:00时区
print("16.3 强行设置为UTC+8:00时区")
print(now.replace(tzinfo=tz_utc_8))
# 强制设置时区为UTC+0:00
print("16.4 强制设置时区为UTC+0:00")
now = datetime.now().replace(tzinfo=timezone.utc)
print(now)
# 强制转为UTC+8:00
print("16.5 强制转为UTC+8:00") 
now = now.astimezone(tz_utc_8)
print(now)


""" 运行结果:
1. 获取当前时间
2025-10-19 21:06:39.860926
1760879199.860944
1760879199860.949
1760879199860
1760879199
2. 获取当前时间的时间戳
时间戳 是以GMT/UTC时间1970-01-01T00:00:00为起点，到当前具体时间的秒数
2025-10-19 13:06:39.860960+00:00 1760879199.86096
2025-10-19 21:06:39.861392+08:00 1760879199.861392
3. 格式化时间
2025-10-19 21:06:39
2025-10-19
2025-10-19 21:06
2025-10-19 21:06:39.861421
2025-10-19 21:06:39.861
2025-10-19 21:06:39.
4. 日期和时间计算
2025-10-19 22:06:39.861435
2025-10-09 20:06:39.861439
5. 解析和格式化日期字符串
2025-02-17 12:45:30
6. 时间戳转换
2024-02-17 12:32:10
7. 时间差计算
9 days, 9:55:28.863891
8. 时间格式化
2025-10-19 21:06:39.863895
2025-10-19 21:06:39.863
2025-10-19 21:06:39.
9. 时间比较
True
10. 时间格式化
2025-10-19 21:06:39.863914
2025-10-19 21:06:39.863
2025-10-19 21:06:39.
11. 将时间转为时间戳
1760065871.0
12. timestamp转换为datetime
2025-10-10 11:11:11
2025-10-10 03:11:11+00:00
13. datetime转为string《string format time》
2025年10月10 11:11:11
Sun, Oct 19 21:06
14. string转为datetime
<class 'datetime.datetime'> 2025-02-17 12:45:30
15. datetime加减
2025-10-19 22:06:39.863965
2025-10-09 20:06:39.863965
16. 时区转换
16.1 获取当前时区
CST
16.2 创建时区UTC+8:00
2025-10-19 21:06:39.863986
16.3 强行设置为UTC+8:00时区
2025-10-19 21:06:39.863965+08:00
16.4 强制设置时区为UTC+0:00
2025-10-19 21:06:39.863994+00:00
16.5 强制转为UTC+8:00
2025-10-20 05:06:39.863994+08:00
"""
