# -*- coding: utf-8 -*-
# @Time    : 2022/10/8
# @Author  : ylf
# @function: STM32CubeMX_Makefile_C_sources格式输出

from ast import Str, Try
from asyncio.windows_events import NULL
from cProfile import label
from email.mime import message
from struct import pack
import os
from tkinter import *
from tkinter import messagebox

# 创建窗口
mainWindow = Tk()

# 设置大小
mainWindow.geometry("580x640")
mainWindow.minsize(width=580, height=640)
mainWindow.title('YLF_DIY_STM32CubeMX_Makefile_C_sources格式输出')
#
cNumber = 0
sv = StringVar()
sv.set('C文件个数：%d' % (cNumber))
#


def scanDir(filePath, delStr):
    # 获取该路径下的所有文件
    try:
        files = os.listdir(filePath)
    except Exception as e:
        messagebox.showinfo(title='异常', message=e)
        return
# 遍历所有文件
    for file in files:
        # 把文件路径和文件名结合起来
        file_d = os.path.join(filePath, file)
        # 判断该文件是单个文件还是文件夹
        if os.path.isdir(file_d):  # 如果是文件夹则递归调用 scanDir() 函数
            scanDir(file_d, delStr)
        else:
            if file_d.endswith('.c'):
                global cNumber
                vsStr = file_d.replace(delStr, '')
                vsStr = vsStr.replace('\\', '/') + ' \\\n'
                textShow.insert(END, vsStr)
                cNumber += 1
                sv.set('C文件个数：%d' % (cNumber))

# 按键回调函数


def btScanDirEvent():
    # 判断文件路径是否为空
    if inputAdr.get() == '':
        # 为空提示
        messagebox.showinfo(title='提示', message='请填写文件路径！')
        return
    else:
        global cNumber
        textShow.delete(1.0, "end")
        cNumber = 0
        filePath = inputAdr.get()
        delStr = inputChange.get()
        scanDir(filePath, delStr)

        return


# 控制区
frameCmd = Frame(mainWindow,  bd='2px')
# 输出显示区
frameText = Frame(mainWindow, bd='2px')

#
reLenLabel = Label(frameCmd, textvariable=sv, height='3')
reLenLabel.grid(row=2, column=0)

# 文件路径
# 标签
adrLabel = Label(frameCmd, text='输入文件路径', height='3')
adrLabel.grid(row=0, column=0)
# 输入框
inputAdr = Entry(frameCmd, bd='2', width='60')
inputAdr.grid(row=0, column=1)
# 需要删除路径
# 标签
changeLabel = Label(frameCmd, text='需要删除路径名称', height='3')
changeLabel.grid(row=1, column=0)
# 输入框
inputChange = Entry(frameCmd, bd='2', width='60',)
inputChange.grid(row=1, column=1)
# 按键
btScanDir = Button(frameCmd, text='开始查找并格式输出',  bg='lightblue',
                   width=20, height=2, command=btScanDirEvent)
btScanDir.grid(row=2, column=1)
# 显示文本
textShow = Text(frameText, width='80', height='40')
textShow.grid(row=3, column=0)

#
frameCmd.pack()
frameText.pack()
# 窗口显示
mainWindow.mainloop()
