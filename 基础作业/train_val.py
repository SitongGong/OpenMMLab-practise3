import os
import random
import shutil

def train_val_process():
    PATH_IMAGE = "C:/Users/gst01/archive/jpeg_images/IMAGES"            # 此处为存储图像的文件夹路径
    all_file_list = os.listdir(PATH_IMAGE)
    all_file_num = len(all_file_list)
    random.shuffle(all_file_list)              # 随机打乱全部数据文件名列表

    train_ratio = 0.8
    test_ratio = 1 - train_ratio
    train_file_list = all_file_list[:int(all_file_num*train_ratio)]
    test_file_list = all_file_list[int(all_file_num*train_ratio):]
    print('数据集图像总数', all_file_num)
    print('训练集划分比例', train_ratio)
    print('训练集图像个数', len(train_file_list))
    print('测试集图像个数', len(test_file_list))

    with open('C:/Users/gst01/archive/train.txt', 'w') as f:                      # 将训练集的名称整理到txt文件中
        f.writelines(line.split('.')[0] + '\n' for line in train_file_list)
        f.close()
    with open('C:/Users/gst01/archive/val.txt', 'w') as f:                        # 将验证集的名称整理到txt文件中
        f.writelines(line.split('.')[0] + '\n' for line in test_file_list)
        f.close()

    f = open("C:/Users/gst01/archive/train.txt", encoding='gbk')
    train_line = []
    for line in f:
        train_line.append(line.strip())              # 训练集图像名称

    val_line = []
    f = open("C:/Users/gst01/archive/val.txt", encoding="gbk")
    for line in f:
        val_line.append(line.strip())                # 验证集图像名称

    mask_train_line = [n.split("_")[1] for n in train_line]
    mask_val_line = [n.split("_")[1] for n in val_line]

    file_dirs = []
    root = ""
    for rot, dir, file in os.walk("C:\\Users\\gst01\\archive\\jpeg_images\\IMAGES"):
        file_dirs = file
        root = rot

    for file_dir in file_dirs:
        file = file_dir.split(".")
        if file[0] in train_line:               # 遍历图像文件夹，若图像名称位于训练集txt文件中，则将其复制到训练集文件夹中
            shutil.copy(root + "\\" + str(file[0]) + ".jpeg", "C:/Users/gst01/archive/train_img")
            os.rename("C:/Users/gst01/archive/train_img/"+str(file[0]) + ".jpeg",       # 重命名图像为jpg格式
                      "C:/Users/gst01/archive/train_img/"+str(file[0].split("_")[1]) + ".jpg")
        if file[0].split("_")[1] in mask_train_line:             # 将图像对应的mask进行移动，并重命名
            shutil.copy("C:\\Users\\gst01\\archive\\png_masks\\MASKS\\seg_" + str(file[0].split("_")[1]) + ".png",
                        "C:/Users/gst01/archive/train_mask")
            os.rename("C:/Users/gst01/archive/train_mask/seg_"+str(file[0].split("_")[1]) + ".png",
                      "C:/Users/gst01/archive/train_mask/"+str(file[0].split("_")[1]) + ".png")
        if file[0] in val_line:                 # 遍历图像文件夹，若图像名称位于验证集txt文件中，则将其复制到验证集文件夹中
            shutil.copy(root + "\\" + str(file[0]) + ".jpeg", "C:/Users/gst01/archive/val_img")
            os.rename("C:/Users/gst01/archive/val_img/" + str(file[0]) + ".jpeg",                    # 重命名图像为jpg格式
                      "C:/Users/gst01/archive/val_img/" + str(file[0].split("_")[1]) + ".jpg")
            if file[0].split("_")[1] in mask_val_line:            # 将图像对应的mask进行移动，并重命名
                shutil.copy(
                    "C:\\Users\\gst01\\archive\\png_masks\\MASKS\\seg_" + str(file[0].split("_")[1]) + ".png",
                    "C:/Users/gst01/archive/val_mask")
                os.rename("C:/Users/gst01/archive/val_mask/seg_" + str(file[0].split("_")[1]) + ".png",
                          "C:/Users/gst01/archive/val_mask/" + str(file[0].split("_")[1]) + ".png")

if __name__=="__main__":
    train_val_process()