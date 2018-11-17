from database import CursorFromConnectionFromPool


class User:
    def __init__(self, first_name, middle_name, last_name, login, password, id = 1):  # Needed to specify all elements I wanted to return.
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.id = id
        self.login = login
        self.password = password



    def __repr__(self):  # This prints out results
        return "<User {} {} {} {}>".format(self.first_name, self.middle_name, self.last_name, self.id)

    def save_to_db(self, first_name, middle_name, last_name, login, password):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('INSERT INTO dbo.t_customer (first_name, middle_name, last_name, login, password) VALUES (%s, %s, %s, %s, %s)',
                           (first_name, middle_name, last_name, login, password))

    def delete_from_db(self, login):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('DELETE FROM dbo.t_customer where login = \'{}\''.format(login))

    @classmethod   # Needed to be class method.
    def load_from_db(cls, login):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM dbo.t_customer where login = \'{}\''.format(login))
            user_data = cursor.fetchone()
            if user_data:
                return cls(first_name=user_data[1], middle_name=user_data[2], last_name=user_data[3], login=user_data[4], password=user_data[5], id=user_data[0] )

