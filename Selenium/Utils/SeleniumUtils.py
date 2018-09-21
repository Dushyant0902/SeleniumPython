from selenium import webdriver


class Utils:
    def initialize_driver(self, browser):

        if browser in "ie":
            return webdriver.Ie("../../drivers/IEDriverServer.exe")

        elif browser in "firefox":
            return webdriver.Firefox(executable_path=r"../../drivers/geckodriver.exe")

        else:
            return webdriver.Chrome("../../drivers/chromedriver.exe")

    def get_driver(self):
        return self.initialize_driver("chrome")

    def get_url(self, url):
        self.driver.get(self, url)


'''
utils = Utils()
driver = utils.initialize_driver("chrome")
driver.get("https://google.com")
driver.close()
'''
