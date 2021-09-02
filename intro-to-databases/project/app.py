from database import Database
from user import User

Database.initialise(database="learning", user="postgres", password="password", host="localhost")

user = User('xxxxxxxxxx', 'Jose', 'Lucas')

user.save_to_db()

user_from_db = User.load_from_db_by_email('jose@schoolofcode.me')

print(user_from_db)



