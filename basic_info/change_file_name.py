# coding=utf-8
import os
import re
import chardet
import sys
reload(sys)
sys.setdefaultencoding('gbk')

def get_code(data):
    # 这个方法会读取所有的数据流后做出判断
    result = chardet.detect(data)
    # print result
    return result['encoding']

    # 高级用法: http://chardet.readthedocs.io/en/latest/usage.html

path = '../data/basic_data/Avator'
# for dir in os.listdir(path):
#     # print dir.decode('gbk').encode('utf-8')
#     new_name = re.sub(' |　|\?', '', dir)
#     print new_name
#     # new_name = new_name.decode('gbk').encode('utf-8')
#     # print new_name
#     print path+'/'+dir
#     os.rename(path+'/'+dir, os.path.join(path, new_name))

import os
for parent, dirnames, filenames in os.walk(path):
    for filename in filenames:
        os.rename(os.path.join(parent, filename), os.path.join(parent, filename.replace(' ', '')))

