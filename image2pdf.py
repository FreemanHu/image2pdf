#!/usr/bin/env python
from PIL import Image
import os
import glob
from tqdm import tqdm

#获得当前列表下的所有的文件，并且按照创建时间排序
file_path = '.'
# 读取的文件后缀名
file_extensions = ['png','jpg']

im_list = []
i = 0
# 遍历每一个文件后缀名
for f_ext in file_extensions:
    # 读取所有该后缀名的文件，并且按照修改时间排序
    for file in tqdm(sorted(glob.glob(file_path + '/*.' + f_ext),\
            key = lambda x: os.path.getmtime(os.path.join(file_path,x)))):
                im_temp = Image.open(file)
                im_temp = im_temp.convert('RGB')
        # 第一个文件赋值给im
                if(i==0):
                    im = im_temp
                    i = 1
                else:
                    # 其他文件添加到im_list
                    im_list.append(im_temp)
# 保存到all.pdf文件
im.save(r'all.pdf',save_all=True, append_images=im_list)
