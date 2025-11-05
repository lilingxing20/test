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


print("="*50)
print("7. 实际应用示例")
print("="*50)

# 创建学生数据
students_df = pd.DataFrame({
    '数学': [85, 92, 78, 90],
    '英语': [88, 79, 95, 87],
    '物理': [92, 85, 88, 94]
}, index=['张三', '李四', '王五', '赵六'])

print("学生成绩表：")
print(students_df)
print()

# 从DataFrame中提取Series
math_scores = students_df['数学']
print("数学成绩Series：")
print(math_scores)
print(f"类型：{type(math_scores)}")

# 对Series进行操作
print(f"\n数学平均分：{math_scores.mean()}")
print(f"数学最高分：{math_scores.max()}")

# 将Series操作结果添加回DataFrame
students_df['总分'] = students_df['数学'] + students_df['英语'] + students_df['物理']
students_df['平均分'] = students_df['总分'] / 3

print("\n添加总分和平均分后：")
print(students_df)


""" 运行结果：
==================================================
7. 实际应用示例
==================================================
学生成绩表：
    数学  英语  物理
张三  85  88  92
李四  92  79  85
王五  78  95  88
赵六  90  87  94

数学成绩Series：
张三    85
李四    92
王五    78
赵六    90
Name: 数学, dtype: int64
类型：<class 'pandas.core.series.Series'>

数学平均分：86.25
数学最高分：92

添加总分和平均分后：
    数学  英语  物理   总分        平均分
张三  85  88  92  265  88.333333
李四  92  79  85  256  85.333333
王五  78  95  88  261  87.000000
赵六  90  87  94  271  90.333333
"""
