from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions


class Utils:
    def __init__(self, browser, timeout):
        if browser in "ie":
            self.driver = webdriver.Ie("../../drivers/IEDriverServer.exe")

        elif browser in "firefox":
            self.driver = webdriver.Firefox(executable_path=r"../../drivers/geckodriver.exe")

        else:
            self.driver = webdriver.Chrome("../../drivers/chromedriver.exe")

        self.wait = WebDriverWait(self.driver, timeout)

    def get_driver(self):
        return self.driver

    def wait_for_element_located(self, by, value):
        self.wait.until(ExpectedConditions.presence_of_element_located(by, value))

    def wait_for_element_to_be_visible(self, by, value):
        self.wait.until(ExpectedConditions.element_to_be_clickable(by, value))

    def get_url(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.close()

    def get_title(self):
        return self.driver.title

    def click(self, by, value):
        Utils.wait_for_element_located(by, value)
        Utils.wait_for_element_to_be_visible(by, value)
        self.driver.find_element(by, value).click()


'''
utils = Utils()
driver = utils.initialize_driver("chrome")
driver.get("https://google.com")
driver.close()
'''
