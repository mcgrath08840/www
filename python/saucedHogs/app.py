from contactinfo import ContactInfo
#from address import Address
#from user import User


me = ContactInfo('jsmith','jsmith@aol.com', '(732)395-1876', '(732)555-5555', '(201)555-5555')
#me.save_to_db('jsmith', '105 Mockingbird Ln', None, 'Detroit', 'MI', '08840')

#me = User("Bob", "Jim", "Smith", 'jsmith', '12345')
me.save_to_db('jsmith','jsmith@aol.com', '(732)395-1876', '(732)555-5555', '(201)555-5555')
#print(me.load_from_db('jsmith'))
#me.delete_from_db('jsmith')
print(me.load_from_db('jsmith'))
#me.delete_from_db('jsmith')
print(me.load_from_db('jsmith'))




