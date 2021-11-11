import sqlite3

try:
  bank = sqlite3.connect('cadastro.db') #Cria o banco e faz a conexão
  print("Conectado com sucesso!")
except Exception:
  print("Não foi possível fazer a conexão!")