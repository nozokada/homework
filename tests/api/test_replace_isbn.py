from http import HTTPStatus


class TestReplaceISBN:

    def test_replace_isbn(self, bookstore, create_test_user, create_test_books):
        user = create_test_user(teardown=True)
        create_test_books(user_id=user.user_id, teardown=True)
        new_isbn = '1234567890123'
        resp = bookstore.replace_isbn(userId=user.user_id, isbn=new_isbn)
        assert resp.status_code == HTTPStatus.OK

    def test_replace_isbn_not_authorized(self, bookstore, create_test_user, create_test_books):
        user = create_test_user(teardown=True)
        create_test_books(user_id=user.user_id, teardown=True)
        new_isbn = '1234567890123'
        token = bookstore.session.headers.pop('Authorization')
        resp = bookstore.replace_isbn(userId=user.user_id, isbn=new_isbn)
        assert resp.status_code == HTTPStatus.OK
        bookstore.session.headers['Authorization'] = token
