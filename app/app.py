import json
import os
import module.check_login
import module.upload_file,module.user_info
from flask import *
from flask_cors import CORS
from __init__ import init
import test2.code_diff
import test2.return_string
app = init()
cors = CORS(app)
SECRET_KEY = os.urandom(24)
host = "0.0.0.0"
port = "9090"
def check_login(func):
    def wrapper( *args, **kwargs):
        if module.check_login.jwt_check(request.cookies.get("session"), SECRET_KEY)['account'] != "guest":
            return func(*args,**kwargs)
        else:
            return json.dumps({
                "status": 0,
                "error": "请登录",
                "data": {}
            })
    return wrapper
@app.route("/login", methods = ['GET', 'POST'])
def login():
    data = json.loads(request.get_data(as_text=True))
    return module.check_login.login(data, SECRET_KEY)
@app.route('/upload', methods=['GET', 'POST'])
# @check_login
def upload_file():
    return module.upload_file.upload_file(request, app)
@app.route('/userInfo', methods=['GET', 'POST'])
# @check_login
def userInfo():
    usernameId = request.form.get("usernameId")
    sql = "select usernameId,name,nickname,r.rights,`describe` from python_homework.user join rights r on r.rights = user.rights where usernameId = %s"
    return module.user_info.get_user_info(sql, [usernameId])





@app.route('/testa', methods=['GET', 'POST'])
def testa():
    return json.dumps({"status": 1,
                       "error": "",
                       "data":  test2.code_diff.jplag()})
@app.route('/testb', methods=['GET', 'POST'])
def testb():
    return json.dumps({"status": 1,
                       "error": "",
                       "data": test2.code_diff.sim()})
@app.route('/testc', methods=['GET', 'POST'])
def testc():
    name=request.args.get("filename")
    return render_template_string(test2.return_string.ret(name))
@app.route('/testd', methods=['GET', 'POST'])
def testd():
    file1 = request.args.get("file1")
    file2 = request.args.get("file2")
    name=request.args.get("filename")
    for i in test2.code_diff.sim():
        if i['id1'] == file1 and i['id2'] == file2:
            return {"status": 1,
                       "error": "",
                       "data":  i['matches']}
    return {"status": 0,
                       "error": "no such file",
                       "data":  []}
app.run(host=host,port=port)