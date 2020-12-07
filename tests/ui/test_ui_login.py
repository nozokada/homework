from homework.resources.constants import BAD_PASSWORD


class TestUILogin:

    def test_login(self, selenium_webdriver, create_test_user, username_generator, password_generator, login_with_ui):
        username = username_generator()
        password = password_generator()
        create_test_user(username=username, password=password, teardown=True)
        login_with_ui(username=username, password=password)
        username_label = selenium_webdriver.find_element_by_id("userName-value")
        assert username_label.text == username

    def test_login_with_bad_password(
        self, selenium_webdriver, create_test_user, username_generator, password_generator, login_with_ui
    ):
        username = username_generator()
        create_test_user(username=username, password=password_generator(), teardown=True)
        login_with_ui(username=username, password=BAD_PASSWORD)
        output = selenium_webdriver.find_element_by_id("output")
        assert output.text == 'Invalid username or password!'

    def test_logout(self, selenium_webdriver, create_test_user, login_with_ui, username_generator, password_generator):
        username = username_generator()
        password = password_generator()
        create_test_user(username=username, password=password, teardown=True)
        login_with_ui(username=username, password=password)
        username_label = selenium_webdriver.find_element_by_id("userName-value")
        assert username_label.text == username

        logout_button = selenium_webdriver.find_element_by_xpath("//button[contains(text(), 'Log out')]")
        logout_button.click()
        login_button = selenium_webdriver.find_element_by_id("login")
        assert login_button.text == 'Login'
