from settings import configGeneral
from selenium import webdriver
import os

# TODO: fix it in order to handle IE and Chrome, at the moment it only works for firefox
def connect(wait_for_driver):
    browser = configGeneral.get_browser()
    driverpath = os.path.dirname(__file__)
    if browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'ie':
        driver = webdriver.Ie()
    elif browser == 'chrome':
        chromedriver = driverpath + "\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver = webdriver.Chrome(chromedriver)
    else:
        print('there is an error getting the browser config')
        exit()
    driver.implicitly_wait(wait_for_driver)
    driver.maximize_window()
    return driver


def open_web(url, driver):
    driver.get(url)
