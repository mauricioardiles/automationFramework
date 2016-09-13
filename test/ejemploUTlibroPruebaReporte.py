import unittest
from utils.selenium_utils import SeleniumConnections
from utils import HTMLTestRunner
import os


class SearchTestsReporte(unittest.TestCase):
    def setUp(self):
        self.driver = SeleniumConnections.connect(30)
        SeleniumConnections.open_web("https://magento.com/search/gss", self.driver)

    def test_search_title_length(self):
        self.search_title_length = self.driver.find_element_by_class_name("search-head-title")
        self.assertEquals(6, len(self.search_title_length.text), "Wrong message len")

    def test_search_title_text(self):
        self.search_title_text = self.driver.find_element_by_class_name("search-head-title")
        self.assertEquals("SEARCH", self.search_title_text.text, "Wrong message")

    def tearDown(self):
        self.driver.quit()
        #dir1 = os.getcwd()
        #outfile = open(dir1 + "\\testReport.html", "w")
        #runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description= 'testing an example')
        #runner.run()

if __name__ == '__main__':
    unittest.main(verbosity=2)
