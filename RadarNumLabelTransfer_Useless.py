"""
这份代码用于处理华农开源的雷达数字检测数据集
不适用于其他兵种
"""

import os
# 华农数据集类别：
# 0 1 2 3 4 5
# 蓝英雄 2 3 4 5 哨兵
# 红英雄 7 8 9 10 哨兵
def process_file(file_path):
    print(f"Processing file: {file_path}")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) > 0:
            print(f"Original line: {parts}")  # 显示原始行内容
            
            if int(parts[0]) >= 6:
                parts[0] = str(int(parts[0])-6)
            new_line = ' '.join(parts)  # 删除最后一列
            modified_lines.append(new_line)
            print(f"Modified line: {new_line}")  # 显示修改后的行内容

    with open(file_path, 'w') as file:
        for line in modified_lines:
            file.write(line + '\n')

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                process_file(file_path)

# Replace 'your_directory_path' with the path to the directory containing your .txt files
directory_path = r'C:\radar\radar_armor_dataset\nong_armor_dataset_v4\labels'
process_directory(directory_path)
