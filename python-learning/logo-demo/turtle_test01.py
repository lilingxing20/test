"""
turtle 是 Python 标准库中的一个模块，用于创建海龟绘图。它提供了一个简单的接口，使你能够在屏幕上绘制图形。
在1966年，Seymour Papert和Wally Feurzig发明了LOGO语言，旨在帮助儿童学习编程。LOGO通过编程控制一个小海龟在屏幕上绘图。后来的Python内置了turtle库，完全继承了这种海龟绘图的功能。

1. 模块功能：
  - Screen命令：
    bgcolor(): 设置背景颜色
    title(): 设置窗口标题
    setup(): 设置窗口大小和位置
    tracer(): 设置绘图更新速度

  - Turtle命令：
    forward() / fd(): 向前移动指定步数
    backward() / bk(): 向后移动指定步数
    right() / rt(): 向右旋转指定角度
    left() / lt(): 向左旋转指定角度
    penup() / pu(): 提起画笔
    pendown() / pd(): 放下画笔
    speed(): 设置绘图速度
    goto(): 移动到指定位置
    setpos(): 设置当前位置
    setposition(): 设置当前位置
    setx(): 设置X坐标
    sety(): 设置Y坐标
    circle(): 绘制圆形
    dot(): 绘制圆点
    stamp(): 留下印记

  - 颜色命令：
    color(): 设置画笔颜色
    begin_fill(): 开始填充
    end_fill(): 结束填充
    fillcolor(): 设置填充颜色

  - 状态控制命令：
    pen(): 激活画笔
    isdown(): 检查画笔是否在画布上
    isvisible(): 检查乌龟是否可见
    showturtle(): 显示乌龟
    hideturtle(): 隐藏乌龟
    reset(): 重置画布
    clear(): 清除绘制内容

  - 窗口操作命令：
    exitonclick(): 点击窗口退出
    onscreenclick(): 设置点击事件
    onkey(): 监听键盘事件
    listen(): 开始监听事件

  - 其他命令：
    write(): 写文本
    distance(): 计算当前位置到某点的距离
    towards(): 获取当前位置指向指定点的角度

2. 基础操作：
  1) 导入 turtle 模块
     import turtle
  2) 创建一个 Turtle 对象
     t = turtle.Turtle()
  3) 设置绘制速度
     t.speed(1)
  4) 绘制一个正方形
     for _ in range(4):
         t.forward(100)
         t.right(90)
  5) 关闭窗口
     t.done()
     # 或者使用 turtle.mainloop() 来启动主事件循环
     # turtle.mainloop()
     # 或者使用 turtle.done() 来关闭窗口
     # turtle.done()
     # 或者使用 turtle.bye() 来关闭窗口
     # turtle.bye()
"""

import turtle

# 设置背景颜色为黄色
turtle.bgcolor("white")

# 设置标题为 "海龟绘图"
turtle.title("海龟绘图")

# 设置窗口大小为 800x600
turtle.setup(800, 600)

# 创建一个 Turtle 对象
t = turtle.Turtle()

# 设置绘制速度为 1（最慢）
t.speed(2)

# 移动画笔
t.setpos(0, 0)

# 填充绿色五边形
t.begin_fill()
# 设置颜色为绿色
t.color("green")
# 绘制一个五边形
for _ in range(5):
    t.forward(100)
    t.right(72)
t.end_fill()

# 移动画笔
t.setpos(100, 100)
# 填充蓝色正方形
t.begin_fill()
# 设置颜色为蓝色
t.color("blue")
# 绘制一个正方形
for _ in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()


# 填充紫色五边形
t.begin_fill()
# 设置颜色为紫色
t.color("purple")
# 绘制一个五边形
for _ in range(5):
    t.forward(-100)
    t.right(72)
t.end_fill()


# 移动画笔
t.setpos(0, 100)
# 移动画笔
t.setpos(0, 0)
# 填充黄色园
t.begin_fill()
# 设置颜色为黄色
t.color("yellow")
# 绘制一个黄色正方形
for _ in range(4):
    t.forward(-100)
    t.right(90)
t.end_fill()

# 移动画笔
t.setpos(50, 50)
# 填充黄色园
t.begin_fill()
# 设置颜色为黄色
t.color("yellow")
# 绘制一个红色五角星
for _ in range(5):
    t.forward(50)
    t.right(144)
# 绘制一个红色五角星
for _ in range(5):
    t.forward(-50)
    t.right(144)
t.end_fill()

# # 窗口保持打开状态, 等待用户关闭窗口
# turtle.mainloop()

# 暂停, 等待用户关闭窗口
turtle.done()

# 关闭窗口
# turtle.bye()
