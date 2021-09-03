from database import Database
from user import User

Database.initialise(database="learning", user="postgres", password="password", host="localhost") # inicializa o bando de dados.

user = User('email_teste@teste.com.br', 'Joao', 'Pedro') # input que sera dado para a tabela.

user.save_to_db() #salvar

user_from_db = User.load_from_db_by_email('email_teste@teste.com.br')

print(user_from_db)



