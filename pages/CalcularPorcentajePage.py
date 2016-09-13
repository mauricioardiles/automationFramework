from Base import BasePage
from Base import InvalidPageException
from selenium.webdriver.common.by import By


class CalcularPorcentaje(BasePage):
    _page_title_locator = "//div[h1[text()='Calcular Porcentaje']]"
    _partir_porcentaje_caja1 = "ciento1"

    def __init__(self, driver):
        super(CalcularPorcentaje, self).__init__(driver)
        self._validate_page(self,driver)

    def _validate_page(self,driver):
        try:
            driver.find_element_by_xpath(self._page_title_locator)
        except:
            raise InvalidPageException("Calcular Porcentaje Page not loaded")

    def _ingresar_valor_1(self,driver,texto):
        caja = driver.find_element_by_id(self._partir_porcentaje_caja1)
        caja.send_keys(texto)
        return caja


