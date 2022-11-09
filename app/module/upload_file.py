import base64
import json
import os
import hashlib
from pathlib import Path

from werkzeug.utils import secure_filename
import module.check_login
from flask import flash, redirect, url_for
ALLOWED_EXTENSIONS = set(['txt','c','cpp','java','py','word'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def upload_file(request, app, SECRET_KEY):
    if request.method == 'POST':
        homeworkId = request.form.get("homeworkId")
        upload_dir = hashlib.md5(homeworkId.encode()).hexdigest()
        ses = request.cookies.get("session") if request.cookies.get("session") is not None else request.form.get("token")
        usernameId = module.check_login.jwt_check(ses, SECRET_KEY)['rights']
        if not Path("./uploads/"+upload_dir).exists():
            os.mkdir("./uploads/"+upload_dir)
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = base64.b64encode(file.filename.encode()).decode().replace("/","-")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'] +"/"+upload_dir + "/", filename))
            return json.dumps(
                {
                    "status": 1,
                    "error": "",
                    "data": "上传成功"
                }
            )
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
