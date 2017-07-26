import pandas as pd



def wirte_data(csvObject, id):
    for x in csvObject.iterrows():
        '''
            Duty,Tel,Name,Company,Sex,Skill,Email
        '''
        data = x[1]
        for i in range(7):
            if pd.isnull(data[i]):
                data[i]= ''
        fopen.write(str(id)+','+data[2]+','+data[4]+','+data[3]+','+data[0]+','+str(data[1])+','+str(data[6])+'\n')
        id += 1

    return id

if __name__ == '__main__':
    basic_info = pd.read_csv('../basic_data/data_t1.csv')
    kz = pd.read_csv('../basic_data/data_kz.csv')
    fopen = open('../basic_data/basic_info.csv', 'w')
    fopen.write('ID,Name,Sex,Company,Duty,Tel,Email' + '\n')

    id = 0
    id1 = wirte_data(basic_info, id)
    id2 = wirte_data(kz, id1)


