from selenium import webdriver
from pytest import fixture


@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()