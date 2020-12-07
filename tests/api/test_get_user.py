from http import HTTPStatus

from homework.models.bookstore import MessageResponse


class TestGetUser:

    def test_get_user(self, create_test_user, get_test_user):
        user = create_test_user(teardown=True)
        created_user = get_test_user(user_id=user.user_id)
        assert user == created_user

    def test_get_other_user(self, account, create_test_user, user_id_generator):
        create_test_user(teardown=True)
        resp = account.get_user(userId=user_id_generator())
        assert resp.status_code == HTTPStatus.UNAUTHORIZED
        assert MessageResponse(**resp.json()) == MessageResponse(code='1207', message='User not found!')

    def test_get_user_not_authorized(self, account, create_test_user):
        user = create_test_user(teardown=True)
        token = account.session.headers.pop('Authorization')
        resp = account.get_user(userId=user.user_id)
        assert resp.status_code == HTTPStatus.UNAUTHORIZED
        assert MessageResponse(**resp.json()) == MessageResponse(code='1200', message='User not authorized!')
        account.session.headers['Authorization'] = token
