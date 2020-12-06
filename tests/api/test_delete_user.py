from http import HTTPStatus


class TestDeleteUser:

    def test_delete_user(self, account, create_test_user):
        user = create_test_user()
        resp = account.delete_user(userId=user.user_id)
        assert resp.status_code == HTTPStatus.NO_CONTENT

    def test_delete_nonexistent_user(self, account, create_test_user):
        create_test_user(teardown=True)
        resp = account.delete_user(userId='invalid_user_id')
        assert resp.status_code == HTTPStatus.OK

    def test_delete_user_not_authorized(self, account, create_test_user):
        user = create_test_user(teardown=True)
        token = account.session.headers.pop('Authorization')
        resp = account.delete_user(userId=user.user_id)
        assert resp.status_code == HTTPStatus.UNAUTHORIZED
        account.session.headers['Authorization'] = token
