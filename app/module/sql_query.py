import pymysql
# def connet(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#     return wrapper
# @connet
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