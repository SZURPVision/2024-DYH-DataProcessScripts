"""
这份脚本用来将装甲板数据集转换成雷达数字识别数据集:
雷达数字识别的类别是: 英雄 工程 三号步兵 四号步兵 五号步兵 哨兵
适用于将装甲板数据集转换成雷达数字识别数据集
"""
import os

def convert_to_yolo_format(cls, x1, y1, x2, y2, x3, y3, x4, y4):
    # 计算边界框的最小和最大x，y值
    all_x = [x1, x2, x3, x4]
    all_y = [y1, y2, y3, y4]
    x_min, x_max = min(all_x), max(all_x)
    y_min, y_max = min(all_y), max(all_y)

    # 计算中心点坐标和边界框的宽度、高度
    x_center = (x_min + x_max) / 2
    y_center = (y_min + y_max) / 2
    width = x_max - x_min
    height = y_max - y_min
    return x_center, y_center, width, height

def process_file(file_path):
    print(f"正在处理文件: {file_path}")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 9:
            cls, x1, y1, x2, y2, x3, y3, x4, y4 = map(float, parts)
            yolo_format = []
            x,y,w,h = convert_to_yolo_format(cls, x1, y1, x2, y2, x3, y3, x4, y4)
            before_cls = int(cls)
            before_cls = before_cls % 9
            if(before_cls >= 6):
                continue
            else:
                before_cls = before_cls - 1
                if before_cls == -1:
                    before_cls = 5
                cls = before_cls
                yolo_format = [cls, x, y, w, h]
                new_line = ' '.join(map(str, yolo_format))
                modified_lines.append(new_line)
                print(f"原始行: {parts}")
                print(f"修改后的行: {new_line}")

    with open(file_path, 'w') as file:
        for line in modified_lines:
            file.write(line + '\n')

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                process_file(file_path)

# 替换 'your_directory_path' 为包含您的 .txt 文件的目录路径
directory_path = r'C:\radar\Label-check-adapt-fourpoint'
process_directory(directory_path)
