from functools import partial
from http import HTTPStatus

import pytest

from homework.models.bookstore import User


@pytest.fixture
def create_test_books(request, bookstore, logger):
    def _(user_id: str, teardown: bool = False):
        isbns = ['9781449325862']
        collection_of_isbns = [{'isbn': isbn} for isbn in isbns]
        resp = bookstore.add_books(userId=user_id, collectionOfIsbns=collection_of_isbns)
        assert resp.status_code == HTTPStatus.CREATED, 'Failed to create test books'
        if teardown:
            request.addfinalizer(partial(bookstore.delete_books, user_id))
        isbn = resp.json()['isbn']
        return isbn

    return _


@pytest.fixture
def create_test_user(request, account, bookstore, username_generator, password_generator, logger):
    def _(username: str = None, password: str = None, teardown: bool = False) -> User:
        logger.info('Creating test user for %s', request.node.name)
        if not username:
            username = username_generator()
        if not password:
            password = password_generator()
        resp = account.create_user(userName=username, password=password)

        assert resp.status_code == HTTPStatus.CREATED, 'Failed to create test user'
        user_info_dict = resp.json()
        user_info_dict['userId'] = user_info_dict.pop('userID')  # TODO: Dev needs to change userID to userId!!!
        user = User(**user_info_dict)

        resp = account.generate_token(userName=username, password=password)
        token = 'Bearer ' + resp.json()['token']
        account.session.headers['Authorization'] = token
        bookstore.session.headers['Authorization'] = token
        if teardown:
            request.addfinalizer(partial(account.delete_user, user.user_id))
        return user

    return _


@pytest.fixture
def get_test_user(account, logger):
    def _(user_id: str) -> User:
        logger.info('Retrieving test user with id %s', user_id)
        resp = account.get_user(userId=user_id)
        assert resp.status_code == HTTPStatus.OK, 'Failed to retrieve test user'
        user = User(**resp.json())
        return user

    return _