from address import Address
#from user import User


me = Address('jsmith','105 Mockingbird Ln', None, 'Detroit', 'MI', '08840')
#me.save_to_db('jsmith','105 Mockingbird Ln', None, 'Detroit', 'MI', '08840')

#me = User("Bob", "Jim", "Smith", 'jsmith', '12345')
#me.save_to_db("Jim", "Bob", "Smith", 'jsmith', '12345')
#print(me.load_from_db('jsmith'))
#me.delete_from_db('jsmith')
print(me.load_from_db('jsmith'))
me.delete_from_db('jsmith')
print(me.load_from_db('jsmith'))




