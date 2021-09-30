from BasePage import BasePage
from selenium.webdriver.common.by import By


class Timeouts:
    TIMEOUT_DEFAULT = 50


class Locators:
    LOCATOR_PRODUCTS_LIST = (By.CSS_SELECTOR, '.item.product.product-item > div')
    LOCATOR_PRODUCT_PRICE = (By.CLASS_NAME, 'price')


class Bags(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "http://magento2demo.firebearstudio.com/gear/bags.html"

    def get_product_price(self):
        return self.find_element(Locators.LOCATOR_PRODUCT_PRICE,
                                 time=Timeouts.TIMEOUT_DEFAULT)

    def get_product(self, product_id):
        LOCATOR_PRODUCT = (By.ID, product_id)
        return self.find_element(LOCATOR_PRODUCT,
                                 time=Timeouts.TIMEOUT_DEFAULT)

    # def get_products_list(self):
    #     all_list = self.find_elements(MagentoSearchLocators.LOCATOR_MAGENTO_SEARCH_GOODS_LIST,
    #                                   time=MagentoTimeouts.TIMEOUT_DEFAULT)
    #     # goods_list = [x.text for x in all_list if len(x.text) > 0]
    #     # goods_list = all_list
    #     return all_list

    def get_products(self):
        products = {}
        # count = len(self.find_elements(MagentoSearchLocators.LOCATOR_MAGENTO_SEARCH_GOODS_LIST,
        #                                time=MagentoTimeouts.TIMEOUT_DEFAULT))
        # elements = SearchHelper.get_products_list(self)
        elements = self.find_elements(Locators.LOCATOR_PRODUCTS_LIST,
                                      time=Timeouts.TIMEOUT_DEFAULT)
        # count = len(elements)
        for i in elements:
            product_id = i.get_attribute("id")
            s = i.text.find('$')
            e = i.text[s:].split()
            products[product_id] = e[0]
            # print('ID:', product_id, 'Price:', e[0])
        return len(elements), products
