import json
import random
import string

import pytest
from selenium import webdriver

from homework.connectors.bookstore import Account
from homework.connectors.bookstore import Bookstore
from homework.resources.constants import SELENIUM_WEBDRIVER_PATH, RESOURCE_DIR, TEST_USER_PREFIX
from homework.utils.logger import LoggerWrapper


@pytest.fixture(scope='session')
def logger():
    return LoggerWrapper()


@pytest.fixture
def account(logger, json_loader):
    logger.debug('Initializing Account connector')
    return Account(base_url='https://demoqa.com/Account/v1/')


@pytest.fixture
def bookstore(logger):
    logger.debug('Initializing Bookstore connector')
    return Bookstore(base_url='https://demoqa.com/Bookstore/v1/')


@pytest.fixture
def selenium_webdriver(request, logger):
    logger.debug('Initializing Selenium driver')
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=SELENIUM_WEBDRIVER_PATH, options=options)
    yield driver

    screenshot_path = str(RESOURCE_DIR / f'{request.node.name}.png')
    driver.save_screenshot(filename=screenshot_path)
    driver.quit()


@pytest.fixture
def username_generator(logger):
    def _(prefix: str = TEST_USER_PREFIX, length: int = 8):
        choices = string.ascii_letters + string.digits
        username = ''.join(random.choices(choices, k=length))
        username = f'{prefix}{username}'
        logger.debug('Generated username %s', username)
        return username

    return _


@pytest.fixture
def password_generator(logger):
    def _(length: int = 24):
        all_character_set = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits
        rand_upper = random.choices(string.ascii_uppercase)
        rand_lower = random.choices(string.ascii_lowercase)
        rand_symbol = random.choices(string.punctuation)
        rand_digit = random.choices(string.digits)

        password = rand_upper + rand_lower + rand_symbol + rand_digit

        for i in range(length - 4):
            password += random.choices(all_character_set)
            random.shuffle(password)

        password = ''.join(password)
        logger.debug('Generated password %s', password)
        return password

    return _


@pytest.fixture
def json_loader(logger):
    def _(path: str):
        logger.debug('Loading JSON content from %s', path)
        with open(path) as file:
            content = json.load(file)
        return content

    return _