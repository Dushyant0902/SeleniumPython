import json
from Selenium.Utils.SeleniumUtils import Utils
from selenium.webdriver.common.by import By


class HomePage(Utils):
    def __init__(self, browser, timeout, new_session):
        super().__init__(browser, timeout, new_session)

        with open("../PageObject/HomePage.json", "r") as file:
            self.xpath = json.load(file)

        # Locators will be added here ->
        self.shopByCategory = self.xpath['shopByCategory']
        self.televisions = self.xpath['televisions']
        self.sonyTvs = self.xpath['sonyTvs']
        self.minPrice = self.xpath['minPrice']
        self.maxPrice = self.xpath['maxPrice']
        self.goBtn = self.xpath['goBtn']

    def click_on_shop_by_category(self):
        self.wait.until(self.expected_conditions.element_to_be_clickable((By.XPATH, self.shopByCategory)))
        self.driver.find_element_by_xpath(self.shopByCategory).click()

    def click_on_television(self):
        self.wait.until(self.expected_conditions.element_to_be_clickable((By.XPATH, self.televisions)))
        self.driver.find_element_by_xpath(self.televisions).click()

    def click_on_sony_tvs(self):
        self.wait.until(self.expected_conditions.element_to_be_clickable((By.XPATH, self.sonyTvs)))
        self.driver.find_element_by_xpath(self.sonyTvs)

    def enter_on_min_price(self, price):
        self.wait.until(self.expected_conditions.presence_of_element_located((By.XPATH, self.minPrice)))
        self.driver.find_element_by_xpath(self.minPrice).clear()
        self.driver.find_element_by_xpath(self.minPrice).send_keys(price)

    def enter_on_max_price(self, price):
        self.wait.until(self.expected_conditions.presence_of_element_located((By.XPATH, self.maxPrice)))
        self.driver.find_element_by_xpath(self.maxPrice).clear()
        self.driver.find_element_by_xpath(self.maxPrice).send_keys(price)

    def click_on_go_btn(self):
        self.wait.until(self.expected_conditions.element_to_be_clickable((By.XPATH, self.goBtn)))
        self.driver.find_element_by_xpath(self.goBtn).click()

    def get_title(self):
        return self.driver.title
