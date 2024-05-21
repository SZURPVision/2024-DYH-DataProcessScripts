"""
这份脚本用来将很暗的数据集通过1*1卷积进行随机亮度增强
适用于雷达装甲板识别,不适合步兵
"""
import cv2
import numpy as np
import os
import random
import shutil
from concurrent.futures import ThreadPoolExecutor
def apply_convolution(image_path, output_path):
    # Load the image
    num = random.randint(2, 6)
    img = cv2.imread(image_path)
    if img is None:
        print(f"Failed to load image {image_path}")
        return

    # Define a 1x1 kernel with a value of 5

    kernel = np.array([[num]])

    # Apply the kernel to the image
    convolved_img = cv2.filter2D(img, -1, kernel)

    # Save the convolved image
    cv2.imwrite(output_path, convolved_img)
    print(f"Image processed and saved: {output_path}")

def copy_label_file(label_path, output_label_path):
    if os.path.exists(label_path):
        shutil.copy2(label_path, output_label_path)
        print(f"Label file copied and saved: {output_label_path}")
    else:
        print(f"No label file found for {label_path}")

def process_directory(directory):
    with ThreadPoolExecutor(max_workers=4) as executor:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    # Original image path
                    file_path = os.path.join(root, file)
                    
                    # Generate new output path for the enhanced image
                    filename_base, file_extension = os.path.splitext(file)
                    output_file_name = f"{filename_base}_enhanced{file_extension}"
                    output_path = os.path.join(root, output_file_name)
                    
                    # Process and save the enhanced image
                    executor.submit(apply_convolution,file_path, output_path)
                    
                    # Copy the corresponding label file, if exists
                    label_path = os.path.splitext(file_path)[0] + '.txt'
                    output_label_name = f"{filename_base}_enhanced.txt"
                    output_label_path = os.path.join(root, output_label_name)
                    executor.submit(copy_label_file,label_path, output_label_path)

# Replace 'your_directory_path' with the path to the directory containing your image files
directory_path = r'C:\radar\armor_dataset\Label-check-adapt-fourpoint'
process_directory(directory_path)
