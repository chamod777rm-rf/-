# -*- coding=utf-8 -*-

from PIL import Image
import argparse
import tkinter as tk
from tkinter import filedialog

# 命令行输入参数处理
parser = argparse.ArgumentParser()

# import tkinter as tk


'''打开选择文件夹对话框'''
root = tk.Tk()
root.withdraw()

# Folderpath = filedialog.askdirectory() #获得选择好的文件夹
Filepath = filedialog.askopenfilename()  # 获得选择好的文件

# print('Folderpath:',Folderpath)
print('Filepath:', Filepath)

parser.add_argument('--file', default=Filepath)  # 输入文件
parser.add_argument('-o', '--output')  # 输出文件
parser.add_argument('--width', type=int, default=80)  # 输出字符画宽
parser.add_argument('--height', type=int, default=80)  # 输出字符画高

# 获取参数
args = parser.parse_args()
# args = Filepath

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_text():
    win = tk.Tk()
    text = tk.Text(win, width=100, height=100)
    text.pack()
    text.insert('end', txt)  # INSERT索引表示光标当前的位置

    win.mainloop()


# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '

    # 获取字符集的长度，这里为70
    length = len(ascii_char)

    # 将RGB值转为灰度值gray，灰度值范围为0-255
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    # 灰度值范围为0-255，而字符集之后70
    # 需要进行如下处理才能将灰度值映射到指定的字符上
    unit = (256.0 + 1) / length

    # 返回灰度值对应的字符
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':

    # 打开并掉帧图片的宽和高
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    # 初始化输出的字符串
    txt = ""

    # 遍历图片中的每一行
    for i in range(HEIGHT):
        # 遍历该行中的每一列
        for j in range(WIDTH):
            # 将（j,i）坐标的RGB像素转为字符后添加到txt字符串
            txt += get_char(*im.getpixel((j, i)))
        # 遍历完一行后需要增加换行符
        txt += '\n'
    # 输出到屏幕
    print(txt)

    get_text()

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)

