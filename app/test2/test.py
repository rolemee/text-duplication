import jwt
import datetime

dic = {
    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
    'iss': 'ChaosMoor',                 #  签名
    'data': {                           #  内容，一般存放该用户id和开始时间
        'a': 1,
        'b': 2,
    },
}


token = jwt.encode(dic, 'secret', algorithm='HS256')                            # 加密生成字符串
print(token)

payload = jwt.decode(token, 'secret', algorithms=['HS256'])  # 解密，校验签名

print(payload)
# print(s)
# print(type(s))