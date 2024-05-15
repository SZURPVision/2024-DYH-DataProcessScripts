import os
import shutil

import cv2
from tqdm import tqdm

# 路径配置
image_dir = r"C:\radar\NumberArmorNo0\train\images"
label_dir = r"C:\radar\NumberArmorNo0\train\labels"
# image_dir = r'C:\radar\NumberArmorNo0\test\img'
# label_dir = r'C:\radar\NumberArmorNo0\test\label'

# 获取所有图像文件
image_files = [
    f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))
]


def draw_yolo_boxes(image, label_path):
    h, w, _ = image.shape
    if os.path.exists(label_path):
        with open(label_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split()
                class_id, x_center, y_center, width, height = map(float, parts)
                x_center, y_center = x_center * w, y_center * h
                width, height = width * w, height * h
                x1, y1 = int(x_center - width / 2), int(y_center - height / 2)
                x2, y2 = int(x_center + width / 2), int(y_center + height / 2)
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(
                    image,
                    str(int(class_id) + 1),
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 0),
                    2,
                )
    return image


start_from = 1208  # Change this to the file number you want to start from
image_files = image_files[start_from:]
destination_dir = r"C:\radar\NumberArmorNo0\BadData"

if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
    
i = 0
while i < len(image_files):
    image_file = image_files[i]
    image_path = os.path.join(image_dir, image_file)
    label_path = os.path.join(label_dir, os.path.splitext(image_file)[0] + ".txt")

    image = cv2.imread(image_path)
    image_with_boxes = draw_yolo_boxes(image, label_path)
    image_with_boxes = cv2.resize(image_with_boxes, (800, 600))

    cv2.putText(
        image_with_boxes,
        f"Image number: {i+1+start_from}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2,
    )

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
