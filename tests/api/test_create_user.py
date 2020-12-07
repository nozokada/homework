from http import HTTPStatus

from homework.models.bookstore import MessageResponse
from homework.resources.constants import BAD_PASSWORD


class TestCreateUser:

    def test_create_new_user(self, create_test_user, get_test_user):
        user = create_test_user(teardown=True)
        created_user = get_test_user(user_id=user.user_id)
        assert user == created_user

    def test_create_existing_user(self, account, create_test_user, username_generator, password_generator):
        username = username_generator()
        password = password_generator()
        create_test_user(username=username, password=password, teardown=True)
        resp = account.create_user(userName=username, password=password)
        assert resp.status_code == HTTPStatus.NOT_ACCEPTABLE
        assert MessageResponse(**resp.json()) == MessageResponse(code='1204', message='User exists!')

    def test_create_new_user_with_bad_format(self, account, username_generator, password_generator):
        resp = account.create_user(userName=username_generator(), what=password_generator())
        assert resp.status_code == HTTPStatus.BAD_REQUEST
        assert MessageResponse(**resp.json()) == MessageResponse(code='1200', message='UserName and Password required.')

    def test_create_new_user_with_weak_password(self, account, username_generator):
        resp = account.create_user(userName=username_generator(), password=BAD_PASSWORD)
        assert resp.status_code == HTTPStatus.BAD_REQUEST
        assert MessageResponse(**resp.json()) == MessageResponse(
            code='1300',
            message='Passwords must have at least one non alphanumeric character, '
                    'one digit (\'0\'-\'9\'), one uppercase (\'A\'-\'Z\'), '
                    'one lowercase (\'a\'-\'z\'), '
                    'one special character '
                    'and Password must be eight characters or longer.'
        )
