from Selenium.PageObject import HomePage
from Selenium.Utils import SeleniumUtils


if __name__ == '__main__':
    utils = SeleniumUtils.Utils
    utils.get_driver()
    utils.get_url()

    homePage = HomePage.HomePage()
    homePage.click_on_shop_by_category()
    homePage.click_on_television()
    homePage.click_on_sony_tvs()
    homePage.enter_on_min_price()
    homePage.enter_on_max_price()
    homePage.click_on_go_btn()
