import pandas as pd

articles = pd.read_csv('../data/works/articles.csv')


fp  = open('../data/works/pro_art.csv', 'w')
fp.write('id;name;article_list\n')
# new_articles = open('../data/works/new_articles.csv', 'w')

professors = pd.read_csv('../data/basic_data/create/basic_info.csv')

id = 1
article_dicts = {}

for data in articles.iterrows():
    authors = data[1][3].strip('"').split(',')
    for author in authors:
        if author not in article_dicts.keys():
            article_dicts[author] = str(id)+','
        else:
            article_dicts[author] += str(id)+','
    print id,':', data[1][0]
    id += 1


for data in professors.iterrows():
    name = data[1][1]
    id = data[1][0]
    if name in article_dicts.keys():
        fp.write(str(id)+ ';' + name + ';' + article_dicts[name]+ '\n')
    else:
        fp.write(str(id)+ ';' + name + ';' +' '+ '\n')





