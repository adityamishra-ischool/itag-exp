#this file is autorun when you import app package

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
