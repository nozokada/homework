from http import HTTPStatus

from homework.models.bookstore import Book, MessageResponse
from tests.constants import INVALID_ISBNS
from tests.constants import EXISTING_ISBNS


class TestGetBook:

    def test_get_book(self, bookstore):
        resp = bookstore.get_book(isbn=EXISTING_ISBNS[0])
        assert resp.status_code == HTTPStatus.OK
        assert Book(**resp.json())

    def test_get_nonexistent_book(self, bookstore):
        resp = bookstore.get_book(isbn=INVALID_ISBNS[0])
        assert resp.status_code == HTTPStatus.NOT_FOUND
        assert MessageResponse(**resp.json()) == MessageResponse(code='1207', message='Book not found!')
