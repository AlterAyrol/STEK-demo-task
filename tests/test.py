import allure
from allure_commons.types import Severity
import time

from STEK_demo_task.start_test_page import StartTestPage
from STEK_demo_task.address_fond_page import AddressFondPage


class TestDemoCase:

    def test_add_district(self, web_browser):
        browser = web_browser
        start_page = StartTestPage()
        address_fond_page = AddressFondPage()

        start_page.enter_login(browser, 'DEMOWEB')
        start_page.enter_password(browser, 'awdrgy')
        start_page.address_fond_click(browser)

        address_fond_page.addresses_of_residents_click(browser)
        address_fond_page.add_something_new_button_click(browser)
        address_fond_page.district_click(browser)
        address_fond_page.district_name_input_field_add(browser, 'new_district')



        time.sleep(5)


