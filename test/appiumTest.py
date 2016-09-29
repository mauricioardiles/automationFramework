import os
import unittest
from appium import webdriver


class ChessAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.0'
        desired_caps['deviceName'] = 'AndroidEmu'
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'Chess Free.apk'))
        desired_caps['appPackage'] = 'uk.co.aifactory.chessfree'
        desired_caps['appActivity'] = '.ChessFreeActivity'
        self.driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_single_player_mode(self):
        element = self.driver.find_element_by_name("PLAY!")
        element.click()
        self.driver.find_element_by_name("Single Player").click()
        textfields = self.driver.find_elements_by_class_name("android.widget.TextView")
        self.assertEqual('MATCH SETTINGS', textfields[0].text)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChessAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)