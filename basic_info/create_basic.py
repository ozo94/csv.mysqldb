# coding=utf-8
import re

def judge(s):
    if s:
        return '1'
    else:
        return '0'

alls = open('../data/basic_data/create/new_all.txt', 'r')
tags = open('../data/basic_data/create/tags.txt', 'r')

all_lines = alls.readlines()
tag_lines = tags.readlines()

fp = open('../data/basic_data/create/basic_info.csv', 'w')
fp.write('id,name,avator,college,institute,tel,email,C,J,Q\n')

for i in range(len(all_lines)):
    index = str(i)
    all_c = re.sub(' |　|\n','',all_lines[i]).split(',')
    tel = all_c[2]
    email = all_c[3]
    C = judge(all_c[4])
    J = judge(all_c[5])
    Q = judge(all_c[6])

    tag_c = re.sub(' |　','',tag_lines[i]).strip('\n').split(';')
    name = tag_c[0]
    avator = 'blank.jpg'
    college = tag_c[1]
    institute = tag_c[2]

    fp.write(index+','+name+','+avator+','+college+','+institute+','+tel+','+email+','+C+','+J+','+Q+'\n')

