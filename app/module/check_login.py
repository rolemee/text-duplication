import json
import jwt

dic = {
    'iss': 'ChaosMoor',  # 签名
    'data': {  # 内容，一般存放该用户id和开始时间
        'account': "guest",
    },
}


def check_login(data, SECRET_KEY):
    if data.get("account") and data.get("password"):
        if True:
            dic['data']['account'] = data.get("account")
            return json.dumps({
                "status": 1,
                "error": "",
                "data": {
                    "session": jwt.encode(dic, SECRET_KEY, algorithm='HS256')
                }
            })
        else:
            return json.dumps({"error": "0"})
    else:
        return "33"
