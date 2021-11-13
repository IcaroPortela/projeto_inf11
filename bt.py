from bottle import run, route, template, request
from banco import *

h = "localhost" #"0.0.0.0" no replit.
p = 8080 #1234 no replit
v = True

@route('/')
def home():
    return template('home')

@route('/login')
def login():
    return template('login')

@route('/login', method="post")
def cadastrar():
    id = request.forms.get('id')
    nome = request.forms.get('Nome')
    email = request.forms.get('e-mail')
    fone = request.forms.get('fone')
    senha = request.forms.get('senha')
    cSenha = request.forms.get('ctrl-senha')
    id = id
    nome = str(nome)
    email = str(email)
    fone = fone
    senha = str(senha)
    cSenha = str(cSenha)
    inserir(id, nome, email, fone, senha, cSenha)
    return template('login', email = email)

@route('/login#login', method="post")
def aft_cad():
    s = request.forms.get('senha')
    if s == request.forms.get('cSenha'):
        return template('home')
    else:
        return "<script>alert('Senha incorreta')</script>"
if __name__ == '__main__':   
    run(host = h,port = p, debug = v, reloader=v)