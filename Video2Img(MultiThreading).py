import cv2
import os
import threading


def video2img(filename, video_path, img_path, fra):
    cnt = 0
    dnt = 0
    cap = cv2.VideoCapture(video_path + os.sep + str(filename))
    while True:
        ret, image = cap.read()
        if image is None:
            break
        if (cnt % fra) == 0:
            cv2.imencode('.jpg', image)[1].tofile(img_path + os.sep + str(filename)[:-4] + '_' + str(dnt) + '.jpg')
            dnt += 1
        cnt += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()


if __name__ == '__main__':
    # 手动输入视频路径、图片保存路径和抽帧频率
    video_path = input("请输入视频文件夹路径：")
    img_path = input("请输入图片保存文件夹路径：")
    fra = int(input("请输入抽帧频率（例如10）："))

    # 获取视频文件列表
    filelist = os.listdir(video_path)

    # 确保目标目录存在
    if not os.path.exists(img_path):
        os.makedirs(img_path)

    threads = []

    for filename in filelist:
        # 仅处理视频文件（根据扩展名过滤）
        if filename.endswith('.mp4') or filename.endswith('.avi') or filename.endswith('.mov'):
            thread = threading.Thread(target=video2img, args=(filename, video_path, img_path, fra))
            threads.append(thread)
            thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print("所有视频处理完毕。")
