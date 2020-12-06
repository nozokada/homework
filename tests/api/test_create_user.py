from http import HTTPStatus


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

    def test_create_new_user_with_bad_format(self, account, username_generator, password_generator):
        resp = account.create_user(userName=username_generator(), what=password_generator())
        assert resp.status_code == HTTPStatus.BAD_REQUEST

    def test_create_new_user_with_weak_password(self, account, username_generator):
        username = username_generator()
        password = 'badpassword'
        resp = account.create_user(userName=username, password=password)
        assert resp.status_code == HTTPStatus.BAD_REQUEST
