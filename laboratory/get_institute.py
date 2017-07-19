import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')

institute = pd.read_csv('../lab_data/yjs.csv', encoding='gb2312')

fp = open('../lab_data/institute.csv', 'w')

fp.write('id,name,city,address,post_code,website\n')

id = 0
for data in institute.iterrows():
    # print data[1]
    name = data[1][0]
    city = data[1][1]
    address = data[1][3]
    post_code = data[1][4]
    if pd.isnull(post_code):
        post_code = ''
    else:
        post_code = str(int(post_code))
    website = data[1][5]

    fp.write(str(str(id)+','+name+','+city+','+address+','+post_code+','+website+'\n'))
    id += 1

