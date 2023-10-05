import allure
# from selene import browser
from selene import be, have


class StartTestPage:

    # locators

    login_locator = "#input-38"
    password_locator = '#input-41'
    address_fond_locator = '//a[@data-test-id="Адресный фонд"]'

    # Actions

    def enter_login(self, browser, login):
        browser.element(self.login_locator).type(login)

    def enter_password(self, browser, password):
        browser.element(self.password_locator).type(password).press_enter()

    def address_fond_click(self, browser):
        browser.element(self.address_fond_locator).click()



