# coding=utf-8
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')

core_sub1 = pd.read_csv('../lab_data/zdxk1.csv')
core_sub2 = pd.read_csv('../lab_data/zdxk1.csv')

fp = open('../lab_data/core_sub.csv', 'w')
fp.write('id,sub,sub_code,college\n')
id = 0
for data in core_sub1.iterrows():
    # print data[1]
    sub = str(data[1][0])
    # filter筛选函数，筛选出满足条件的字符内容
    sub_code = filter(str.isdigit, sub)
    sub_name = sub.strip(sub_code)
    college = data[1][1]

    fp.write(str(id)+ ',' + sub_code+ ',' + sub_name + ',' + college + '\n')
    id += 1


for data in core_sub2.iterrows():
    # print data[1]
    sub = str(data[1][0])
    # filter筛选函数，筛选出满足条件的字符内容
    sub_code = filter(str.isdigit, sub)
    sub_name = sub.strip(sub_code)
    college = data[1][1]

    fp.write(str(id)+ ',' + sub_code+ ',' + sub_name + ',' + college + '\n')
    id += 1

