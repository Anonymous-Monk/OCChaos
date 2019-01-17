# -*- coding: utf-8 -*-

from Class.OCChaosImgMd5Change import OCChaosImgMd5Change
from Class.OCChaosPrefixRe import OCChaosPrefixRe
from Class.OCChaosUselessClassfile import  OCChaosUselessClassfile
from Class.OCChaosUselessCode import OCChaosUselessCode
from Class.OCChaosConfig import OCChaosConfig
import json
import os,sys

keys=["pre_str","pre_to_str","suf_set","project_path","pbxpro_path","img_suf_set","file_floadPath","classArray","h_file_mark_arr","m_file_mark_arr"]

class OCChaos(object):

    def __init__(self,path=sys.path[0]+"/config.json"):
        self.path_config = OCChaosConfig(path=path)
        pass


    def changePrefixCallBack(self):
        pre = self.config.getPre_str()
        pre_to = self.config.getPre_to_str()
        if len(pre_to) == 0  and len(pre) == 0:
            print("类名旧前缀与新前缀没有设置")
            return
        OCChaosPrefixRe().start_rename()
        # print(self.path_config.get())

    def changeMd5CallBack(self):
        project_path = self.path_project_dir.get()
        img_suf = self.path_config.getImg_suf_set()
        if len(project_path) == 0 or len(img_suf) == 0:
            print("工程路径与图片文件后缀没有设置")
            return
        OCChaosImgMd5Change().start_change_img_md5()

    def createUselessClassCallBack(self):
        project_path = self.path_project_dir.get()
        output_path = self.path_output.get()
        if len(project_path) == 0 or len(output_path) == 0:
            print("工程路径与输出路径没有设置")
            return
        OCChaosUselessClassfile().start_create_files(fileCount=20,output_path=output_path)

    def insertUselessCodeCallBack(self):
        config_path = self.path_config.get()
        project_path = self.path_project_dir.get()
        if len(project_path)==0:
            print("工程路径没有设置")
            return
        OCChaosUselessCode().start_create_useless_code(project_path)

def check_file()->bool:
    print("请输入配置文件路径(请严格按照配置示例进行配置):")
    file_check_flag = True
    config_path = input()
    if config_path.endswith(".json"):
        with open(config_path, 'r') as f:
            temp = json.loads(f.read())
            for k in keys:
                if k not in temp:
                    print(k+"键值不存在或者错误,请检查配置文件\n")
                    file_check_flag = False

        if file_check_flag:
            return config_path,os.path.exists(config_path)
        else:
            check_file()
    else:
        print("需要输入正确的配置文件路径！")
        check_file()

def select_funtion(config_path:str):

    print("请选择要执行的功能:\n1.更换文件前缀;\n2.生成无用的.h .m文件;\n3.更改资源图片的md5值;\n4.已有.h .m添加废弃代码\n\n请输入序号，按回车")
    chaos = OCChaos(path=config_path)
    cmd_str = input()
    if cmd_str is "1":
        print("更换文件前缀")

        chaos.changePrefixCallBack()
    elif cmd_str is "2":
        print("生成无用的.h .m文件")
        chaos.createUselessClassCallBack()
    elif cmd_str is "3":
        print("更改资源图片的md5值")
        chaos.changeMd5CallBack()
    elif cmd_str is "4":
        print("已有.h .m添加废弃代码")
        chaos.insertUselessCodeCallBack()
    else:
        print("请输入正确序号！")
        start_action()

def start_action():

    config_path,file_check_result = check_file()
    if file_check_result == False:
        check_file()
        return
    while True:
        select_funtion(config_path)

if __name__ == '__main__':
    start_action()
