import os
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile(config.py)
db = SQLAlchemy(app)

@app.route('/shyam')
def hello():
    return '<div style="color:red">Hello World!</div>'


