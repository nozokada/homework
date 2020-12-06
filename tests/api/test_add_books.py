from http import HTTPStatus


class TestAddBooks:

    def test_add_books(self, create_test_user, bookstore):
        user = create_test_user(teardown=True)
        resp = bookstore.add_books(userId=user.user_id, collectionOfIsbns=[{'isbn': '9780984782802'}])
        assert resp.status_code == HTTPStatus.OK

    def test_add_books_not_authorized(self, create_test_user, bookstore):
        user = create_test_user(teardown=True)
        token = bookstore.session.headers.pop('Authorization')
        resp = bookstore.add_books(userId=user.user_id, collectionOfIsbns=[{'isbn': '9780984782802'}])
        assert resp.status_code == HTTPStatus.UNAUTHORIZED
        bookstore.session.header['Authorization'] = token
