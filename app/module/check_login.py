import json
import jwt
import module.sql_query
dic = {
    'iss': 'Rolemee',  # 签名
    'data': {  # 内容，一般存放该用户id和开始时间
        'account': "guest",
        'rights' : "0",
    },
}
def jwt_check(session,SECRET_KEY):
    print(jwt.decode(session, SECRET_KEY, algorithms=['HS256']))
    try:
        return jwt.decode(session, SECRET_KEY, algorithms=['HS256'])['data']
    except:
        return {'account':'guest'}


def login(data, SECRET_KEY):
    if data.get("account") and data.get("password"):
        sql = "select usernameId,password,a.rights,`describe` from python_homework.user a join rights r on r.rights = a.rights where usernameId = %s and password = %s"
        res = module.sql_query.sql_query(sql,[data.get("account"),data.get("password")])
        if res is not None:
            dic['data']['account'] = data.get("account")
            dic['data']['rights'] = res[2]
            print(dic)
            return json.dumps({
                "status": 1,
                "error": "",
                "data": {
                    "session": jwt.encode(dic, SECRET_KEY, algorithm='HS256')
                }
            })
        else:
            return json.dumps({
                "status": 0,
                "error": "账号或密码错误",
                "data": {}
            })
    else:
        return json.dumps({
                "status": 0,
                "error": "参数丢失",
                "data": {}
            })
