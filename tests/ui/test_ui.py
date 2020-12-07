class TestUI:

    def test_login(self, selenium_webdriver, create_test_user, username_generator, password_generator, login_with_ui):
        username = username_generator()
        password = password_generator()
        create_test_user(username=username, password=password, teardown=True)
        login_with_ui(username=username, password=password)
        username_label = selenium_webdriver.find_element_by_id('userName-value')
        assert username_label.text == username

    def test_login_fail(
        self, selenium_webdriver, create_test_user, username_generator, password_generator, login_with_ui
    ):
        username = username_generator()
        create_test_user(username=username, password=password_generator(), teardown=True)
        login_with_ui(username=username, password='badpassword')
        output = selenium_webdriver.find_element_by_id('output')
        assert output.text == 'Invalid username or password!'
