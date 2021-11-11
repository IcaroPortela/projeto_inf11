import sqlite3

try:
    banco = sqlite3.connect('meubanco.db') // cria e conecta com o banco
    print("Conexão bem sucedida!")
except Exception:
    print("Erro banco não criado")

try:
    banco = sqlite3.connect('meubanco.db')
    cursor = banco.cursor()
    cursor.execute("""
        create table cadastro(
            id integer primary key,
            nome text,
            email text,
            telefone integer,
            senha text,
            con_senha text
        );
    """)
except Exception:
    print("Erro! Não foi possível cadastra!")

def inserir(email,senha):
    banco = sqlite3.connect('meubanco.db')
    cursor = banco.cursor()
    cursor.execute("""
        insert into cadastro value(?,?)
    """,email,senha)