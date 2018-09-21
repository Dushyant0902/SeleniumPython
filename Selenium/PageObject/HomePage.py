import json
from Selenium.Utils import SeleniumUtils

with open("HomePage.json", "r") as file:
    xpath = json.load(file)


class HomePage:
    selenium_utils = SeleniumUtils.Utils
    driver = selenium_utils.get_driver()
    # Locators will be added here ->
    shopByCategory = driver.find_element_by_xpath(xpath['shopByCategory'])
    televisions = driver.find_element_by_xpath(xpath['televisions'])
    sonyTvs = driver.find_element_by_xpath(xpath['sonyTvs'])
    minPrice = driver.find_element_by_xpath(xpath['minPrice'])
    maxPrice = driver.find_element_by_xpath(xpath['maxPrice'])
    goBtn = driver.find_element_by_xpath(xpath['goBtn'])

    def click_on_shop_by_category(self):
        self.shopByCategory.click()

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

print(xpath['shopByCategory'])