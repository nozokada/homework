import pytest

from tests.constants import DEMO_QA_URL


class TestUIBookstore:

    @pytest.mark.parametrize('book_at', [0, 2, 5])
    def test_filter_books(self, selenium_webdriver, get_book_title_and_link, book_at):
        expected_book_title, book_link = get_book_title_and_link(at=book_at)
        search_textbox = selenium_webdriver.find_element_by_id("searchBox")
        search_textbox.send_keys(expected_book_title)
        book_title, _ = get_book_title_and_link(at=0)
        assert expected_book_title == book_title

    @pytest.mark.parametrize('book_at', [1, 3, 4])
    def test_load_book(self, selenium_webdriver, get_book_title_and_link, book_at):
        expected_book_title, book_link = get_book_title_and_link(at=book_at)
        book_link.click()
        book_title = selenium_webdriver.find_element_by_xpath(
            "//div[@id='title-wrapper']//label[@id='userName-value']"
        ).text
        assert expected_book_title == book_title

    @pytest.mark.parametrize('page_size', [5, 10, 20, 25, 50, 100])
    def test_num_of_book_rows(self, selenium_webdriver, page_size):
        selenium_webdriver.get(f'{DEMO_QA_URL}/books')
        page_size_selector = selenium_webdriver.find_element_by_xpath(
            "//span[@class='select-wrap -pageSizeOptions']/select"
        )
        for option in page_size_selector.find_elements_by_tag_name("option"):
            if option.get_attribute('value') == str(page_size):
                option.click()
                break
        book_rows = selenium_webdriver.find_elements_by_xpath("//div[@class='rt-tbody']//div[@class='rt-tr-group']")
        assert page_size == len(book_rows)
