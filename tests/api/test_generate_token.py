from http import HTTPStatus


class TestGenerateToken:

    def test_generate_token(self, account, create_test_user, username_generator, password_generator):
        username = username_generator()
        password = password_generator()
        create_test_user(username=username, password=password, teardown=True)
        resp = account.generate_token(userName=username, password=password)
        assert resp.status_code == HTTPStatus.OK

    def test_generate_token_bad_format(self, account, create_test_user, username_generator, password_generator):
        username = username_generator()
        password = password_generator()
        create_test_user(username=username, password=password, teardown=True)
        resp = account.generate_token(userName=username, what=password)
        assert resp.status_code == HTTPStatus.BAD_REQUEST

    def test_generate_token_bad_password(self, account, create_test_user, username_generator, password_generator):
        username = username_generator()
        create_test_user(username=username, password=password_generator(), teardown=True)
        resp = account.generate_token(userName=username, password='badpassword')
        assert resp.status_code == HTTPStatus.OK
