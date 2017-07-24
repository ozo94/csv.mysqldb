# coding=utf-8
from db import set_connect
import pandas as pd

# 所选的重点学科的代码
selected = {'0802', '0804', '0805', '0806', '0808', '0809', '0811',
        '0812', '0817', '0830', '0831'}

fp = open('../lab_data/seleted_core_sub.csv', 'w')
fp.write('id,code,sub,college\n')

conn = set_connect()
cursor = conn.cursor()

id = 0

for x in selected:
    x = str(x)
    find_sub = "SELECT * FROM core_sub \
                       WHERE  sub LIKE '%s'" % (x+'%')

    cursor.execute(find_sub)

    datas = cursor.fetchall()
    for data in datas:
        code = data[1]
        sub = data[2].encode('utf-8')
        college = data[3].encode('utf-8')
        id = id + 1
        fp.write(str(id)+','+str(code)+','+sub+','+college+'\n')
        print data[0], sub

cursor.close()
conn.close()


