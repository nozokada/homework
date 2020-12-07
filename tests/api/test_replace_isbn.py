from http import HTTPStatus

from homework.models.bookstore import Book
from homework.models.bookstore import CodeResponse
from homework.resources.constants import NEW_ISBNS


class TestReplaceISBN:

    def test_replace_isbn(self, bookstore, create_test_user, create_test_books):
        user = create_test_user(teardown=True)
        create_test_books(user_id=user.user_id, teardown=True)
        resp = bookstore.replace_isbn(userId=user.user_id, isbn=NEW_ISBNS[0])
        assert resp.status_code == HTTPStatus.OK
        assert Book(**resp.json())

    def test_replace_isbn_with_bad_format(self, bookstore, create_test_user, create_test_books):
        user = create_test_user(teardown=True)
        create_test_books(user_id=user.user_id, teardown=True)
        resp = bookstore.replace_isbn(userId=user.user_id, what=NEW_ISBNS[0])
        assert resp.status_code == HTTPStatus.BAD_REQUEST
        assert CodeResponse(**resp.json()) == CodeResponse(code='1200', message='UserId and ISBN required.')

    def test_replace_isbn_not_authorized(self, bookstore, create_test_user, create_test_books):
        user = create_test_user(teardown=True)
        create_test_books(user_id=user.user_id, teardown=True)
        token = bookstore.session.headers.pop('Authorization')
        resp = bookstore.replace_isbn(userId=user.user_id, isbn=NEW_ISBNS[0])
        assert resp.status_code == HTTPStatus.UNAUTHORIZED
        assert CodeResponse(**resp.json()) == CodeResponse(code='1200', message='User not authorized!')
        bookstore.session.headers['Authorization'] = token
