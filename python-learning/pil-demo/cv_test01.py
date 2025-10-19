"""
opencv 是一个开源的计算机视觉库，支持多种图片处理操作，如图像读取、显示、转换、滤波等。
  1. 安装
    pip install opencv-python
  2. 读取图片
    img = cv2.imread(img_path)
    # 显示图像
    cv2.imshow("image", img)
    cv2.waitKey(0)
    # 关闭窗口
    cv2.destroyAllWindows()
"""

import os
import cv2

print("version:", cv2.__version__)

# 读png文件
current_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(current_dir, "image.png")
img = cv2.imread(img_path)
 
# 显示图像信息
# print("image info:", img)

# 获取图像高宽像素
sp = img.shape
height = sp[0]   # height(rows) of image
width = sp[1]    # width(colums) of image
chanael = sp[2]  # the pixels value is made up of three primary colors
print ( 'width: %d \nheight: %d \nnumber: %d' % (width, height, chanael))

# 显示图像
cv2.imshow("image", img)
cv2.waitKey(0)

# 关闭窗口
cv2.destroyAllWindows()

# 转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 显示灰度图像
cv2.imshow("gray", gray)
cv2.waitKey(0)
# 保存灰度图像
cv2.imwrite(os.path.join(current_dir, "gray_image.png"), gray)
# 关闭窗口
cv2.destroyAllWindows()
