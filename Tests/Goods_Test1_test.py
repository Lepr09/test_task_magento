from Magento import SearchHelper


def test_magento1_search(browser):
    magento_main_page = SearchHelper(browser)
    magento_main_page.go_to_site()
    magento_main_page.enter_word("Hello")
    magento_main_page.click_on_the_search_button()
    elements = magento_main_page.check_navigation_bar()
    assert "Картинки" and "Видео" in elements

