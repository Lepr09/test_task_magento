from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        # driver.maximize_window()
        driver.implicitly_wait(10)
        self.base_url = "http://magento2demo.firebearstudio.com/"
        # self.base_url = "http://magento2demo.firebearstudio.com/gear/bags.html"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def open_page(self):
        return self.driver.get(self.base_url)

    def open_new_page(self, url):
        return self.driver.get(url)

    # def open_page(self, time=10):
    #     return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(),
    #                                                   message=f"Can't open page")
