import json
import os
import module.check_login
import module.upload_file,module.user_info, module.file_operation
from flask import *
from flask_cors import CORS
from __init__ import init
import test2.code_diff
import test2.return_string
from functools import wraps
app = init()
cors = CORS(app ,resources=r'/*')
SECRET_KEY = os.urandom(24)
host = "0.0.0.0"
port = "9090"
def check_login(func):
    @wraps(func)
    def wrapper( *args, **kwargs):
        if request.cookies.get("session") is not None:
            ses = request.cookies.get("session")
        else:
            ses = request.form.get("token")
        print(module.check_login.jwt_check(ses, SECRET_KEY))
        if module.check_login.jwt_check(ses, SECRET_KEY)['account'] != "guest":
            return func(*args,**kwargs)
        else:
            return json.dumps({
                "status": 0,
                "error": "请登录",
                "data": {}
            })
    return wrapper
def check_rights(func):
    @wraps(func)
    def wrapper( *args, **kwargs):
        if request.cookies.get("session") is not None:
            ses = request.cookies.get("session")
        else:
            ses = request.form.get("token")
        print(module.check_login.jwt_check(ses, SECRET_KEY))
        if module.check_login.jwt_check(ses, SECRET_KEY)['rights'] != 0 :
            return func(*args,**kwargs)
        else:
            return json.dumps({
                "status": 0,
                "error": "暂无权限",
                "data": {}
            })
    return wrapper
@app.route("/login", methods = ['GET', 'POST'])
def login():
    data = json.loads(request.get_data(as_text=True))
    return module.check_login.login(data, SECRET_KEY)
@app.route('/upload', methods=['GET', 'POST'])
@check_login
def upload_file():
    return module.upload_file.upload_file(request, app, SECRET_KEY)
@app.route('/userInfo', methods=['GET', 'POST'])
@check_login
def userInfo():
    usernameId = request.form.get("usernameId")
    sql = "select usernameId,name,nickname,r.rights,`describe` from python_homework.user join rights r on r.rights = user.rights where usernameId = %s"
    return module.user_info.get_user_info(sql, [usernameId])
@app.route("/getHomeworkList", methods=['GET', 'POST'])
@check_login
def getHomeworkList():
    rights = module.check_login.jwt_check(request.cookies.get("session"), SECRET_KEY)['rights']
    return module.user_info.get_user_homeworkList(request,rights)
@app.route("/getHomeworkContent", methods=['GET',"POST"])
@check_login
@check_rights
def getHomeworkConntent():
    return module.file_operation.getFile(request)
@app.route("/checkAllHomework", methods=['GET',"POST"])
@check_login
@check_rights
def checkAllHomework():
    return json.dumps({"status": 1,
                       "error": "",
                       "data":  module.file_operation.checkAllHomework(request)})
@app.route("/fileDiff", methods=['GET','POST'])
def fileDiff():
    return module.file_operation.fileDiff(request)




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