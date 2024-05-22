import cv2,os

'''
读取文件夹下图片，对文件夹下所有图片进行指定区域涂黑，并保存到指定路径
'''
def read_path(file_pathname):
    #遍历该目录下的所有图片文件
    for filename in os.listdir(file_pathname):
        print(filename)
        img = cv2.imread(file_pathname+'/'+filename)
        #img(指定区域) = (RGB色)
        img[0:80, 0:500] = (0,0,0)
        #保存路径示例："E:/resources/desk/20240412/Hikr"
        cv2.imwrite('E:/resources/desk/20240412/THikr'+"/"+filename,img)

#读取的目录,替换为文件夹名，示例："E:/resources/desk/20240412/Hikr"
read_path("E:/resources/desk/20240412/Hikr")