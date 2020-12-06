from http import HTTPStatus


class TestGetUser:

    def test_get_user(self, account, create_test_user):
        user = create_test_user(teardown=True)
        resp = account.get_user(userId=user.user_id)
        assert resp.status_code == HTTPStatus.OK

    def test_get_other_user(self, account, create_test_user):
        create_test_user(teardown=True)
        resp = account.get_user(userId='other_user_id')
        assert resp.status_code == HTTPStatus.UNAUTHORIZED

    def test_get_user_not_authorized(self, account, create_test_user):
        user = create_test_user(teardown=True)
        token = account.session.headers.pop('Authorization')
        resp = account.get_user(userId=user.user_id)
        assert resp.status_code == HTTPStatus.UNAUTHORIZED
        account.session.headers['Authorization'] = token
