from database import Database
from user import User

Database.initialise(user='postgres', password='odin1', database='learning', host='localhost')

my_user = User('william08840@yahoo.com', 'William', 'Sauce', None)
my_user.save_to_db()

my_user = User.load_from_db_by_email('william08840@yahoo.com')

print(my_user)
print('My User Infor: {}, {}, {}'.format(my_user.first_name, my_user.last_name, my_user.id) )





