import os

import requests

import module.check_login
from flask import *
from flask_cors import CORS
from werkzeug.utils import secure_filename
from __init__ import init

import test2.code_diff
import test2.return_string

app = init()
cors = CORS(app)
SECRET_KEY = os.urandom(24)
host = "0.0.0.0"
port = "9090"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route("/login", methods = ['GET', 'POST'])
def login():
    data = json.loads(request.get_data(as_text=True))
    return module.check_login.check_login(data, SECRET_KEY)
@app.route('/a', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
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