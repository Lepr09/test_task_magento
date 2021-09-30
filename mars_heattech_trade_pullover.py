from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Timeouts:
    TIMEOUT_DEFAULT = 10


class Locators:
    LOCATOR_REVIEW_BUTTON = (By.ID, 'tab-label-reviews')
    LOCATOR_NICKNAME_INPUT = (By.ID, 'nickname_field')
    LOCATOR_SUMMARY_INPUT = (By.ID, 'summary_field')
    LOCATOR_REVIEW_INPUT = (By.ID, 'review_field')
    LOCATOR_SUBMIT_BUTTON = (By.CLASS_NAME, 'action.submit.primary')
    ADMIN_DASHBOARD_URL = 'http://magento2demo.firebearstudio.com/admin'
    LOCATOR_MARKETING = (By.ID, 'menu-magento-backend-marketing')
    LOCATOR_PENDING_REVIEWS = (By.CLASS_NAME, 'item-catalog-reviews-ratings-pending.level-2')
    LOCATOR_RATING = (By.ID, 'Rating_1_label')

    LOCATOR_LAST_PENDING_REVIEW = (By.XPATH, '//*[@id="reviewGrid_table"]/tbody/tr[1]')
    LOCATOR_DELETE_REVIEW = (By.ID, 'delete')
    LOCATOR_CONFIRM_DELETE_REVIEW = (By.XPATH, '//*[@id="html-body"]/div[5]/aside/div[2]/footer/button[2]')
    LOCATOR_STATUS_APPROVED = (By.ID, 'status_id')
    LOCATOR_SAVE_REVIEW = (By.ID, 'save_button')


class Mars(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "http://magento2demo.firebearstudio.com/mars-heattech-trade-pullover.html"

    # def get_product_price(self):
    #     return self.find_element(MagentoSearchLocators.LOCATOR_MAGENTO_SEARCH_GOOD_PRICE,
    #                              time=MagentoTimeouts.TIMEOUT_DEFAULT).text

    # def get_products_list(self):
    #     all_list = self.find_elements(MagentoSearchLocators.LOCATOR_MAGENTO_SEARCH_GOODS_LIST,
    #                                   time=MagentoTimeouts.TIMEOUT_DEFAULT)
    #     # goods_list = [x.text for x in all_list if len(x.text) > 0]
    #     goods_list = all_list
    #     return goods_list

    # def get_products(self):
    #     products = {}
    #     count = len(self.find_elements(MagentoSearchLocators.LOCATOR_MAGENTO_SEARCH_GOODS_LIST,
    #                                    time=MagentoTimeouts.TIMEOUT_DEFAULT))
    #     # print('Products count:', count)
    #     elements = SearchHelper.get_products_list(self)
    #     for i in elements:
    #         product_id = i.get_attribute("id")
    #         s = i.text.find('$')
    #         e = i.text[s:].split()
    #         products[product_id] = e[0]
    #         # print('ID:', product_id, 'Price:', e[0])
    #     return count, products

    def click_on_review(self):
        return self.find_element(Locators.LOCATOR_REVIEW_BUTTON,
                                 time=Timeouts.TIMEOUT_DEFAULT)

    def input_nickname(self):
        return self.find_element(Locators.LOCATOR_NICKNAME_INPUT,
                                 time=Timeouts.TIMEOUT_DEFAULT)

    def input_summary(self):
        return self.find_element(Locators.LOCATOR_SUMMARY_INPUT,
                                 time=Timeouts.TIMEOUT_DEFAULT)

    def input_review(self):
        return self.find_element(Locators.LOCATOR_REVIEW_INPUT,
                                 time=Timeouts.TIMEOUT_DEFAULT)

    def click_on_rating(self):
        return self.find_element(Locators.LOCATOR_RATING,
                                 time=Timeouts.TIMEOUT_DEFAULT)

    def click_on_submit(self):
        return self.find_element(Locators.LOCATOR_SUBMIT_BUTTON,
                                 time=Timeouts.TIMEOUT_DEFAULT)

    def open_admin_dashboard(self):
        return self.open_new_page(Locators.ADMIN_DASHBOARD_URL)

    def click_on_marketing(self):
        return self.find_element(Locators.LOCATOR_MARKETING,
                                 time=Timeouts.TIMEOUT_DEFAULT)

    def click_on_pending_reviews(self):
        return self.find_element(Locators.LOCATOR_PENDING_REVIEWS,
                                 time=Timeouts.TIMEOUT_DEFAULT)

    def click_on_last_pending_review(self):
        return self.find_element(Locators.LOCATOR_LAST_PENDING_REVIEW,
                                 time=Timeouts.TIMEOUT_DEFAULT)

    def click_on_set_status_approved(self):
        tmp = Select(self.find_element(Locators.LOCATOR_STATUS_APPROVED,
                                       time=Timeouts.TIMEOUT_DEFAULT))
        return tmp.select_by_value('1')

    def click_on_save_review(self):
        return self.find_element(Locators.LOCATOR_SAVE_REVIEW,
                                 time=Timeouts.TIMEOUT_DEFAULT)
