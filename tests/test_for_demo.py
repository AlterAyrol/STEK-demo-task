import allure
from allure_commons.types import Severity
from selene import be, have
from selene import by


from STEK_demo_task.start_test_page import StartTestPage
from STEK_demo_task.address_fond_page import AddressFondPage


@allure.tag('district smoke check')
@allure.label("owner", "AlterAyrol")
class TestDemoCase:

    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "AlterAyrol")
    @allure.epic('Тестирование вкладок в боковом меню')
    @allure.feature('Реестр "Адресный фонд"')
    @allure.story("Проверка кнопки реестра 'Адресный фонд' на кликабельность и соответствие текста кнопки")
    def test_element_is_available(self, web_browser, browser_report):
        address_fond = 'Адресный фонд'
        addresses_of_residents = 'Адреса проживающих'

        browser, site_login, site_password = web_browser
        start_page = StartTestPage()
        address_fond_page = AddressFondPage()

        start_page.enter_login(browser, site_login)
        start_page.enter_password(browser, site_password)

        if browser.element('//div[@class="v-card__actions"]/button[@type="button"]').wait_until(have.text('Да')):
            browser.element('//div[@class="v-card__actions"]/button[@type="button"]').click()

        start_page.check_text_address_fond(browser, text=address_fond)
        start_page.address_fond_clickable(browser)

        start_page.address_fond_click(browser)

        address_fond_page.check_text_address_fond(browser, text=addresses_of_residents)
        address_fond_page.address_fond_clickable(browser)


    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "AlterAyrol")
    @allure.epic('Тестирование вкладок в боковом меню')
    @allure.feature('Реестр "Адресный фонд"')
    @allure.story("Создание нового района в реестре")
    def test_add_district(self, web_browser, browser_report):
        new_district_name = 'new_district'

        browser, site_login, site_password = web_browser
        start_page = StartTestPage()
        address_fond_page = AddressFondPage()

        start_page.enter_login(browser, site_login)
        start_page.enter_password(browser, site_password)

        if browser.element('//div[@class="v-card__actions"]/button[@type="button"]').wait_until(have.text('Да')):
            browser.element('//div[@class="v-card__actions"]/button[@type="button"]').click()

        start_page.address_fond_click(browser)

        address_fond_page.addresses_of_residents_click(browser)
        address_fond_page.add_something_new_button_click(browser)
        address_fond_page.district_click(browser)
        address_fond_page.district_name_input_field_add(browser, district_name=new_district_name)

        address_fond_page.check_text_district_on_page(browser, text=new_district_name)

    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "AlterAyrol")
    @allure.epic('Тестирование вкладок в боковом меню')
    @allure.feature('Реестр "Адресный фонд"')
    @allure.story("Создание изменение названия района в реестре")
    def test_change_district_name(self, web_browser, browser_report):
        change_district_name = 'changed district name'

        browser, site_login, site_password = web_browser
        start_page = StartTestPage()
        address_fond_page = AddressFondPage()

        start_page.enter_login(browser, site_login)
        start_page.enter_password(browser, site_password)

        if browser.element('//div[@class="v-card__actions"]/button[@type="button"]').wait_until(have.text('Да')):
            browser.element('//div[@class="v-card__actions"]/button[@type="button"]').click()

        start_page.address_fond_click(browser)

        address_fond_page.addresses_of_residents_click(browser)

        address_fond_page.edit_button_click(browser)
        address_fond_page.select_all_text(browser)
        address_fond_page.district_name_input_field_add(browser, district_name=change_district_name)

        address_fond_page.check_text_district_on_page(browser, text=change_district_name)

    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "AlterAyrol")
    @allure.epic('Тестирование вкладок в боковом меню')
    @allure.feature('Реестр "Адресный фонд"')
    @allure.story("Удаление района в реестре")
    def test_delete_new_district(self, web_browser, browser_report):
        browser, site_login, site_password = web_browser
        start_page = StartTestPage()
        address_fond_page = AddressFondPage()

        start_page.enter_login(browser, site_login)
        start_page.enter_password(browser, site_password)

        if browser.element('//div[@class="v-card__actions"]/button[@type="button"]').wait_until(have.text('Да')):
            browser.element('//div[@class="v-card__actions"]/button[@type="button"]').click()

        start_page.address_fond_click(browser)

        address_fond_page.addresses_of_residents_click(browser)
        address_fond_page.select_input_control(browser)

        address_fond_page.delete_button_click(browser)
        address_fond_page.yes_button_click(browser)


@allure.tag('logaut smoke check')
@allure.label("owner", "AlterAyrol")
class TestLogoutCase:
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "AlterAyrol")
    @allure.epic('Тестирование меню пользователя в верхней навигационной панели')
    @allure.feature('Меню пользователя')
    @allure.story("Логаут из меню пользователя")
    def test_logout(self, web_browser, browser_report):
        enter_text = 'Вход'

        browser, site_login, site_password = web_browser
        start_page = StartTestPage()

        start_page.enter_login(browser, site_login)
        start_page.enter_password(browser, site_password)

        if browser.element('//div[@class="v-card__actions"]/button[@type="button"]').wait_until(have.text('Да')):
            browser.element('//div[@class="v-card__actions"]/button[@type="button"]').click()

        start_page.user_menu_click(browser)
        start_page.exit_button_click(browser)
        start_page.check_text_enter_form(browser, text=enter_text)



