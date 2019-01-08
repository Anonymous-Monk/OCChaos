# -*- coding: utf-8 -*-
import OCChaos_prefix_re
import OCChaos_useless_classfile
import OCChaos_img_md5_change
import OCChaos_useless_code

if __name__ == '__main__':

    #更换前缀
    OCChaos_prefix_re.start_rename()

    #生成无用的.h  .m file
    #默认主动生成20对文件
    OCChaos_useless_classfile.start_create_files(fileCount=20)

    #更改资源图片md5
    OCChaos_img_md5_change.start_change_img_md5()

    #在.h 和.m 中添加废弃代码
    OCChaos_useless_code.start_create_useless_code()