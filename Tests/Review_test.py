import allure

from mars_heattech_trade_pullover import Mars
from time import sleep


class Credentials:
    Nickname = 'Test nickname'
    Summary = 'Test summary'
    Review = 'Test review'


def test_reviews(browser):
    Mars_page = Mars(browser)
    with allure.step(f'Open page'):
        Mars_page.open_page()
    with allure.step(f'Click on review'):
        button = Mars_page.click_on_review()
        button.click()
    sleep(2)
    with allure.step(f'Fill nickname'):
        Mars_page.input_nickname().send_keys(Credentials.Nickname)
    with allure.step(f'Fill summary'):
        Mars_page.input_summary().send_keys(Credentials.Summary)
    with allure.step(f'Fill review'):
        Mars_page.input_review().send_keys(Credentials.Review)
    sleep(2)
    with allure.step(f'Click rating'):
        button = Mars_page.click_on_rating()
        button.click()
    with allure.step(f'Click submit button'):
        button = Mars_page.click_on_submit()
        button.click()
    sleep(2)
    with allure.step(f'Open admin dashboard'):
        Mars_page.open_admin_dashboard()
    with allure.step(f'Click Marketing'):
        button = Mars_page.click_on_marketing()
        button.click()
    sleep(2)
    with allure.step(f'Click Pending reviews'):
        button = Mars_page.click_on_pending_reviews()
        button.click()
    sleep(2)
    with allure.step(f'Click last review'):
        button = Mars_page.click_on_last_pending_review()
        button.click()
    with allure.step(f'Set status'):
        Mars_page.click_on_set_status_approved()
    sleep(2)
    with allure.step(f'Save review'):
        button = Mars_page.click_on_save_review()
        button.click()
    sleep(2)
    with allure.step(f'Open page'):
        Mars_page.open_page()
    with allure.step(f'Click on review'):
        button = Mars_page.click_on_review()
        button.click()
    sleep(2)
