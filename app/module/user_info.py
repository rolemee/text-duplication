import json

import module.sql_query

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