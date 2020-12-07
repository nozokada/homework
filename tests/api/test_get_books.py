from http import HTTPStatus

from homework.models.bookstore import Book
from homework.resources.constants import ALL_BOOKS_FILE_PATH


class TestGetBooks:

    def test_get_books(self, bookstore, json_loader):
        resp = bookstore.get_books()
        assert resp.status_code == HTTPStatus.OK
        actual_books = [Book(**book) for book in resp.json()['books']]
        expected_books = [Book(**book) for book in json_loader(ALL_BOOKS_FILE_PATH)['books']]
        assert actual_books == expected_books
