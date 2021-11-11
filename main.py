from bottle import Bottle, run, \
     template, debug, static_file
from modulos.banco import *

#import os, sys

#dirname = os.path.dirname(sys.argv[0])

app = Bottle()
debug(True)

@app.route('/templates/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='/Projeto_INF11/templates/css')

"""@app.route('/static/<filename:re:.*\.js>')
def send_js(filename):
    return static_file(filename, root=dirname+'/static/asset/js')
"""
@app.route('/')
def index():
    return template('home')

run(app, host='0.0.0.0', port = 1234, reloader=True, debug=True)