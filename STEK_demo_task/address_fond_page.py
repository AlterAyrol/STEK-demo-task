import allure
# from selene import browser
from selene import be, have
from selene import by
from selenium.webdriver import ActionChains, Keys
from selene import command


class AddressFondPage:

    # locators

    addresses_of_residents_locator = '//a[@data-test-id="Адреса проживающих"]'
    add_something_new_button_locator = '//button[@data-cy="btn-add"]'
    district_locator_by_text = 'Район'
    district_name_input_field_locator = '//input[@data-cy="stack-input"]'
    table_locator = '//div[@class="v-data-table__wrapper"]/table'
    edit_button_locator = '//div[@class="row no-gutters"]//button[@data-cy="btn-edit"]'
    input_control_locator = '//div[@class="v-input__slot"]//div[@class="v-input--selection-controls__input"]'
    delete_button_locator = '//button[@data-cy="btn-delete"]'
    button_yes_and_no_locator = '//div[@data-test-id="stack-yes-no"]//div[@class="v-card__actions"]//button[@type="button"]'

    # Actions

    @allure.step('Нажатие кнопки "Адреса проживающих"')
    def addresses_of_residents_click(self, browser):
        browser.element(self.addresses_of_residents_locator).click()

    @allure.step('Нажатие кнопки "Добавить запись"')
    def add_something_new_button_click(self, browser):
        browser.element(self.add_something_new_button_locator).click()

    @allure.step('Нажатие кнопки "Район"')
    def district_click(self, browser):
        browser.element(by.text(self.district_locator_by_text)).click()

    @allure.step('Ввод названия района')
    def district_name_input_field_add(self, browser, district_name):
        browser.element(self.district_name_input_field_locator).type(district_name).press_enter()

    @allure.step('Проверка: название района есть в списке районов')
    def check_text_district_on_page(self, browser, text):
        browser.element(self.table_locator).should(have.text(text))

    @allure.step('Проверка: кнопка "Адресный фонд" кликабельна')
    def address_fond_clickable(self, browser):
        browser.element(self.addresses_of_residents_locator).should(be.clickable)

    @allure.step('Проверка: текст кнопки соответствует эталону')
    def check_text_address_fond(self, browser, text):
        browser.element(self.addresses_of_residents_locator).should(have.text(text))

    @allure.step('Нажатие кнопки редактирования у последней записи в списке районов')
    def edit_button_click(self, browser):
        browser.all(self.edit_button_locator)[-1].click()

    @allure.step('Выделение всего текста')
    def select_all_text(self, browser):
        browser.element(self.district_name_input_field_locator).perform(command.select_all)

    @allure.step('Нажатие кнопки отметки у последней записи в списке')
    def select_input_control(self, browser):
        browser.all(self.input_control_locator)[-1].click()

    @allure.step('Нажатие кнопки "Удалить запись"')
    def delete_button_click(self, browser):
        browser.element(self.delete_button_locator).click()

    @allure.step('Нажатие кнопки "да" при удалении записи')
    def yes_button_click(self, browser):
        browser.all(self.button_yes_and_no_locator).first.click()



