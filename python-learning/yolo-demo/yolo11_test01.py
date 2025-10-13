"""
此脚本用于加载预训练的 YOLO 模型，对本地图片、网络图片以及视频进行目标检测
    1.运行前需要安装第三方库 ultralytics，可使用以下命令进行安装：
        pip install ultralytics
    2.若安装过程中出现超时问题，可使用国内镜像源进行安装，命令如下：
        pip install -i https://mirrors.aliyun.com/pypi/simple/ ultralytics
"""

import os

from ultralytics import YOLO


def perform_object_detection(
    url='https://ultralytics.com/images/bus.jpg',
    save_dir='assets'):
    """
    执行目标检测任务
        1. 参数:
            url (str): 要进行检测的(图片、视频)的路径或在线URL，默认为 'https://ultralytics.com/images/bus.jpg'
            save_dir (str): 保存检测结果的文件夹路径，默认为 './assets'
    """
    # 0. 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_save_dir = os.path.join(current_dir, save_dir)
    print(absolute_save_dir)
    # 创建保存结果的文件夹（如果不存在）
    os.makedirs(absolute_save_dir, exist_ok=True)
    # 改变当前工作目录
    os.chdir(absolute_save_dir)

    # 1. 加载预训练模型，如果没有文件，首次运行自动下载
    model = YOLO(os.path.join(current_dir, "models/yolo11n.pt"))
    # 参数详解
    #     show=True 显示检测结果图片
    #     save=True 保存检测结果图片，会创建指定的文件夹
    #     project=save_dir 指定保存结果的文件夹路径
    model(url, show=True, save=True, project=absolute_save_dir)


def main():
    print('python yolo study...')

    # 预训练的 YOLO 模型，对本地图片、网络图片以及视频进行目标检测
    perform_object_detection()
    perform_object_detection(
        url='https://imgcdn.cna.com.tw/Eng/WebEngPhotos/800/2025/20250527/1024x698_763747498679.jpg',
        save_dir='assets_cna',
    )


if __name__ == '__main__':
    main()
