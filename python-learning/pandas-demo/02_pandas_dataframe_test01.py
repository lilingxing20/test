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
print("1. 创建DataFrame的多种方式")
print("="*50)

# 方式1：从字典创建（最常用）
data = {
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [20, 21, 19, 22],
    '成绩': [90, 85, 92, 88],
    '城市': ['北京', '上海', '广州', '深圳']
}

df = pd.DataFrame(data)
print("从字典创建的DataFrame：")
print(df)
print()

# 方式2：从列表的列表创建
data_list = [
    ['张三', 20, 90, '北京'],
    ['李四', 21, 85, '上海'],
    ['王五', 19, 92, '广州'],
    ['赵六', 22, 88, '深圳']
]

df_list = pd.DataFrame(data_list, 
                      columns=['姓名', '年龄', '成绩', '城市'])
print("从列表创建的DataFrame：")
print(df_list)
print()

# 方式3：从Series创建
name_series = pd.Series(['张三', '李四', '王五', '赵六'])
age_series = pd.Series([20, 21, 19, 22])
score_series = pd.Series([90, 85, 92, 88])

df_series = pd.DataFrame({
    '姓名': name_series,
    '年龄': age_series,
    '成绩': score_series
})
print("从Series创建的DataFrame：")
print(df_series)
print()


""" 运行结果：
==================================================
1. 创建DataFrame的多种方式
==================================================
从字典创建的DataFrame：
   姓名  年龄  成绩  城市
0  张三  20  90  北京
1  李四  21  85  上海
2  王五  19  92  广州
3  赵六  22  88  深圳

从列表创建的DataFrame：
   姓名  年龄  成绩  城市
0  张三  20  90  北京
1  李四  21  85  上海
2  王五  19  92  广州
3  赵六  22  88  深圳

从Series创建的DataFrame：
   姓名  年龄  成绩
0  张三  20  90
1  李四  21  85
2  王五  19  92
3  赵六  22  88

"""
