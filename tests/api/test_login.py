from http import HTTPStatus

from homework.models.bookstore import CodeResponse


class TestLogin:

    def test_login(self, account, create_test_user, username_generator, password_generator):
        username = username_generator()
        password = password_generator()
        create_test_user(username=username, password=password, teardown=True)
        resp = account.login(userName=username, password=password)
        assert resp.status_code == HTTPStatus.OK
        assert resp.json() is True

    def test_login_bad_format(self, account, create_test_user, username_generator, password_generator):
        username = username_generator()
        password = password_generator()
        create_test_user(username=username, password=password, teardown=True)
        resp = account.login(userName=username, what=password)
        assert resp.status_code == HTTPStatus.BAD_REQUEST
        assert CodeResponse(**resp.json()) == CodeResponse(code='1200', message='UserName and Password required.')

    def test_login_bad_password(self, account, create_test_user, username_generator, password_generator):
        username = username_generator()
        create_test_user(username=username, password=password_generator(), teardown=True)
        resp = account.login(userName=username, password='badpassword')
        assert resp.status_code == HTTPStatus.NOT_FOUND
        assert CodeResponse(**resp.json()) == CodeResponse(code='1207', message='User not found!')
