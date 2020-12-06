from http import HTTPStatus

from homework.models.bookstore import Book


class TestGetBook:

    def test_get_book(self, bookstore):
        resp = bookstore.get_book(isbn='9781449325862')
        assert resp.status_code == HTTPStatus.OK
        assert Book(**resp.json())

    def test_get_non_existent_book(self, bookstore):
        resp = bookstore.get_book(isbn='invalid_isbn')
        assert resp.status_code == HTTPStatus.NOT_FOUND
