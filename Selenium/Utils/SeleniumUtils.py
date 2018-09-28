from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions


class Utils:
    def __init__(self, browser, timeout, new_session):
        if new_session is True:
            if browser in "ie":
                self.driver = webdriver.Ie("../../drivers/IEDriverServer.exe")

            elif browser in "firefox":
                self.driver = webdriver.Firefox(executable_path=r"../../drivers/geckodriver.exe")

            else:
                self.driver = webdriver.Chrome("../../drivers/chromedriver.exe")

            self.wait = WebDriverWait(self.driver, timeout)
            self.expected_conditions = expected_conditions
            self.driver.maximize_window()
        else:
            self.wait = self.get_wait()
            self.driver = self.get_driver()

    def get_driver(self):
        if not self.driver:
            return None
        else:
            return self.driver

    def get_wait(self):
        return self.wait

    def wait_for_element_located(self, by, value):
        self.wait.until(expected_conditions.presence_of_element_located(by, value))

    def wait_for_element_to_be_visible(self, value):
        self.wait.until(expected_conditions.element_to_be_clickable())

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
