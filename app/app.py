import os
from werkzeug.utils import secure_filename
import requests

from __init__ import init
from flask import *
from flask import Flask
from flask_cors import CORS, cross_origin
app = init()
cors = CORS(app)
SECRET_KEY = os.urandom(24)
host = "0.0.0.0"
port = "9090"

UPLOAD_FOLDER = '.\\uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY
@app.route("/" , methods = ['GET', 'POST'])
def index():
    session['init'] = 1
    if session.get('username') == "guest" or session.get("username") is None:
        return redirect("/login", code=301)
    else:
        return request.cookies.get("session")
@app.route("/login", methods = ['GET', 'POST'])
def login():
    session['init'] = 1
    print(request.form.get("username", default="guest"))
    print(request.form.get("password", default="guest"))
    print(request.cookies.get("session"))
    if session.get('username') == "guest" or session.get("username") is None:
        # 改
        if request.form.get("password",default="guest") == "asd" and request.form.get("username",default="guest") != "asd":
            session["username"] = request.form.get("username",default="guest")
            return request.cookies.get("session")
        return render_template("login.html")
    else:
        return json.dumps({"session":request.cookies.get("session")})


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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




app.run(host=host,port=port)