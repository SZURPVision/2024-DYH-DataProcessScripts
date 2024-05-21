"""
这份脚本用来查看四点框并检查数据集是否有脏数据,按下d键可以将脏数据移动到某个文件夹
适用于四点装甲板识别
"""
import os
import shutil

import cv2
from tqdm import tqdm
import numpy as np
# 路径配置
# image_dir = r"C:\radar\NumberArmorNo0\valid\images"
# label_dir = r"C:\radar\NumberArmorNo0\valid\labels"
image_dir = r'C:\fourpoints\CK\9'
label_dir = r'C:\fourpoints\CK\9'

# 获取所有图像文件
image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]

def draw_yolo_boxes(image, label_path):
    if os.path.exists(label_path):
        with open(label_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                if not line.strip():
                    continue
                parts = line.strip().split()
                class_id = int(parts[0])
                points = [(float(x)) for x in parts[1:]]
                points[0::2] = [x * image.shape[1] for x in points[0::2]]
                points[1::2] = [x * image.shape[0] for x in points[1::2]]
                print(points)
                points: np.ndarray[os.Any, np.dtype[np.floating[np._32Bit]]] = np.array(points, np.int32).reshape((-1, 1, 2))
                cv2.polylines(image, [points], True, (0, 255, 0), 2)
                cv2.putText(
                    image,
                    str(class_id),
                    tuple(points[0][0]),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 0),
                    2,
                )
    return image


start_from = 0  # Change this to the file number you want to start from
image_files = image_files[start_from:]
# 目标路径 
destination_dir = r"C:\radar\test\BadData"

if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
    
i = 0
print(f"Total images: {len(image_files)}")
while i < len(image_files):
    image_file = image_files[i]
    print(f"Processing image: {image_file}")
    image_path = os.path.join(image_dir, image_file)
    label_path = os.path.join(label_dir, os.path.splitext(image_file)[0] + ".txt")

    image = cv2.imread(image_path)
    image_with_boxes = draw_yolo_boxes(image, label_path)
    image_with_boxes = cv2.resize(image_with_boxes, (800, 600))

    # cv2.putText(
    #     image_with_boxes,
    #     f"Image number: {i+1+start_from}",
    #     (10, 30),
    #     cv2.FONT_HERSHEY_SIMPLEX,
    #     1,
    #     (255, 255, 255),
    #     2,
    # )

    cv2.imshow("Image", image_with_boxes)

    key = cv2.waitKey(0)
    if key == ord("d"):  # Press 'd' to move the file
        shutil.move(image_path, destination_dir)
        if os.path.exists(label_path):
            shutil.move(label_path, destination_dir)
        print(f"Moved {image_path} and {label_path} to {destination_dir}")
        image_files.pop(i)
    elif key == ord("q"):  # Press 'q' to go to the previous image
        i = max(0, i - 1)
    elif key == ord("e"):  # Press 'e' to go to the next image
        i += 1
    else:
        break

    cv2.destroyAllWindows()
