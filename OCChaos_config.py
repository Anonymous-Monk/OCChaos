# -*- coding: utf-8 -*-

#需要修改的类名前缀 （需替换）
pre_str = 'ZTY'
# 新的类名前缀 （需替换）
pre_to_str = 'TY'
# 搜寻以下文件类型 （根据自己需求替换）
suf_set = ('.h', '.m', '.xib', '.storyboard', '.mm')
# 项目路径   （找到自己的项目路径）
project_path = '/Volumes/Files/Document/LionMobi/TestIpa/TestIpa'
# 项目project.pbxproj文件路径 需要更新配置文件中的类名 （找到自己的项目project.pbxproj路径）
pbxpro_path = '/Volumes/Files/Document/LionMobi/TestIpa/TestIpa.xcodeproj/project.pbxproj'

# 设置以这些结尾的
img_suf_set = ('.png', '.jpg')

# 在目标.h  .m 文件所在的路径
file_floadPath = '/Volumes/Files/Document/LionMobi/TestIpa/TestIpa'

# .h文件里属性的类型从这个数组里随机选(按需修改)
classArray = ['NSString', 'UILabel', 'NSDictionary', 'NSData', 'UIScrollView', 'UIView', 'UITextView', 'UITableView',
              'UIImageView']

# .h   .m  文件中 需要在哪种标识后面添加废弃代码(按需修改)
h_file_mark_arr = ["l;", "m;", "n;", "q;", "y;"] # 往凡是以"l;", "m;","n;","q;","y;"这些中的某一个结尾的oc语句后添加废弃代码
m_file_mark_arr = ["n];", "w];", "m];", "c];", "p];", "q];", "l];"] # 往凡是以"n];", "w];","m];","c];","p];","q];","l];"这些中的某一个结尾的oc语句后添加废弃代码
