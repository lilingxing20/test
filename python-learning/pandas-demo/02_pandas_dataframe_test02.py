""" spandas 系列（DataFrame）

DataFrame是pandas中最重要的数据结构，它可以理解为一个二维表格，每一行代表一个数据记录，每一列代表一个变量。

DataFrame的主要特点包括：
- 每列可以是不同的数据类型（如整数、浮点数、字符串等）
- 每列可以有一个名称（列索引）
- 每行可以有一个名称（行索引）
- 可以对行和列进行操作（如选择、过滤、排序等）
- 可以进行统计分析（如计算均值、标准差、相关系数等）
- 可以进行数据可视化（如绘制折线图、柱状图、散点图等）

本文将介绍pandas中DataFrame的创建、基本属性、访问、条件筛选、修改、删除等操作。

"""

import pandas as pd


data = {
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [20, 21, 19, 22],
    '成绩': [90, 85, 92, 88],
    '城市': ['北京', '上海', '广州', '深圳']
}
df = pd.DataFrame(data)

print("="*50)
print("2. DataFrame的核心属性")
print("="*50)

print("DataFrame基本信息：")
print(f"形状：{df.shape}")           # (行数, 列数)
print(f"列名：{df.columns}")         # 列索引
print(f"索引：{df.index}")           # 行索引
print(f"数据类型：\n{df.dtypes}")    # 每列的数据类型
print(f"基本信息：")
print(df.info())
print(f"统计描述：\n{df.describe()}") # 数值列的统计描述
print()


""" 运行结果：
==================================================
2. DataFrame的核心属性
==================================================
DataFrame基本信息：
形状：(4, 4)
列名：Index(['姓名', '年龄', '成绩', '城市'], dtype='object')
索引：RangeIndex(start=0, stop=4, step=1)
数据类型：
姓名    object
年龄     int64
成绩     int64
城市    object
dtype: object
基本信息：
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   姓名      4 non-null      object
 1   年龄      4 non-null      int64 
 2   成绩      4 non-null      int64 
 3   城市      4 non-null      object
dtypes: int64(2), object(2)
memory usage: 260.0+ bytes
None
统计描述：
              年龄         成绩
count   4.000000   4.000000
mean   20.500000  88.750000
std     1.290994   2.986079
min    19.000000  85.000000
25%    19.750000  87.250000
50%    20.500000  89.000000
75%    21.250000  90.500000
max    22.000000  92.000000

"""
