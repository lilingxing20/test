"""
一个基于Tkinter的随机温馨提醒窗口系统，功能是创建 300 个随机位置、随机背景色、窗口，并在 10 秒后自动关闭，这些窗口可以看到很多温柔的提示语，给对方很温馨的感觉。
"""

import random  # 导入random库，用于生成随机内容
import tkinter as tk  # 导入Tkinter库，用于创建GUI窗口


def create_window(root):
    """
    创建子窗口，生成一个独立的提示窗口，包含窗口位置、内容、样式等设置
    """
    # 1. 创建子窗口（使用Toplevel而非Tk，避免多主窗口冲突）
    window = tk.Toplevel(root)  # root是后续定义的主窗口，作为父容器
 
    # 2. 获取屏幕宽高，用于计算窗口位置
    screen_width = root.winfo_screenwidth()  # 获取屏幕宽度（像素）
    screen_height = root.winfo_screenheight()  # 获取屏幕高度（像素）
 
    # 3. 随机生成窗口位置（确保窗口完全显示在屏幕内）
    window_width = 250  # 窗口宽度
    window_height = 60  # 窗口高度
    # x坐标范围：0 ~ 屏幕宽度-窗口宽度（避免窗口右侧超出屏幕）
    x = random.randrange(0, screen_width - window_width)
    # y坐标范围：0 ~ 屏幕高度-窗口高度（避免窗口底部超出屏幕）
    y = random.randrange(0, screen_height - window_height)
 
    # 4. 设置窗口标题和大小位置
    window.title('温馨提示')  # 窗口标题
    # 格式："宽x高+X坐标+Y坐标"，用于固定窗口大小和位置
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
 
    # 5. 随机选择提示语
    tips = [
        '多喝水哦~', '保持微笑呀', '每天都要元气满满',
        '记得吃水果', '保持好心情', '好好爱自己', '你很棒的',
        '梦想成真', '期待下一次见面', '你好幽默',
        '顺顺利利', '早点休息', '愿所有烦恼都消失',
        '别熬夜', '今天过得开心嘛', '天冷了，多穿衣服'
    ]
    tip = random.choice(tips)  # 从列表中随机选一条提示语
 
    # 6. 随机选择背景颜色
    bg_colors = [
        'lightpink', 'skyblue', 'lightgreen', 'lavender',
        'lightyellow', 'plum', 'coral', 'bisque', 'aquamarine',
        'mistyrose', 'honeydew', 'lavenderblush', 'oldlace'
    ]
    bg = random.choice(bg_colors)  # 从列表中随机选一种背景色
 
    # 7. 创建标签组件，显示提示语
    tk.Label(
        window,  # 父容器为当前窗口
        text=tip,  # 显示的文字（随机选中的提示语）
        bg=bg,  # 背景色（随机选中的颜色）
        font=('微软雅黑', 16),  # 字体和字号
        width=30,  # 标签宽度
        height=3  # 标签高度
    ).pack()  # 将标签添加到窗口中
 
    # 8. 设置窗口置顶（确保不被其他窗口遮挡）
    window.attributes('-topmost', True)
 
    # 9. 10秒后自动关闭当前窗口（10000毫秒 = 10秒）
    window.after(10000, window.destroy)  # after(延迟时间, 执行函数)：延迟后销毁窗口
 
    return window  # 返回创建的窗口对象


def create_multiple_windows(root, count=300, delay=0.01):
    """
    通过递归调用实现批量创建窗口，避免使用多线程导致的 GUI 冲突
    """
    # 递归终止条件：当窗口数量为0时，触发程序收尾
    if count <= 0:
        # 所有窗口创建完成后，10秒后关闭主程序（确保所有子窗口先关闭）
        root.after(10000, root.destroy)
        return  # 结束递归
    
    # 1. 调用create_window()创建一个窗口
    create_window(root)
    
    # 2. 延迟一段时间后，递归创建下一个窗口（非阻塞方式）
    # after(延迟毫秒数, 函数, 参数1, 参数2, ...)：延迟后执行函数
    root.after(
        int(delay * 1000),  # 延迟时间（转换为毫秒，0.01秒 = 10毫秒）
        create_multiple_windows,  # 递归调用自身
        root,  # 必须传递root参数
        count - 1,  # 窗口数量减1
        delay  # 保持延迟时间不变
    )


def main():
    """
    主程序入口，负责创建主窗口、隐藏主窗口、批量创建子窗口、启动事件循环
    """
    # 1. 创建主窗口（作为所有子窗口的父容器）
    root = tk.Tk()
    # 2. 隐藏主窗口（主窗口仅用于调度，不需要显示）
    root.withdraw()
 
    # 3. 开始批量创建窗口：300个窗口，间隔0.01秒
    create_multiple_windows(root, 200, 0.01)
 
    # 4. 启动Tkinter事件循环（保持程序运行，等待用户交互或定时事件）
    root.mainloop()


if __name__ == '__main__':
    main()  # 启动主程序
