from Selenium.PageObject.HomePage import HomePage
from Selenium.PageObject.CategoryPage import CategoryPage
from Selenium.Utils.Setup import Setup
import unittest


class AddProduct(Setup):
    def test_a_search_tv(self):
        homepage = HomePage(self.driver, self.wait)
        homepage.get_url("https://www.amazon.in")
        homepage.click_on_shop_by_category()
        homepage.click_on_television()
        homepage.click_on_sony_tvs()
        homepage.enter_on_min_price("10000")
        homepage.enter_on_max_price("25000")
        homepage.click_on_go_btn()
        title = homepage.get_title()
        if "Televisions" in title:
            print("search_tv : PASS")
        else:
            print("search_tv : FAIL")

    @unittest.skip('hi')
    def test_mix(self):
        homepage = HomePage(self.driver, self.wait)
        homepage.get_url("https://www.amazon.in")
        homepage.click_on_shop_by_category()
        category_page = CategoryPage(self.driver, self.wait)
        category_page.click_on_television()
        title = category_page.get_title()
        if "Televisions" in title:
            print("search_tv : PASS")
        else:
            print("search_tv : FAIL")
        category_page.close()

    def test_verify_links_on_category(self):
        print("This is 2nd test")


if __name__ == '__main__':
    unittest.main()
