import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')

core_sub = pd.read_csv('../lab_data/zdxk1.csv')

fp = open('../lab_data/core_sub.csv', 'w')
fp.write('id,sub,sub_code,college\n')

for data in core_sub.iterrows():
    # print data[1]
    sub_code = ''
    for s in data[1][0]:
        if s <='0' and