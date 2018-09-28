from Selenium.PageObject.HomePage import HomePage
from Selenium.PageObject.CategoryPage import CategoryPage


def search_tv():
    homepage = HomePage("chrome", 15, True)
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
    homepage.close()


def mix():
    homepage = HomePage("chrome", 15, True)
    homepage.get_url("https://www.amazon.in")
    homepage.click_on_shop_by_category()
    category_page = CategoryPage("chrome", 15, False)
    category_page.click_on_television()
    title = category_page.get_title()
    if "Televisions" in title:
        print("search_tv : PASS")
    else:
        print("search_tv : FAIL")
    category_page.close()


def verify_links_on_category():
    pass


if __name__ == '__main__':
    mix()
