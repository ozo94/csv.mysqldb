import pandas as pd

basic_info = pd.read_csv('../basic_data/data_t1.csv')
fopen = open('../basic_data/basic_info.csv', 'w')

id = 0
fopen.write('ID,Name,Sex,Company,Duty,Tel,Email'+'\n')

for x in basic_info.iterrows():
    '''
        Duty,Tel,Name,Company,Sex,Skill,Email
    '''
    data = x[1]
    for i in range(7):
        if pd.isnull(data[i]):
            data[i]= ''
    fopen.write(str(id)+','+data[2]+','+data[4]+','+data[3]+','+data[0]+','+str(data[1])+','+str(data[6])+'\n')
    id += 1