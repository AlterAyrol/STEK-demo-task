import allure
# from selene import browser
from selene import be, have


class StartTestPage:

    # locators

    login_locator = "#input-38"
    password_locator = '#input-41'
    address_fond_locator = '//a[@data-test-id="Адресный фонд"]'
    user_menu_locator = '//button[@data-cy="user-menu"]'
    exit_button_locator = '//button[@title="Выход"]'
    enter_form_locator = '//form[@class="v-form"]'

    # Actions

    def enter_login(self, browser, login):
        browser.element(self.login_locator).type(login)

    def enter_password(self, browser, password):
        browser.element(self.password_locator).type(password).press_enter()

    def address_fond_clickable(self, browser):
        browser.element(self.address_fond_locator).should(be.clickable)

    def check_text_address_fond(self, browser, text):
        browser.element(self.address_fond_locator).should(have.text(text))

    def address_fond_click(self, browser):
        browser.element(self.address_fond_locator).click()

    def user_menu_click(self, browser):
        browser.element(self.user_menu_locator).click()

    def exit_button_click(self, browser):
        browser.element(self.exit_button_locator).click()

    def check_text_enter_form(self, browser, text):
        browser.element(self.enter_form_locator).should(have.text(text))


