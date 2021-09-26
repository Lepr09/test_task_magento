from BasePage import BasePage
from selenium.webdriver.common.by import By

# base_url = "http://magento2demo.firebearstudio.com/gear/bags.html"


class MagentoTimeouts:
    TIMEOUT_DEFAULT = 2


class MagentoSearchLocators:
    LOCATOR_MAGENTO_SEARCH_PRICE = (By.ID, "text")
    LOCATOR_MAGENTO_SEARCH_BUTTON = (By.ID, "text")
    # LOCATOR_MAGENTO_SEARCH_GOODS_LIST = (By.CLASS_NAME, "price-box price-final_price")
    LOCATOR_MAGENTO_SEARCH_BUTTONS = (By.CLASS_NAME, "search2__button")
    # LOCATOR_MAGENTO_SEARCH_GOODS_LIST = (By.CLASS_NAME, "product-item-info")
    LOCATOR_MAGENTO_SEARCH_GOODS_LIST = (By.CSS_SELECTOR, ".item.product.product-item")
    # LOCATOR_MAGENTO = (By.CSS_SELECTOR, ".service__name")
    # data-price-amount

# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector


class SearchHelper(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "http://magento2demo.firebearstudio.com/gear/bags.html"

    # def enter_word(self, word):
    #     search_field = self.find_element(MagentoSearchLocators.LOCATOR_MAGENTO_SEARCH_FIELD)
    #     search_field.click()
    #     search_field.send_keys(word)
    #     return search_field

    # def super(self).__init__(self, driver):
    #     self.driver = driver
    # base_url = "http://magento2demo.firebearstudio.com/gear/bags.html"

    def get_product_price(self):
        return self.find_element(MagentoSearchLocators.LOCATOR_MAGENTO_SEARCH_PRICE,
                                 time=MagentoTimeouts.TIMEOUT_DEFAULT).text

    def click_on_good(self):
        return self.find_element(MagentoSearchLocators.LOCATOR_MAGENTO_SEARCH_BUTTON,
                                 time=MagentoTimeouts.TIMEOUT_DEFAULT).click()

    # def get_products_list(self):
    #     all_list = self.find_elements(MagentoSearchLocators.LOCATOR_MAGENTO_SEARCH_GOODS_LIST,
    #                                   time=MagentoTimeouts.TIMEOUT_DEFAULT)
    #     goods_list = [x.text for x in all_list if len(x.text) > 0]
    #     return goods_list

    def get_products_list(self):
        all_list = self.find_elements(MagentoSearchLocators.LOCATOR_MAGENTO_SEARCH_GOODS_LIST,
                                      time=MagentoTimeouts.TIMEOUT_DEFAULT)
        # goods_list = [x.text for x in all_list if len(x.text) > 0]
        goods_list = all_list
        return goods_list
