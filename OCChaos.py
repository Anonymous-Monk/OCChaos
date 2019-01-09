# -*- coding: utf-8 -*-

from OCChaosImgMd5Change import OCChaosImgMd5Change
from OCChaosPrefixRe import OCChaosPrefixRe
from OCChaosUselessClassfile import  OCChaosUselessClassfile
from OCChaosUselessCode import OCChaosUselessCode

import tkinter as tk
import tkinter.messagebox
from tkinter.filedialog import askdirectory,askopenfilename

class OCChaos(object):

    def __init__(self):
        pass

    def selectConfigPath(self):
        path_ = askopenfilename()
        self.path_config.set(path_)

    def selectProjectDirPath(self):
        path_ = askdirectory()
        self.path_project_dir.set(path_)

    def selectOutPutDirPath(self):
        path_ = askdirectory()
        self.path_output.set(path_)

    def changePrefixCallBack(self):
        config_path = self.path_config.get()
        if len(config_path) == 0:
            tk.messagebox.askquestion(title="错误",message="请选择配置文件路径")
            return
        OCChaosPrefixRe().start_rename()
        # print(self.path_config.get())

    def changeMd5CallBack(self):
        config_path = self.path_config.get()
        project_path = self.path_project_dir.get()
        if len(config_path) == 0 or len(project_path) == 0:
            tk.messagebox.askquestion(title="错误", message="配置文件或工程代码文件目录不能为空")
            return
        OCChaosImgMd5Change().start_change_img_md5()

    def createUselessClassCallBack(self):
        config_path = self.path_config.get()
        project_path = self.path_project_dir.get()
        output_path = self.path_output.get()
        if len(config_path) == 0 or len(project_path) == 0 or len(output_path) == 0:
            tk.messagebox.askquestion(title="错误", message="配置文件或工程代码文件目录或输出文件目录不能为空")
            return
        OCChaosUselessClassfile().start_create_files(fileCount=20,output_path=output_path)

    def insertUselessCodeCallBack(self):
        config_path = self.path_config.get()
        project_path = self.path_project_dir.get()
        if len(config_path) == 0 or len(project_path)==0:
            tk.messagebox.askquestion(title="错误",message="配置文件或工程代码文件目录不能为空")
            return
        OCChaosUselessCode().start_create_useless_code(project_path)

    def showWindow(self):
        # 创建主窗口,用于容纳其它组件
        root = tk.Tk()
        # 给主窗口设置标题内容
        root.title("一些马甲包的可用到的功能")
        root.maxsize(600, 400)
        root.minsize(600, 400)

        # 获取屏幕 宽、高 居中显示
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        # 计算 x, y 位置
        x = (ws / 2) - (600 / 2)
        y = (hs / 2) - (400 / 2)
        root.geometry('%dx%d+%d+%d' % (600, 400, x, y))


        self.path_config = tk.StringVar()
        self.path_project_dir = tk.StringVar()
        self.path_output = tk.StringVar()

        tk.Label(root, text="配置文件目录路径:").grid(row=0, column=0)
        tk.Entry(root, textvariable=self.path_config).grid(row=0, column=1)
        tk.Button(root, text="点击选择配置文件", command=self.selectConfigPath).grid(row=0, column=2)

        tk.Label(root, text="工程目录:").grid(row=1, column=0)
        tk.Entry(root, textvariable=self.path_project_dir).grid(row=1, column=1)
        tk.Button(root, text="点击选择工程目录", command=self.selectProjectDirPath).grid(row=1, column=2)

        tk.Label(root, text="输出文件目录:").grid(row=2, column=0)
        tk.Entry(root, textvariable=self.path_output).grid(row=2, column=1)
        tk.Button(root, text="点击选择输出文件目录", command=self.selectOutPutDirPath).grid(row=2, column=2)

        # text_old_fix = StringVar()
        # text_new_fix = StringVar()
        # Entry(root,text = '原始前缀',textvariable=text_old_fix).grid(row=3, column=0)
        # Entry(root,text = '新前缀',textvariable=text_new_fix).grid(row=3, column=1)
        tk.Button(root, text="批量修改前缀", command=self.changePrefixCallBack).grid(row=3, column=0)
        tk.Button(root, text="修改资源文件Md5", command=self.changeMd5CallBack).grid(row=3, column=1)
        tk.Button(root, text="生成无用类", command=self.createUselessClassCallBack).grid(row=3, column=2)
        tk.Button(root, text="已有类插入垃圾代码", command=self.insertUselessCodeCallBack).grid(row=3, column=3)

        # 主程序执行
        tk.mainloop()

if __name__ == '__main__':

    # #更换前缀
    # OCChaosPrefixRe().start_rename()
    #
    # #生成无用的.h  .m file
    # #默认主动生成20对文件
    # OCChaosUselessClassfile().start_create_files(fileCount=20)
    #
    # #更改资源图片md5
    # OCChaosImgMd5Change().start_change_img_md5()

    #在.h 和.m 中添加废弃代码
    # OCChaosUselessCode().start_create_useless_code()
    chaos = OCChaos()
    chaos.showWindow()