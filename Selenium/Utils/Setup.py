import unittest
from Selenium.Utils.SeleniumUtils import Utils
import datetime


class Setup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utils = Utils("chrome", 30, True)
        cls.driver = utils.get_driver()
        cls.wait = utils.get_wait()
        print('Execution Started at', str(datetime.datetime.now()))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        pass

    def tearDown(self):
        pass
