from Magento import SearchHelper
from time import sleep


def test_verify_prices(browser):
    magento_main_page = SearchHelper(browser)
    magento_main_page.open_page()
    elements = magento_main_page.get_products_list()
    print('')
    for i in elements:
        product_id = i.get_attribute("id")
        s = i.text.find('$')
        e = i.text[s:].split()
        print('ID:', product_id, 'Price:', e[0])

    # for x in range(len(elements)):
    #     a = elements[x].text.split()
    # print('price ' + str(x), a[-1])
    # print('!!!!', elements[0].text)
    # class="item product product-item"
