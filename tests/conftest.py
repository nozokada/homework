from functools import partial
from http import HTTPStatus

import pytest

from homework.models.bookstore import ISBNResponse
from homework.models.bookstore import User
from tests.constants import DEMO_QA_URL
from tests.constants import NEW_ISBNS


@pytest.fixture
def create_test_books(request, bookstore, logger):
    def _(user_id: str, teardown: bool = False) -> ISBNResponse:
        collection_of_isbns = [{'isbn': isbn} for isbn in NEW_ISBNS]
        resp = bookstore.create_books(userId=user_id, collectionOfIsbns=collection_of_isbns)
        assert resp.status_code == HTTPStatus.CREATED, f'Failed to create test books with ISBNs {NEW_ISBNS}'
        isbn = ISBNResponse(**resp.json())
        if teardown:
            request.addfinalizer(partial(bookstore.delete_books, user_id))
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

        assert resp.status_code == HTTPStatus.CREATED, f'Failed to create test user with username {username}'
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
        assert resp.status_code == HTTPStatus.OK, f'Failed to retrieve test user with user id {user_id}'
        user = User(**resp.json())
        return user

    return _


@pytest.fixture
def login_with_ui(selenium_webdriver, create_test_user, username_generator, password_generator):
    def _(username: str, password: str):
        selenium_webdriver.get(f'{DEMO_QA_URL}/login')
        username_field = selenium_webdriver.find_element_by_id('userName')
        password_field = selenium_webdriver.find_element_by_id('password')
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button = selenium_webdriver.find_element_by_id('login')
        login_button.click()

    return _


@pytest.fixture
def get_book_title_and_link(selenium_webdriver):
    def _(at: int):
        selenium_webdriver.get(f'{DEMO_QA_URL}/books')
        book_rows = selenium_webdriver.find_elements_by_xpath("//div[@class='rt-tbody']//div[@class='rt-tr-group']")
        book_link = book_rows[at].find_element_by_xpath("//div[@class='action-buttons']/span/a")
        return book_link.text, book_link

    return _
