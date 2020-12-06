from http import HTTPStatus


class TestDeleteBook:

    def test_delete_book(self, bookstore, create_test_user, create_test_books):
        user = create_test_user(teardown=True)
        isbn = create_test_books(user_id=user.user_id, teardown=True)
        resp = bookstore.delete_book(isbn=isbn, userId=user.user_id)
        assert resp.status_code == HTTPStatus.NO_CONTENT

    def test_delete_book_not_authorized(self, bookstore, create_test_user, create_test_books):
        user = create_test_user(teardown=True)
        isbn = create_test_books(user_id=user.user_id, teardown=True)
        token = bookstore.session.headers.pop('Authorization')
        resp = bookstore.delete_book(isbn=isbn, userId=user.user_id)
        assert resp.status_code == HTTPStatus.UNAUTHORIZED
        bookstore.session.headers['Authorization'] = token
