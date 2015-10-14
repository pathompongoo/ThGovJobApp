__author__ = 'gmzo'

from ThGovJobApp import app

@app.route('/')
def index():
    return '<h1>Hello World.</h1>'

