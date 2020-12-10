from tests.constants import DEMO_QA_URL


class TestUIProfile:

    def test_profile(self, selenium_webdriver, create_test_user, username_generator, password_generator, login_with_ui):
        username = username_generator()
        password = password_generator()
        create_test_user(username=username, password=password, teardown=True)
        login_with_ui(username=username, password=password)
        username_label = selenium_webdriver.find_element_by_id("userName-value")
        assert username_label.text == username

    def test_profile_not_logged_in(self, selenium_webdriver):
        selenium_webdriver.get(f'{DEMO_QA_URL}/profile')
        not_logged_in_label = selenium_webdriver.find_element_by_id("notLoggin-label")
        assert not_logged_in_label.text == 'Currently you are not logged into the Book Store application, ' \
                                           'please visit the login page to enter or register page to register yourself.'
