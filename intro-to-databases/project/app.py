from user import user

my_user = user('jose@hotmail.com', 'Matheus', 'Marcos', None)
print(my_user)

my_user.save_to_db()



