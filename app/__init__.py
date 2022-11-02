from flask import Flask, render_template,request


def init():
    app = Flask(__name__, template_folder='./templates', static_folder='./static', static_url_path='')
    return app