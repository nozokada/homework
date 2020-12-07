from http import HTTPStatus

from homework.models.bookstore import CodeResponse
from homework.resources.constants import TEST_ISBNS


class TestCreateBooks:

    def test_create_books(self, create_test_user, create_test_books):
        user = create_test_user(teardown=True)
        create_test_books(user_id=user.user_id, teardown=True)

    def test_create_books_not_authorized(self, create_test_user, bookstore):
        user = create_test_user(teardown=True)
        token = bookstore.session.headers.pop('Authorization')
        collection_of_isbns = [{'isbn': isbn} for isbn in TEST_ISBNS]
        resp = bookstore.add_books(userId=user.user_id, collectionOfIsbns=collection_of_isbns)
        assert resp.status_code == HTTPStatus.UNAUTHORIZED
        assert CodeResponse(**resp.json()) == CodeResponse(code='1200', message='User not authorized!')
        bookstore.session.headers['Authorization'] = token
