from http import HTTPStatus

from homework.models.bookstore import TokenResponse, MessageResponse
from homework.resources.constants import BAD_PASSWORD


class TestGenerateToken:

    def test_generate_token(self, account, create_test_user, username_generator, password_generator):
        username = username_generator()
        password = password_generator()
        create_test_user(username=username, password=password, teardown=True)
        resp = account.generate_token(userName=username, password=password)
        assert resp.status_code == HTTPStatus.OK

        actual_response = TokenResponse(**resp.json())
        assert actual_response.token
        assert actual_response.expires

        expected_response = TokenResponse(status='Success', result='User authorized successfully.')
        expected_response.token = actual_response.token
        expected_response.expires = actual_response.expires
        assert actual_response == expected_response

    def test_generate_token_bad_password(self, account, create_test_user, username_generator, password_generator):
        username = username_generator()
        create_test_user(username=username, password=password_generator(), teardown=True)
        resp = account.generate_token(userName=username, password=BAD_PASSWORD)
        assert resp.status_code == HTTPStatus.OK
        assert TokenResponse(**resp.json()) == TokenResponse(status='Failed', result='User authorization failed.')

    def test_generate_token_bad_format(self, account, create_test_user, username_generator, password_generator):
        username = username_generator()
        password = password_generator()
        create_test_user(username=username, password=password, teardown=True)
        resp = account.generate_token(userName=username, what=password)
        assert resp.status_code == HTTPStatus.BAD_REQUEST
        assert MessageResponse(code='1200', message='UserName and Password required.')
