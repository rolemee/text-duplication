import pymysql

def sql_query(sql, list):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         database='python_homework')
    cursor = db.cursor()
    cursor.execute(sql, list)
    data = cursor.fetchone()
    db.close()
    return data
