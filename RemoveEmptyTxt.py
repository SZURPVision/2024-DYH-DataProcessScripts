# -*- coding: utf-8 -*-
import json
import cv2
from glob import glob
import os
#用于去除没有对应图片的txt文件

txt_path = input("请输入文件夹路径：")
img_path = txt_path

files = glob(txt_path + "*.txt")  # 找出所有的txt文件
# files = os.listdir(txt_path)
# print(files)
files = [i.split('/')[-1].split('.txt')[0] for i in files]
print(files)

for file in files:
    print(file)
    txt_file = txt_path + file + '.txt'
    img_file = img_path + file + '.jpg'
    img = cv2.imread(img_file)
    if img is None:
        os.remove(txt_file)
        continue
