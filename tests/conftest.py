import os

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv

from utils import attach


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


# @pytest.fixture(scope='function', params=[
#     pytest.param('chrome', id='chrome'),
#     pytest.param('firefox', id='firefox')
# ])
@pytest.fixture(scope='function')
def web_browser(request):

    browser.config.base_url = 'https://demo.app.stack-it.ru/fl/.'

    # options = Options()

    # if request.param == 'chrome':
    #     selenoid_capabilities = {
    #         "browserName": "chrome",
    #         "browserVersion": "100.0",
    #         "selenoid:options": {
    #             "enableVNC": True,
    #             "enableVideo": True
    #         }
    #     }
    #     options.capabilities.update(selenoid_capabilities)
    #
    # elif request.param == 'fireFox':
    #     selenoid_capabilities = {
    #         "browserName": "firefox",
    #         "browserVersion": "97.0",
    #         "selenoid:options": {
    #             "enableVNC": True,
    #             "enableVideo": True
    #         }
    #     }
    #     options.capabilities.update(selenoid_capabilities)
    #
    # login = os.getenv('LOGIN')
    # password = os.getenv('PASSWORD')
    #
    # driver = webdriver.Remote(
    #     command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
    #     options=options)
    #
    # browser.config.driver = driver

    driver_options = webdriver.ChromeOptions()
    browser.config.driver_options = driver_options

    driver = browser.open('/')

    yield driver

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)

    # if request.param == 'chrome':
    #     attach.add_logs(browser)

    browser.quit()


@pytest.fixture(scope='function', params=[
    pytest.param([1920, 1080], id='FullHD'),
    pytest.param([2560, 1440], id='2k'),
    pytest.param([4096, 2160], id='4k'),
    pytest.param([800, 600], id='Small')
])
def window_size(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield
