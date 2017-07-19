# coding=utf-8
import pandas as pd
# pyhton 默认的编译脚本是ascii,出现超出ascii码的文件，重载一下脚本编码
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 整理985,211高校数据，以及所有的学校的信息
college = pd.read_csv('../lab_data/2016_college.csv' , encoding='gb2312')
college_112 = open('../lab_data/college_112.csv', 'w')
college_all = open('../lab_data/college_all.csv', 'w')

college_112.write('id,college,city,985,211\n')
college_all.write('id,college,city\n')

num = 0
for data in college.iterrows():
    num += 1
    id = data[1][0]
    college = data[1][1]
    city = data[1][2]

    try:
        if id[0] >= '0' and id[0] <= '9' :
            if num <= 43 and num != 3 :
                college_112.write(id + ',' + college + ',' + city + ',1,1' + '\n')
                print id, college, city
            elif num >44 and num < 118:
                college_112.write(id + ',' + college + ',' + city + ',0,1' + '\n')
            elif num >= 118:
                college_all.write(id + ',' + college + ',' + city + '\n')
    except Exception,e:
        print e
        # print id, college, city

