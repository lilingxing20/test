"""
PIL Python Imaging Library  曾是 Python 图像处理的领军工具，但由于其维护停滞不前于是 Pillow 诞生了。
Pillow 是一个 Python 图像处理库，提供了广泛的图像操作功能，如打开、编辑、保存、转换和处理图像。它是 Python Imaging Library（PIL）的一个分支，并提供对常见图像格式的支持，如 JPEG、PNG、GIF 等。
Pillow 可用于图像裁剪、缩放、旋转、颜色调整、滤镜应用等任务。
使用方法：
  1. 安装 Pillow：可以使用 pip 安装 Pillow 库，命令为 `pip install pillow`。
  2. 导入 Pillow 模块：在 Python 脚本中导入 Pillow 模块，通常使用 `from PIL import Image`。
  3. 打开图像：使用 `Image.open()` 方法打开图像文件，将图像加载到内存中。
  4. 图像操作：使用 Pillow 提供的方法对图像进行操作，如裁剪、缩放、旋转、颜色调整等。
  5. 保存图像：使用 `Image.save()` 方法将处理后的图像保存到文件中。
"""

import os
from PIL import Image


current_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(current_dir, 'image.png')
image = Image.open(filename)

# 显示图像
image.show()

# 图像信息
print(f"format: {image.format}")  # 图像格式
print(f"size: {image.size}")      # 图像尺寸（宽度, 高度）
print(f"mode: {image.mode}")      # 图像模式（如 RGB、L 等）

# 图像操作
# 例如，将图像转换为灰度图像
gray_image = image.convert('L')
gray_image.show()

# 保存图像
gray_image.save(os.path.join(current_dir, "gray_image.jpg"))
