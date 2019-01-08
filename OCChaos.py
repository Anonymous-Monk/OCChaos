# -*- coding: utf-8 -*-

from OCChaosImgMd5Change import OCChaosImgMd5Change
from OCChaosPrefixRe import OCChaosPrefixRe
from OCChaosUselessClassfile import  OCChaosUselessClassfile
from OCChaosUselessCode import OCChaosUselessCode

if __name__ == '__main__':

    #更换前缀
    OCChaosPrefixRe().start_rename()

    #生成无用的.h  .m file
    #默认主动生成20对文件
    OCChaosUselessClassfile().start_create_files(fileCount=20)

    #更改资源图片md5
    OCChaosImgMd5Change().start_change_img_md5()

    #在.h 和.m 中添加废弃代码
    OCChaosUselessCode().start_create_useless_code()