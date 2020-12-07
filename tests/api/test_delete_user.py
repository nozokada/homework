from http import HTTPStatus

from homework.models.bookstore import CodeResponse


class TestDeleteUser:

    def test_delete_user(self, account, create_test_user):
        user = create_test_user()
        resp = account.delete_user(userId=user.user_id)
        assert resp.status_code == HTTPStatus.NO_CONTENT
        assert resp.text == ''

    def test_delete_nonexistent_user(self, account, create_test_user):
        create_test_user(teardown=True)
        resp = account.delete_user(userId='invalid_user_id')
        assert resp.status_code == HTTPStatus.OK
        assert CodeResponse(code='1207', message='User Id not correct!')

    def test_delete_user_not_authorized(self, account, create_test_user):
        user = create_test_user(teardown=True)
        token = account.session.headers.pop('Authorization')
        resp = account.delete_user(userId=user.user_id)
        assert resp.status_code == HTTPStatus.UNAUTHORIZED
        assert CodeResponse(code='1200', message='User not authorized!')
        account.session.headers['Authorization'] = token
