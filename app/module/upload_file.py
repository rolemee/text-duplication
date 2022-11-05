import json
import os
from werkzeug.utils import secure_filename
from flask import flash, redirect, url_for
ALLOWED_EXTENSIONS = set(['txt','c','cpp','java','py','word'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def upload_file(request, app):
    if request.method == 'POST':
        usernameId = request.form.get("homeworkId")
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return json.dumps(
                {
                    "status": 1,
                    "error": "",
                    "data": {"filename":filename}
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
