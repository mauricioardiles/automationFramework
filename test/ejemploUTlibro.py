import unittest
from utils.selenium_utils import SeleniumConnections


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = SeleniumConnections.connect(30)
        SeleniumConnections.open_web("https://magento.com/search/gss", self.driver)

    def test_search_title_length(self):
        self.search_title_length = self.driver.find_element_by_class_name("search-head-title")
        self.assertEquals(5, len(self.search_title_length.text), "Wrong message len")

    def test_search_title_text(self):
        self.search_title_text = self.driver.find_element_by_class_name("search-head-title")
        self.assertEquals("SEARCH", self.search_title_text.text, "Wrong message")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
