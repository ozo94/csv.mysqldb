# coding=utf-8
import pandas as pd
from db import set_connect

path = '../data/basic_data/final_result'

career = open(path + '/career.txt', 'r').readlines()
contribute = open(path + '/contribute.txt', 'r').readlines()
job = open(path + '/job.txt', 'r').readlines()

basic = pd.read_csv('../data/basic_data/create/basic_info.csv')

info = open('../data/basic_data/create/details.csv', 'w')

info.write('id;name;college;career;contribute;job\n')

def suit(name, college, data_lines, fp):
    for i in range(len(data_lines)):
        lines = data_lines[i].split(';')
        name1 = lines[0]
        college1 = lines[1]
        data = lines[3].strip('\n')

        if name == name1 and college == college1:
            fp.write(';'+ data)
            return True

    fp.write(';')
    return False



for data in basic.iterrows():
    id = str(data[1][0])
    name = data[1][1]
    college = data[1][3]
    info.write(id + ';' + name + ';' + college)
    suit(name, college, career,  info)
    suit(name, college, contribute,  info)
    suit(name, college, job,  info)

    info.write('\n')


