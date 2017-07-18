# coding=utf-8
import MySQLdb

def set_connect():

    config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'passwd': '1234',
        'db': 'professor',
        'charset': 'utf8'
    }

    conn = MySQLdb.connect(**config)
    return conn

if __name__ == '__main__':

    # connect test
    conn = set_connect()
    cursor = conn.cursor()

    sql = "SELECT * FROM basic_info \
           WHERE Name = '%s'" % ("王志新")

    cursor.execute(sql)
    data = cursor.fetchone()

    for x in data:
        print x