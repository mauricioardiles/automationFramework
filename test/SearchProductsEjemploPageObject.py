from utils.selenium_utils import SeleniumConnections
from utils.selenium_utils import SeleniumScreenShot
from pages.SearchProductsExamplePage import SearchProductsExamplePage

environment = __name__
driver = SeleniumConnections.connect(10)
SeleniumConnections.open_web("https://magento.com/search/gss", driver)
searchPP = SearchProductsExamplePage(driver)
searchPP.search_field.clear()
SeleniumScreenShot.takeScreenshot(driver,"C:\\Users\\Santex\\PycharmProjects\\PycharmProjects\\automationFramework\\reports")
searchPP.search_field.send_keys("phones")
SeleniumScreenShot.takeScreenshot(driver)
searchPP.search_field.submit()
SeleniumScreenShot.takeScreenshot(driver)
driver.quit()