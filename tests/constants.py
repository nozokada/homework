from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
HOMEWORK_DIR = ROOT_DIR / 'homework'
RESOURCE_DIR = HOMEWORK_DIR / 'resources'
SELENIUM_WEBDRIVER_PATH = RESOURCE_DIR / 'chromedriver'
ALL_BOOKS_FILE_PATH = RESOURCE_DIR / 'all_books.json'

DEMO_QA_URL = 'https://demoqa.com'

SELENIUM_GRID_HUB_URL = 'http://localhost:4444/wd/hub'
SELENIUM_GRID_RUN = False

TEST_USER_PREFIX = 'test_user_'
BAD_PASSWORD = 'badpassword'
SPECIAL_CHARACTERS = '!@#$%^&*'

NEW_ISBNS = ['9780984782802']
EXISTING_ISBNS = ['9781449325862']
INVALID_ISBNS = ['8781449325862']

SELENIUM_WAIT_IN_SEC = 60
