import json
from selenium.webdriver.common.by import By
from Selenium.Utils.SeleniumUtils import Utils


class HomePage(Utils):
    def __init__(self, driver):
        self.driver = driver
        # Locators will be added here ->
        with open("../PageObject/HomePage.json", "r") as file:
            self.xpath = json.load(file)

        self.shopByCategory = self.xpath['shopByCategory']
        self.televisions = By.XPATH, self.xpath['televisions']
        self.sonyTvs = By.XPATH, self.xpath['sonyTvs']
        self.minPrice = By.XPATH, self.xpath['minPrice']
        self.maxPrice = By.XPATH, self.xpath['maxPrice']
        self.goBtn = By.XPATH, self.xpath['goBtn']

    '''
     self.shopByCategory = self.driver.find_element_by_xpath(xpath['shopByCategory'])
     self.televisions = self.driver.find_element_by_xpath(xpath['televisions'])
     self.sonyTvs = self.driver.find_element_by_xpath(xpath['sonyTvs'])
     self.minPrice = self.driver.find_element_by_xpath(xpath['minPrice'])
     self.maxPrice = self.driver.find_element_by_xpath(xpath['maxPrice'])
     self.goBtn = self.driver.find_element_by_xpath(xpath['goBtn'])
    '''

    def click_on_shop_by_category(self):
        HomePage.click(By.XPATH, self.xpath['shopByCategory'])

    def click_on_television(self):
        self.televisions.click()

    def click_on_sony_tvs(self):
        self.sonyTvs.click()

    def enter_on_min_price(self):
        self.minPrice.send_keys("10000")

    def enter_on_max_price(self):
        self.maxPrice.send_keys("25000")

    def click_on_go_btn(self):
        self.goBtn.click()
