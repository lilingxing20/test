"""
Tkinter 是 Python 标准库中的一个模块，用于创建图形用户界面 (GUI)。它是 Python 的默认 GUI 库，提供了许多控件（如按钮、标签、文本框等），可以用来开发桌面应用程序。Tkinter 基于 Tcl/Tk，是一个轻量级的 GUI 工具包，易于使用且兼容多个平台（Windows、Linux、macOS）。
"""

import tkinter as tk

# 创建 Tk 对象 root 作为根窗口，并设置了窗口的标题和大小。
root = tk.Tk()
root.title("用户信息表单")
root.geometry("300x300")

# Label 创建标签。
# Entry 创建输入框，供用户输入信息。
name_label = tk.Label(root, text="姓名:")
name_label.pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

gender_label = tk.Label(root, text="性别:")
gender_label.pack(pady=5)

# Radiobutton 控件来创建单选按钮
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(root, text="男", variable=gender_var, value="男")
male_radio.pack(pady=5)
female_radio = tk.Radiobutton(root, text="女", variable=gender_var, value="女")
female_radio.pack(pady=5)

# 提交按钮
submit_button = tk.Button(root, text="提交")
submit_button.pack(pady=20)

# 启动主事件循环
root.mainloop()
