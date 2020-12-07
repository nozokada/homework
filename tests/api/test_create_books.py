from http import HTTPStatus

from homework.models.bookstore import MessageResponse
from homework.resources.constants import EXISTING_ISBNS
from homework.utils.deauthorizer import Deauthorizer


class TestCreateBooks:

    def test_create_books(self, create_test_user, create_test_books):
        user = create_test_user(teardown=True)
        create_test_books(user_id=user.user_id, teardown=True)

    def test_create_books_with_bad_format(self, bookstore, create_test_user):
        user = create_test_user(teardown=True)
        collection_of_isbns = [{'isbn': isbn} for isbn in EXISTING_ISBNS]
        resp = bookstore.create_books(userId=user.user_id, what=collection_of_isbns)
        assert resp.status_code == HTTPStatus.BAD_REQUEST
        assert MessageResponse(code='1200', message='UserID and Collection of ISBNs required.')

    def test_create_books_not_authorized(self, bookstore, create_test_user):
        user = create_test_user(teardown=True)
        collection_of_isbns = [{'isbn': isbn} for isbn in EXISTING_ISBNS]
        with Deauthorizer(bookstore):
            resp = bookstore.create_books(userId=user.user_id, collectionOfIsbns=collection_of_isbns)
        assert resp.status_code == HTTPStatus.UNAUTHORIZED
        assert MessageResponse(**resp.json()) == MessageResponse(code='1200', message='User not authorized!')
