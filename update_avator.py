# coding=utf-8
import os
from db import set_connect
import MySQLdb

def get_avator(path):
    path_dir = os.listdir(path)
    judge_table = {}

    # 获取图片中的教授名字，所在学校, 匹配图片
    for dir in path_dir:
        img_name = dir.decode('gbk').encode('utf-8').split('.jpg')[0]
        data = img_name.split('_')
        Company = data[0]
        Name = data[1]

        # 以姓名，公司为key，将图片存入字典
        key = (Name, Company)

        fp = open(os.path.join(path, dir))
        img = fp.read()
        fp.close()

        judge_table[key] = img

    # print 'LINzhongqin',judge_table[('林忠钦','上海交通大学')]

    return judge_table

def update_avator(table, conn):
    cursor = conn.cursor()

    # 在basic_info中寻找对应的专家，获取id
    for key in table.keys():
        # print key[1], key[0]
        # ID, Name, Sex, Company, Duty, Tel, Email
        find_professor = "SELECT * FROM basic_info \
                WHERE Name = '%s' AND Company = '%s'" % (key[0], key[1])
        cursor.execute(find_professor)
        data = cursor.fetchone()

        try:
            id = data[0]
            print id, key[0]
            # 将对应的id ，img 存入表avator中
            img = MySQLdb.escape_string(table[key])
            add_avator = "REPLACE INTO avator (ID, img) \
                          VALUES ('%d', '%s' )" % (id, img)
            cursor.execute(add_avator)
            conn.commit()
            print 'sucess'
        except Exception,e:
            print  e

    cursor.close()
    conn.close()

if __name__ == '__main__':
    path = 'Avator'

    #  头像的存储
    judge_table = get_avator(path)

    conn = set_connect()
    update_avator(judge_table, conn)





