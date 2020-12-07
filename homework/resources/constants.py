from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent
HOMEWORK_DIR = Path(__file__).parent.parent
RESOURCE_DIR = HOMEWORK_DIR / 'resources'
SELENIUM_WEBDRIVER_PATH = '/Users/nokada/Downloads/chromedriver'
ALL_BOOKS_FILE_PATH = RESOURCE_DIR / 'all_books.json'

DEMO_QA_URL = 'https://demoqa.com'

TEST_USER_PREFIX = 'test_user_'

NEW_ISBNS = ['9780984782802']
EXISTING_ISBNS = ['9781449325862']
INVALID_ISBNS = ['8781449325862']
