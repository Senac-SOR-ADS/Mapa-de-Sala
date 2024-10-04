#coding:utf-8
from flask import Flask, session
from datetime import timedelta
from os import urandom

app = Flask(__name__)

app.secret_key = urandom(12)

app.permanent_session_lifetime = timedelta(minutes=10)
app.session_refresh_each_request = True

from App.controllers import routes
