#!/usr/bin/env python
# encoding: utf-8
# @Time : 2019-08-06 18:54

__author__ = 'Ted'

from PIL import Image
import os


def combine_pic(folder):
    # 读取地图轮廓图
    img = Image.open("china.png")

    w,h = img.size
    #新建与主图一样大的白色底图
    new_img = Image.new('RGB',(w,h),'#FFFFFF')

    unit_size = 20

    #根据小格尺寸，计算大图可容纳小图数量
    y_index = h//unit_size
    x_index = w//unit_size

    pic_list = []
    for item in os.listdir(folder):
        #对文件夹中的 jpg 图片格式筛选
        if item.endswith(".jpg") or item.endswith(".jpeg") :
            pic_list.append(item)

    #获取素材图片数目
    total = len(pic_list)
    x=0
    y=0

    for i in range(x_index*y_index):
        #提醒进度的语句
        print(f"目前进度{i}/{x_index*y_index}")
        try:
            # 对素材图缩放至小格大小
            test = Image.open(f"{folder}/" + pic_list[i%total]).resize((unit_size,unit_size), Image.ANTIALIAS)
        except IOError:
            print("有1位朋友的头像读取失败，跳过该头像")  # 有些人没设置头像，就会有异常
            continue

        #将缩放成小格的素材图按顺序贴到白色底图上
        new_img.paste(test,(x*unit_size,y*unit_size))
        x+=1
        if x==x_index:
            x=0
            y+=1

    print("素材图合成完毕！")
    #将合成的素材图存至 out.jpg
    new_img.save("out.jpg",quality=100)

#如果不想每次都生成图，可以运行一次后注释掉这句，参数为文件夹名字
combine_pic("TED")

#读取合成后的素材图
src1 = Image.open("out.jpg")

#读取地图轮廓图
src2 = Image.open("china.png")

src1.paste(src2,(0,0),src2)

src1.save("result.png")
print("地图轮廓添加完毕！")






