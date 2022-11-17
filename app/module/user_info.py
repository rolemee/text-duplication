import json

import module.sql_query
from datetime import date, datetime

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)
def get_user_info(sql ,list):
    data = module.sql_query.sql_query(sql,list)
    return json.dumps({
                "status": 1,
                "error": "",
                "data": {
                    "usernameId":data[0],
                    "name":data[1],
                    "nickname": data[2],
                    "rights": data[3],
                    "describe": data[4]
                }
            })

def get_user_homeworkList(request , rights):
    if rights == 0:
        sql = "select h.homeworkId,homeworkName,homeworkDescribe,homework_type,start_time,stop_time,is_Finish,teacher_name from user_homework right join homework h on h.homeworkId = user_homework.homeworkId right join user u on u.usernameId = user_homework.usernameId where user_homework.usernameId = %s"
        data = module.sql_query.sql_query_all(sql, [request.form.get("usernameId")])
        if data is None:
            return json.dumps({
                "status": 1,
                "error": "",
                "data": {}
            })
        data_list = []
        for i in data:
            data_list.append({
                "homeworkId":i[0],
                "homeworkName":i[1],
                "homeworkDescribe": i[2],
                "homework_type": i[3],
                "start_time": i[4],
                "stop_time": i[5],
                "is_Finish": i[6],
                "teacherName": i[7]
            })
        return json.dumps({
            "status": 1,
            "error": "",
            "data": data_list
        },cls=ComplexEncoder)
    if rights == 1:
        sql = "select h.homeworkId,homeworkName,homeworkDescribe,homework_type,start_time,stop_time,completeness,teacher_name from user_homework right join homework h on h.homeworkId = user_homework.homeworkId right join user u on u.usernameId = user_homework.usernameId where user_homework.usernameId = %s"
        data = module.sql_query.sql_query_all(sql, [request.form.get("usernameId")])
        if data is None:
            return json.dumps({
                "status": 1,
                "error": "",
                "data": {}
            })
        data_list = []
        for i in data:
            data_list.append({
                "homeworkId":i[0],
                "homeworkName":i[1],
                "homeworkDescribe": i[2],
                "homework_type": i[3],
                "start_time": i[4],
                "stop_time": i[5],
                "completeness": i[6],
                "teacher_name": i[7]
            })
        return json.dumps({
            "status": 1,
            "error": "",
            "data": data_list
        },cls=ComplexEncoder)

