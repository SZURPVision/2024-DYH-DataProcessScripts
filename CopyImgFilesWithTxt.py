import os
import shutil


def move_files_with_same_name_as_txt(source_dir, dest_dir):
    """
    遍历指定文件夹下的所有txt文件，并将同名jpg文件和这些txt文件移动到另一个文件夹中。

    :param source_dir: 要遍历的源文件夹
    :param dest_dir: 文件移动到的目标文件夹
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.txt'):
                txt_file_path = os.path.join(root, file)
                jpg_file_name = os.path.splitext(file)[0] + '.jpg'
                jpg_file_path = os.path.join(root, jpg_file_name)

                if os.path.exists(jpg_file_path):
                    shutil.move(txt_file_path, dest_dir)
                    shutil.move(jpg_file_path, dest_dir)
                    print(f"Moved: {txt_file_path} and {jpg_file_path} to {dest_dir}")


if __name__ == "__main__":
    source_directory = input("请输入要遍历的源文件夹路径：")
    destination_directory = input("请输入目标文件夹路径：")
    move_files_with_same_name_as_txt(source_directory, destination_directory)
