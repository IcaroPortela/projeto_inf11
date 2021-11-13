import sqlite3

try:
    banco = sqlite3.connect('meubanco.db') # cria e conecta com o banco
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
    cursor.fetchall()

def inserir(id, nome, email, telefone, senha, c_senha):
    try:
        banco = sqlite3.connect('meubanco.db')
        cursor = banco.cursor()
        cursor.execute("insert into cadastro values(?,?,?,?,?,?)",(id, nome, email, telefone, senha, c_senha))
        for row in cursor.execute('select * from cadastro'):
            print(row)
    except:
        print(cursor.fetchall())
        print("Não foram inseridos valores no banco")

#inserir(1,'icaro portela','ip@gmail.com',81982238756,'1234','1234')
