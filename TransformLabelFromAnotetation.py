"""
这份脚本用来去掉LabelRobomaster标签最后一行大小装甲板和绿灯类(36)
适用于步兵装甲板数据集微处理
"""
import os

def process_file(file_path):
    print(f"Processing file: {file_path}")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) > 0:
            print(f"Original line: {parts}")  # 显示原始行内容
            temp_num = int(parts[0])
            # temp_num %= 9
            if temp_num == 36:
                continue  # 如果类别为36，跳过这行，即删除这行
            new_line = ' '.join(parts[:-1])  # 删除最后一列
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
directory_path = r'C:\radar\装甲板数据集\Label-check-adapt-fourpoint'
process_directory(directory_path)
