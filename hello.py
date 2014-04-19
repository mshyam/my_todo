import os
from flask import Flask

app = Flask(__name__)

@app.route('/shyam')
def hello():
    return '<div style="color:red">Hello World!</div>'


