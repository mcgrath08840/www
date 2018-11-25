from database import CursorFromConnectionFromPool


class ContactInfo:
    def __init__(self, login, email, home_phone, mobile_phone, fax_number, id=None):  # Needed to specify all elements I wanted to return.
        self.login = login
        self.email = email
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.fax_number = fax_number
        self.id = id

    def __repr__(self):  # This prints out results
        return "<User Contact Info: {} {} {} {}>".format(self.email, self.home_phone, self.mobile_phone, self.fax_number)

    def save_to_db(self, login, email, home_phone, mobile_phone, fax_number):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('INSERT INTO dbo.t_contact_info (contact_id, email, home_phone, mobile_phone, fax_number) VALUES ((select customer_id from dbo.t_customer where login = %s), %s, %s, %s, %s)',
                           (login, email, home_phone, mobile_phone, fax_number))

    def delete_from_db(self, login):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('DELETE FROM dbo.t_contact_info where contact_id = (select customer_id from dbo.t_customer where login = \'{}\')'.format(login))

    @classmethod   # Needed to be class method.
    def load_from_db(cls, login):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM dbo.t_contact_info where contact_id = (select customer_id from dbo.t_customer where login = \'{}\')'.format(login))
            user_data = cursor.fetchone()
            if user_data:
                return cls(login, email=user_data[1], home_phone=user_data[2], mobile_phone=user_data[3], fax_number=user_data[4], id=user_data[0])

