import os
from flask import Flask
from parse_rest.connection import register
from flask import request
from flask import render_template

#register(jNs7bIRWAuvgY3EZMoRkrUyNus3708XOBjGftpzL, NxmOSAToOGSAtnpLzrrsQJT5z83TnsEBULjE0rHP);

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	 username = request.cookies.get('username');
	 isLoggedIn = request.cookies.get('isLoggedIn');
	 if username and not usename.isspace() and isLoggedIn and not isLoggedIn.isspace():
	 	return render_template('index.html')
	 else: 
		 return render_template('login.html') 

@app.route('/login',methods=['POST'])
def login():
	return "200"

