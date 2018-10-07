import json
from Selenium.Utils.SeleniumUtils import Utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected_conditions


class CategoryPage(Utils):
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

        with open("../PageObject/CategoryPage.json", "r") as file:
            self.xpath = json.load(file)

        # Locators will be added here ->
        self.televisions = self.xpath['televisions']
        self.homeEntertainmentSystems = self.xpath['homeEntertainmentSystems']
        self.headphones = self.xpath['headphones']
        self.speakers = self.xpath['speakers']
        self.mP3MediaPlayersAccessories = self.xpath['mP3MediaPlayersAccessories']
        self.cameras = self.xpath['cameras']
        self.refrigerators = self.xpath['refrigerators']

    def click_on_television(self):
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.televisions)))
        self.driver.find_element_by_xpath(self.televisions).click()

    def click_on_home_entertainment_systems(self):
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.homeEntertainmentSystems)))
        self.driver.find_element_by_xpath(self.homeEntertainmentSystems).click()

    def click_on_headphones(self):
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.headphones)))
        self.driver.find_element_by_xpath(self.headphones).click()

    def click_on_speakers(self):
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.speakers)))
        self.driver.find_element_by_xpath(self.speakers).click()

    def click_on_mp3_media_players_accessories(self):
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.mP3MediaPlayersAccessories)))
        self.driver.find_element_by_xpath(self.mP3MediaPlayersAccessories).click()

    def click_on_cameras(self):
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.cameras)))
        self.driver.find_element_by_xpath(self.cameras).click()

    def click_on_refrigerators(self):
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.refrigerators)))
        self.driver.find_element_by_xpath(self.refrigerators).click()

    def get_title(self):
        return self.driver.title
