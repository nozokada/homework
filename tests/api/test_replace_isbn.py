from http import HTTPStatus

from homework.models.bookstore import Book
from homework.models.bookstore import MessageResponse
from tests.constants import NEW_ISBNS
from homework.utils.deauthorizer import Deauthorizer


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
        assert MessageResponse(**resp.json()) == MessageResponse(code='1200', message='UserId and ISBN required.')

    def test_replace_isbn_not_authorized(self, bookstore, create_test_user, create_test_books):
        user = create_test_user(teardown=True)
        create_test_books(user_id=user.user_id, teardown=True)
        with Deauthorizer(bookstore):
            resp = bookstore.replace_isbn(userId=user.user_id, isbn=NEW_ISBNS[0])
        assert resp.status_code == HTTPStatus.UNAUTHORIZED
        assert MessageResponse(**resp.json()) == MessageResponse(code='1200', message='User not authorized!')
