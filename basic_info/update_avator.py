# coding=utf-8
import os
import re
import chardet

import MySQLdb
from db import set_connect

def get_code(data):
    # 这个方法会读取所有的数据流后做出判断
    result = chardet.detect(data)
    print result
    return result['encoding']

    # 高级用法: http://chardet.readthedocs.io/en/latest/usage.html

def get_avator(path):
    path_dir = os.listdir(path)
    judge_table = {}

    # 获取图片中的教授名字，所在学校, 匹配图片
    for dir in path_dir:
        # dir = dir.decode(get_code(dir)).encode('utf-8')
        img_name = dir.decode('gbk').split('.jpg')[0]
        data = img_name.split('_')
        Company = data[0]
        # Name = re.sub(' |　', '', data[1])
        Name = data[1].replace(' ', '')

        # 以姓名，公司为key，将图片存入字典, 以二进制流的方式读取图片信息
        key = (Name, Company)
        fp = open(os.path.join(path, dir), 'rb')
        img = fp.read()
        fp.close()

        judge_table[key] = img

    # print 'LINzhongqin',judge_table[('林忠钦','上海交通大学')]

    return judge_table

def update_avator(table, conn):
    cursor = conn.cursor()
    num = 0
    miss = 0

    # 在basic_info中寻找对应的专家，获取id
    for key in table.keys():
        # print key[1], key[0]
        # basic_info表的信息： ID, Name, Sex, Company, Duty, Tel, Email
        find_professor = "SELECT * FROM basic_info \
                WHERE name = '%s' AND college = '%s'" % (key[0], key[1])
        cursor.execute(find_professor)
        data = cursor.fetchone()

        try:
            id = data[0]
            # print id, key[0]
            # print table[key]
            # 将对应的id ，img 存入表avator中，escape将流进行安全的转义（不转义%/_）
            img = MySQLdb.escape_string(table[key])
            add_avator = "REPLACE INTO avator (ID, img) \
                          VALUES ('%d', '%s' )" % (id, img)
            cursor.execute(add_avator)

            add_avator_path = "update basic_info set avator = '%s'\
                               WHERE id = '%s'" % (str(id)+'.jpg', id)
            cursor.execute(add_avator_path)

            conn.commit()
            # print 'sucess'
            num += 1
        except Exception,e:
            print  e, key[0], key[1]
            miss += 1
    print num
    print miss
    cursor.close()
    conn.close()

if __name__ == '__main__':
    path = '../data/basic_data/Avator'

    #  头像的存储
    judge_table = get_avator(path)

    conn = set_connect()
    update_avator(judge_table, conn)





