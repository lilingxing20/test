import tkinter as tk
import random


# 创建窗口
window = tk.Tk()
window.title('祝福')

# 设置窗口大小
window_width = 300
window_height = 100

# 获取屏幕宽度和高度
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# 计算窗口在屏幕中心的坐标
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# 设置窗口大小和位置
window.geometry(f'{window_width}x{window_height}+{x}+{y}')

# 设置窗口置顶
window.attributes('-topmost', True)

# 定义随机背景色列表
background_colors = [
    'lightpink', 'skyblue', 'lightgreen', 'lavender',
    'lightyellow', 'plum', 'coral', 'bisque', 'aquamarine',
    'mistyrose', 'honeydew', 'lavenderblush', 'oldlace',
    'mintcream', 'aliceblue', 'antiquewhite', 'azure', 'beige'
]

# 创建标签，设置文字居中显示
label = tk.Label(
    window, 
    text='', 
    font=('Arial', 18),
    width=window_width//10,  # 设置合适的宽度
    height=window_height//25,  # 设置合适的高度
    anchor='center',  # 文字居中
    justify='center'
)
label.pack(expand=True)  # 使用expand参数确保标签在窗口中居中
 
# 祝福语列表
blessings = ['亲爱的朋友', '新婚快乐', '愿你们幸福美满', '爱情长存']

# 使用索引跟踪当前显示的祝福语
def show_blessing(index=0):
    if index < len(blessings):
        blessing = blessings[index]
        print(blessing)
        
        # 每次切换祝福语时随机选择新的背景色
        random_bg = random.choice(background_colors)
        
        # 更新窗口背景色
        window.configure(bg=random_bg)
        
        # 更新标签文本和背景色
        label.config(text=blessing, bg=random_bg)
        
        # 1秒后显示下一条祝福语
        window.after(1000, show_blessing, index + 1)
    else:
        print('祝福语播报完毕，谢谢观赏！')
        # 所有祝福语显示完毕后，2秒自动关闭窗口
        window.after(2000, window.destroy)

# 开始显示第一条祝福语
show_blessing()

# 启动Tkinter事件循环
window.mainloop()
