# coding=utf-8
from flask import Flask
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config.update(dict(
    UPLOAD_FOLDER=UPLOAD_FOLDER,
    DATABASE=os.path.join(app.root_path, 'blog.db'),
    DEBUG=True,
    SECRET_KEY='default',
    USERNAME='admin',
    PASSWORD='default'
))

app.config.from_envvar('PLOG_SETTINGS', silent=True)
import src.blog

