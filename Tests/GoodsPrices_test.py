import allure
from bags import Bags
from time import sleep


def test_verify_prices(browser):
    bags_page = Bags(browser)
    bags_page.open_page()
    products = bags_page.get_products()[1]
    for i in products:
        with allure.step(f'Check price for product {i}'):
            product = bags_page.get_product(i)
            product.click()
            # TODO: переписать на логический wait по expected_conditions
            sleep(2)  # Потому что цена не успевает появиться
            try:
                price = bags_page.get_product_price().text
            except:
                print('Not found price')
                price = ''
            # price = price.text()
            assert products.get(i) == price
            bags_page.open_page()
