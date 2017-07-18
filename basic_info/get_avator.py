# coding=utf-8
from db import set_connect
import os

def get_avator(conn, id, path):
    '''

    :param conn: 数据库链接
    :param id:  专家的id
    :param path: 存放头像缓存的路径
    :return: 返回头像的路径
    '''

    # 头像缓存在get_avator中，如果存在就无需从数据库中获取了（以id.jpg的方式缓存）
    img_name = str(id) + '.jpg'
    avator_path = os.path.join(path, img_name)

    if os.path.exists(avator_path):
        return avator_path
    # 缓存中没有，从数据库中获取
    else:
        cursor = conn.cursor()
        find_avator = "SELECT * FROM avator \
                   WHERE ID = '%d'" % (id)
        cursor.execute(find_avator)


        try:
            img = cursor.fetchone()[1]
            print img
            avator = open(avator_path, 'wb')
            avator.write(img)
            avator.close()
            return avator
        except:
            print 'cant find avator, give a blank one'
            return os.path.join(path, 'blank.jpg')

if __name__ == '__main__':
    path = '../get_avator'
    conn = set_connect()
    for id in range(226):
        avator = get_avator(conn, id, path)
    print avator