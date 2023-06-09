import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pageobjects.ColourCatalogue import ColourCatalogue
from tests.StartShopping import StartShopping
from tests.confest import setup_and_teardown


@pytest.mark.usefixtures("setup_and_teardown")
class TestSample:
    def test_one(self):
        colour_catalogue = ColourCatalogue(self.driver)
        colour_catalogue.click_view_cart()
        time.sleep(5)

    def test_two(self):
        colour_catalogue = ColourCatalogue(self.driver)
        colour_catalogue.enter_search_name("lucid dream")
        colour_catalogue.click_search_button()
        colour_catalogue.click_paint1()
        colour_catalogue.enter_pincode_number1("600037")
        colour_catalogue.click_check_button1()
        colour_catalogue.click_add_to_cart_button1()
        time.sleep(10)
        colour_catalogue.hover_paint_name()
        time.sleep(5)
        colour_catalogue.click_paint_name_options()
        colour_catalogue.click_paint_name2()
        time.sleep(3)
        colour_catalogue.enter_pincode_number2("600037")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,400);")
        time.sleep(3)
        colour_catalogue.click_check_button2()
        time.sleep(3)
        colour_catalogue.click_add_to_cart_button2()
        time.sleep(10)

    def test_three(self):
        colour_catalogue = ColourCatalogue(self.driver)
        colour_catalogue.enter_search_name("lucid dream")
        colour_catalogue.click_search_button()
        colour_catalogue.click_paint1()
        colour_catalogue.enter_pincode_number1("600037")
        colour_catalogue.click_check_button1()
        colour_catalogue.click_add_to_cart_button1()
        time.sleep(10)
        colour_catalogue.hover_paint_name()
        time.sleep(5)
        colour_catalogue.click_paint_name_options()
        colour_catalogue.click_paint_name2()
        time.sleep(3)
        colour_catalogue.enter_pincode_number2("600037")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,400);")
        time.sleep(3)
        colour_catalogue.click_check_button2()
        time.sleep(3)
        colour_catalogue.click_add_to_cart_button1()
        time.sleep(5)
        colour_catalogue.click_view_cart()
        time.sleep(5)
        colour_catalogue.click_remove_button()
        time.sleep(10)

    def test_four(self):
        colour_catalogue = ColourCatalogue(self.driver)
        colour_catalogue.enter_search_name("lucid dream")
        colour_catalogue.click_search_button()
        colour_catalogue.click_paint1()
        colour_catalogue.enter_pincode_number1("600037")
        colour_catalogue.click_check_button1()
        colour_catalogue.click_add_to_cart_button1()
        time.sleep(10)
        colour_catalogue.hover_paint_name()
        time.sleep(5)
        colour_catalogue.click_paint_name_options()
        colour_catalogue.click_paint_name2()
        time.sleep(3)
        colour_catalogue.enter_pincode_number2("600037")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,400);")
        time.sleep(3)
        colour_catalogue.click_check_button2()
        time.sleep(3)
        colour_catalogue.click_add_to_cart_button1()
        time.sleep(5)
        colour_catalogue.click_view_cart()
        time.sleep(5)
        for a in range(14):
            colour_catalogue.click_increase_product1()

        for b in range(10):
            colour_catalogue.click_increase_product2()
        time.sleep(10)

    def test_five(self):
        colour_catalogue = ColourCatalogue(self.driver)
        colour_catalogue.enter_search_name("lucid dream")
        colour_catalogue.click_search_button()
        colour_catalogue.click_paint1()
        colour_catalogue.enter_pincode_number1("600037")
        colour_catalogue.click_check_button1()
        colour_catalogue.click_add_to_cart_button1()
        time.sleep(10)
        colour_catalogue.hover_paint_name()
        time.sleep(5)
        colour_catalogue.click_paint_name_options()
        colour_catalogue.click_paint_name2()
        time.sleep(3)
        colour_catalogue.enter_pincode_number2("600037")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,400);")
        time.sleep(3)
        colour_catalogue.click_check_button2()
        time.sleep(3)
        colour_catalogue.click_add_to_cart_button1()
        time.sleep(5)
        colour_catalogue.click_view_cart()
        time.sleep(10)
        for a in range(14):
            colour_catalogue.click_increase_product1()

        for b in range(10):
            colour_catalogue.click_increase_product2()

        for c in range(10):
            colour_catalogue.click_decrease_product1()

        for d in range(5):
            colour_catalogue.click_decrease_product2()

        time.sleep(10)

    def test_six(self):
        start_shopping = StartShopping(self.driver)
        start_shopping.click_view_cart()
        time.sleep(5)
        start_shopping.click_start_shopping()
        time.sleep(20)

    def test_seven(self):
        colour_catalogue = ColourCatalogue(self.driver)
        colour_catalogue.enter_search_name("lucid dream")
        colour_catalogue.click_search_button()
        colour_catalogue.click_paint1()
        colour_catalogue.enter_pincode_number1("600037")
        colour_catalogue.click_check_button1()
        colour_catalogue.click_add_to_cart_button1()
        time.sleep(10)
        colour_catalogue.hover_paint_name()
        time.sleep(5)
        colour_catalogue.click_paint_name_options()
        colour_catalogue.click_paint_name2()
        time.sleep(3)
        colour_catalogue.enter_pincode_number2("600037")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,400);")
        time.sleep(3)
        colour_catalogue.click_check_button2()
        time.sleep(3)
        colour_catalogue.click_add_to_cart_button1()
        time.sleep(5)
        colour_catalogue.click_view_cart()
        time.sleep(5)
        colour_catalogue.click_redirect_page()
        time.sleep(10)

    def test_eight(self):
        colour_catalogue = ColourCatalogue(self.driver)
        colour_catalogue.enter_search_name("lucid dream")
        colour_catalogue.click_search_button()
        colour_catalogue.click_paint1()
        colour_catalogue.enter_pincode_number1("600037")
        colour_catalogue.click_check_button1()
        colour_catalogue.click_add_to_cart_button1()
        time.sleep(10)
        colour_catalogue.hover_paint_name()
        time.sleep(5)
        colour_catalogue.click_paint_name_options()
        colour_catalogue.click_paint_name2()
        time.sleep(3)
        colour_catalogue.enter_pincode_number2("600037")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,400);")
        time.sleep(3)
        colour_catalogue.click_check_button2()
        time.sleep(3)
        colour_catalogue.click_add_to_cart_button1()
        time.sleep(5)
        colour_catalogue.click_view_cart()
        time.sleep(5)
        colour_catalogue.total_name_display()
        colour_catalogue.total_amount_dispay()
        time.sleep(10)

    def test_nine(self):
        colour_catalogue = ColourCatalogue(self.driver)
        colour_catalogue.enter_search_name("lucid dream")
        colour_catalogue.click_search_button()
        colour_catalogue.click_paint1()
        colour_catalogue.enter_pincode_number1("600037")
        colour_catalogue.click_check_button1()
        colour_catalogue.click_add_to_cart_button1()
        time.sleep(10)
        colour_catalogue.hover_paint_name()
        time.sleep(5)
        colour_catalogue.click_paint_name_options()
        colour_catalogue.click_paint_name2()
        time.sleep(3)
        colour_catalogue.enter_pincode_number2("600037")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,400);")
        time.sleep(3)
        colour_catalogue.click_check_button2()
        time.sleep(3)
        colour_catalogue.click_add_to_cart_button1()
        time.sleep(5)
        colour_catalogue.click_view_cart()
        time.sleep(5)
        colour_catalogue.click_checkout_button()
        colour_catalogue.enter_login_mobile_number("8668129276")
        colour_catalogue.click_submit()
        time.sleep(50)
