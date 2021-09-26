import Magento
from Magento import SearchHelper
from time import sleep


def test_verify_prices(browser):
    magento_main_page = SearchHelper(browser)
    # print('!!!!!!!!!!')
    # print(magento_main_page.base_url)
    magento_main_page.open_page()
    elements = magento_main_page.get_products_list()
    link = elements[0].get_attribute('a')
    print('link', link)
    # a = elements[4].text.split()
    # print('!!!!', elements[0].text)
    # print('bukobki', a[-1])
    # for x in range(len(elements)):
    #     a = elements[x].text.split()

        # print('price ' + str(x), a[-1])
    # print('!!!!', elements[0].text)
    # print('Elements:', elements)
    # magento_main_page.enter_word("Hello")
    # magento_main_page.get_product_price()
    # elements = magento_main_page.find_elements()
    # assert "Картинки" and "Видео" in elements
    # sleep(5)

# class="item product product-item"
