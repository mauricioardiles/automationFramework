from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SearchProductsExamplePage(object):
    search_field ={}
    driver = {}
    products = {}

    def __init__(self, driver):
        self.driver = driver
        # self.search_field = driver.find_element_by_id("edit-keys")
        # self.search_field = driver.find_element(by='id', value="edit-keys")
        self.search_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "edit-keys")))
        self.products = driver.find_elements_by_xpath("//@class['search-results']/../@class['gss-results']/../b")