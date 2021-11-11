from bottle import run, route, static_file, template, request
from banco import *
@route('/')
def login():
    email = request.forms.get('usuario')
    senha = request.forms.get('senha')
    inserir(email,senha)
    return template('login', email = email)