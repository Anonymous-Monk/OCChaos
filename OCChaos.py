# -*- coding: utf-8 -*-

from Class.OCChaosImgMd5Change import OCChaosImgMd5Change
from Class.OCChaosPrefixRe import OCChaosPrefixRe
from Class.OCChaosUselessClassfile import  OCChaosUselessClassfile
from Class.OCChaosUselessCode import OCChaosUselessCode
from Class.OCChaosConfig import OCChaosConfig

import os,sys

class OCChaos(object):

    def __init__(self):
        self.path_config = OCChaosConfig(path=sys.path[0]+"/config.json")
        pass


    def changePrefixCallBack(self):
        config_path = self.path_config.get()
        if len(config_path) == 0:
            return
        OCChaosPrefixRe().start_rename()
        # print(self.path_config.get())

    def changeMd5CallBack(self):
        config_path = self.path_config.get()
        project_path = self.path_project_dir.get()
        if len(config_path) == 0 or len(project_path) == 0:
            return
        OCChaosImgMd5Change().start_change_img_md5()

    def createUselessClassCallBack(self):
        config_path = self.path_config.get()
        project_path = self.path_project_dir.get()
        output_path = self.path_output.get()
        if len(config_path) == 0 or len(project_path) == 0 or len(output_path) == 0:
            return
        OCChaosUselessClassfile().start_create_files(fileCount=20,output_path=output_path)

    def insertUselessCodeCallBack(self):
        config_path = self.path_config.get()
        project_path = self.path_project_dir.get()
        if len(config_path) == 0 or len(project_path)==0:
            return
        OCChaosUselessCode().start_create_useless_code(project_path)


if __name__ == '__main__':

    chaos = OCChaos()
    pass

    #更换前缀
    # OCChaosPrefixRe().start_rename()

    #生成无用的.h  .m file
    #默认主动生成20对文件
    # OCChaosUselessClassfile().start_create_files(fileCount=20)

    #更改资源图片md5
    # OCChaosImgMd5Change().start_change_img_md5()

    #在.h 和.m 中添加废弃代码
    # OCChaosUselessCode().start_create_useless_code()
    # chaos = OCChaos()
    # chaos.showWindow()