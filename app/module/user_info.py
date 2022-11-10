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
        sql = "select h.homeworkId,homeworkName,homeworkDescribe,homework_type,start_time,stop_time,is_Finish from user_homework join homework h on h.homeworkId = user_homework.homeworkId join user u on u.usernameId = user_homework.usernameId where u.usernameId = %s"
        data = module.sql_query.sql_query(sql, [request.form.get("usernameId")])
        if data is None:
            return json.dumps({
                "status": 1,
                "error": "",
                "data": {}
            })
        return json.dumps({
            "status": 1,
            "error": "",
            "data": {
                "homeworkId":data[0],
                "homeworkName":data[1],
                "homeworkDescribe": data[2],
                "homework_type": data[3],
                "start_time": data[4],
                "stop_time": data[5],
                "is_Finish": data[6],
            }
        },cls=ComplexEncoder)
    if rights == 1:
        sql = "select h.homeworkId,homeworkName,homeworkDescribe,homework_type,start_time,stop_time,similarity from user_homework join homework h on h.homeworkId = user_homework.homeworkId join user u on u.usernameId = h.usernameId where h.usernameId = %s"
        data = module.sql_query.sql_query(sql, [request.form.get("usernameId")])
        if data is None:
            return json.dumps({
                "status": 1,
                "error": "",
                "data": {}
            })

        return json.dumps({
            "status": 1,
            "error": "",
            "data": {
                "homeworkId":data[0],
                "homeworkName":data[1],
                "homeworkDescribe": data[2],
                "homework_type": data[3],
                "start_time": data[4],
                "stop_time": data[5],
                "similarity": data[6],
            }
        },cls=ComplexEncoder)


