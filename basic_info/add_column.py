# coding=utf-8
import MySQLdb
from db import set_connect
import pandas as pd

web = pd.read_csv('../basic_data/url_t1.csv')

# 为basic_info表添加web这个属性(专家的主页信息)
conn = set_connect()
cursor = conn.cursor()

# 初次添加时执行
# add_web = "alter table basic_info add web TEXT"
# cursor.execute(add_web)

for data in web.iterrows():
    name = data[1][0]
    web =  data[1][1]
    print name,web

    if pd.isnull(web):
        web = ''

    sql = "update basic_info set web = '%s'\
                   WHERE Name = '%s'" % (web, name)

    cursor.execute(sql)
    # 所有更新、插入等操作后，都要进行一次提交
    conn.commit()

cursor.close()
conn.close()