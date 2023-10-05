import allure
# from selene import browser
from selene import be, have


class AddressFondPage:

    # locators

    addresses_of_residents_locator = '//a[@data-test-id="Адреса проживающих"]'
    add_something_new_button_locator = '//button[@data-cy="btn-add"]'
    district_locator = '//div[@class="menuable__content__active"]/div[@data-cy="stack-menu-list"]/div[@data-cy="stack-menu-list-item"]'
    district_name_input_field_locator = '#input-540'

    # Actions

    def addresses_of_residents_click(self, browser):
        browser.element(self.addresses_of_residents_locator).click()

    def add_something_new_button_click(self, browser):
        browser.element(self.add_something_new_button_locator).click()

    def district_click(self, browser):
        browser.by(have.text('Район')).click()

    def district_name_input_field_add(self, browser, district_name):
        browser.element(self.district_name_input_field_locator).type(district_name).press_enter()





