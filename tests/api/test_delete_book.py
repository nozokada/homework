from http import HTTPStatus

from homework.models.bookstore import CodeResponse
from homework.resources.constants import INVALID_ISBNS


class TestDeleteBook:

    def test_delete_book(self, bookstore, create_test_user, create_test_books):
        user = create_test_user(teardown=True)
        isbn_resp = create_test_books(user_id=user.user_id, teardown=True)
        resp = bookstore.delete_book(isbn=isbn_resp.isbn, userId=user.user_id)
        assert resp.status_code == HTTPStatus.NO_CONTENT
        assert resp.text == ''

    def test_delete_nonexistent_book(self, bookstore, create_test_user):
        user = create_test_user(teardown=True)
        resp = bookstore.delete_book(isbn=INVALID_ISBNS[0], userId=user.user_id)
        assert resp.status_code == HTTPStatus.NOT_FOUND
        assert CodeResponse(**resp.json()) == CodeResponse(code='1207', message='Book not found!')

    def test_delete_book_not_authorized(self, bookstore, create_test_user, create_test_books):
        user = create_test_user(teardown=True)
        isbn_resp = create_test_books(user_id=user.user_id, teardown=True)
        token = bookstore.session.headers.pop('Authorization')
        resp = bookstore.delete_book(isbn=isbn_resp.isbn, userId=user.user_id)
        assert resp.status_code == HTTPStatus.UNAUTHORIZED
        assert CodeResponse(**resp.json()) == CodeResponse(code='1200', message='User not authorized!')
        bookstore.session.headers['Authorization'] = token
