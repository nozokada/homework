from uplink import Consumer, get, post, Body, delete, Query, put


class Account(Consumer):

    @post('Authorized')
    def login(self, **login_view_model: Body):
        pass

    @post('GenerateToken')
    def generate_token(self, **login_view_model: Body):
        pass

    @post('User')
    def create_user(self, **model: Body):
        pass

    @delete('User/{userId}')
    def delete_user(self, userId):
        pass

    @get('User/{userId}')
    def get_user(self, userId):
        pass


class Bookstore(Consumer):

    @get('Books')
    def get_books(self):
        pass

    @post('Books')
    def add_books(self, **add_list_of_books: Body):
        pass

    @delete('Books')
    def delete_books(self, userId: Query):
        pass

    @get('Book')
    def get_book(self, isbn: Query):
        pass

    @delete('Book')
    def delete_book(self, **string_object: Body):
        pass

    @put('Books/{isbn}')
    def replace_isbn(self, isbn, **replace_isbn: Body):
        pass
