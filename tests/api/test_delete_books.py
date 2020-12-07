from http import HTTPStatus

from homework.models.bookstore import CodeResponse


class TestDeleteBooks:

    def test_delete_books(self, bookstore, create_test_user, create_test_books):
        user = create_test_user(teardown=True)
        create_test_books(user_id=user.user_id, teardown=True)
        resp = bookstore.delete_books(userId=user.user_id)
        assert resp.status_code == HTTPStatus.NO_CONTENT
        assert resp.text == ''

    def test_delete_books_not_authorized(self, bookstore, create_test_user, create_test_books):
        user = create_test_user(teardown=True)
        create_test_books(user_id=user.user_id, teardown=True)
        token = bookstore.session.headers.pop('Authorization')
        resp = bookstore.delete_books(userId=user.user_id)
        assert resp.status_code == HTTPStatus.UNAUTHORIZED
        assert CodeResponse(**resp.json()) == CodeResponse(code='1200', message='User not authorized!')
        bookstore.session.headers['Authorization'] = token
