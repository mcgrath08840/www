from database import CursorFromConnectionFromPool


class Address:
    def __init__(self, login, street_address_1, street_address_2, city, state, zip_code, id=None):  # Needed to specify all elements I wanted to return.
        self.login = login
        self.street_address_1 = street_address_1
        self.street_address_2 = street_address_2
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.id = id

    def __repr__(self):  # This prints out results
        return "<User Address: {} {} {} {}>".format(self.street_address_1, self.street_address_2, self.city, self.zip_code)

    def save_to_db(self, login, street_address_1, street_address_2, city, state, zip_code):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('INSERT INTO dbo.t_address (address_id, street_address_1, street_address_2, city, state, zip_code) VALUES ((select customer_id from dbo.t_customer where login = %s), %s, %s, %s, %s, %s)',
                           (login, street_address_1, street_address_2, city, state, zip_code))

    def delete_from_db(self, login):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('DELETE FROM dbo.t_address where address_id = (select customer_id from dbo.t_customer where login = \'{}\')'.format(login))

    @classmethod   # Needed to be class method.
    def load_from_db(cls, login):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM dbo.t_address where address_id = (select customer_id from dbo.t_customer where login = \'{}\')'.format(login))
            user_data = cursor.fetchone()
            if user_data:
                return cls(login, street_address_1=user_data[1], street_address_2=user_data[2], city=user_data[3], state=user_data[4], zip_code=user_data[5], id=user_data[0])

